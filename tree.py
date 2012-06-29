
from node import *

class Tree:
   trunk=""
   def AddNode(self, node):
      if ( self.trunk=="" ):
         self.trunk=node
      else :
         self.trunk.AddNode(node)

   def PrintNodes(self):
      if ( self.trunk == "" ) :
         return
      self.trunk.PrintNodes()
   
   def Search(self, param):
      node=""
      if isinstance( param, int):
         node = Node(param)
      if isinstance( param, Node):
         node = param
      
      return self.trunk.Search(node)