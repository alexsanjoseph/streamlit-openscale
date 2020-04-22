
import streamlit as st
import os
import dropbox
import csv
import pandas as pd
from src.dropbox_aux import *
from datetime import datetime
from plotnine import *
from src.css import current_css
from src.plot import plot_and_save

st.markdown(current_css, unsafe_allow_html=True)
st.markdown("# Openscale + Streamlit = Awesome")

DROPBOX_KEY = os.environ['DROPBOX_OPENSCALE_ACCESS_KEY']
FOLDER_NAME = "/openscale"
TEMP_FILE_NAME = "image.png"

dbx = dropbox.Dropbox(DROPBOX_KEY)

username = st.sidebar.selectbox("Select User", ["Alex", "Malavika"])
date_start = st.sidebar.date_input("Start Date", pd.to_datetime("2018-08-01"))
date_end = st.sidebar.date_input("End Date", datetime.today())
smooth_factor = st.sidebar.slider("Select smoothening factor", 0.01, 0.5, 0.12)

latest_file = get_latest_file_name_from_dropbox(dbx, FOLDER_NAME, username)
scale_data_df = download_file_data_from_dropbox(dbx, FOLDER_NAME, latest_file)

scale_data_df_cleaned = scale_data_df \
    .loc[:, ["dateTime", "weight"]] \
    .assign(timestamp=pd.to_datetime(scale_data_df['dateTime'])) \
    .query("timestamp >= @date_start & timestamp <= @date_end") 

plot_and_save(scale_data_df_cleaned, smooth_factor, TEMP_FILE_NAME)
st.image(TEMP_FILE_NAME)
