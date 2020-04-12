import streamlit as st

def get_dropbox_key():
    pass

@st.cache
def get_latest_file_from_dropbox(dbx, folder_name, username):
    files_list = dbx.files_search(folder_name, query=username + "*.csv")
    return sorted([(x.metadata.name, str(x.metadata.server_modified))  for x in files_list.matches], key = lambda x: x[1])[-1][0]
