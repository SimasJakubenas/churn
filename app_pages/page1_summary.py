import streamlit as st


def page_summary():

    st.write("### Quick Project Summary")

    st.info(
        f"**Project Terms & Jargon**\n"
        f"* A **customer** is a person who consumes your service or product.\n"
        f"* A **prospect** is a potential customer.\n"
        f"* A **churned** customer is a user who has stopped using your product or service.\n "
        f"* This customer has a **tenure** level, the number of months this person " 
        f"has used our product/service.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset represents a **customer base from a Telco company** "
        f"containing individual customer data on the products and services "
        f"(like internet type, online security, online backup, tech support), "
        f"account information (like contract type, payment method, monthly charges) "
        f"and profile (like gender, partner, dependents).")

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in understanding the patterns from the customer base "
        f"so that the client can learn the most relevant variables that are correlated to a "
        f"churned customer.\n"
        f"* 2 - The client is interested in determining potential factors that "
        f"could maintain and/or bring the prospect to a non-churnable cluster."
        )
    
  
    if st.checkbox(f"**Dataset Content Abbreviations**"):
        st.table(
            [
                {
                    "Variable": "customerid",
                    "Explain": "Unique customer identifier",
                    "Type of Data": "Numeric",
                    "Units": "Number"
                },
                {
                    "Variable": "gender",
                    "Explain": "Gender of the customer",
                    "Type of Data": "Binary",
                    "Units": "0 (female) / 1 (male)"
                },
                {
                    "Variable": "SeniorCitizen",
                    "Explain": "Customer is a senior citizen",
                    "Type of Data": "Binary",
                    "Units": "0 (No) / 1 (Yes)"
                },
                {
                    "Variable": "Partner",
                    "Explain": "Customer has a partner",
                    "Type of Data": "Binary",
                    "Units": "False/ True"
                },
                {
                    "Variable": "Dependents",
                    "Explain": "Customer has dependents",
                    "Type of Data": "Binary",
                    "Units": "False/ True"
                },
                {
                    "Variable": "tenure",
                    "Explain": "Number of months with the company",
                    "Type of Data": "Numeric",
                    "Units": "Months"
                },
                {
                    "Variable": "PhoneService",
                    "Explain": "Customer has a phone service",
                    "Type of Data": "Binary",
                    "Units": "False/ True"
                },
                {
                    "Variable": "MultipleLines",
                    "Explain": "Customer has multiple lines",
                    "Type of Data": "Binary",
                    "Units": "False/ True"
                },
                {
                    "Variable": "InternetService",
                    "Explain": "Type of internet service",
                    "Type of Data": "Categorical",
                    "Units": "DSL / Fiber optic / No"
                },
                {
                    "Variable": "OnlineSecurity",
                    "Explain": "Customer has online security",
                    "Type of Data": "Categorical",
                    "Units": "No/ Yes/ No service"
                },
                {
                    "Variable": "OnlineBackup",
                    "Explain": "Customer has online backup",
                    "Type of Data": "Categorical",
                    "Units": "No/ Yes/ No service"
                },
                {
                    "Variable": "DeviceProtection",
                    "Explain": "Ccustomer has device protection",
                    "Type of Data": "Categorical",
                    "Units": "No/ Yes/ No service"
                },
                {
                    "Variable": "TechSupport",
                    "Explain": "Customer has tech support",
                    "Type of Data": "Categorical",
                    "Units": "No/ Yes/ No service"
                },
                {
                    "Variable": "StreamingTV",
                    "Explain": "Customer has streaming TV",
                    "Type of Data": "Categorical",
                    "Units": "No/ Yes/ No service"
                },
                {
                    "Variable": "StreamingMovies",
                    "Explain": "Customer has streaming movies",
                    "Type of Data": "Categorical",
                    "Units": "No/ Yes/ No service"
                },
                {
                    "Variable": "Contract",
                    "Explain": "Type of contract the customer has",
                    "Type of Data": "Categorical",
                    "Units": "Month-to-month/ 1y/ 2y"
                },
                {
                    "Variable": "PaperlessBilling",
                    "Explain": "Customer has paperless billing",
                    "Type of Data": "Binary",
                    "Units": "False/ True"
                },
                {
                    "Variable": "PaymentMethod",
                    "Explain": "Preferred payment method",
                    "Type of Data": "Categorical",
                    "Units": "Type of pay"
                },
                {
                    "Variable": "MonthlyCharges",
                    "Explain": "Monthly charges for service",
                    "Type of Data": "Numeric",
                    "Units": "$"
                },
                {
                    "Variable": "TotalCharges",
                    "Explain": "Total charges for service",
                    "Type of Data": "Numeric",
                    "Units": "$"
                },
                {
                    "Variable": "Churn",
                    "Explain": "Customer has churned or not",
                    "Type of Data": "Binary",
                    "Units": "False/ True"
                }
            ]
        )
        
        # Custom JavaScript to hide the index column of the table
        hide_index_js ="""
            <script>
                const tables = window.parent.document.querySelectorAll('table');
                tables.forEach(table => {
                    const indexColumn = table.querySelector('thead th:first-child');
                    if (indexColumn) {
                        indexColumn.style.display = 'none';
                    }
                    const indexCells = table.querySelectorAll('tbody th');
                    indexCells.forEach(cell => {
                        cell.style.display = 'none';
                    });
                });
            </script>
            """
        # Use components.html to inject the JavaScript
        st.components.v1.html(hide_index_js, height=0)
            