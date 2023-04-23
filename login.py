import os

import asyncio
import streamlit as st
from httpx_oauth.clients.google import GoogleOAuth2
from streamlit_javascript import st_javascript

redirect_url = os.getenv("GOOGLE_REDIRECT")


async def write_authorization_url(client):
    authorization_url = await client.get_authorization_url(
        redirect_url,
        scope=["profile", "email"],
        extras_params={"access_type": "offline"},
    )
    return authorization_url


async def write_access_token(client, code):
    token = await client.get_access_token(code, redirect_url)
    return token


async def get_user_info(client, token):
    user_id, user_email = await client.get_id_email(token)
    return user_id, user_email


async def revoke_token(client, token):
    return await client.revoke_token(token)


def login_button():
    if st.button("Continue with Google"):
        auth_url = asyncio.run(write_authorization_url(st.session_state.client))
        st_javascript(f'window.open("{auth_url}").then(window.close)')


def logout_button():
    if st.button("Logout"):
        asyncio.run(revoke_token(st.session_state.client, st.session_state.token["access_token"]))
        del st.session_state["user_email"]
        del st.session_state["user_id"]
        del st.session_state["token"]
        st.experimental_rerun()


def login():
    st.session_state.client = GoogleOAuth2(os.getenv("GOOGLE_CLIENT_ID"), os.getenv("GOOGLE_CLIENT_SECRET"))

    if "token" not in st.session_state:
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
                    st.session_state.token = token
                    st.session_state.user_id, st.session_state.user_email = asyncio.run(
                        get_user_info(st.session_state.client, token["access_token"])
                    )
                    logout_button()
                    return st.session_state.user_id, st.session_state.user_email
    else:
        logout_button()
        return st.session_state.user_id, st.session_state.user_email
