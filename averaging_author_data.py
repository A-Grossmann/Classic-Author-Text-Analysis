import pandas as pd
import csv
from sklearn import preprocessing

#Read data
data = pd.read_csv("Author_Data.csv")
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

#Get a list of Authors
Author_list = list(set(data['Author_Name'].tolist()))
print(Author_list)

#Dataframe for the values of each author
col_list = data.columns.values.tolist()
col_list.remove('Author_Name')
print(col_list)


#Creats the Dataframe of the authors means
author_df = pd.DataFrame(columns=col_list)
for Author in Author_list:
	new_data = data.drop(data.index[data['Author_Name'] != Author], inplace=False)
	new_data = new_data[['Avg Sentance Length', 'Average Word Length', 'Nouns', 'Adjectives', 'Coordinating Conjunction', 'Cardinal Number', 'Determiner', 'Preposition or Subordinating Conjunction', 'Adjective', 'Adjective, Comparative', 'Adjective, Superlative', 'Modal', 'Noun, singular or mass', 'Noun, Plural', 'Possessive Pronoun Phrase', 'Adverb', 'Adverb, Comparative', 'Verb, Base Form', 'Verb, Past Tense', 'Verb, Gerund or Present Participle', 'Verb, Past Participle', 'Verb, non-3rd Person Singular Present', 'Verb 3rd Person Singular Present', 'Wh-determiner', 'Possessive Wh-pronoun']].mean()
	new_data['Author_Name'] = Author
	print(author_df)
	author_df = author_df.append(new_data,ignore_index=True)


author_df = author_df.drop('Book Name', axis=1)
print(author_df)

#Normalizes data

#author_df = ((author_df-author_df.mean())/author_df.std())

#determining which features vary the greatest as a ratio of their mean
author_df = (author_df.var())/(author_df.mean())

author_df.to_csv("C:\\Users\\Andy_Code\\Desktop\\Project\\Author_Like\\Author_Averages.csv")


#The Following features showed the heighest variance arount the mean to keep for the model: 
'''
 'Determiner', 'Possessive Pronoun Phrase', 
sent_length, word_length, ,'Nouns','Adjectives', 'Possessive Pronoun Phrase', 
'Verb 3rd Person Singular Present', 'Possessive Pronoun Phrase', 'Noun, singular or mass', 'Modal', Avg Sentance Length','Nouns'
'''

