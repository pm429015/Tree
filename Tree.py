'''
Created on Oct 25, 2013

@author: pm429015

Very basic tree implementation
see http://www.cs.usfca.edu/~galles/visualization/BST.html for more info
'''
class BinaryTreeNode:
    
    def __init__(self,value):
        self.__value = value
        self._left = None
        self._right = None
        self._height = None

    def addRight(self):
        raise NotImplementedError

    def addLeft(self):
        raise NotImplementedError
    
    def showValue(self):
        return self.__value
    
    def changeValue(self,change):
        self.__value = change
    


class BinaryTree(BinaryTreeNode):
    
    def add(self,new,side):
        if side == 'R':
            leaf = BinaryTree(new)
            temp = self
            while temp._right != None:
                temp = temp._right
            temp._right = leaf
            
        elif side =='L':
            leaf = BinaryTree(new)
            temp = self
            while temp._left != None:
                temp = temp._left
            temp._left = leaf
    

            
    def showRight(self):
        if self._right != None:
            return self._right.showValue()
        
    def showLeft(self):
        if self._left != None:
            return self._left.showValue()
        
    def preorder(self):
        print self.showValue()
        if self._left != None:
            self._left.preorder()
        if self._right != None:
            self._right.preorder()
    
    def inorder(self):
        if self._left != None:
            self._left.inorder()
        print self.showValue()
        if self._right != None:
            self._right.inorder()
            
    def postorder(self):
        if self._left != None:
            self._left.postorder()
        if self._right != None:
            self._right.postorder()
        print self.showValue()
    
class BinarySearchTree(BinaryTree):
     
    def add(self,new):
        result = self.search(new)
        if result[1] == 1:
            newNode = BinarySearchTree(new)
            result[0]._right = newNode
        elif result[1] == -1:
            newNode = BinarySearchTree(new)
            result[0]._left = newNode 
        else:
            print 'No Duplicate'
    
    def search(self,new):
        
        currentValue = self.showValue()
        left = self.showLeft()
        right = self.showRight()
        
        if new == currentValue:
            print "the item " + str(new) +" is found "
            return (self,self)
        
        elif new == left:
            print "the item " + str(new) +" is found "
            return (self,self._left) #parent and self
        
        elif new == right:
            print "the item " + str(new) +" is found "
            return (self,self._right) #parent and self
        
        elif new > currentValue:
            if self._right != None:
                return self._right.search(new)
            else:
                return (self,1)
        elif new < currentValue:
            
            if self._left != None:
                return self._left.search(new)
            else:
                return (self,-1)

        

        
    def delete(self,item):
        #search the target item
        #if item exist, return target's parent and target
        
        result = self.search(item) 
        try :
            
            if result[1]._left and result[1]._right:  #if the node has two childern
                pointer = result[1]._left
                parent = None
                while pointer._right != None:
                    parent = pointer
                    pointer = pointer._right
                result[1].changeValue(pointer.showValue())

                if pointer._left != None:
                    parent._left = pointer._left
                    parent._right = None
                else:
                    parent._right = None

            elif result[1]._left: #if the target node only has left child
                #comparing with target parent node's value and connect to the target node 's child
                if result[0].showValue() > result[1].showValue():
                    result[0]._left = result[1]._left
                elif result[0].showValue() < result[1].showValue():
                    result[0]._right = result[1]._left
                else:
                    print 'Error equal value'
                    
            elif result[1]._right:#Again, new check if it has only right child
                if result[0].showValue() > result[1].showValue():
                    result[0]._left = result[1]._right
                elif result[0].showValue() < result[1].showValue():
                    result[0]._right = result[1]._right
                else:
                    print 'Error equal value'
            else: #if no child, connect None to parent
                if result[0].showValue() > result[1].showValue():
                    result[0]._left = None
                elif result[0].showValue() < result[1].showValue():
                    result[0]._right = None
                else:
                    print 'Error equal value'
                    
            
        except AttributeError:
            print 'The item is not found. Stop'


if __name__ == '__main__':
    bst = BinarySearchTree(7)
    bst.add(4)
    bst.add(1)
    bst.add(5)
    bst.add(16)
    bst.add(8)
    bst.add(11)
    bst.add(12)
    bst.add(15)
    bst.add(9)
    bst.add(2)
    bst.add(6)
    bst.add(20)
    
    # add duplicate
    bst.add(2)    
    #delete exist value
    bst.delete(16)
    
    #delete non exit value
    bst.delete(100)
    
    # search a value
    bst.search(15)
    
    #print
    bst.preorder()
    bst.inorder()
    bst.postorder()