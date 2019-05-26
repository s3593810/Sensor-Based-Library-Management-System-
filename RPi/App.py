#!/usr/bin/env python
from receptionist import Receptionist
import sys
from RPi import ReceptionPi
from UserDB import UserDB
from FacialRecognition_Drive import FaceRecognition_Drive


class App:
    """
    This class shows the Library Management System
    Menu options as well as ensures basic functionalities.

    ...

    Methods
    -------
    menu()
        This method shows and runs the main functionalities 
        of the Library Managment System consol application.

    """
    def menu():
        re = Receptionist()
        drive = FaceRecognition_Drive()
        receptionPi = ReceptionPi()
        print("""
    =====================================================
    *          *                    *       *  *  *       
    *          *  *               * *      *        *     
    *          *    *           *   *        * 
    *          *      *       *     *          *
    *          *        *   *       *     *       *
    * * * *    *          *         *      * *  *  *
    ======================================================
            """)
        while True:
            print("  ************MAIN MENU**************")
            choice = input("""
        1: Register
        2: Log in using username and passward
        3: Log in using face recognation
        4: Quit/Log Out

        Please enter your choice: """)

            if choice == '1':
                re.register()
            elif choice == '2':
                name = re.login()
                if name is not False:
                    receptionPi.login(name)

            elif choice == '3':
                data = drive.face_Recognation()
                receptionPi.login(name)
            elif choice == '4':
                sys.exit()
            else:
                print("You must only select either 1,2,3 or 4.")
                print("Please try again")


if __name__ == "__main__":
    App().menu()
