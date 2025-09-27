def reverse_dll(head):
    curr = head
    prev_node = None
    while curr:
        curr.prev, curr.next = curr.next, curr.prev
        prev_node = curr
        curr = curr.prev
    return prev_node

dll = DoublyLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_beginning(30)
dll.head = reverse_dll(dll.head)
dll.print_list()  
