class ListNode:
    def __init__(self,val,next_node=None):
        self.val=val
        self.next=next_node

class LinkedList:
    
    def __init__(self):
        self.head=ListNode(-1)
        self.tail=self.head
    
    def get(self, index: int) -> int:
        i=0
        curr=self.head.next
        while curr:
            if i==index:
                return curr.val
            i+=1
            curr=curr.next
        
        return -1

    def insertHead(self, val: int) -> None:
        curr=ListNode(val)
        curr.next=self.head.next
        self.head.next=curr
        if not curr.next:
            self.tail=curr        

    def insertTail(self, val: int) -> None:
        curr=ListNode(val)
        self.tail.next=curr
        self.tail=curr
        

    def remove(self, index: int) -> bool:
        i=0
        curr=self.head
        while i<index and curr:
            i+=1
            curr=curr.next
        if not curr or not curr.next:
            return False
        if curr.next==self.tail:
            self.tail=curr
        curr.next=curr.next.next
        return True
        

    def getValues(self) -> List[int]:
        curr=self.head.next
        ans=[]
        while curr:
            ans.append(curr.val)
            curr=curr.next
        return ans
        
