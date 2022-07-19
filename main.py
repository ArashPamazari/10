
from serial import Series
from clip import Clip
from mov import Film
from Docu import Documentory
from media import Media
from actor import Actor


class main:
    def __init__(self):
        self.list = []
        line = open('dataset.csv').read().split('\n')

        for i in range(4):
            info = line[i].split(',')
            
            if info[6] == 'movie':
                film = Film({"name":info[0], 'director':info[1],'score':float(info[2]), 'url':info[3], 'duration':int(info[4]),'cast':info[5],'zhanr': info[6]})
                self.list.append(film)

            elif info[6] == 'Documentary':
                documentory = Documentory({"name":info[0], 'director':info[1],'score':float(info[2]), 'url':info[3], 'duration':int(info[4]),'cast':info[5],'zhanr': info[6]})
                self.list.append(documentory)


            elif info[6] == 'Clip':
                clip = Clip({"name":info[0], 'director':info[1],'score':float(info[2]), 'url':info[3], 'duration':int(info[4]),'cast':info[5],'zhanr': info[6]})
                self.list.append(clip)

            elif info[6] == 'Serial':
                series = Series({"name":info[0], 'director':info[1],'score':float(info[2]), 'url':info[3], 'duration':int(info[4]),'cast':info[5],'zhanr': info[6]})
                self.list.append(series)

    def AddList(self):
        print(
        '1: Film\n', 
        '2: Documentary\n', 
        '3: Clip\n', 
        '4: Series')
        menuu = int(input('enter number of menu: '))

        name = input('name: ')
        director = input('Director')
        imdb_score = int(input('IMDB Score: '))
        url = input('URL: ')
        duration = int(input('time: '))
        cast = input('Actress: ')

        if menuu == 1:
            self.list.append(Film(name, director, imdb_score, url, duration, cast))
            print('done')

        elif menuu == 2:
            sub = input('subject: ')
            self.list.append(Documentory(name, director, imdb_score, url, duration, cast, sub))
            print('done')

        elif menuu == 3:
            self.list.append(Clip(name, director, imdb_score, url, duration, cast))
            print('done')
            
        elif menuu == 4:
            episods = int(input('episodes:'))
            self.list.append(Series(name, director, imdb_score, url, duration, cast, episods))
            print('done')

    def EditList(self):
        print(
        '1: Film\n', 
        '2: Documentary\n', 
        '3: Clip\n', 
        '4: Series')
        menuu = int(input('enter number of menu: '))
        i = main.Search(self)
        if menuu == 1:
            Film.edit_Film(self.list[i])
        elif menuu == 2:
            Documentory.edit_Doc(self.list[i])
        elif menuu == 3:
            Clip.EditClip(self.list[i])
        elif menuu == 4:
            Series.Edit_Series(self.list[i])

    def DeleteList(self):
        i = main.Search(self)
        if i is not None:
            del (self.list[i])
            print('Deleted')

    def Search(self):
        name = input("search by name: ")
        for i in range (len(self.list)):
            if self.list[i]['name'] == name:
                print('done')
                break
            else:
                print('not found')

    def durationSearch(self):
        print('enter the movie time between a and b')     
        a = int(input('Enter a: '))
        b = int(input('Enter b: '))
        for i in range(len(self.list)):
            if a <= self.list[i] <= b:
                print(Media.Show_Info(i))
        else:
            print('error')

    def Saveandexit(self):
        f = open('datasetminione.csv', 'w')
        for i in self.list:
            row = str(self.list[i]['name'])+ ','+ self.list[i]['director']+ ',' + str(self.list[i]['imdbscore'])+ ',' + self.list[i]['url'] + self.list[i]['duration']+ ','+ self.list[i]['cast']+ ','+ '\n'
            f.write(row)
        f.close()
        exit()                

    def Show_list(self):
        for i in range(len(self.list)):
            print(self.list[i])

    def menu(self):
        print(
        '1: add\n', 
        '2: edit\n', 
        '3: search\n', 
        '4: serach by Duration\n',
        '5: show list\n',
        '6: delet\n',
        '7: download\n',
        '8: save and exit\n')

        while True:
            menuu = int(input('enter number of menu: '))
            if menuu == 1:
                self.AddList()
            elif menuu == 2:
                self.EditList()
            elif menuu == 3:
                self.Search()
            elif menuu == 4:
                self.durationSearch()
            elif menuu == 5:
                self.Show_list()
            elif menuu == 6:
                self.DeleteList()
            elif menuu == 7:
                Media.Download(self)
            elif menuu == 8:
                self.Saveandexit()

a = main()
a.__init__()
a.menu()
