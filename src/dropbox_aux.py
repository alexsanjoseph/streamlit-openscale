import pandas as pd
from io import StringIO


def get_dropbox_key():
    pass


def get_latest_file_name_from_dropbox(dbx, folder_name, username):
    files_list = dbx.files_search(folder_name, query=username + "*.csv")
    return sorted([(x.metadata.name, str(x.metadata.server_modified))  for x in files_list.matches], key = lambda x: x[1])[-1][0]


def download_file_data_from_dropbox(dbx, folder_name, latest_file):

    meta, res = dbx.files_download(folder_name + "/" + latest_file)
    file_output = res.content.decode("utf-8")
    return pd.read_csv(StringIO(file_output)).query("dateTime!='0.0'")
