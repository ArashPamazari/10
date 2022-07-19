from media import Media
class Clip(Media):
    def __init__(self,N,D,IS,url,du,casts,mu,cat):
        Media.__init__(self,N,D,IS,url,du,casts)
        self.music= mu
        self.categories = cat
    def EditClip(self):
        choose = int(input('choose 1 for replace name','\n', 
            'choose 2 for replace url','\n',
            'choose 3 for replace categories'))
        if choose == 1:
            Replace_name = input('Enter your name: ')
            self.name = Replace_name
        elif choose == 2:
            Replace_url = input('Enter your url: ')
            self.url = Replace_url
        elif choose == 3:
            Replace_categories = input('Enter your category name: ')
            self.categories = Replace_categories
        else:
            print('error')
    
    def show_info(self):
       Media.Show_Info(self)
       print('the cat is:', self.categories, "the music is :" , self.music)

