"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):

        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
    
        if self.head is None:
            return None
            
        else:
            retval = self.head.value

            if self.length == 1:
                self.head = None
                self.tail = None

            else:
                self.head = self.head.next
                self.head.prev = None
            
            self.length -= 1

            return retval

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)

        if self.tail is None:
            self.tail = new_node
            self.head = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
    
        if self.tail is None:
            return None
            
        else:
            retval = self.tail.value

            if self.length == 1:
                self.head = None
                self.tail = None

            else:
                self.tail = self.tail.prev
                self.tail.next = None
            
            self.length -= 1

            return retval


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):

        if self.head == node:
            return True

        val = node.value
        self.delete(node)
        self.add_to_head(val)
        return True





    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):

        if self.tail == node:
            return True

        val = node.value
        self.delete(node)
        self.add_to_tail(val)
        return True



    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # print("self.length: " + str(self.length) )

        if self.head == node:
            self.head = self.head.next
        if self.tail == node:
            self.tail = self.tail.prev
        node.delete()

        self.length -= 1

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        
        if self.length == 0:
            return None

        else:
            cursor = self.head
            retval = cursor.value

            while cursor.next is not None:
                cursor = cursor.next
                retval = max(retval, cursor.value)

        return retval

            
