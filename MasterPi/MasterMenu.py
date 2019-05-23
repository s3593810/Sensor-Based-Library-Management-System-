import MySQLdb
from sampleinsert import SamInsert
from add_event import Add_event
from MasterDrive import MasterDrive
import datetime
from datetime import datetime

event = Add_event()
getDetails = SamInsert()

class Menu:
    """

  
    
    Methods
    -------
   
    runMenu()
        Prints out all the master py menu options 
        for user to select.

    
    """
    drive=MasterDrive()
    def runMenu(self, user):

        while(True):
            print("Welcome {}".format(user["firstname"]))
            self.drive.insertUser(user)
            print("1. Search a Book")
            print("2. Borrow a Book")
            print("3. Return a Book")
            print("4. Logout")
            selection = input("Select an option: ")
            print()

            if(selection == "1"):
                self.search()
            elif(selection == "2"):
                self.drive.BorrowBook()
            elif(selection == "3"):
                self.drive.ReturnBook()
            elif(selection == "4"):
                break
            else:
                print("Invalid input - please try again.")

    def search(self):
        print("1.Search by ID")
        print("2.Search by Title")
        print("3.Search by Author")
        print("4.Search by PublishedDate")
        
        selection = input("Select an option: ")
        if(selection == "1"):
                self.drive.SearchID(self.drive.searchOptions(selection))
        elif(selection == "2"):
                self.drive.SearchTitle(self.drive.searchOptions(selection))
        elif(selection == "3"):
                self.drive.SearchAuthor(self.drive.searchOptions(selection))
        elif(selection == "4"):
                self.drive.SearchDate(self.drive.searchOptions(selection))
    


