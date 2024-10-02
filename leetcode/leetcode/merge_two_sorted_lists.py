from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        
        current = head
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 or list2
        return head.next
        
             
        # total = len(list1) + len(list2)
        # new_list = []
        # for i in range(total):
        #     if i % 2 == 0:
        #         new_list.append(list1[0])
        #         list1.pop(0)
        #     else:
        #         new_list.append(list2[0])
        #         list2.pop(0)
        
        


if __name__ == '__main__':
    mtl = Solution()
    print(mtl.mergeTwoLists(ListNode(1), ListNode(2)))
        
