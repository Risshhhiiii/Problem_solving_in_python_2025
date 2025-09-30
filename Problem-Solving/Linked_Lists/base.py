class node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class linked_list:
    def __init__(self):
        self.head = None    
    
    def append(self, data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    def print_list(self):
        temp = self.head
        while temp :
            print(temp.data,end="->")
            temp = temp.next
        print(None)

l1 = linked_list()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
l1.append(50)
l1.print_list()


#leetcode : 876 , 141 ,142 ,19 ,206