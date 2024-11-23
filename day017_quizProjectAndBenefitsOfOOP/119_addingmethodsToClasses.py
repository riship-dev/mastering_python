class User:
    def __init__(self, user_id, username):
        self.username = username
        self.user_id = user_id
        self.followers = 0
    
    def follow(self, user):
        user.followers += 1

user1 = User(1, "rishi")
user2 = User(2, "john doe")

user1.follow(user2)
print(user2.followers)