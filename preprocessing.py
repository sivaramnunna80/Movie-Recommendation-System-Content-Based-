import pandas as pd
import ast
from nltk.stem import PorterStemmer

df=pd.read_csv("DataSet.csv")

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df=df.dropna()

df=df.drop(columns=["Unnamed: 0","budget",'key_0',"original_language",
                    'popularity', 'production_companies',
                    'production_countries', 'release_date',
                    'revenue', 'runtime','spoken_languages',
                    'status','vote_average','vote_count',"homepage","id","original_title","title_y"])

df.rename(columns={"title_x":"title"},inplace=True)

print(df['tagline'][0])

def extracting(data):
    list=[]
    for i in ast.literal_eval(data):
        list.append(i['name'])
    return list

def extracting_cast(data):
    list=[]
    count=0
    for i in ast.literal_eval(data):
        if count!=10:
            list.append(i['name'])
            count +=1
        else:break
    return list

def extracting_crew(data):
    list=[]
    for i in ast.literal_eval(data):
        if i['job']=='Director':
            list.append(i['name'].lower())
            break
    return list

df['genres']=df['genres'].apply(extracting)
df['genres']=df['genres'].apply(lambda x:[i.replace(" ","").lower() for i in x ])

df['keywords']=df['keywords'].apply(extracting)
df['keywords']=df['keywords'].apply(lambda x:[i.replace(" ","").lower() for i in x ])

df['cast']=df['cast'].apply(extracting_cast)
df['cast']=df['cast'].apply(lambda x:[i.replace(" ","").lower() for i in x ])

df['crew']=df['crew'].apply(extracting_crew)
df['crew']=df['crew'].apply(lambda x:[i.replace(" ","").lower() for i in x ])

df['overview']=df['overview'].apply(lambda x:x.lower().split())

df['tagline']=df['tagline'].apply(lambda x:x.lower().split())

df['tag_title']=df['title'].apply(lambda x:x.replace(" ","").split())


df['tags']=df['genres']+df['keywords']+df['cast']+df['crew']+df['overview']+df['tag_title']+df['tagline']

new_df=df[['movie_id','title','tags']]

ps=PorterStemmer()
def stemming(row):
    list=[]
    for word in row:
        list.append(ps.stem(word))
    return " ".join(list)
new_df['tags']=new_df['tags'].apply(stemming)

new_df.to_csv("cleaned_dataset.csv")





