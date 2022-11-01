# %% packages %%
import pandas as pd
from pyparsing import col
import streamlit as st
import json
st.set_page_config(layout='wide')

# %%
#df=pd.read_excel('/Users/soumyabrata.ghosh/code-repo/dmit/CONVINCE-ORCHESTRA + PREDICOVID + IGSS data dictionary 25-OCT-2022.xlsx',sheet_name='CONVINCE-ORCHESTRA')
# %% Read from Google Sheet
sheet_id = '18uUJCYmS4-LtyBm-kPVzyl45iEGE6o_p88xW7pdxYkE'
sheet_name = 'ORCHESTRAGlossary'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
df_gs = pd.read_csv(url)

# %%
styl = f'''<style>
.element-container {{
    max-height: 300px;
    overflow-x: hidden;
    overflow-y: scroll;
}}

</style>
'''
st.markdown(styl, unsafe_allow_html=True)

# df_gs
# %%
#st.write(df_gs)
st.subheader('Variable selection for data export')
top_cols1, top_cols2= st.columns(2)
with top_cols1:
    st.code('Click "Explore variables" to view variables in each category.')
    container = st.container()
with top_cols2:
    st.code('Select the category checkboxes, click Submit, then copy the json below.')
    container_json = st.container()
# %%
st.code('Variable categories:')
selected_cat = {}
cols = st.columns(5)
cat_list = list(df_gs['categories'].dropna().unique())

with st.form(key='my_form'):
    cat_no = 1
    for cat in cat_list:
        with cols[int(cat_no/(int(len(cat_list)/5)+1))]:
            selected_cat[cat]=st.checkbox(cat)
            if st.button('Explore variables',key=cat):
                container.write("Category: "+str(cat))
                container.table(df_gs[df_gs['categories'] == cat]['question'])
        cat_no = cat_no + 1
    #with cols[-1]:
    st.form_submit_button('Submit')
container_json.code(json.dumps(selected_cat, indent = 4) )
#container_json.json(selected_cat)

