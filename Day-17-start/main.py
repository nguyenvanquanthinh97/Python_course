class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follows(self, user):
        self.followers += 1
        user.following += 1

    def __str__(self):
        return "id: {}, username: {}, followers: {}, following: {}".format(self.id, self.username, self.followers, self.following)


user_01 = User("001", "Leo")
user_02 = User("002", "John")
user_01.follows(user_02)

print(user_01)
print(user_02)
