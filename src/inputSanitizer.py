"""
This Python file sanitizes the raw information which accepts/rejects the format before it is added into the database.
"""

class InputSanitizer :
    def __init__(self):
        pass

    def inputSanitizer(self, pros_cred) :
        """
        Function - To merge all the checks and reply a final verdict
        Para : pros_cred - dictionary to pass to input sanitizer
        Return : boolean 
        """
        pass

    def checkLength(self, pros_cred) :
        """
        Function - To check the length of the password
        Para : pros_cred - dictionary to pass to input sanitizer
        Return : boolean
        """
        pass

    def checkSpeChar(self, pros_cred) :
        """
        Function - To create a new credential then process it through input sanitizer
        Para : pros_cred - dictionary to pass to input sanitizer
        Return : boolean
        """
        pass

    def checkPhrases(self, pros_cred) :
        """
        Function - To create a new credential then process it through input sanitizer
        Para : pros_cred - dictionary to pass to input sanitizer
        Return : boolean
        """
        pass
