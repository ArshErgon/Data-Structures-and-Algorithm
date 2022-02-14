

# Remove Dups! Write code to remove duplicates from an unsorted linked list.


# clearly the linked list is not sorted...
# if the linked list was sorted we could use a prev_prt to check with a next_prt
# we can use a set to store the data/elements which we have seen, and when we see them again we can delete them
# it will be an space O(n) image if a linked list doesnt have any duplicates our set will be filled by unique elements
# I'm thinking to do this by sorting the array and then using a prev_prt and next_prt, a sorting process would O(nlogn)

# O(n) space: O(n)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, element):
        newNode = Node(element)
        if self.head:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = newNode
        else:
            self.head = newNode

    def removeDuplicates(self):
        seen = set()
        seen.add(self.head.data)
        curr = self.head
        while curr and curr.next:
            if curr.next.data in seen:
                # print(curr.data, curr.next.data)
                curr.next = curr.next.next
                curr = curr.next

            else:
                seen.add(curr.next.data)
                curr = curr.next
        
        # print(seen)
        
    def showResult(self):
        res = str()
        curr = self.head
        while curr.next != None:
            res += str(curr.next.data)+'-->'
            curr = curr.next

        return res


obj = LinkedList()
x = [1,1,1,2, 2, 3, 3, 4, 3, 6, 2,1]
for i in x:
    obj.add(i)


print(obj.showResult())
print(obj.removeDuplicates())
print(obj.showResult())
