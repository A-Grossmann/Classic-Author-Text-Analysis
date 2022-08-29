import os
import pandas as pd
import numpy as np
# import seaborn as sn
 
# Loading the dataset
data = pd.read_csv("Author_Data.csv")
 
# Numeric columns of the dataset
numeric_col = ['Avg Sentance Length','Average Word Length','Nouns','Adjectives','Coordinating Conjunction', 'Cardinal Number', 'Determiner', 'Preposition or Subordinating Conjunction', 'Adjective', 'Adjective, Comparative', 'Adjective, Superlative', 'Modal', 'Noun, singular or mass', 'Noun, Plural', 'Possessive Pronoun Phrase', 'Adverb', 'Adverb, Comparative', 'Verb, Base Form', 'Verb, Past Tense', 'Verb, Gerund or Present Participle', 'Verb, Past Participle', 'Verb, non-3rd Person Singular Present', 'Verb 3rd Person Singular Present', 'Wh-determiner', 'Possessive Wh-pronoun']

 
# Correlation Matrix formation
corr_matrix = data.loc[:,numeric_col].corr()
pd.set_option("display.max_columns", None)
print(corr_matrix)

corr_matrix.to_csv("C:\\Users\\Andy_Code\\Desktop\\Project\\Author_Like\\correlation.csv")
