class library():
    def __init__(self):
        self.books_name=[]
    def add_book(self,title,author):
        temp_list=[title,author]
        self.books_name.append(temp_list)
        
    def remove_book(self,title):
        for i in self.books_name:
            if title==i[0]:
                self.books_name.remove(i)
    def search_book(self,title):
        flag=False
        for i in self.books_name:
            if title==i[0]:
                flag=True
                break
        if  flag==True: print(f"we have {title}") 
        else: print(f"sorry we dont have {title}")
    def show_books(self):
        print(self.books_name)


