from collections import namedtuple
from collections import deque
from collections import OrderedDict, defaultdict, Counter

Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)

print(p.y)

my_deque = deque()
my_deque.append(10)
my_deque.appendleft(20)
my_deque.appendleft(30)
my_deque.appendleft(40)
print(len(my_deque))
my_deque.rotate(1)
print(my_deque)

od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["e"] = 5
od["c"] = 3
od["d"] = 4

od["f"] = 6
od["g"] = 7
print(od)

cnt = Counter({"counter": 1, "spam": 2, "egg": 1})
print(cnt.most_common())
