

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import words
from nltk.corpus import stopwords
import os
import csv
import nltk
import pandas as pd
import matplotlib.pyplot as plt



class text_analysis:

	def __init__(self,file):
		#Open previous csv/dataframe file
		Author_df = pd.read_csv('Author_Data.csv')
		#delete empty made columns
		Author_df = Author_df.loc[:, ~Author_df.columns.str.contains('^Unnamed')]
		self.attribute_list =[]
		self.file = file
		self.delimiters = ['\n', ' ', " ",',', '.', '?', '!', ':','www', '[',']','*','_','(',')','/','0','1','2','3','4','5','6','7','8','9','@',"'",'"','-','%','$','#','�']
		self.tags_dict = {
		'CC': 'Coordinating Conjunction','CD':'Cardinal Number','DT':'Determiner','IN':'Preposition or Subordinating Conjunction','JJ':'Adjective',
'JJR':'Adjective, Comparative','JJS':'Adjective, Superlative','MD':'Modal','NN':'Noun, singular or mass','NNS':'Noun, Plural','PRP':'Personal Pronoun Phrase',
'PRP':'Possessive Pronoun Phrase','RB':'Adverb','RBR':'Adverb, Comparative','VB':'Verb, Base Form','VBD':'Verb, Past Tense','VBG':'Verb, Gerund or Present Participle',
'VBN':'Verb, Past Participle','VBP':'Verb, non-3rd Person Singular Present','VBZ':'Verb 3rd Person Singular Present','WDT':'Wh-determiner',
'WP':'Wh-pronoun','WP':'Possessive Wh-pronoun'
		}
		self.tag_type_list = list(self.tags_dict.keys())
		self.tag_name_list = list(self.tags_dict.values())
		self.text_master_list = text_analysis.text_to_list(file,'utf-8',self.delimiters)
		self.content = open(file).read()
		self.author_name,self.book_name = text_analysis.pop_author_from_title(file)	
		self.attribute_list.append(self.author_name)
		self.attribute_list.append(self.book_name)
		print(self.attribute_list)
		self.sentance_list = text_analysis.sentances_return(file)
		self.average_sent_length = text_analysis.average_sentance_length(self.sentance_list)
		self.attribute_list.append(self.average_sent_length)
		print('Average Sentance Length:{}'.format(self.average_sent_length))
		self.text_without_stop_words = text_analysis.text_no_stop(self.text_master_list)
		self.text_tolkenized_dict = text_analysis.tolkenize_freq_list(self.text_master_list)
		self.list_of_keys =list(self.text_tolkenized_dict.keys())
		self.only_english_words = text_analysis.only_english_words(self.text_tolkenized_dict)
		self.average_word_len = text_analysis.average_word_length(self.only_english_words)
		self.attribute_list.append(self.average_word_len)
		print('Average Word Length:{}'.format(self.average_word_len))
		self.total = text_analysis.tolkenizer_totaler(self.only_english_words)
		self.perc_noun = text_analysis.percent_noun(self.only_english_words, self.total)
		self.attribute_list.append(self.perc_noun)
		print('% Nouns:{}'.format(self.perc_noun))
		self.perc_adj = text_analysis.percent_adjs(self.only_english_words, self.total)
		self.attribute_list.append(self.perc_adj)
		print('% Adjatives:{}'.format(self.perc_adj))
		text_analysis.print_all_tag_percent(self,self.only_english_words,self.total,self.tags_dict)
#		self.attribute_list.append(' ')
		print(len(self.attribute_list))
		print(self.attribute_list)
		print(Author_df)
#		Author_df.loc[:,~Author_df.columns.str.match("Unnamed")]
#		print(Author_df)
		Author_df.loc[len(Author_df)] = self.attribute_list 
#		print(Author_df)
		
		print(Author_df)
		#Add entry to dictionary
		Author_df.to_csv("C:\\Users\\Andy_Code\\Desktop\\Project\\Author_Like\\Author_Data.csv")
		#Add a if clause or replace clause that doesnt allow you to rewrite over it
