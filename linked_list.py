class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linked_List:
    def __init__(self):
        self.head=None
    def addBeginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    def insert_at_index(self,data,index):
        if index==0:
            N.addBeginning(data)
        
        position=0
        curr_node=self.head
        while curr_node is not None and position+1!=index:
            position +=1
            curr_node=curr_node.next
        if curr_node is not None:
            new_node=Node(data)
            new_node.next=curr_node.next
            curr_node.next=new_node
        # return curr_node.next
    def add_at_end(self,data):
        new_node=Node(data)
        print(new_node)
        if self.head is None:
            self.head=new_node
        curr_node=self.head
        while curr_node.next :
            curr_node=curr_node.next
        curr_node.next=new_node
    def update_val(self,data,index):
        
        curr_node=self.head
        position=0
        while curr_node is not None and position+1!=index:
            position+=1
            curr_node=curr_node.next
        if curr_node is not None:
            curr_node.data=data
        
    def remove_last_node(self):
        if self.head is None:
            return 
        if self.head.next is None:
            self.head=None
        curr_node=self.head
        while curr_node.next and curr_node.next.next:
            curr_node=curr_node.next
        curr_node.next=None
    def remove_at_index(self,index):
        if index==0:
            self.head=None
        curr_node=self.head
        position=0
        while curr_node is not None and curr_node.next is not None and position+1!=index:
            curr_node=curr_node.next
            position+=1
        curr_node.next=curr_node.next.next
    def reverse_ll_2(self,left,right):
        dummy=Node(None)
        dummy.next=self.head
        leftpre=dummy
        curr=self.head
        for i in range(left-1):
            leftpre=leftpre.next
            curr=curr.next
        prevhead=curr
        emp=Node(None)
        for j in range(right-left+1):
            nextnode=curr.next
            curr.next=emp
            emp=curr
            curr=nextnode
        leftpre.next=emp
        prevhead.next=curr
        return dummy.next
    def reverse_k_group(self,k):
        dummy=Node(0)
        dummy.next=self.head
        curr_node=self.head
        count=1
        while curr_node:
            curr_node=curr_node.next
            count+=1
        gprev=dummy
        while count>=k:
            kth = self.findkth(gprev,k)
            if not kth:
                break
            gnext=kth.next
            curr_node=gprev.next
            prev=kth.next
            while curr_node!=gnext:
                temp=curr_node.next
                curr_node.next=prev
                prev=curr_node
                curr_node=temp
            tmp=gprev.next
            gprev.next=kth
            gprev=tmp
            count-=k
        return dummy.next
    


    def findkth(self,curr,k):
        while k>0 and curr:
            curr=curr.next
            k-=1
        return curr

    def reverse_ll(self):
        dummy=Node(None)
        curr_node=self.head
        while curr_node!=None:
            next_node=curr_node.next
            curr_node.next=dummy
            dummy=curr_node
            curr_node=next_node
        self.head=dummy
        return self.head

    def printll(self):
        curr=self.head
        while curr!=None:
            print(curr.data)
            curr=curr.next
            
N=Linked_List()
N.addBeginning("5")
N.addBeginning("4")
N.addBeginning("3")
N.addBeginning("2")
N.addBeginning("1")
# N.insert_at_index("a",0)
# N.insert_at_index("b",1)
#N.add_at_end("h")
# N.reverse_ll_2(1,1)
N.reverse_k_group(2)
# N.reverse_ll()
# N.update_val("f",5)
# N.remove_last_node()
# N.remove_at_index(1)
print(N.printll())

