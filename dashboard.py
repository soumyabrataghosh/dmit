# %% packages %%
import pandas as pd
from pyparsing import col
import streamlit as st
import json
#st.set_page_config(layout='wide')
st.set_page_config(
    page_title="LIMT - Variable selection and export",
    page_icon="💾",
    layout="wide",
    initial_sidebar_state="expanded",
)
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
    max-height: 500px;
    overflow-x: hidden;
    overflow-y: scroll;
}}
.stButton button {{
    position: fixed;
    bottom: 10%;
    right: 10%;
    z-index: 9999;
}}
.stDownloadButton button {{
    position: fixed;
    bottom: 5%;
    right: 10%;
    z-index: 9999;   
}}

</style>
'''
st.markdown(styl, unsafe_allow_html=True)

# df_gs
# %%
#st.write(df_gs)
st.sidebar.title('LIMT')
st.sidebar.header('LCSB Information Minimisation Toolkit (Alpha)')
st.sidebar.subheader('Variable selection for data export')
top_cols1, top_cols2= st.columns([2,1])

with top_cols1:
    st.markdown('Click `Explore variables` to explore and select variables in each category. After selction, click on `Submit` Button and then click `Download JSON` button.')
    #container = st.container()``

    # %%
    selected_cat = {}
    #cols = st.columns(2)
    cat_list = list(df_gs['categories'].dropna().unique())

    with st.form(key='my_form'):
        cat_no = 1
        for cat in cat_list:
            #with cols[int(cat_no/(int(len(cat_list)/2)+1))]:
            selected_cat[cat]={'all_var':st.checkbox(cat)}
            #if st.button('Explore variables',key=cat):
            with st.expander('Explore variables'):
                container = st.container()
                container.write("Category: "+str(cat))
                var_list = df_gs[df_gs['categories'] == cat][['question','CON-ORC_uui']].dropna().apply(tuple, axis=1)
                for var_item in var_list:
                    selected_cat[cat][var_item[1]]=container.checkbox(var_item[0],key=str(cat)+str(var_item[1]))
                

            cat_no = cat_no + 1
        #with cols[-1]:
        st.form_submit_button('Submit', type="primary")
    json_string = json.dumps(selected_cat, indent = 4)
    st.download_button(
        label="Download JSON",
        file_name="data.json",
        mime="application/json",
        data=json_string,
        key = "jsondown",
    )

#container_json.json(selected_cat)
with top_cols2:
    container_json = st.container()
    container_json.code(json_string)

st.sidebar.markdown('Bug report and contact: soumyabrata.ghosh@uni.lu')