
import streamlit as st
import os
import dropbox
import csv
import pandas as pd
from io import StringIO
from dropbox_aux import *
from datetime import datetime
from plotnine import *
st.markdown("# Openscale + Streamlit = Awesome")

DROPBOX_KEY = os.environ['DROPBOX_OPENSCALE_ACCESS_KEY']
USERNAME = "Alex"
FOLDER_NAME = "/openscale"
TEMP_FILE_NAME = "image.png"
dbx = dropbox.Dropbox(DROPBOX_KEY)

latest_file = get_latest_file_from_dropbox(dbx, FOLDER_NAME, USERNAME)

meta, res = dbx.files_download(FOLDER_NAME + "/" +  latest_file)
file_output = res.content.decode("utf-8")
scale_data_df = pd.read_csv(StringIO(file_output))

scale_data_df_cleaned = scale_data_df\
    .loc[:,["dateTime", "weight"]] \
    .assign(timestamp = pd.to_datetime(scale_data_df['dateTime']))

plot_output = (ggplot(scale_data_df_cleaned, aes(x = 'timestamp', y = 'weight')) + 
#   facet_wrap('~', ncol = 1, scales = 'free') +
  geom_point(size = 0.5))

plot_output.save(TEMP_FILE_NAME, dpi = 200)
st.image(TEMP_FILE_NAME)