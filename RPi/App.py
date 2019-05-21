#!/usr/bin/env python
from receptionist import Receptionist
import sys
import RPi
from FacialRecognition_Drive import FaceRecognition_Drive


class App:
    def menu():
        re = Receptionist()
        drive = FaceRecognition_Drive()
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
                    RPi.login(name)
            elif choice == '3':
                data = drive.face_Recognation()
                RPi.login(data)
            elif choice == '4':
                sys.exit()
            else:
                print("You must only select either 1,2,3 or 4.")
                print("Please try again")


if __name__ == "__main__":
    App().menu()
