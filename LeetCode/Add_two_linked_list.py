# Definition for singly-linked list.
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.getNumber(list=l1)
        num2 = self.getNumber(list=l2)
        return self.getList(num=num1 + num2)
    
    def getList(self, num: int):
        if num == 0:
            return ListNode(0)
        res = None
        while num > 0:
            temp = num%(10)
            num = (num - temp)//10
            if res is None: 
                res = ListNode(val=temp, next=None)
                curr = res
            else:
                curr.next= ListNode(val=temp, next=None)
                curr = curr.next
        print_list(res)
        return res

    def getNumber(self, list: ListNode):
        mul = 1
        num = 0
        while list is not None:
            num=num +list.val*mul
            list= list.next
            mul = mul* 10
        return num
        

l1 =ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=None)))))
l2 =ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=None)))


l1 =ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None)))
l2 =ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))
# l1 =ListNode(val=0, next=None)
# l2 =ListNode(val=0, next=None)
sol = Solution()

sol.addTwoNumbers(l1=l1, l2=l2)