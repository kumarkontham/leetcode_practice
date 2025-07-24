class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_List:
    def __init__(self):
        self.head=None
    def add_at_end(self,data):
        dummy=Node(0)
        dummy.next=self.head
        new_node=Node(data)
        
        if self.head is None:
            self.head=new_node
        curr_node=self.head
        while curr_node.next :
            curr_node=curr_node.next
        curr_node.next=new_node
    def addBeginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
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

    def printll(self):
        curr=self.head
        while curr!=None:
            print(curr.data)
            curr=curr.next
group=Linked_List()
group.addBeginning("6")
group.addBeginning("5")
group.addBeginning("4")
group.addBeginning("3")
group.addBeginning("2")
group.addBeginning("1")
# group.add_at_end(2)
# group.add_at_end(3)
# group.add_at_end(4)
# group.add_at_end(5)

group.reverse_k_group(2)
print(group.printll())
