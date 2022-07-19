from media import Media
class Film(Media):
    def __init__(self,N,D,IS,url,du,casts):
        Media.__init__(self,N,D,IS,url,du,casts)
    def edit_Film(self):
        choose = int(input('choose 1 : edit imdbscore','\n'
        'choose 2 : edit url','\n'
        'choose 3 : edit casts'))
        if choose == 1:
            imdbs = float(input('imdbscore:'))
            self.imdb_score = imdbs
            print('Done')
        elif choose == 2:
            url = input('URL: ')
            self.url = url
            print('Done')
        elif choose == 3:
            casts = input('Casts: ')
            self.cast = casts
            print('Done')
        else:
            print('Error')
    def show_info(self):
        Media.Show_Info(self)
