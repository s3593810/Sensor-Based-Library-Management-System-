# LMS
PIoT 

This project is about creating a smart library system using Raspberrypi Model 3B device, along with webcamera.

This project used 
-2 Raspbery Pi devices
-Scoket Programming to Communicate between 2 devices
-Google cloud storage for database storage.
-Used Voice Recognition techniques as well as facial recognition techniques.

Finally as an user this system works as:
There is a reception pi where an user can walk up to login to the system. 
The user can either login using manual typing or using facial recognition.
Once Logged in the Master pi starts running and shows Library Managment Menu options.
Where user can search for book, borrow a book, return a book and logout.

For search options user can search by ID, Name, Title and Publication date of the book.
To borrow a book either user can user QR Code scanning or by Manual means.
To return a book user can use QR code or by manual means using keyboard.

The admin of the libary can use a website (falsk based) to add, remove and see reports or generate visualization about 
the performance of the library.
A flask api is used underneath to maintain communication betwwen website and cloud databe. 
