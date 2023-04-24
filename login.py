import os

import asyncio
import streamlit as st
from httpx_oauth.clients.google import GoogleOAuth2


async def write_authorization_url(client):
    authorization_url = await client.get_authorization_url(
        os.getenv("GOOGLE_REDIRECT"),
        scope=["profile", "email"],
        extras_params={"access_type": "offline"},
    )
    return authorization_url


async def write_access_token(client, code):
    token = await client.get_access_token(code, os.getenv("GOOGLE_REDIRECT"))
    return token


async def get_user_info(client, token):
    user_id, user_email = await client.get_id_email(token)
    return user_id, user_email


async def revoke_token(client, token):
    return await client.revoke_token(token)


def login_button():
    auth_url = asyncio.run(write_authorization_url(st.session_state.client))
    st.columns(3)[1].write(f'<br><a href="{auth_url}" target="_blank" class="loginButton">Continue with Google</a>'
                           '''<style>.loginButton {
    text-decoration: none;
    color: rgb(49, 51, 63) !important;
    display: inline-flex;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.25rem;
    user-select: none;
    background-color: white;
    border: 1px solid rgba(49, 51, 63, 0.2);
}
.loginButton\\:hover {
    border-color: rgb(255, 75, 75);
    color: rgb(255, 75, 75) !important;
    text-decoration: none;
}</style>''', unsafe_allow_html=True)


def logout_button():
    st.sidebar.write(f"Hello {st.session_state.user_email}")
    if st.sidebar.button("Logout"):
        asyncio.run(revoke_token(st.session_state.client, st.session_state.cookies["token"]))
        del st.session_state["user_email"]
        del st.session_state["user_id"]
        st.session_state.cookies["token"] = ""
        st.session_state.cookies.save()
        st.experimental_rerun()


def login():
    if "user_id" in st.session_state:
        logout_button()
        return

    st.session_state.client = GoogleOAuth2(os.getenv("GOOGLE_CLIENT_ID"), os.getenv("GOOGLE_CLIENT_SECRET"))

    if "token" not in st.session_state.cookies or st.session_state.cookies["token"] == "":
        try:
            code = st.experimental_get_query_params()["code"]
        except (BaseException,):
            login_button()
        else:
            try:
                token = asyncio.run(write_access_token(st.session_state.client, code))
            except (BaseException,):
                login_button()
            else:
                if token.is_expired():
                    login_button()
                else:
                    st.session_state.cookies["token"] = token["access_token"]
                    st.session_state.cookies.save()
                    st.session_state.user_id, st.session_state.user_email = asyncio.run(
                        get_user_info(st.session_state.client, token["access_token"])
                    )
                    logout_button()
    else:
        token = st.session_state.cookies["token"]
        try:
            st.session_state.user_id, st.session_state.user_email = asyncio.run(
                get_user_info(st.session_state.client, token)
            )
            logout_button()
        except (BaseException,):
            st.session_state.cookies["token"] = ""
            st.session_state.cookies.save()
            login_button()
