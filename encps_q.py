# question 1
class UserProfile:
    def __init__(self,username):
        self.__username = username
    @property
    def username(self):
        return self.__username

user1 = UserProfile("yaakov")
print (user1.username)

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

# question 4
class UserProfile:
    def __init__(self,username):
        self.__username = username
        self.__followers = 0

    @property
    def followers (self):
        return self.__followers
    
    def add_follow (self,):
        self.__followers += 1
    
    def unfollow (self):
        if self.__followers >=1:
            self.__followers -= 1
        else:
            print ("no followers to unfollow (: ")
        
profile1 = UserProfile("yaakov")
profile1.add_follow()
profile1.add_follow()
profile1.add_follow()

profile1.unfollow()
print (profile1.followers)

# question 5
class UserProfile:
    def __init__(self, username,bio):
        self.username = username
        self._bio = bio

    @property
    def bio (self):
        return self._bio
    
class VerifiedUser (UserProfile):
    def __init__(self, username, bio,badge):
        super().__init__(username, bio)
        self.badge = badge

    def full_description(self):
        print(f"{self.username} {self.badge}: {self.bio}")
vu = VerifiedUser("player", "quarterback", "&&&")
vu.full_description()

# question 6
class UserProfile:
    def __init__(self, username,age):
        self.username = username
        self.__age = age
    
    @property
    def age (self):
        return self.__age
    @age.setter
    def age (self, new_age):
        if 13<=new_age<=120:
            self.__age = new_age
        else:
            print ("invalid age")

user1 = UserProfile("yaakov", 26)
user1.age = 10
user1.age = 200
user1.age = 25
print (user1.age)

# question 7
class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
    
    def check_password (self,attempt):
        if attempt == self.__password:
            return True
        else:
            return False
    
    def change_password(self,old,new):
        if old == self.__password:
            self.__password = new
        else:
            print ("Incorrect old Password")

user1 = UserAccount("yaakov", 123456)
print (user1.check_password(1233456))
user1.change_password(123456,654321)
print (user1.check_password(654321))


# question 8 
class Post:
    def __init__(self, author,content):
        self.author = author
        self.content = content
        self.__likes = 0
        self.__liked_by = []
    @property
    def likes(self):
        return self.__likes
    
    def like (self,username):
        if username not in self.__liked_by:
            self.__liked_by.append(username)
            self.__likes +=1

    def unlike (self,username):
        if username  in self.__liked_by:
            self.__liked_by.remove(username)
            self.__likes -= 1

    def status (self):
        print (f"Post by {self.author}: {self.__likes} likes")
post1 = Post("yaakov","Hello World")

post1.like("ephraim")
post1.like("shmuel")
post1.like("Chaim")
post1.unlike("ephraim")
post1.like("shmuel")
post1.status()

# question 9
class UserProfile:
    def __init__(self, username):
        self.username = username
        self.__is_public = True
        self.__show_email = False
        self.__show_age = False

    @property
    def is_public (self):
        return self.__is_public
    
    @is_public.setter
    def is_public(self,value):
        if type(value) == bool:
            self.__is_public = value
        else:
            print (f"(value) must be True or False")

    @property
    def show_email (self):
        return self.__show_email
    
    @show_email.setter
    def show_email(self,value):
        if type(value) == bool:
            self.__show_email = value
        else:
            print (f"(value) must be True or False")

    @property
    def show_age (self):
        return self.__show_age
    
    @show_age.setter
    def show_age(self,value):
        if type(value) == bool:
            self.__show_age = value
        else:
            print (f"(value) must be True or False")

    def privacy_summary (self):
        print (f"Show Age: {self.show_age} | Show Email: {self.show_email} | Is Public: {self.is_public} ")

user1 = UserProfile("yaakov")
user1.is_public = True
user1.show_age = 123
user1.privacy_summary()


# question 10
class UserAccount:
    def __init__(self,username,email,password,age):
        self.__username = username
        self.__email = email
        self.__password = password
        self.__age = age
        self._login_count = 0

    @property
    def username (self):
        return self.__username
    @username.setter
    def username(self,new):
        if len(new) >=3:
            self.__username = new
        else:
            print("invalid new username")

    @property
    def email (self):
        return self.__email
    @email.setter
    def email (self,new):
        if '@' in new:
            self.__email = new
        else:
            print ("invalid email")

    @property
    def age (self):
        return self.__age
    @age.setter
    def age (self,new):
        if 13 <= new <= 120:
            self.__age = new
        else:
            print ("invalid age")

    def check_password (self,attempt):
        if attempt == self.__password:
            return True
        else:
            print ("passwords to not match")
    
    def change_password(self,old, new):
        if old == self.__password:
            self.__password = new
        else:
            print ("invalid old password")

    def login(self, password):
        if password == self.__password:
            self._login_count += 1
        else:
            print("Login Failed")

    def account_summary(self):
        print ("Username:", self.username)
        print ("Email:", self.email)
        print ("Age:", self.age)
        print("Login Count", self._login_count)

user1 = UserAccount ("yaakov", "1@3", 12345, 26)
user1.login("12345678")
user1.login("12348")
user1.login(12345)
user1.age = 34
user1.email = "234@123"
user1.account_summary()


    


