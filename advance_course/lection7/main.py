#Cтек на связном списке

class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None
    def __str__(self) -> str:
        return f"[{self.val}]"

list1, list2, list3 = ListNode(1), ListNode(2), ListNode(3)
list1.next, list2.next = list2, list3

head = list1
print(head)

def push(node):
    global head
    node.next = head
    head = node
def pop():
    global head
    res = head.val
    head = head.next
    return res

push(ListNode(-3))
push(ListNode(-2))
push(ListNode(-1))

for _ in range(6):
    print(pop())
 


