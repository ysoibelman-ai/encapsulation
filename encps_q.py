# # question 1
# class UserProfile:
#     def __init__(self,username):
#         self.__username = username
#     @property
#     def username(self):
#         return self.__username

# user1 = UserProfile("yaakov")
# print (user1.username)

# # question 2
# class UserProfile:
#     def __init__(self,username,email):
#         self.__username = username
#         self.__email = email

#     @property
#     def username(self):
#         return self.__username
    
#     @property
#     def email(self):
#         return self.__email

# user1 = UserProfile("yaakov", "1@2")
# user2 = UserProfile("ephy", "1@3")
# print (user1.username, user1.email)
# print (user2.username, user2.email)

# question 3
class UserProfile:
    def __init__(self, username):
        self.__username = username

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self,new_username):
        if len(new_username) >= 3:
            self.__username = new_username
        else:
            print (f"Username too short")

p = UserProfile("alice")
p.username = "ab"
p.username = "alexis"
print (p.username)
