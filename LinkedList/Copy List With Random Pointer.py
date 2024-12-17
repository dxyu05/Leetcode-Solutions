"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # my first intuition is that we need to loop through the original linked list
        # the problem asks us to create a deep copy of the list, as in containing n new nodes
        # we can do this in one pass. However the catch is that there are random pointers in this list
        # one way to approach this is to go in two passes. One to copy all the original nodes into new nodes
        # and then another pass to assign all the random nodes to actual nodes in the list
        # however this might also need an additional data structure anyways 
        # then the best way (currently I can think of) is this two pass solution
        # using a hashmap to map old nodes to copied nodes
        # there however is another solution which uses interweaving that can find
        # a solution in O(n) time and O(1) memory complexity
        
        # this is the hashmap implementation, O(1) time complexity and O(n) memory complexity

        # if the list is empty (edge case)
        if head == None:
            return None

        hashmap = {}
        
        # creating a curr and copy of the curr
        curr = head
        copy = Node(head.val, None, None)

        hashmap[head] = copy

        curr = curr.next

        # while our current node has a next in the list
        # we create a copy, put it in the hashmap and set 
        # our previous node's .next to it
        while curr:
            new = Node(curr.val, None, None)
            hashmap[curr] = new
            copy.next = new
            
            copy = copy.next
            curr = curr.next

        curr = head

        # now all we need to do is just update the random
        while curr:
            if curr.random != None:
                hashmap[curr].random = hashmap[curr.random]

            curr = curr.next

        return hashmap[head]
    
    # # this is the interweaving solution, O(1) time complexity and O(1) memory complexity
    
    # # if the list is empty (edge case)
    #     if head == None:
    #         return None

    #     curr = head

    #     # first loop, set the next pointer to the copy
        
    #     while curr:
    #         copy = Node(curr.val)
    #         copy.next = curr.next
    #         copy.random = curr.random
            
    #         curr.next = copy
    #         curr = copy.next

    #     curr = head.next

    #     # second loop, assign randoms
    #     while curr:
    #         if curr.random != None:
    #             curr.random = curr.random.next

    #         curr = curr.next

    #     copy = head.next
    #     curr = head.next
    #     prev = head

    #     # third loop split it up
    #     while curr:
    #         if curr.next:
    #             prev.next = prev.next.next
    #             curr.next = curr.next.next
    #         else:
    #             prev.next = None
    #             curr.next = None

    #         curr = curr.next

    #     return copy


        