from email import header
from tkinter.messagebox import NO


class Node:
    def __init__(self,val):
        self.val=val
        self.next= None

class LinkedList:
    def __init__(self):
        self.head=None

# Create a linkedlist

    def insertStart(self,value):
        node= Node(value)
        node.next=self.head
        self.head= node

    def insertAtEnd(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next

        temp.next=node
        node.next=None


    def insertAfter(self,givenNode,value):
        node=Node(value)
        node.next= givenNode.next
        givenNode.next= node

    def reverseList(self, A, B):
        self.head=A
simpleList= LinkedList()

node1= Node(5)
node2= Node(10)
node3= Node(15)

simpleList.head=node1
simpleList.head.next=node2
node2.next= node3
node3.next=None
simpleList.insertAfter(simpleList.head.next,34)
temp= simpleList.head
while temp!=None:
    print(temp.val)
    temp=temp.next


    

