import numpy as np
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from nltk import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

movies=pd.read_csv('pro_movies.csv')
credits=pd.read_csv('pro_credits.csv')
#print(movies.head(5))
#print(credits.head(5))

#merge dataframe
movies = pd.merge(movies, credits, on='title')
print(movies.info())


'''
Valuable columns
genres, id, keywords, title, overview, cast, crew
'''
# updating ......
movies=movies[['movie_id','title','overview','genres','keywords','cast','crew']]

#movies.isnull().sum()
movies.dropna(inplace=True)

#print(movies.duplicated().sum())
#in dict ,converting to list
# yeh object jo hoga string h but yeh function list mien convert karega



def convert(obj):
    L=[]
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L


def convert2(obj):
    L=[]
    counter=0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter+=1              # bcz we only want first three cast name
        else:
            break
    return L


def fetch_dir(obj):
    L=[]
    for i in ast.literal_eval(obj):
        if i['job']=='Director':
            L.append(i['name'])
            break
    return L

def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    
    return " ".join(y)

def recommend(movie):
    index = df[df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True, key=lambda x: x[1])[1:6]
    for i in distances:
        print(df.iloc[i[0]].title)
    return

print('******************************************')
print()
#print(movies.iloc[0].cast)
#it returns thelst of dict that have all cast
#       Extracting all necessary names and data from lsit of dict. to list by using functions defined


movies['genres']=movies['genres'].apply(convert)
movies['keywords']=movies['keywords'].apply(convert)
movies['cast']=movies['cast'].apply(convert2)
movies['crew']=movies['crew'].apply(fetch_dir)
movies['overview']=movies['overview'].apply(lambda x:x.split())

movies['genres']=movies['genres'].apply(lambda x:[i.replace(" ","")for i in x])
movies['keywords']=movies['keywords'].apply(lambda x:[i.replace(" ","")for i in x])
movies['cast']=movies['cast'].apply(lambda x:[i.replace(" ","")for i in x])
movies['crew']=movies['crew'].apply(lambda x:[i.replace(" ","")for i in x])

#creating new columns

movies['tags']=movies['overview']+movies['genres']+movies['keywords']+movies['cast']+movies['crew']
df=movies[['movie_id','title','tags']]
df['tags']=df['tags'].apply(lambda x: " ".join(x))


cv=CountVectorizer(max_features=5000,stop_words='english')
vectors=cv.fit_transform(df['tags']).toarray()


ps=PorterStemmer()
df['tags']=df['tags'].apply(stem)
similarity=cosine_similarity(vectors)


pickle.dump(df.to_dict(),open('movies.pkl','wb'))
pickle.dump(similarity,open('similarity.pkl','wb'))

