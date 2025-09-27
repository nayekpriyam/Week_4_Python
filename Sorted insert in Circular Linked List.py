def sorted_insert(head, data):
    new_node = CNode(data)
    if not head:
        new_node.next = new_node
        return new_node

    curr = head
    if data < head.data:
        while curr.next != head:
            curr = curr.next
        curr.next = new_node
        new_node.next = head
        return new_node

    while curr.next != head and curr.next.data < data:
        curr = curr.next
    new_node.next = curr.next
    curr.next = new_node
    return head

cll.head = sorted_insert(cll.head, 15)
cll.print_list()  
