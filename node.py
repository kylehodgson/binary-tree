
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
   
   def Search(self, node):
      if ( node.value == self.value) :
         return "Found {0}".format(node.value)
      if ( self.value < node.value ):
         if ( isinstance( self.higher, Node)):
            return self.higher.Search(node)
      if ( self.value > node.value ) :
         if ( isinstance( self.lower, Node)):
            return self.lower.Search(node)
   
   def Delete(self, node):
      if ( self.lower!="" and node.value == self.lower.value  and self.lower.higher == "" and self.lower.lower == "") :
         print "Deleting!"
         self.lower=""
      if ( self.higher!="" and node.value == self.higher.value and self.higher.higher == "" and self.higher.lower == "") :
         print "Deleting!"
         self.higher=""
         
         