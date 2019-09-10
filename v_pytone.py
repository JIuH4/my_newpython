import datetime
from math import ceil


class Avatar:
    avatar_url = "net avatara"

    def add_avatar(self, url: str):
        if isinstance(url, str):
            self.avatar_url = url


class PremiumMode:
    premium_enabled = False

    def add_premium_mode(self):
        self.premium_enabled = True


class User(Avatar, PremiumMode):

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


class Author(User):
    def __init__(self, name, date_of_birth):
        super().__init__(name, date_of_birth)
        self.posts = []

    def add_post(self, post_content: str):
        if isinstance(post_content, str):
            self.posts.append(post_content)

    def remove_post(self, post_index: int):
        if isinstance(post_index, int):
            try:
                self.posts.pop(post_index - 1)
            except IndexError:
                print("takogo posta net")


user1 = Author("Poul", datetime.date(1987, 11, 2))
user2 = Author("Ben", datetime.date(1983, 2, 10))
user3 = Author("Chuck", datetime.date(1980, 1, 20))

user1.add_friends([user1, user2, user3, user3, "DSFA"])
user2.add_friends([user1, user2, user3, user3, "DSFA"])
user3.add_friends([user1, user2, user3, user3, "DSFA"])

print(user1.name, user1.get_age(), [u.name for u in user1.friends])
print(user2.name, user2.get_age(), [u.name for u in user2.friends])
print(user3.name, user3.get_age(), [u.name for u in user3.friends])

user1.add_post("11")
user1.add_post("22")
user1.add_post("33")

user1.remove_post(1)
user1.remove_post(6)

print(user1.posts)

user1.add_avatar("avatar1")
user1.add_premium_mode()
user2.add_avatar("avatar2")
user2.add_premium_mode()

print(user1.avatar_url, user1.premium_enabled)
print(user2.avatar_url, user2.premium_enabled)
print(user3.avatar_url, user3.premium_enabled)
