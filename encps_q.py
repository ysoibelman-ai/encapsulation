# question 1
class UserProfile:
    def __init__(self,username):
        self.__username = username
    @property
    def username(self):
        return self.__username

user1 = UserProfile("yaakov")
print (user1.username)
print (user1.__username)
