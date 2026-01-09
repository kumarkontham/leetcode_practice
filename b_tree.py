from collections import deque
class b_tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        # self.next = None
class binary_tree:
    def __init__(self,):
        self.queue = deque()
    def insert_node_data(self,root,data):
        if not root:
            return b_tree(data)
        elif root.data > data:
                root.left = self.insert_node_data(root.left,data)
        else:
            root.right = self.insert_node_data(root.right,data)
        return root
    def implement_b_tree(self,root,data):
        if not root:
            return b_tree(data)
        elif not root.left:
            root.left = self.implement_b_tree(root.left,data)
        elif not root.right:
            root.right = self.implement_b_tree(root.right,data)
        else:
            self.implement_b_tree(root.left,data)
        return root
    def display(self,root):
        if not root:
            return 
        self.display(root.left)
        print(root.data,end="->")
        self.display(root.right)
    def same_tree(self,p,q):
        if not p and not q:
            return True
        if not p or not q or (p.data != q.data):
            return False
        return self.same_tree(p.left,q.left) and self.same_tree(p.right,q.right)
    def dfs(self,root):
        if not root:
            return 0
        left_height = self.dfs(root.left)
        right_height = self.dfs(root.right)
        return 1+max(left_height,right_height)
    def invert_tree(self,root):
        if not root:
            return None
        self.invert_tree(root.left)
        self.invert_tree(root.right)
        root.left,root.right =  root.right, root.left
        return root
    def construct_tree(self,preorder,inorder):#[3,9,20,15,7]
        def build_tree(preorder,inorder):
            if not preorder or not inorder:
                return None
            root = b_tree(preorder[0]) #root = 3 2.3left =9
            mid = inorder.index(preorder[0])
            root.left = self.construct_tree(preorder[1:mid+1],inorder[:mid])#[9],[9]
            root.right = self.construct_tree(preorder[mid+1:],inorder[mid+1:])
            return root
        return build_tree(preorder,inorder)
    def construct_post_in(self,postorder,inorder):
        hashmap = {}
        for i in range(len(inorder)):
            if inorder[i] not in hashmap:
                hashmap[inorder[i]] = i
        def helper_fun(left,right):
            if left > right:
                return None
            root = b_tree(postorder.pop())
            index = hashmap[root.data]
            root.right = helper_fun(index+1,right)
            root.left = helper_fun(left,index-1)
            return root 
        return helper_fun(0,len(inorder)-1)
    def display(self,root):
        if root:
            self.queue.append(root)
        while self.queue:
            temp=self.queue.popleft()
            print(temp.data,end="->")
            if temp.left:
                self.queue.append(temp.left)
            if temp.right:
                self.queue.append(temp.right) 
        
    def level_order(self,root):
        if root:
            self.queue.append(root)
            while self.queue:
                temp=self.queue.popleft()
                if not temp.next:
                    print(temp.data,"->","#")
                else:
                    print(temp.data,"->",temp.next.data)
                if temp.left is not None:
                    self.queue.append(temp.left)
                if temp.right is not None:
                    self.queue.append(temp.right)
    def populating_next_right_pointers(self,root):
        print(root.data)
        self.queue.append(root)
        self.queue.append(None)
        while self.queue:
            new_node = self.queue.popleft()
            if new_node == None:
                if not self.queue:
                    break
                self.queue.append(None)
                continue
            elif self.queue[0] == None:
                new_node.next = None
            elif self.queue[0] != None:
                new_node.next = self.queue[0]
            if new_node!=None:
                if new_node.left:
                    self.queue.append(new_node.left)
                if new_node.right:
                    self.queue.append(new_node.right)
        return root
    def flatten_tree(self,root):
        def tree_linked_list(root):
            if not root:
                return
            left_node = tree_linked_list(root.left)
            right_node = tree_linked_list(root.right)
            if root.left:
                left_node.right = root.right
                root.right = root.left
                root.left =None
            start_node = left_node or right_node or root 
            print(start_node.data)
            return start_node
        return tree_linked_list(root) 
    def pri(self,root):
        while root:
            print(root.data)
            root = root.right
    def path_sum(self,root,target_sum):
        curr_sum = 0
        def find_path(root,curr_sum):
            if not root:
                return False 
            curr_sum+=root.data
            if curr_sum == target_sum:
                return True
            return find_path(root.left,curr_sum) or find_path(root.right,curr_sum)
        return find_path(root,curr_sum)
    curr_sum = 0
    total_sum =0
    def sum_root_to_leaf(self,root):
        if not root:
            return None 
        self.curr_sum = self.curr_sum*10 + root.data
        if not root.left and not root.right:
            self.total_sum += self.curr_sum
            print(self.total_sum)
        self.sum_root_to_leaf(root.left)
        self.sum_root_to_leaf(root.right)
        self.curr_sum = self.curr_sum//10
        return self.total_sum
    max_sum = float('-inf')
    def maximum_path_sum(self,root):
        def dfs(root):
            if not root:
                return 0
            left_sum = max(0,dfs(root.left))
            right_sum = max(0,(dfs(root.right)))
            curr_sum = root.data+left_sum+right_sum
            self.max_sum = max(curr_sum,self.max_sum)
            return root.data+max(left_sum,right_sum)
        dfs(root)
        return self.max_sum
        
obj = binary_tree()
# root = None
# preorder = [9,15,7,20,3]
# inorder = [9,3,15,20,7]
# root_node=obj.construct_post_in(preorder,inorder)
# print(obj.display(root_node))

p=None
# q=None
# nodes_p = [1,2,3]
# nodes = [1,2,3,4,5,7]
tree_nodes = [1,2,3]
for i in tree_nodes:
    # root = obj.insert_node_data(root,i)
    p = obj.implement_b_tree(p,i)
    # q = obj.implement_b_tree(q,i)
# print(obj.display(root))
# print(obj.invert_tree(root))
# print(obj.display(root))
# print(obj.level_order(root))
print(obj.display(p))
# print(obj.path_sum(p,22))
# print(obj.sum_root_to_leaf(p))
print(obj.maximum_path_sum(p))
# print(obj.same_tree(p,q))
# obj.display(p)
# print(obj.populating_next_right_pointers(p))
# print(obj.level_order(p))
# print(obj.flatten_tree(p))
# print(obj.pri(p))
