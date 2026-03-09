import streamlit as st
import os
st.write("Project files:", os.listdir())
st.write("Dataset exists:", os.path.exists("VehiclesDetectionDataset"))                    