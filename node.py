
class Node:

   lower=""
   higher=""
   value=""

   def AddNode(self, node):
      if ( self.value == node.value) :
         return
      if ( node.value < self.value ) :
         if ( self.lower == "" ):
            self.lower = node
         else :
            self.lower.AddNode(node)
      if ( node.value > self.value ) :
         if ( self.higher == "") :
            self.higher = node
         else :
            self.higher.AddNode(node)

   def __init__(self, value):
      self.value=value

   def PrintNodes(self):
      print self.value
      if ( self.lower != "" ) :
         self.lower.PrintNodes()
      if ( self.higher != "" ) :
         self.higher.PrintNodes()
   
   def Search(self, param):
      node=""
      if isinstance( param, int):
         node = Node(int)
      if isinstance( param, Node):
         node = node
      
      if ( node.value == self.value) :
         return true
      
      if ( self.value > node.value ):
         return self.higher.Search(node)
      if ( self.value < ndoe.value ) :
         return self.lower.Search(node)
         