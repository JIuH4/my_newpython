def function_name(x):
    return x * x


print(function_name(2))


def is_al_to_smock(age: int) -> bool:
    if age > 18:
        return True
    elif age == 18:
        return True

    else:
        return False


def check(age):
    if is_al_to_smock(age):
        return "mozno"
    else:
        return "nelzya"


print(check(19))

i = 0
while i < 100:
    i += 1

my_list = range(2, 100, 3)
for i in my_list:
    print(i)
