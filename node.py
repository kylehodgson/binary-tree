
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
   def WalkNodes(self):
      print self.value
      if ( self.lower != "" ) :
         self.lower.WalkNodes()
      if ( self.higher != "" ) :
         self.higher.WalkNodes()