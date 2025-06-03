"""
The Python file containing all the functions to perform CRUD operations on the credentials.
"""

class CredentialManager :
    def __init__(self):
        pass

    def createCred(self, raw_cred) :
        """
        Function - To create a new credential then process it through input sanitizer
        Para : raw_cred - dictionary to pass to input sanitizer
        Return : result of Input sanitizer
        """
        pass

    def addCred(self, pros_cred) :
        """
        Function - To add the processed credential into the database
        Para : pros_cred - the processed credential dictionary to pass to add it in database
        Return : Null
        """
        pass

    def fetchCred(self, read_login) :
        """
        Function - To fetch a existing credential from the database
        Para : read_login - string to match the login id to fetch the password
        Return : the dictionary of login id and password
        """
        pass

    def updateCred(self, raw_cred) :
        """
        Function - To create a new credential 
        Para : raw_cred - dictionary to pass to add it in database
        Return : Null
        """
        pass

    def deleteCred(self, read_login) :
        """
        Function - To create a new credential 
        Para : raw_cred - dictionary to pass to add it in database
        Return : Null
        """
        pass

    