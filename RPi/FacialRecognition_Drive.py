from faceRecognition import FaceRecognition
from userDB import UserDB


class FaceRecognition_Drive:
    """ 
    This class comprises of functionalities to recognise a persons face 
    and helps registering and log into the system using facial recognition techniques.
    
    Objects
    -------
    faceRecognation 
        Creates objects of FaceRecognition class.

    db
        Creates objects of UserDB class.

    Methods
    -------
    face_Recognation()
        Captures image using mounted camera and srecognises users face.

    sendToDB(name)
        Saves the captured image based user information in the database
        and matches based on the captured image.

    """
    faceRecognation = FaceRecognition()
    db = UserDB()

    def face_Recognation(self):
        result = self.faceRecognation.recognise()
        if result is None:
            self.faceRecognation.capture()
            self.faceRecognation.encode()
            result = self.faceRecognation.recognise()
            return self.sendToDB(result)
        else:
            return self.sendToDB(result)

    def sendToDB(self, name):
        """
        Parameter
        ---------
        name: str
            takes in users name based on the captured image.    

        """
        if self.db.isExist(name):
            return self.db.getUserInformation(name)
        else:
            username = name
            name = name.split('_')
            fname, lname = name
            self.db.insert(username, None, fname, lname, None)
            return self.db.getUserInformation(username)
