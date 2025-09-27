def delete_node(head, key):
    curr = head
    while curr:
        if curr.data == key:
            if curr.prev:
                curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
            if curr == head:
                head = curr.next
            break
        curr = curr.next
    return head

dll = DoublyLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.head = delete_node(dll.head, 10)
dll.print_list()  
