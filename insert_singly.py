class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def print_list(self):
        temp = self.head
        linked_list = ''
        while(temp):
            linked_list += (str(temp.data) + " ")
            temp = temp.next
        print(linked_list)
    
    def insertNode(self,val,pos):
        target = Node(val)
        if(pos == 0):
            target.next = self.head
            self.head = target
        def previous(pos):
            temp = self.head
            count = 1
            if(count<pos):
                temp = temp.next
                count += 1
            return temp
        pre = previous(pos)
        nextnode = pre.next

        pre.next = target
        target.next = nextnode
        

l = Linkedlist()
l.head = Node(3)
l2 = Node(4)
l3 = Node(2)
l4 = Node(5)

l.head.next = l2
l2.next = l3
l3.next = l4

l.insertNode(10,3)
l.insertNode(1,0)
l.insertNode(6,4)
l.insertNode(10,7)

l.print_list()