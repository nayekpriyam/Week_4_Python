def pairwise_swap(head):
    curr = head
    while curr and curr.next:
        curr.data, curr.next.data = curr.next.data, curr.data
        curr = curr.next.next
    return head

dll.head = pairwise_swap(dll.head)
dll.print_list()  