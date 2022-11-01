#%% import %%
import nltk
nltk.download('all')
# %% example
def tagit(text_string):
    text = nltk.word_tokenize(" ".join(str(text_string).split("_")))
    tagged_text=nltk.pos_tag(text)
    print(tagged_text)

# %%
for text in tagged_text:
    if text[1] == 'NNP':
        print(text[0])
# %%
import pandas as pd
sheet_id = "18uUJCYmS4-LtyBm-kPVzyl45iEGE6o_p88xW7pdxYkE"
sheet_name = "ORCHESTRAGlossary"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
# %%
convince_glossary=pd.read_csv(url)
# %%
for ele in convince_glossary['question']:
    tagit(ele)
# %%
