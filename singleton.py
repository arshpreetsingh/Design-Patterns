'''
User of that class should be allowed to create only
Single-Instance of that class.

'''

class Singleton:
    __instance = "Great-Developers"
    def __init__(self):
        if Singleton.__instance!="Great-Developers":
            raise Exception("This is not Allowed")
        else:
            Singleton.__instance=self
Singleton()
# Will through Exception at this point!
Singleton()
