import pandas as pd
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import messagebox

# df = pd.read_csv(
#     "https://gist.githubusercontent.com/jwalsh/ce1dc0436aba5b7a5c9666f47fa5a380/raw/5ce3854392b43ff97907112d344fc008229b0445/titanic.csv")
#
# # print(df.columns)
# # df["AgeMult"] = df["Age"].apply(lambda x: x * 2)
# # print(df[df["Survived"] > 0][["Survived", "Age", "SibSp", "Fare", "AgeMult"]].describe())
# # df["Age"].plot("hist")
# # plt.show()
#
# df=df.groupby("Sex")
# print(df["Survived"].describe())


def show_message():
    messagebox.showinfo("GUI Python", message.get())


root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")

message_button = Button(text="Click Me", command=show_message)
message_button.place(relx=.5, rely=.5, anchor="c")

root.mainloop()