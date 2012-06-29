

class Tree:
   trunk=""
   def AddNode(self, node):
      if ( self.trunk=="" ):
         self.trunk=node
      else :
         self.trunk.AddNode(node)

   def WalkNodes(self):
      if ( self.trunk == "" ) :
         return
      self.trunk.WalkNodes()