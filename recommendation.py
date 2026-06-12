import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

import time

class Engine:
    def __init__(self,datapath):
        self.datapath=datapath
        self.df=pd.read_csv(self.datapath)

        # start=time.time()
        self.cv=TfidfVectorizer(max_features=5000,stop_words="english")
        self.vectors=self.vectored()
        # print("vec:", time.time() - start)
        
        # start=time.time()
        self.similarity_mat=cosine_similarity(self.vectors)
        # print("sim:", time.time() - start)

    
    def vectored(self):
        return self.cv.fit_transform(self.df['tags']).toarray()
    
    def top_recommendations(self,movie,n=5):
        
        movie_idx=self.df[self.df["title"]==movie].index[0]
        distances=list(enumerate(self.similarity_mat[movie_idx]))
        distances=sorted(distances,key=lambda x:x[1],reverse=True)
        
        recommendations=[]
        for i in distances[1:n+1]:
                    recommendations.append({
            "title": self.df.iloc[i[0]]['title'],
            "movie_id": self.df.iloc[i[0]]['movie_id']
        })
        return recommendations    
    
if  __name__=="__main__":
    obj=Engine("cleaned_dataset.csv")
    print(obj.top_recommendations("Harry Potter and the Philosopher's Stone"))

