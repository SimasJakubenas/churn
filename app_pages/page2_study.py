import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


COLOR1 = '#26b6a9'
COLOR2 = 'white'
BACKGROUND_COLOR = '#262730'
ACCENT_COLOR1 = '#3097CD'
ACCENT_COLOR2 = '#EF3535'

sns.set_theme(style="whitegrid", rc={"axes.facecolor": BACKGROUND_COLOR}) 


def page_study():
    df = pd.read_csv('outputs/datasets/collection/WA_Fn-UseC_-Telco-Customer-Churn.csv')
    target_var = 'Churn'
    vars_to_study = [
        'OnlineSecurity', 'PaperlessBilling', 'TechSupport', 'MonthlyCharges', 'OnlineBackup', 'Contract', 'tenure'
        ]

    st.write("### Telco Churn Study")
    st.info(
        f"#### Business Requirement 1\n"
        f"* The client is interested in discovering how listed variables are "
        f"correlated customer churn."
    )

    if st.checkbox("Inspect customer data"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns."
            f"You can see the first 10 rows displayed below:")
        
        st.dataframe(df.head(10))

    st.write("---")

    """Correlation Study Findings"""
    st.write(
        f"* Correlation studies were conducted to better understand how "
        f"the variables are correlated to  **`Churn`**. \n\n"
        f"* Bellow are the most correlated variables in regards to **`Churn`** "
    )


    variable_info = [
        "* Customers with no online security are almost 4 times more likely to churn \n",
        "* Customers that use paperless billing are almost 60% more likely to churn \n",
        "* Customers with no tech support are almost 4 times more likely to churn \n",
        "* Customers with higher monthly charges are more likely to churn. There is a significant jump in churn level at 66$ range indicating a dissatisfaction level with particular service \n",
        "* Customers with no online backup tend to churn more often \n",
        "* Customers with month-to-month contact tend to churn the most by a large margin. This is the most significant indicator for churn \n",
        "* Customers with longer tenure tend to churn less. Churn level is halved at 3 month milestone and is halved yet again at 6 months. This is also very significant indicator \n"
    ]
    
    tabs = st.tabs(vars_to_study)
    tab_counter = 0
    
    for tab in tabs:
        with tab:
            st.info(variable_info[tab_counter])
            plot_churn_correlation(df, target_var, vars_to_study[tab_counter])
            tab_counter += 1


def plot_churn_correlation(df: pd.DataFrame, target_var: str, variable: str) -> None:
    df_cat = df.select_dtypes(include=['object', 'category'])
    df_cat_vars = list(df_cat.columns)
    
    if variable not in df_cat_vars:
        plot_numerical(df, variable, target_var)
        print("\n\n")
    else:
        plot_categorical(df, variable, target_var)
        print("\n\n")


def plot_categorical(df: pd.DataFrame, col: str, target_var: str) -> None:

    plot_coloring(plt)
    plt.figure(figsize=(12, 5), facecolor=BACKGROUND_COLOR)
    sns.countplot(data=df, x=col, hue=target_var, palette=[ACCENT_COLOR1, ACCENT_COLOR2])
    plt.ylabel("Count", rotation=0, labelpad=30) 
    plt.title(f"{col}", fontsize=20)
    st.pyplot(plt)
    
    data_metrics_for_categorical_variables(df, col, target_var)


def plot_numerical(df: pd.DataFrame, col: str, target_var: str) -> None:
    
    plot_coloring(plt)
    plt.figure(figsize=(12, 5), facecolor=BACKGROUND_COLOR)
    sns.histplot(data=df, x=col, hue=target_var, kde=True, element="step",
                palette=[ACCENT_COLOR1, ACCENT_COLOR2], bins=24)
    
    plt.ylabel("Count", rotation=0, labelpad=30) 
    plt.title(f"{col}", fontsize=20)
    st.pyplot(plt)


def plot_coloring(plt: plt.figure) -> None:
    
    plt.rcParams['text.color'] = COLOR2
    plt.rcParams['axes.labelcolor'] = COLOR2
    plt.rcParams['xtick.color'] = COLOR2
    plt.rcParams['ytick.color'] = COLOR2
    plt.rcParams['grid.color'] = COLOR1

    ax = plt.axes()
    plt.setp(ax.spines.values(), color=COLOR1)


def data_metrics_for_categorical_variables(df: pd.DataFrame, col: str, target_var: str) -> None:
    
    sorted_data, grouped = data_metrics_for_individual_value(df, col, target_var)
    
    _, *cols = st.columns(len(grouped) + 1)
    
    for i, col in enumerate(cols):
        col.metric(
            f"{sorted_data[i][f'{target_var}_no']}/{sorted_data[i][f'{target_var}_yes']}",
            f"{sorted_data[i][f'{target_var}_perc']}%")


def data_metrics_for_individual_value(df: pd.DataFrame, col: str, target_var: str) -> dict:
    
    grouped = df.groupby(df[col])[target_var]
    
    variable_ordering_keys = df[col].unique().tolist()
    values = [x for x in range(len(variable_ordering_keys))]

    # Convert to dictionary
    priority_dictionary = dict(zip(variable_ordering_keys, values))
    
    churn_count = []
    
    for i, value in enumerate(grouped):
        group_values = value[1].value_counts()
        variable_churn = {'value': value[0]}
        variable_churn[f'{target_var}_yes'] = group_values.iloc[1]
        variable_churn[f'{target_var}_no'] = group_values.iloc[0]
        variable_churn[f'{target_var}_perc']= round(group_values.iloc[1] * 100 / group_values.iloc[0], 1)
        
        churn_count.append(variable_churn)
    
    # Sort using custom order
    sorted_data = sorted(churn_count, key=lambda x: priority_dictionary[x["value"]])
    
    return sorted_data, grouped
