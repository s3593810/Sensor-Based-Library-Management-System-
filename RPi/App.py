from receptionist import Receptionist
import sys
import RPi
from userDB import UserDB
# from pi_opencv.drive import Drive


def menu():
    re = Receptionist()
    while True:

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
        print("  ************MAIN MENU**************")

        choice = int(input("""
 1: Register
 2: Log in using username and passward
 3: Log in using face recognation
 4: Quit/Log Out

 Please enter your choice: """))

        if choice == 1:

            re.register()
        elif choice == 2:
            name = re.login()
            if name is not False:
                RPi.connect(name)
        elif choice == 3:
            # facial recognition
            db = UserDB()
            db.getUserInformation("a")

            # drive = Drive()
            # RPi.connect(drive.face_Recognation())
        elif choice == 4:
            sys.exit()
        else:
            print("You must only select either 1,2,3 or 4.")
            print("Please try again")
            menu()


menu()
