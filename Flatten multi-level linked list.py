class MultiLevelNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None

def flatten(head):
    if not head:
        return None
    curr = head
    while curr:
        if curr.child:
            next_node = curr.next
            child_head = flatten(curr.child)
            curr.next = child_head
            temp = child_head
            while temp.next:
                temp = temp.next
            temp.next = next_node
            curr.child = None
        curr = curr.next
    return head

def print_flattened(head):
    curr = head
    while curr:
        print(curr.data, end=' ')
        curr = curr.next
    print() 