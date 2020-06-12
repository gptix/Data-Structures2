class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next
        





class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None
        # reference to the tail of the list
        self.tail = None

    def add_to_tail(self, value):
        # wrap the input value in a node
        new_node = Node(value, None)
        # check if there is no head (i.e., the list is empty)
        if not self.head:
            # if the list is initially empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # we have a non-empty list, add the new node to the tail
        else:
            # set the current tail's next reference to our new node
            self.tail.set_next(new_node)
            # set the list's tail reference to the new node
            self.tail = new_node

    def remove_head(self):
        # return None if there is no head (i.e. the list is empty)
        if not self.head:
            return None
        # if head has no next, then we have a single element in our list
        if not self.head.get_next():
            # get a reference to the head
            head = self.head
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None
            # return the value
            return head.get_value()
        # otherwise we have more than one element in our list
        value = self.head.get_value()
        # set the head reference to the current head's next node in the list
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        if not self.head:
            return None
        
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        return value

    def contains(self, value):
        if not self.head:
            return False
    
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node 
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()










class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.storage.head = new_node
            self.storage.tail = new_node
            self.size += 1
        else: # LL is not empty. We will put things on the tail, and take them from the head
            self.storage.tail.next_node = new_node
            self.storage.tail = new_node
            self.size += 1
        # print(self.size)
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            retval = self.storage.head.value
            self.storage.head = self.storage.head.next_node
            self.size -= 1
            return retval








class Stack:
    def __init__(self):
        self.storage = LinkedList()

    def __len__(self):
        retval = 0
        curr = self.storage.head
        if curr is not None:
            retval += 1
            while curr.next_node is not None:
                retval += 1
                curr = curr.next_node
        return retval

    def push(self, value):
        new_node = Node(value)
        if self.storage.head == None:
            self.storage.head = new_node
            self.storage.tail = new_node
        
        else:
            new_node.next_node = self.storage.head
            self.storage.head = new_node

    def pop(self):
        if self.storage.head == None:
            return None
        else:
            retval = self.storage.head.value
            self.storage.head = self.storage.head.next_node
            return retval












"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = value
            
        elif value < self.value: # go left
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
                
        else: # go right
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
               

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        # print(target)

        if self.value == target:
            return True

        if (target < self.value) and (self.left is not None):
            return self.left.contains(target)

        elif self.right is not None:
            return self.right.contains(target)

        else:
            return False


    # Return the maximum value found in the tree
    def get_max(self):

        ret_max = self.value

        if self.right is not None:
            ret_max = max(ret_max, self.right.get_max())

        return ret_max

    


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self is None:
            return True
        
        else:
            if self.left is not None:
                self.left.for_each(fn)
            if self.right is not None:
                self.right.for_each(fn)
            self.value = fn(self.value)

            return True


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            node.in_order_print(node.left)

        print(node.value)

        if node.right is not None:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        
    #     queue = [node]

    #     while queue != []:
    #         current = queue.pop(0)
    #         if current.right:
    #             queue.append(current.right)
    #         if current.left:
    #             queue.append(current.left)
    #         print(current.value)

        # def bft_print(self, node):
        
        q = Queue()
        q.enqueue(node)
        
        while q.size != 0:
            current = q.storage.head.value
            if current.right is not None:
                q.enqueue(current.right)
            if current.left is not None:
                q.enqueue(current.left)
            print(q.dequeue().value)
            
            
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        
        stack = [node]
        
        # while stack != []:
        #     current = stack.pop(-1)
        #     if current.left:
        #         stack.append(current.left)
        #     if current.right:
        #         stack.append(current.right)
        #     print(current.value)


        s = Stack()
        s.push(node)
        
        while len(s) > 0:
            current = s.pop()
            if current.left is not None:
                s.push(current.left)
            if current.right is not None:
                s.push(current.right)
            print(current.value)









    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):

        print(node.value)
        
        if node.left is not None:
            node.pre_order_dft(node.left)

        if node.right is not None:
            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        
        if node.left is not None:
            node.post_order_dft(node.left)

        if node.right is not None:
            node.post_order_dft(node.right)

        print(node.value)
