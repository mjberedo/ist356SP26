import streamlit as st
import pandas as pd
from check_functions import clean_currency

url = 'https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv'
checks = pd.read_csv(url)
st.write("Raw Data")
st.dataframe(checks)

checks['total_amount_of_check_clean'] = checks['total_amount_of_check'].apply(clean_currency)
checks['gratuity_clean'] = checks['gratuity'].apply(clean_currency)

#calculations
checks['calculated_gratuity'] = checks['total_amount_of_check_clean'] * checks['gratuity_clean'] / 100
checks['difference'] = checks['calculated_gratuity'] - checks['gratuity_clean']
checks['price_per_item'] = checks['total_amount_of_check_clean'] / checks['number_of_items']
checks['price_per_person'] = checks['total_amount_of_check_clean'] / checks['number_of_people']
checks['items_per_person'] = checks['number_of_items'] / checks['number_of_people']
checks['tip_percentage'] = checks['gratuity_clean'] / checks['total_amount_of_check_clean'] * 100

st.write("Cleaned Data")
st.dataframe(checks)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Average Check Amount", f"${checks['total_amount_of_check_clean'].mean():.2f}")
col2.metric("Average Gratuity", f"${checks['gratuity_clean'].mean():.2f}")
col3.metric("Average Tip Percentage", f"{checks['tip_percentage'].mean():.2f}%")
col4.metric("Average Price Per Item", f"${checks['price_per_item'].mean():.2f}")

