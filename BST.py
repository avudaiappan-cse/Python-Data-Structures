#Binary Search Tree 

#BST OPERATIONS

#INSERT --> FIND --> DELETE-->GET SIZE -->TRAVERSALS

#BST INSERT

#START AT ROOT

#ALWAYS INSERT NODE AS LEAF


#BST FIND


#START AT ROOT

#RETURN DATA IF FOUND :
#            ELSE RETURN FALSE

#DELETE

#3 POSSIBLE CASES

#LEAF NODE
#1 CHILD
#2 CHILDREN

class Tree:
    def __init__ (self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    def insert(self,data):
        if self.data == data:
            return False 
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)
            else: 
                self.left = Tree(data)
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = Tree(data)
                return True 
    def find(self,data):
        if self.data == data:
            return data  
        elif self.data > data:
            if self.left is None:
                return False 
            else:
                return self.left.find(data) 
        elif self.data < data:
            if self.right is None:
                return False 
            else : 
                return self.right.find(data) 
    

    def get_size(self):
        if self.left is not None and self.right is not None:
            return 1 + self.left.get_size() + self.right.get_size() 
        elif self.left:
            return 1 + self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()
        else: 
            return 1 
        
    def preorder(self):
        if self is not None:
            print(self.data,end=" ")
            if self.left is not None:
                self.left.preorder() 
            if self.right:
                self.right.preorder() 
    
    def inorder(self) : 
        if self is not None:
            if self.left is not None:
                self.left.inorder() 
            print(self.data, end=" ")
            if self.right is not None:
                self.right.inorder() 
