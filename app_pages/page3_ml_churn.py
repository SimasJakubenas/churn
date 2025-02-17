import streamlit as st


def page_churn():

    st.write("### ML Pipeline: Predict Prospect Churn")
    st.info(
        f"* The pipeline was tuned aiming at least 0.80 Recall on 'Yes Churn' class, "
        f"since we are interested in this project in detecting a potential churner. \n"
        f"* The model f1-score and accuracy is 86%."
    )

    st.write("---")
    st.write("* The model was trained and all the features.")
    st.write("---")
    
    tab1, tab2 = st.tabs(["Model Performace", "Best Model"])
    
    with tab1:
        st.image("static/images/model_performance.png")
        
    with tab2:
        st.image("static/images/best_model.png")
        