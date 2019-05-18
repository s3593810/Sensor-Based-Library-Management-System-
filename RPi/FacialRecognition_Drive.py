from faceRecognition import FaceRecognition
from userDB import UserDB


class FaceRecognition_Drive:
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
        if self.db.isExist(name):
            return self.db.getUserInformation(name)
        else:
            username = name
            name = name.split('_')
            fname, lname = name
            self.db.insert(username, None, fname, lname, None)
            return self.db.getUserInformation(username)
