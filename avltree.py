class Treenode:
    def __init__(self,key):
        self.val = key
        self.left = None 
        self.right = None
        self.height = 1
class AVL_Tree:
    def __init__(self):
        self.root = None
    def insertion(self,key):
        self.root = self._insertion(self.root,key)
    def _insertion(self,root,key):
        if not root:
            return Treenode(key)
        elif key < root.val:
            root.left = self._insertion(root.left,key)
        elif key > root.val:
            root.right = self._insertion(root.right,key)
        else:
            return root
        
        self.update_height(root)
        bf = self.get_balance_factor(root)
        if bf<-1 and root.right.val < key:
            return self.Left_rotation(root)
        if bf > 1 and root.left.val > key:
            return self.Left_rotation(root)
        if bf > 1 and root.left.val < key:
            print(bf)
            root.left = self.Left_rotation(root.left)
            return self.right_rotation(root)
        if bf < -1 and  root.right.val > key:
            print(bf)
            root.right = self.right_rotation(root.right)
            return self.Left_rotation(root)
        return root
    def Left_rotation(self,root):
        y  = root.right
        temp = y.left
        y.left = root
        root.right = temp
        return y
    def right_rotation(self,root):
        y = root.left
        temp = y.right
        y.right = root
        root.left = temp
        return y
    def get_balance_factor(self,root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    def update_height(self,root):
        root.height = 1+max(self.get_height(root.left),self.get_height(root.right))
        return root.height
    def get_height(self,root):
        if not root:
            return 0
        return root.height
    def inorder(self):
        self._inorder(self.root)
    def _inorder(self,root):
        if root:
            self._inorder(root.left)
            print(root.val,end=" ")
            self._inorder(root.right)
tree = AVL_Tree()
list1 = [30,35,33,40]
for i in list1:
    tree.insertion(i)
tree.inorder()
