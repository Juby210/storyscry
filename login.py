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
    st.markdown(f'[Continue with Google]({auth_url})')


def logout_button():
    if st.button("Logout"):
        asyncio.run(revoke_token(st.session_state.client, st.session_state.cookies["token"]))
        del st.session_state["user_email"]
        del st.session_state["user_id"]
        del st.session_state.cookies["token"]
        st.experimental_rerun()


def login():
    st.session_state.client = GoogleOAuth2(os.getenv("GOOGLE_CLIENT_ID"), os.getenv("GOOGLE_CLIENT_SECRET"))

    if "token" not in st.session_state.cookies:
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
            login_button()
