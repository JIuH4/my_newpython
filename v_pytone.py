import datetime
from math import ceil
import csv
import networkx as nx
import matplotlib.pyplot as plt


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

    def get_age(self):
        return ceil((datetime.date.today() - self.date_of_birth).days / 365)

    def __str__(self):
        return self.name


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


class SocialNetwork:

    def __init__(self):
        self.users = []
        self.users = nx.Graph()

    def add_user(self, new_user_s):
        if isinstance(new_user_s, list):
            for user in new_user_s:
                if isinstance(user, User):
                    self.users.add_node(user.name, user=new_user_s)
        elif isinstance(new_user_s, User):
            self.users.add_node(new_user_s.name, user=new_user_s)

    def add_friend(self, name_of_first_friend: str, name_of_second_friend: str):
        self.users.add_edge(name_of_first_friend, name_of_second_friend)

    def recomend_friend(self, name: str):
        friends = list(nx.neighbors(self.users, name))
        result = set()

        for friend in friends:
            for n in nx.neighbors(self.users, friend):
                if n != name:
                    result.add(n)

        return result.difference(set(friends))


def remove_user(self, name: str):
    if isinstance(name, str):
        try:
            self.users.remove_node(name)
        except IndexError:
            print("takogo usera net")


def export_csv(self):
    with open("vpit.csv", "wt") as f:
        w = csv.DictWriter(f, ["name", "datetime"])
        w.writeheader()

        for user in self.users.nodes:
            w.writerow(dict(name=user.name, datetime=str(user.date_of_birth)))


# def __getitem__(self, item):
#     return list(map(lambda x: str(x), list(filter(lambda x: x.name == item, self.users.nodes))))


sn = SocialNetwork()

user1 = Author("Poul", datetime.date(1987, 11, 2))
user2 = Author("Ben", datetime.date(1983, 2, 10))
user3 = Author("Chuck", datetime.date(1980, 1, 20))
user4 = Author("Chuck2", datetime.date(1980, 1, 21))
user5 = Author("Chuck3", datetime.date(1980, 1, 22))

user1.add_avatar("avatar1")
user1.add_premium_mode()
user2.add_avatar("avatar2")
user2.add_premium_mode()

sn.add_user([user1, user2, user3, user4, user5])
sn.add_friend(user1.name, user3.name)
sn.add_friend(user1.name, user5.name)
sn.add_friend(user2.name, user3.name)
sn.add_friend(user4.name, user5.name)
sn.add_friend(user3.name, user4.name)
sn.add_friend(user3.name, user5.name)

nx.draw_networkx(sn.users)
plt.show()

print([n for n in sn.recomend_friend("Poul")])
