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
            linked_list += (str(temp.data)+' ')
            temp = temp.next
        print(linked_list)
l = Linkedlist()
l.head = Node(3)
l2 = Node(4)
l3 = Node(2)
l4 = Node(5)

l.head.next = l2
l2.next = l3
l3.next = l4

l.print_list()




