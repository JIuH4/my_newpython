import datetime
from math import ceil


class User:

    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
        self.friends = []

    def get_age(self):
        return ceil((datetime.date.today() - self.date_of_birth).days / 365)

    def get_friends(self):
        return self.friends

    def add_friends(self, new_friend_s):

        if isinstance(new_friend_s, list):
            for user in new_friend_s:
                if isinstance(user, User):
                    if self.friends.count(user) == 0 and self != user:
                        self.friends.append(user)
        elif isinstance(new_friend_s, User):
            self.friends.append(new_friend_s)


user1 = User("Poul", datetime.date(1987, 11, 2))
user2 = User("Ben", datetime.date(1983, 2, 10))
user3 = User("Chuck", datetime.date(1980, 1, 20))

user1.add_friends([user1, user2, user3, user3, "DSFA"])
user2.add_friends([user1, user2, user3, user3, "DSFA"])
user3.add_friends([user1, user2, user3, user3, "DSFA"])

print(user1.name, user1.get_age(), [u.name for u in user1.friends])

print(user2.name, user2.get_age(), [u.name for u in user2.friends])
print(user3.name, user3.get_age(), [u.name for u in user3.friends])
