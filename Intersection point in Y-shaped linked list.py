def get_intersection(head1, head2):
    def get_length(head):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        return count

    len1 = get_length(head1)
    len2 = get_length(head2)
    diff = abs(len1 - len2)

    long = head1 if len1 > len2 else head2
    short = head2 if len1 > len2 else head1

    for _ in range(diff):
        long = long.next

    while long and short:
        if long == short:
            return long.data
        long = long.next
        short = short.next
    return None 