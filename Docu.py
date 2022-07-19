from media import Media
class Documentory(Media):
    def __init__(self, N, D, IS, url, du, casts, sub):
        Media.__init__(self,N,D,IS,url,du,casts)
        self.sub = sub
    def edit_Doc(self):
        choose = int(input('choose 1: enter your name , choose 2 : enter your url , choose 3 : enter your subject '))
        if choose == 1:
            Replace_name = input("enter your name: ")
            self.name = Replace_name
        elif choose == 2:
            Replace_url = input('enter ypur url: ')
            self.url = Replace_url
        elif choose == 3:
            Replace_sub = input('enter your subject: ')
            self.sub = Replace_sub
        else:
            print('error')
    def show_info(self):
        Media.Show_Info(self)
        print('Subject:', self.sub)




