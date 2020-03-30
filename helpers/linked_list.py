class Node:
    def __init__(self, x, parent=None):
        self.val = x
        self.next = None
        if parent:
            parent.next = self

    def __str__(self):
        head = self
        values = []
        while head:
            values.append(head.val)
            head = head.next

        return ', '.join([str(x) for x in values])
