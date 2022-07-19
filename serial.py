from media import Media

class Series(Media):
    def __init__(self, N, D, IS, url, du, casts, Epis):
        Media.__init__(self,N,D,IS,url,du,casts)
        self.epis = Epis

    def Edit_Series(self):
        choose = input('choose 1: name','\n'
        'choose 2: imdb','\n',
        'choose 3: url','\n',
        'choose 4 : episod')
        if choose == 1:
            name = input("name: ")
            self.name = name
        elif choose == 2:
            imdbs = float(input('imdb-score :'))
            self.imdb_score = imdbs
        elif choose == 3:
            url = input('URL: ')
            self.url = url
        elif choose == 4:
            RE_Epis = int(input('new Episods: '))
            self.RE_Epis = RE_Epis
        else:
            print('Error')
    def show_info(self):
        Media.Show_Info(self)
        print ('episode:',self.RE_Epis)