from database_books import DatabaseBooks

class Menu:
    def main(self):
        with DatabaseBooks() as db:
            db.createBookTable()
        self.runMenu()

    def runMenu(self):
        while(True):
            print()
            print("1. List Books")
            print("2. Insert Books")
            print("3. Search Books")
            print("4. Delete Book")
            print("5. Quit")
            selection = input("Select an option: ")
            print()

            if(selection == "1"):
                self.listBooks()
            elif(selection == "2"):
                self.insertBook()
            elif(selection == "3"):
                self.searchBooks()
            elif(selection == "4"):
                self.deleteBook()   
            elif(selection == "5"):
                print("Goodbye!")
                break
            else:
                print("Invalid input - please try again.")

    def listBooks(self):
        print("--- Books ---")
        print("{:<7} {:<20}  {:<10}  {}".format("BookID", "Title", "Author", "PublishedDate"))
        with DatabaseBooks() as db:
            for book in db.getBooks():
                print("{:<7}  {:<20}  {:<10}  {}".format(book[0], book[1], book[2], book[3]))

    def insertBook(self):
        print("--- Insert Book ---")
        name = input("Enter the Book's Name: ")
        author = input("Enter the Book's Author Name: ")
        publish = input ("Enter the Book's Published Date: ")

        with DatabaseBooks() as db:
            if(db.insertBook(name, author, publish)):
                print("{} inserted successfully.".format(name))
            else:
                print("{} failed to be inserted.".format(name))

    def searchBooks(self):
        print("--- Search Books Choose Search Method ---")
        print("1. Search by Title")
        print("2. Search by Author")
        print("3. Search by Publication Date")
        selection = input("Select an option: ")
        print()
        if(selection == "1"):
           self.searchName()
           print ("alu")

        elif(selection == "2"):
            author=("Insert the Author Name: ")
            self.searchByAuthor(author)
        elif(selection == "3"):
            publish=("Insert the Published Date: ")
            self.searchByPublish(publish)
        else:
            print("Invalid input - please try again.")

    def deleteBook(self):
         print("--- Delete Books ---")
         name = input("Enter the Book's Name: ")
         
    def searchName(self):
        name=("Insert the Book Title: ")
        with DatabaseBooks() as db:
            for book in db.searchByName(name):
                print("{:<7} {:<20}  {:<10}  {}".format("BookID", "Title", "Author", "PublishedDate"))
                print("{:<7}  {:<20}  {:<10}  {}".format(book[0], book[1], book[2], book[3]))


if __name__ == "__main__":
    Menu().main()
