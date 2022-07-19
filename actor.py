class Actor :
    def __init__(self , name , family , AW):
        self.name = name
        self.family = family
        self.Award = AW



    def show(self):
        print('name:',self.name , 'family:',self.family,'award:',self.Award)

