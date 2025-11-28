from mylibrary import library


if __name__=="__main__":
    print("barname mostaghiman ejra shod!")


book=library()
# book.add_book("riazi","sara")
# book.add_book("prog","arman")
# book.show_books()
# book.search_book("riazi")
# book.remove_book("riazi")
# book.show_books()
# book.search_book("riazi")

while True:
    print("if you wanna add books, type [add]")
    print("if you wanna remove a book, type [remove]")
    print("if you wanna search a book, type [search]")
    print("if you wanna show books list, type [show]")
    print("if you wanna exit, type [exit]")
    what_to_do=input()
    if what_to_do=="exit":
        break
    elif  what_to_do=="add":
        title=input("type yitle: ")
        authur=input("type authur name: ")
        book.add_book(title,authur)
        
    elif what_to_do=="remove":
        title=input("type title you wanna remove: ")
        book.remove_book(title)
        
    elif what_to_do=="search":
        title=input("type title of book you wanna serach: ")
        book.search_book(title)
        
    elif what_to_do=="show":
        book.show_books()
    else:
        print("Invalid command! try again.")
