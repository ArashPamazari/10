from pytube import YouTube 
from actor import Actor 
class Media:
    def __init__(self,N,D,IS,url,du,casts):
        self.name = N
        self.director = D
        self.imdb_score = IS
        self.url = url
        self.duration = du
        self.cast = casts 

    def Show_Info(self):
        print('Name:', self.name,'\n',
         'Director:', self.director,'\n', 
         'IMDB_Score:', self.imdb_score,'\n', 
         'URL:',self.url,'\n', 
         'Duration:', self.duration, '\n', 
         'Casts:', self.cast)
         
    def casts(self):
        casts = self.cast.split(" , ")
        for actor in casts:
            Actor(actor).show()

    def Download(self):
        try:
            YouTube(input("enter url")).streams.first().download()
            print("Done")
        except:
            print("error")

    