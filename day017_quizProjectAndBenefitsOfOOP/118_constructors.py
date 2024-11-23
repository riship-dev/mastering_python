'''
class User:
    pass

user1 = User()
user1.name = "rishi" # Can create data members outside class unlike in C++
print(user1.name)
'''

class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0 # Default value

user1 = User(1, "rishi")