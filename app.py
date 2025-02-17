import streamlit as st

from app_pages.multipage import MultiPage
from app_pages.page1_summary import page_summary
from app_pages.page2_study import page_study
from app_pages.page3_ml_chern import page_churn


app = MultiPage(app_name= "Telco Churnometer")

app.app_page("Project Summary", 'house', page_summary)
app.app_page("Study", 'graph-up-arrow', page_study)
app.app_page("ML Churn Prediction", 'arrow-repeat', page_churn)

app.run()