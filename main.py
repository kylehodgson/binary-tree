from pprint import pprint
from node import *
from tree import *

t = Tree()
for i in reversed ( range(100)):
   n = Node(i)
   t.AddNode(n)

print t.Search(25)
print t.Search(250)

for i in range(100):
   t.Delete(i)
   

