# Acknowledgement
# This code is adapted from week 10 tutorial for learning purposes

import speech_recognition as sr
import MySQLdb
import subprocess


class SpeechRecognition:
    """
    This class helps recognising users voice to run further Library 
    functionalities.

    Attributes
    ---------
    MIC_NAME: Str
        Hard Coded to identify particular Mic device to take voice inputs.
    
    Methods
    -------

    main()
        Takes in voice input to search based on the inputed voice.

    getKeyToSearch()
        Takes in voice input and runs it to check and convert in to speech using 
        googles voice recognition feature and return it as key.

    """

    MIC_NAME = "Microsoft® LifeCam HD-3000: USB Audio (hw:1,0)"

    def main(self):
        key = self.getKeyToSearch()
        if(key is None):
            print("Failed to get the search key.")
            self.main()
        return key

    def getKeyToSearch(self):

        # To test searching without the microphone uncomment this line of code
        # return input("Enter the first name to search for: ")

        # Set the device ID of the mic that we specifically want to use to avoid ambiguity
        for i, microphone_name in enumerate(sr.Microphone.list_microphone_names()):
            if(microphone_name == self.MIC_NAME):
                device_id = i
                break

        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone(device_index=device_id) as source:
            # clear console of errors
            subprocess.run("clear")

            # wait for a second to let the recognizer adjust the
            # energy threshold based on the surrounding noise level
            r.adjust_for_ambient_noise(source)

            print("Say the search key .")
            try:
                audio = r.listen(source, timeout=1.5)
            except sr.WaitTimeoutError:
                return None

        # recognize speech using Google Speech Recognition
        key = None
        try:
            key = r.recognize_google(audio)
        except(sr.UnknownValueError, sr.RequestError):
            pass
        finally:
            return key
