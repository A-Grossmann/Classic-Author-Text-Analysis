from sklearn.model_selection import train_test_split 
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


#Read data
data = pd.read_csv("Author_Data.csv")
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

#Encode Author names
all_author_list = data['Author_Name'].tolist()
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
authors_encoded=le.fit_transform(all_author_list)
print(authors_encoded)


#Data was normalized and analized in a csv file using the following:
'''
Normalized_data = data.drop(['Book Name','Author_Name'],axis=1)
Normalize data
Normal = Normalized_data.std()
Normalized_data = (Normalized_data-Normalized_data.mean())/Normalized_data.std()
Normalized_data.to_csv("C:\\Users\\Andy_Code\\Desktop\\Project\\Author_Like\\Normalized_data.csv")
Normal.to_csv("C:\\Users\\Andy_Code\\Desktop\\Project\\Author_Like\\Normal.csv")
'''

#The Following features were kept: 
'''
'Cardinal Number', 'Determiner', 'Preposition or Subordinating Conjunction', 'Adjective', 'Adjective, Comparative', 'Adjective, Superlative', 'Modal', 'Noun, singular or mass', 'Noun, Plural', 'Possessive Pronoun Phrase', 'Adverb', 'Adverb, Comparative', 'Verb, Base Form', 'Verb, Past Tense', 'Verb, Gerund or Present Participle', 'Verb, Past Participle', 'Verb, non-3rd Person Singular Present', 'Verb 3rd Person Singular Present', 'Wh-determiner', 'Possessive Wh-pronoun'
sent_length, word_length, ,'Nouns','Adjectives', 'Possessive Pronoun Phrase', 'Verb, non-3rd Person Singular Present', 'Determiner',
'''
#The rest below were dropped:
data = data.drop(['Book Name','Coordinating Conjunction', 'Cardinal Number', 
	'Preposition or Subordinating Conjunction', 'Adjective', 'Adjective, Comparative',
	'Adjective, Superlative', 'Modal', 'Noun, singular or mass', 'Noun, Plural', 
	'Adverb',  'Verb, Base Form', 'Verb, Past Tense', 'Verb, Gerund or Present Participle',
	'Wh-determiner','Adverb, Comparative','Verb, Past Participle',  'Verb 3rd Person Singular Present',
	'Possessive Wh-pronoun'],axis=1)


#Make two sets one with the features,X, and one with the classifiers,Y.
X = data.drop(['Author_Name'],axis=1) 
Y = data['Author_Name']

#Normalize remaining data
data_columns = X.columns.values.tolist()
X = (X-X.mean())/X.std()

# Splitting the dataset into 80% training data and 20% testing data.
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.20, random_state=0)

#Create KNN Classifier
knn = KNeighborsClassifier(n_neighbors=3)
print(knn)

#Train the model using the training sets
knn.fit(X_train, Y_train)

#Predict the response for test dataset
y_pred = knn.predict(X_test)

# Model Accuracy
print("Accuracy:",metrics.accuracy_score(Y_test, y_pred))

#Loop to find the best number of neighbors
nu_neighbors = [1,2,3,4,5,6,7,8,9,10]
for nu in nu_neighbors:
	print(nu)
	knn = KNeighborsClassifier(n_neighbors=nu)
	knn.fit(X_train, Y_train)
	y_pred = knn.predict(X_test)
	print("Accuracy:",metrics.accuracy_score(Y_test, y_pred))
