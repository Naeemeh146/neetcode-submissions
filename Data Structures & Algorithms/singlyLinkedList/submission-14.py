class NodeList:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        if not self.head:
            return -1
        count = 0
        cur = self.head
        while cur:
            if count == index:
                return cur.val
            cur = cur.next
            count+=1
        return -1
        

    def insertHead(self, val: int) -> None:
        
        new_node = NodeList(val)
        tmp = self.head
        self.head = new_node 
        self.head.next = tmp

        

    def insertTail(self, val: int) -> None:
        
        new_node = NodeList(val)
        if not self.head:
            self.head = new_node
            return 
        
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
        return
        

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        if index == 0:
           
            self.head = self.head.next
            return True

        
        count = 1
        cur = self.head
        while cur and cur.next:
            if index == count:
                tmp = cur.next.next
                cur.next = tmp
                cur = tmp
                return True
            cur = cur.next
            count +=1

        return False
        

    def getValues(self) -> List[int]:
        array_val = []
        if not self.head:
            return array_val

        cur = self.head
        while cur:
            array_val.append(cur.val)
            cur = cur.next
        return array_val
        
