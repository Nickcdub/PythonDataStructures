class Node: 
        def __init__(self,data=None):
            self.data=data
            self.next=None

class LinkedList:
    def __init__(self):
         self.head = Node()
         self.size = 0
         self.tail = self.head
         
    def append(self,data):
        new_node = Node(data)
        cur = self.head
        while(cur.next!=None):
            cur=cur.next
        cur.next = new_node
        self.size = self.size+1

    def length(self):
        return self.size
    
    def display(self):
        cur=self.head
        result = "["
        while(cur.next!=None):
             result+=str(cur.next.data)+", "
             cur=cur.next
        if self.size > 0: result=result[:-2]
        result+="]"
        return(result)
    
    def __str__(self):
        return self.display()

    def prepend(self, data):
        newData = Node(data)
        newData.next = self.head.next
        self.head.next = newData
        self.size+=1
    
    def deleteAt(self, index):
        cur=self.head
        tempData = None
        if(index>=0 and index<self.size):
            #Start at -1 because self.head comes before index 0
            for _ in range(index):
                cur = cur.next
            tempData = cur.next.data
            cur.next = cur.next.next
            self.size-=1
        return tempData

    def get(self, index):
        cur=self.head
        if(index>=0 and index<self.size):
            for _ in range(index):
                cur = cur.next
            return cur.next.data
        
    

my_list = LinkedList()
print(my_list.display() + " Size: "+ str(my_list.size))
my_list.append("Hello")
my_list.append(3)
print(my_list.display() + " Size: "+ str(my_list.size))
my_list.prepend("Prepend")
print(my_list.display() + " Size: "+ str(my_list.size))
my_list.deleteAt(2)
print(my_list.display() + " Size: "+ str(my_list.size))
print(my_list.get(2))

testList = LinkedList()
testList.append(5)
testList.append(True)
testList.prepend("prepend")
testList.append("end")
print(my_list.display() + " Size: "+ str(my_list.size))

print(testList.deleteAt(2))
print(testList.deleteAt(0))
print(testList)
print(testList.deleteAt(2))

