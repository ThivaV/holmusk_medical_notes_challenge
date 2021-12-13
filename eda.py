# %%
import pandas as pd
import numpy as np
import spacy
# %%
df = pd.read_csv('./dataset/ClinNotes.csv')
df.head()
# %%
df.info()
# %%
df.category.unique()
# %%
df.isnull().sum()
# %%
df.category.value_counts()
# %%
nlp = spacy.load("en_core_web_lg")
# %%