#		author_analysis.loc[len(zuthor_analysis.index)] = [self.author_name, self.book_name, self.average_sent_length,self.average_word_len,self.perc_nouns,self ...]

	def pop_author_from_title(filename):
		filename = filename.replace('.txt','')
		filename_list = filename.split('_')
		Author_Name = f'{filename_list[1]}, {filename_list[0]}'
		print(Author_Name)
		Book_Name =''
		for i in range(2,len(filename_list)):
			Book_Name += filename_list[i] + ' '
		print(Book_Name)
		return Author_Name, Book_Name
		
	def text_to_list(file,encode,delimiters):
	#	Takes a text file and produces a list of all the words and symbols. 
	#	delimiters must be defined as a list.   

		with open(file,encoding = encode) as content:
			words = content
			for delimiter in delimiters:
			    master_word_list = []
			    for word in words:
			    	master_word_list += word.split(delimiter)
			    	words = master_word_list

	#	filtering out all blank enteries
		master_word_list = list(filter(lambda x: (x != ''), master_word_list))
		
	#	making list into lower case for uniformity
		for i in range(len(master_word_list)):
		    master_word_list[i] = master_word_list[i].lower()
		return master_word_list



	def tolkenize_freq_list(master_word_list):
		tolkenized_dict = {}
		for word in master_word_list:
		        if tolkenized_dict.get(word) == None:
		                tolkenized_dict[word] = 1	                
		        else:
		                tolkenized_dict[word] += 1
		return tolkenized_dict

	def only_english_words(dic):
	#	return only english words in a tolkenized dictionary using a librairy 
		new_dict = {}
		vocab = words.words()
		for word in vocab:
			new_dict[word] = dic.pop(word,None)

	#	delete all 'None' value enteries
		for key, value in dict(new_dict).items():
			if value == None:
				del new_dict[key]
		return new_dict

	def return_type(dic,type_tag):
		type_list = []
		for sentence in dic:
			for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
				if (pos == type_tag):
					type_list.append(word)
		for x in type_list:
			if x == 'not':
				type_list.remove(x)	
		return type_list

	def return_nouns(dic):
		#Returns nouns list from tolkenized dictionary
		nouns = []
		for sentence in dic:
			for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
				if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
					nouns.append(word)
		return nouns

	def return_adjs(dic):
		#Returns adjitives list from tolkenized dictionary
		adjs = []
		for sentence in dic:
			for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
				if (pos == 'JJ' or pos == 'JJR' or pos == 'JJS'):
					adjs.append(word)
		return adjs



	def tolkenizer_totaler(dic):
		#Totals all values
		total = sum(dic.values())
		return total

	def key_value_from_list(keys,dic):
		#keys are a list of keys in the dictionary
		total_values = 0
	#	counter = 0
		for item in keys:
			total_values+=dic[item]
			# counter += 1
		return total_values

	def percent_total(total_count_in_dic, total_count):
		percent_tot = total_count_in_dic/total_count
		return percent_tot

	def percent_noun(words,total):
		nouns = text_analysis.return_nouns(words)
		total_nouns = text_analysis.key_value_from_list(nouns,words)
		perc_nouns = round((text_analysis.percent_total(total_nouns,total))*100, 3)
		return perc_nouns

	def percent_adjs(words,total):
		adjs = text_analysis.return_adjs(words)
		total_adjs = text_analysis.key_value_from_list(adjs,words)
		percent_adjs = round((text_analysis.percent_total(total_adjs,total))*100,3)
		return percent_adjs

	def percent_type(words,total,tag_type):
		type_words = text_analysis.return_type(words,tag_type)
		total_type_words = text_analysis.key_value_from_list(type_words,words)
		percent_type = round((text_analysis.percent_total(total_type_words,total))*100,3)
		return percent_type

	def printing_type(self,words,total,tag_type,tag_name):
		#words are the words included in the text, total is the total words, tag type is the tag for the nltk dictionary, tag_name is the name for the tag
		percent = text_analysis.percent_type(words,total,tag_type)
		print('% {}:{}'.format(tag_name,percent))
		self.attribute_list.append(percent)
#		tag_name = tag_name.remove("'",'')
#		self.tag_name = percent
#		print(locals())
		return percent

	def print_all_tag_percent(self,words,total,tags_dictionary):
		for tag,name in tags_dictionary.items():
			text_analysis.printing_type(self,words,total,tag,name)

	def text_no_stop(data):
		#uses nltk stopwords library to eliminate them from list
		stopWords = set(stopwords.words('english'))
		wordsFiltered = []
		for w in data:
			if w not in stopWords:
				wordsFiltered.append(w)
		return wordsFiltered

	def freq_plot(text,list_of_words):
		plt.figure(figsize=(14, 8))  # change figsize to (width, height), the size you want
		nltk.draw.dispersion.dispersion_plot(text, list_of_words, title="Frequency of Words")

	def sentances_return(file):
		#returns sentances of a file
		text = open(file).read()
		sentances = nltk.tokenize.sent_tokenize(text)
		delimiters = ['\n']
		for delimiter in delimiters:
			master_word_list = []
			for sentance in sentances:
				master_word_list += sentance.split(delimiter)
				words = master_word_list
		master_word_list = list(filter(lambda x: (x != ''), master_word_list))
		return master_word_list

	def average_sentance_length(sentance_list):
		no_of_sentances = len(sentance_list)
		total = 0
		for sentance in sentance_list:
			total+=len(sentance)
		average = round((int(total)/int(no_of_sentances)),3)
		return average

	def average_word_length(words):
		no_of_words = len(words)
		total = 0
		for word in words:
			total+=len(word)
		average = round((int(total)/int(no_of_words)),3)
		return average



#Create instances for all txt files in the directory

path_of_the_directory = 'C:\\Users\\Andy_Code\\Desktop\\Project\\Author_Like'
ext = ('.txt')
for file in os.listdir(path_of_the_directory):
    if file.endswith(ext):
    	print(f'{file}')
    	file = text_analysis(f'{file}') 
    else:
        continue


