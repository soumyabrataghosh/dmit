# %% packages %%
import pandas as pd
import streamlit as st

# %%
df=pd.read_excel('/Users/soumyabrata.ghosh/code-repo/dmit/CONVINCE-ORCHESTRA + PREDICOVID + IGSS data dictionary 25-OCT-2022.xlsx',sheet_name='CONVINCE-ORCHESTRA')
# %% Read from Google Sheet
sheet_id = '18uUJCYmS4-LtyBm-kPVzyl45iEGE6o_p88xW7pdxYkE'
sheet_name = 'ORCHESTRAGlossary'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
df_gs = pd.read_csv(url)

# %%
# df_gs
# %%
st.write(df_gs)
# %%
selected_cat = {}
with st.form(key='my_form'):
    for cat in list(df_gs['categories'].dropna().unique()):
        selected_cat[cat]=st.checkbox(cat)
    st.form_submit_button('Submit')
st.write(selected_cat)


# %%
