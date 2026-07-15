# # question 1
# class UserProfile:
#     def __init__(self,username):
#         self.__username = username
#     @property
#     def username(self):
#         return self.__username

# user1 = UserProfile("yaakov")
# print (user1.username)

# question 2
class UserProfile:
    def __init__(self,username,email):
        self.__username = username
        self.__email = email

    @property
    def username(self):
        return self.__username
    
    @property
    def email(self):
        return self.__email

user1 = UserProfile("yaakov", "1@2")
user2 = UserProfile("ephy", "1@3")
print (user1.username, user1.email)
print (user2.username, user2.email)


    


