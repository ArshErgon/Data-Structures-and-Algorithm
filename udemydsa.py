# import time

# def findNum(listOfNumbers, numToFind):

#     for num in listOfNumbers:
#         if num == numToFind:
#             print(listOfNumbers[num], "for Loop")
    
#     count = 0
#     while count < len(listOfNumbers):
#         if listOfNumbers[count] == numToFind:
#             print(listOfNumbers[count], "while loop")
#             break
#         count+=1

# listOfNumbers = list(range(1, 21))
# findNum(listOfNumbers, 6)


# def commonItemsFind(list1, list2):
#     start_time = time.time()
#     for list1_item in list1:
#         for list2_item in list2:
#             if list1_item == list2_item:
#                 print("Match found: ", list1_item, list2_item)
#     print(start_time-time.time())

# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
# list2 = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 99]
# commonItemsFind(list1, list2)



# def commonItemDict(list1, list2):
#     start_time = time.time()
#     dict_items = dict()
#     for list1_item in (list1):
#         dict_items[list1_item] = True
    
#     for list2_item in list2:
#         if list2_item in dict_items:
#             print(dict_items[list2_item])
    
#     print(start_time-time.time())


# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
# list2 = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 99]
# commonItemDict(list1, list2)


# Push method in Python

# class PUSH(object):
#     def __init__(self):
#         self.list1 = list()
#         self.lengOfele = 0

#     def showInfo(self):
#         self.lengOfEle()
#         print(self.list1, f'length: ', self.lengOfele)
#         ele = self.list1
#         deletation_of_ele = int(input("Enter the Index to delete the element: "))
#         try:
#             if deletation_of_ele:
#                 self.deleteByIndex(deletation_of_ele-1)
#         except Exception:
#             pass
#         print(self.list1, 'length: ', len(self.list1))


#     def push(self, ele):
#         self.list1.append(ele)

#     def pop(self):
#         self.list1.pop(-1)

#     def deleteByIndex(self, indexOfList):
#         self.list1.pop(indexOfList)
    
#     def lengOfEle(self):
#         for ele in self.list1:
#             self.lengOfele+=1



# obj = PUSH()
# obj.push("hey")
# # obj.lengOfEle()
# # obj.deleteByIndex(0)
# obj.showInfo()


# A program to reverse a string! self made

# def stringReverse(stringToReversed):
#     string = str()
#     counter = 1
#     if type(stringToReversed) == str:
#         while counter <= len(stringToReversed):
#             string += stringToReversed[-counter]
#             counter+=1
#         print(string)
#     elif type(stringToReversed) == int:
#         stringToReversed = str(stringToReversed)
#         while counter <= len((stringToReversed)):
#             string += str(stringToReversed[-counter])
#             counter+=1
#         print(int(string))


# stringReverse('Arsh Ergon Hello')


# Merge two sorted array or list into one sorted array or list 

# def MergeList(list1, list2):
#     mergeList = list()
#     counterList = 0

#     list1_item = list1[0]
#     list2_item = list2[0]
    # while list1_item or list2_item:               # DO TRY AGAIN THIS
#     # while counterList <= 4:                     # there's problem in this Algo
#         if list1_item < list2_item:
#             mergeList = list1_item
#             print(mergeList)
#             list1_item = list1[counterList+1]
#         else:
#             mergeList = list2_item
        
#         counterList+=1
#     print(mergeList)


# MergeList([3, 7, 9, 4], [1, 2, 5, 7])


# Dictonaries in python: Data Structure Hash Table


# def dict_items(key, value):
#     dictItem = dict()
#     dictItem[key] = value
#     print(dictItem)

# dict_items(10, "2000")
# dict_items(20, "900")



# Knowing the character code of words

# def charCode(words):
#     chars = [ord(x) for x in words]
#     print(chars)

# charCode("Arsh")

# def commonFastFind(array):
#     insertdict = dict()
#     for key,value in enumerate(array):
#         if not value in insertdict:
#             insertdict[value] = key
#         else:
#             print(value)
#             break


# commonFastFind([2, 3, 1, 1, 2])


#   #   #
#   #   # LinkedList 


# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def inseration(self, data):
#         newNode  = Node(data)
#         if self.head:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = newNode
#         else:
#             self.head = newNode

#     def printList(self):
#         current = self.head
#         while current:
#             print(current.data)
#             current = current.next


# obj = LinkedList()
# obj.inseration([5,4,3,2,1])
# print(obj.inseration([5,4,3,2,1]))
# obj.append(9)

# obj.printList()



# class BinarySearch:
#     def __init__(self, data, target):
#         self.data = data
#         self.target = target
#         self.left = 0
#         self.right = len(data) - 1

#     def split(self):
#         while(self.left<=self.right):
#             mid = (self.right + self.left)//2
#             if self.data[mid] == self.target:
#                 print(self.data[mid])
#                 break
#             elif self.data[mid] < self.target:
#                 self.left = mid + 1
#             else:
#                 self.right = mid - 1

# obj = BinarySearch([1,2,3,4,5,6,7,8,9,10], 9)
# obj.split()


# Student data DSA program

# class StudentsData:
#     def __init__(self):
#         self.ID = None
#         self.name = None
#         self._class = None
#         self.GPA = None
#         self.dict_ = dict()

#     def takeInput(self):
#         while True:
#             self.ID = (input("Enter ID: "))
#             if self.ID == "" or self.ID == None:
#                 break
#             else:
#                 self.name = input("Enter Name: ")
#                 self._class = int(input("Enter Class: "))
#                 self.GPA = float(input("Enter GPA: "))
#                 self.dict_[int(self.ID)] = self.name,self._class,self.GPA
            
#     def showOut(self):
        
#         for students_code in self.dict_.keys():
#             print(students_code, self.dict_[students_code], len(self.dict_))

#     def searchStudent(self):
#         missing_student_Name = input("Enter name: ")
#         if missing_student_Name in self.dict_.values():90
#             print(self.dict_.get(missing_student_Name))

# obj = StudentsData()
# obj.takeInput()
# obj.searchStudent()
# obj.showOut()



# Finding Smallest number in a list by linear search
# def smallInList(list_):
#     small = list_[0]
#     for ele in range(0, len(list_)):
#         if list_[ele] > small:
#             small = list_[ele]
#     print(small)

# smallInList([7, 3, 9, 2, 4,  3 ,1])


# binarySearch for finding the smallest term

# def binarySearch(list_):
#     small = list_[0]

#     left = 0
#     right = len(list_) - 1 
#     while left <= right:
#         mid = (left + right)// 2
#         if list_[mid] <= small:
#             print(list_[mid])
#             left = mid + 1
#         else:
#             right = mid - 1

# binarySearch([10, 9, 5, 2 , 1])


#  LinkedList

# class Node(object):
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next



# class LinkedList(object):
#     def __init__(self):
#         self.head = None

#     def insert(self, data):
#         global newNode
#         newNode = Node(data)
#         if self.head:
#             current = self.head
#             while self.head:
#                 current = current.next
#             current.next = newNode()
#         else:
#             self.head = newNode

#     def searching(self, target):
#         current = self.head
#         while current != None:
#             print("1")
#             if current.data == target:
#                 print(current)
#             current = current.next
#             print("2")

#     def show(self):
#         current = self.head
#         while current:
#             print(current.data)
#             current = current.next
 


# obj = LinkedList()
# obj.insert([10, 20, 30, 40, 50, 60, 70, 80])
# if obj.searching(10):
#     print('found')
# else:
#     print("No")
# obj.show()

# CodeWars Question

# def multi(arr1, arr2):
#     try:
#         sorted([x**2 for x in arr1]) == sorted(arr2)
#     except:
#         pass

# x = [121, 144, 19, 161, 19, 144, 19, 11]
# y = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

# x = [121, 144, 19, 161, 19, 144, 19, 11]
# y = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

# x = [121, 144, 19, 161, 19, 144, 19, 11]
# y = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]

# multi(x, y)

# ---------------------------------------------------------------------

# firstKSum Program
# import time
# def firstKSum(k):
#     start_time = time.time()
#     return sum(list(range(k+1))), start_time - time.time()

# for x in range(10000):
#     print(firstKSum(x))


#  ListStack

# class ListStack(object):
#     def __init__(self):
#         self.elements = list()

#     def push(self, data):
#         self.elements.append(data)
    
#     def pop(self):
#         return self.elements.pop()

#     def showList(self):
#         return self.elements

#     def peek(self):
#         try:
#             return self.elements[-1]
#         except Exception:
#             return 0

#     def isEmpty(self):
#         if len(self.elements) == 0:
#             return True
#         return False
    
#     def __len__(self):
#         return len(self.elements)
    
# obj = ListStack()
# for ele in range(1, 11):
#     obj.push([1,2])
# print(obj.showList())
# print(obj.pop())
# print(obj.peek())
# print(obj.isEmpty())
# print(obj.__len__())


#  BadStack with inheritance!
#  Not a best practice 

# class BadStack(ListStack):
#     def push(self, item):
#         return self.elements.insert(5, item) # insert item reverse order when you use the first arg in the dot(.)insert
#     def pop(self):
#         index = self.elements.index(max(self.elements))
#         return self.elements.pop(index), index, "is removed"
#     def peek(self):
#         return self.elements[0]
#     def showStack(self):
#         return self.elements

# obj = BadStack()
# for x in range(1, 11):
#     (obj.push(x))
# print(obj.pop())
# print(obj.peek())
# print(obj.showStack())

# ListQueueSimple

# class ListQueueSimple(object):
#     def __init__(self):
#         self.queue = list()
    
#     def enqueue(self, data):
#         return self.queue.append(data)

#     def dequeue(self):
#         return self.queue.pop(0)
    
#     def __len__(self):
#         return len(self.queue)

#     def isEmpty(self):
#         return len(self.queue) == 0

# obj = ListQueueSimple()
# for ele in range(1, 11):
#     obj.enqueue(ele)
# print(obj.dequeue())
# print(obj.__len__())
# print(obj.isEmpty())

# FakeListQueueDelete

# class FakeListQueue(object): 
#     def __init__(self):
#         self.element_list = list()
#         self.head = 0
    
#     def enqueue(self, data):
#         return self.element_list.append(data)

#     def peek(self):
#         return self.element_list[self.head]

#     def dequeue(self):
#         item = self.element_list[self.head]
#         self.head+=1
#         if self.head > len(self.element_list) // 2:
#             self.element_list = self.element_list[self.head:]
#             self.head = 0
#         return item


#     def __len__(self):
#         return len(self.element_list) - (self.head)

#     def isEmpty(self):
#         return len(self.element_list) == 0

#     def showElement(self):
#         return self.element_list

# obj = FakeListQueue()
# for ele in range(1, 11):
#     obj.enqueue(ele)
# print(obj.peek())
# print(obj.dequeue())
# print(obj.__len__())
# print(obj.isEmpty())
# print(obj.showElement())


# ListDequeue

# class ListDeque(object):
#     def __init__(self):
#         self.list_element = list()

#     def add_item_first(self, data):
#         return self.list_element.insert(0, data)

#     def add_item_last(self, data):
#         return self.list_element.append(data)
    
#     def remove_item_first(self):
#         return self.list_element.pop(0)
    
#     def remove_item_last(self):
#         return self.list_element.pop()

#     def showInfo(self):
#         return self.list_element
    
#     def __len__(self):
#         return len(self.list_element)

# obj = ListDeque()
# for ele in range(1, 5):
#     obj.add_item_first(ele)
# for ele in range(5, 10):
#     obj.add_item_last(ele)
# print(obj.remove_item_first())
# print(obj.remove_item_last())
# print(obj.showInfo())
# print(obj.__len__())


# class ListNode(object):
#     def __init__(self, data, prev=None, next=None):
#         self.data = data
#         self.prev = prev
#         self.next = next

#         if prev is not None:
#             self.prev.next = self
#             self.next.prev = self

# class DoublyLinkedListNode(object):
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

#     def addFirst(self, data):
        


# obj = DoublyLinkedListNode()
# obj.addFirst(12)


# Student GPA Calculator

# grade = {
#         'A+' :4.0, 'A' :4.0, 'A-' :3.67, 'B+' :3.33, 'B' :3.0, 'B-' :2.67,
#         'C+' :2.33, 'C' :2.0, 'C' :1.67, 'D+' :1.33, 'D' :1.0, 'F' :0.0
#     }

# class GPACal(object):
    
#     def __init__(self):
#         self.subject = 0
#         self.total_marks = 0
        
    
#     def inputFun(self):
#         done = False
#         while not done:
#             score = input().upper()
#             if score == "" or None:
#                 done = True
#             elif score not in grade:
#                 print("Error")
#             else:
#                 self.subject += 1
#                 self.total_marks += grade[score]

#         if self.subject > 0:
#             print(self.subject/self.total_marks)

# obj = GPACal()
# obj.inputFun()


# Next Iteration ---------------------------------
# class Progression(object):
#     def __init__(self, start=0):
#         self._current = start
    
#     def _advance(self):
#         self._current += 1

#     def __next__(self):
#         if self._current is None:
#             raise StopIteration()
#         else:
#             answer = self._current
#             self._advance()
#             return answer
    
#     def __iter__(self):
#         return self
    
#     def print_progress(self, n):
#         print(' '.join(str(next(self))for j in range(n)))


# obj = Progression()
# print(obj.__next__())
# print(obj.__iter__())
# print(obj.print_progress(30))


# Python Range! built-in methods-----------------------------------
# class Range(object):
#     def __init__(self, start, stop=None, step=1):
#         if step == 0:
#             raise ValueError("step must be")

#         if stop is None:
#             start, stop = 0, start 

#         self.length = max(0,(stop-start + step+1) // step )

#         self.start = start
#         self.step = step


#     def __len__(self):
#         return self.length

#     def __getitem__(self, k):
#         if k < 0:
#             k+=len(self)
        
#         if not 0 <= k < self.length:
#             raise IndexError
#         return self.start+k*self.step


# obj = Range(9)
# print(obj.__len__())
# print(obj.__getitem__(4))
    

# Factorial with Recursion-------------------

# def fact(num):
#     if num == 0:
#         return 1
#     else:
#          return num*fact(num-1)
        
# print(fact(3))


# BinarySearch method------------------------
# def binarySearch(num, target):
#     low = 0
#     high = len(num)-1
#     while low <= high:
#         mid = high + low // 2
#         if num[mid] == target:
#             print("Found a match", num[mid])
#             break
#         elif num[mid] < target:
#             low +=1
#         else:
#             high -= 1

# binarySearch([1,2,3,4,5, 6, 7, 8, 9, 10], 10)



# InserationSort--------------------------
# def inserationSort(list_of_nums):
#     for k in range(len(list_of_nums)):
#         cur = list_of_nums[k]
#         j = k
#         while j > 0 and list_of_nums[j-1] > cur:
#             list_of_nums[j] = list_of_nums[j-1]
#             j-=1
#             list_of_nums[j] = cur
#     return list_of_nums

# print(inserationSort([5,4,3,2,1]))


# SimpleStack

# class Stack(object):
#     def __init__(self):
#         self._stack_container = list()

#     def push(self, item):
#         self._stack_container.append(item)

#     def pop(self):
#         if self.is_empty():
#             raise "Error: empty stack"
#         return self._stack_container.pop()

#     def top(self):
#         if self.is_empty():
#             raise "Error: empty stack"
#         return self._stack_container[-1]

#     def is_empty(self):
#         return len(self._stack_container) == 0

#     def __len__(self):
#         return len(self._stack_container)

#     def __show__(self):
#         return self._stack_container

# obj = Stack()
# for ele in range(10):
#     obj.push(ele)
# print(obj.pop())
# print(obj.top())
# print(obj.is_empty())
# print(obj.__len__())
# print(obj.__show__())


# ArrayQueue

# class ArrayQueue(object):

#     DEFAULT_SIZE = 10

#     def __init__(self):
#         self._size = 0
#         self._front = 0
#         self.array = [0] * ArrayQueue.DEFAULT_SIZE

#     def __len__(self):
#         return self._size
    
#     def is_empty(self):
#         return self.__len__() == 0

#     def first(self):
#         if self.is_empty():
#             print('Empty')
#         return self.array[self._front]

#     def dequeue(self):
#         if self.is_empty():
#             raise "empty"
#         answer = self.array[self._front]
#         self.array[self._front] = None
#         self._size -= 1
#         return answer


#     def enqueue(self, data):
#         if len(self._size.__str__()) == len(self.array):
#             self.resize = (2 * len(self.array))
#         avail = (self._front + self._size) % len(self.array)
#         self.array[avail] = 0
#         self._size += 1

#     def resize(self, cap):
#         old = self.array
#         self.array = [None] * cap
#         walk = self._front
#         for k in range(self._size):
#             self.array[k] = old[walk]
#             walk = (1 + walk) % len(old)
#         self._front = 0

#     def show(self):
#         return self.array

    
# obj = ArrayQueue()
# obj.__len__()
# obj.enqueue(10)
# obj.enqueue(12)
# obj.enqueue(15)
# print(obj.enqueue(18))

# print(obj.dequeue())
# print(obj.resize(4))
# print(obj.__len__())
# print(obj.show())


# ====================================================================================================
# LinkedStack or LinkedList Singly STACK

# class LinkedStack(object):

#     class Node:
#         __slots__ = '_element', '_next'
#         def __init__(self, element, next):
#             self._element = element
#             self._next = next

    
#     def __init__(self):
#         self._head = None
#         self._size = 0


#     def __len__(self):
#         return self._size

#     def is_empty(self):
#         return self._size == 0

#     def push(self, value):
#         self._head = self.Node(value, self._head)
#         self._size += 1

    
#     def top(self):
#         if self.is_empty():
#             raise "Empty"

#         return self._head._element

#     def pop(self):
#         if self.is_empty():
#             raise "Empty"
#         answer = self._head._element
#         self._head = self._head._next
#         self._size -= 1

#         return answer

#     def showItem(self):
#         return self._head._element, self.__len__()
    

# obj = LinkedStack()
# for ele in range(1, 5):
#     obj.push(ele)
# print("Top: ", obj.top())
# print("Empty: ", obj.is_empty())
# print("Length: ", obj.__len__())
# print('Pop: ',obj.pop())
# print("Showing: ", obj.showItem())



# ====================================================================================================
# Implementing of Queue in LinkedList

# class LinkedQueue(object):

#     class Node(object):
#         def __init__(self, element, next):
#             self._element = element
#             self._next = next

        
#     def __init__(self):
#         self._head = None
#         self._tail = None
#         self._size = 0

#     def __len__(self):
#         return self._size

#     def is_empty(self):
#         return self._size == 0

#     def first(self):
#         if self.is_empty():
#             raise "Empty"
#         return self._head._element

#     def second(self):
#         if self.is_empty():
#             raise "Empty"
#         return (self._head._next._element)

#     def dequeue(self):
#         if self.is_empty():
#             raise "Empty"
#         answer = self._head._element
#         self._head = self._head._next
#         self._size -= 1
#         if self.is_empty():
#             self._tail = None
#         return answer

#     def enqueue(self, data):
#         newNode = self.Node(data, None)
#         if self.is_empty():
#             self._head = newNode
#         else:
#             self._tail._next = newNode
#         self._tail = newNode
#         self._size += 1
        

# obj = LinkedQueue()
# for ele in range(1, 5):
#     (obj.enqueue(ele))

# print("First: ", obj.first())
# print("Second: ", obj.second())
# print("__len__: ", obj.__len__())
# print("is_empty: ", obj.is_empty())
# print("dequeue: ", obj.dequeue())
# print("__len__: ", obj.__len__())


# ===============================================================
# Circular LinkedList

# class CircularLinkedList(object):

#     class Node(object):
#         def __init__(self, element, next):
#             self._element = element
#             self._next = next

#     def __init__(self):
#         self._tail = None
#         self._size = 0

#     def __len__(self):
#         return self._size

#     def is_empty(self):
#         return self._size == 0

#     def first(self):
#         if self.is_empty():
#             raise "Empty"
#         head = self._tail._next
#         return head._element

#     def second(self):
#         return self._tail._next

#     def last(self):
#         return self._tail._element

#     def dequeue(self):
#         if self.is_empty():
#             raise "Empty"
#         oldhead = self._tail._next
#         if self._size == 1:
#             self._tail = None
#         else:
#             self._tail._next = oldhead._next
#         self._size -= 1
#         return oldhead._element

#     def enqueue(self, data):
#         newNode = self.Node(data, None)
#         if self.is_empty():
#             newNode._next = newNode
#         else:
#             newNode._next = self._tail._next
#             self._tail = newNode
#         self._tail = newNode
#         self._size += 1

#     def rotate(self):
#         if self._size > 0:
#             self._tail = self._tail._next




# obj = CircularLinkedList()
# for ele in range(1, 5):
#     ('Enqueue: ', obj.enqueue(ele), ele)

# print('Empty: ', obj.is_empty())
# print('Length: ', obj.__len__())
# print('First: ', obj.first())
# print('Second: ', obj.second())
# print("Last: ", obj.last())
# print('Dequeue: ', obj.dequeue())
# print('Length: ', obj.__len__())



# Doubly LinkedList

# class DoublyLinked(object):

#     class Node(object):
#         def __init__(self, element, prev, next,):
#             self._element = element
#             self._prev = prev
#             self._next = next

#     def __init__(self):
#         self._header = self.Node(None, None, None)
#         self._tailer = self.Node(None, None, None)
#         self._header._next = self._tailer
#         self._tailer._prev = self._header
#         self._size = 0

#     def __len__(self):
#         return self._size

#     def is_empty(self):
#         return self._size == 0

#     def insert(self, data, firstD, secD):
#         newNode = self.Node(data, firstD, secD)
#         firstD._next = newNode
#         secD._prev = newNode
#         self._size += 1
#         return newNode

#     def delete(self, node):
#         firstD = node._prev
#         secD = node._next
#         firstD._prev = firstD
#         secD._next = secD
#         self._size -= 1
#         element = node._element
#         node._prev = node._next = node._element = None
#         return element

    

# obj = DoublyLinked()

# print(obj.insert(5, 6 , 3))

# print(obj.is_empty())

# print(obj.__len__())


# class Tree(object):

#     class Position(object):

#         def element(self):
#             raise NotImplementedError("Element")
        
#         def __eq__(self, other):
#             raise NotImplementedError("__eq__")
        
#         def __ne__(self, other):
#             return not (self == other)

#     def root(self):
#         raise NotImplementedError("Root")
    
#     def parent(self, p):
#         raise NotImplementedError("Parent")

#     def num_children(self, p):
#         raise NotImplementedError("NumChildren")

#     def children(self, p):
#         raise NotImplementedError("Children")

#     def __len__(self):
#         raise NotImplementedError("__len__")

#     def is_root(self, p):
#         return self.root() == p

#     def is_leaf(self, p):
#         return self.num_children() == p

#     def is_empty(self):
#         return len(self) == 0


# obj = Tree()
# print(obj.is_empty())




# Reverse a string but in a different order

# def stringToReversed(string):
#     s = string.split()[::-1]
#     print(s)

# stringToReversed("Hello world how are you?")

# def factorial(n):
#     if n == 0: return 1
#     return n * factorial(n-1)

# print(factorial(5))


# def get_sum(a, b):
#     if a < 0:
#         return a + 0 + a + b
#     elif b < 0:
#         return b + 0 + b + a
#     return a + b if a != b else b


# print(get_sum(-1, 0))


# CODEWARE PROBLEM

# number_dict = {
#         1   : "one",
#         2   : "two",
#         3   : "three",
#         4   : "four",
#         5   : "five",
#         6   : "six",
#         7   : "seven",
#         8   : "eight",
#         9   : "nine",
#         0   : "zero",
#     }

# def numbers_of_letters(num):
    

#     last_result = list()
#     semi_last = str()
#     str_num = str(num)
#     for loop in str_num:
#         semi_last += (number_dict[int(loop)])
#     last_result.append(semi_last)
#     last_result.append(number_dict[len(semi_last)])
#     while True:
#         if last_result[-1] != number_dict[len(last_result[-1])]:
#             last_result.append(number_dict[len(last_result[-1])])
#         else:
#             break
        
    
#     print(last_result)

# numbers_of_letters(99)

# SortedNumber Reverse CODEWARE
# def sortNum(number):
#     l = list()
#     l.extend(str(number))

#     s = str()
#     for x in sorted(l):
#         s+=x
    
#     return int(str(s)[::-1])

# print(sortNum(39285))


# Persisitan Bugger CODEWARE

# def persistence(num):
#     if num < 10:
#         return 0 
#     num_str = str(num)
#     total = 1
#     for i in num_str:
#         total = total * int(i)
#     return 1+ persistence(total)

# print(persistence(39))

# Mumbling

# def mumbling(string):
#     output = []
#     for count, value in enumerate(string):
#         output.append(value.upper() + value.lower()*count)
#     return "-".join(output)

# print(mumbling("arsh"))


# Printing the higest and lowest code_wars

# def high_low(number):
#     nn = [int(s) for s in numbers.split(" ")]
#     return "%i %i" % (max(nn),min(nn))
    
# high_low('1 2 3 4 6')

# Perfect Square

# import math

# def perfect_square(number):
#     num = math.sqrt(number)
#     return num**2 == float(number)

# print(perfect_square(4))


# mean leetCode

# def mean(num1, num2):
#     leng = len(num1)+len(num2)
#     l = sum(num1)+sum(num2)
#     return (l/leng)

# print(mean([1,2], [3,4]))


# Bus Stop Program CodeWars

# def busStopProgram(bus_stop):
#     num1 = num2 = 0
#     for x in range(len(bus_stop)):
#         num1 = num1 + bus_stop[x][0]
#         num2 = num2 + bus_stop[x][1]

#     return num1 - num2



# print(busStopProgram([[10,0],[3,5],[5,8]]))


# Change binary to Decimal but binary list elements codewars

# def binaryList(numberList):
#     str_binary = "".join([(x) for x in str(numberList)])
#     return int(str_binary, 2)

# print(binaryList(1001))



# light sabers codewars

# def lighsabers(name=""):
#     return 18 if name == "Zach" else 0

# print(lighsabers("Zach"))


# spinWord reversing the words if the sentence has more than 5 words CODEWARS

# def spinWord(string):
#     return string.join(x for x in string.split())
    

# print(spinWord("Hey, this is another"))


# IsoGrams Program Codewars, oppositie words

# def isoGrams(word):
#     strVar = str()
#     for x in word.lower():
#         if x not in strVar:
#             strVar+=x
#     return len(strVar)==len(word)

        

# print(isoGrams(""))


# Exes and ohs Codewars

# def exes_ohs(string):
#     if string.lower().count('x') == string.lower().count('o'):
#         return True
#     elif 'x' and 'o' not in string:
#         return True
#     else:
#         return False

# print(exes_ohs('xxoo'))
        

# words into sentences codewars

# def wordsIntoSentence(words):
#     return " ".join(x for x in words)

# print(wordsIntoSentence(['hello', 'world']))


# getting the middle character codewars

# def middle(string):
#     if len(string) %2 == 0:
#         return string[len(string)//2-1] + string[len(string)//2]
#     else:
#         return string[len(string)//2]
        

# print(middle("ars"))


# split strings and adding '_' if its odd


# def splitString(string):
#     if len(string) % 2 == 0:
#         return string.split()
#     else:
#         return string.split()

# print(splitString("arsh"))


# powering program 1^2+2^2+2^2 = 9 Codewars

# def power(number):
#     return sum([int(str(x))**2 for x in number])
# print(power([0, 3, 4, 5]))
# # 9 + 14 + 25


# does my number look big in this. codewars

# def narasicticNumber(number):
#     return sum([int(x)**(len(number.__str__())) for x in number.__str__()]) == number


# print(narasicticNumber(4887))

# Sentence Smash


# def sentenceSmash(sentence): codewars
#     return " ".join([x for x in sentence])

# print(sentenceSmash(['hello', 'hey', 'world']))


# removeSmallest number

# def removeSmallest(number):
#     # return number.sort()
#     print(number.pop(number.index(min(number))))
#     print(number)

# print(removeSmallest([1, 1,2,1,4,1]))


# sum of digits example: 942 = 9 + 4 + 2 = 15 = 1 + 5 = 6 STOP
# CodeWars

# def sumOfDigits(num):
#     if len(str(num)) == 1:
#         return num
#     return sumOfDigits(sum([int(x) for x in str(num)]))

# print(sumOfDigits(942))


# Make negative number CodeWars

# def make_negative(number):
#     if number > 0:
#         return '-'+str(number)
#     else:
#         return number
    
# print(make_negative(12))


# Count_Monkeys CodeWars

# def monkeys_count(number):
#     return list(range(1, number+1))

# print(monkeys_count(10))


# return the missing letter CodeWars

# def missingLetter(letters):
#     # for x in range(ord(letters[0]), ord(letters[0])+len(letters)+1):
#     #     if chr(x) not in letters:
#     #         return chr(x)

#     return ''.join([chr(x) for x in range(ord(letters[0]), ord(letters[0])+len(letters)+1) if chr(x) not in letters])

#     # return lengthOfLetter

# print(missingLetter(['a','b','c','d','f']))


# Alphabet war CodeWars
# Couldn't solve it
# def alphabetWar(fight):
#     right = left = 0
#     alpha_dict_right = {
#         'w' : 4,
#         'p' : 3,
#         'b' : 2,
#         's' : 1,
#     }
#     alpha_dict_left = {
#         'z' : 1,
#         'd' : 2,
#         'm' : 4,
#         'q' : 3
#     }
#     for letter in fight:
#         if alpha_dict_right[letter] in alpha_dict_right.keys():
#             right += 1
#         elif alpha_dict_left[letter] in alpha_dict_left.keys():
#             left += 1
        
    
#     if right > left:
#         return 'Right side wins!'
#     elif left > right:
#         return 'Left side wins!'
#     else:
#         return 'Lets fight again!'
#     # print(alpha_dict_left['z'])
# print(alphabetWar('zdqmwpbs'))



# array differences in list CodeWars

# def arrayDifference(array1, array2):
#     return list(set(array1) - set(array2))
# print(arrayDifference([1,2], [1]))


# count the positive and negative numbers in a list

# def countNumbers(array):
#     x= (len(array)//2)
#     a = b = 0
#     for i in array[:x]:
#         print(i)
#         if i > 0:
#             a +=1
#     for i2 in array[x:]:
#         if i2 < 0:
#             b+=i2
#     y = (a, b)

#     return a, b



# print(countNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))


# multiple of indexes CodeWars

# def multipleOfIndexes(array):
#     newArray = list()
#     for key, value in enumerate(array):
#         if key**2 == array[key]:
#             newArray.append(value)
#         print(key**2, ':', array[key])
#     return newArray

# (multipleOfIndexes([22, -6, 32, 82, 9, 25]))



# keep hydrated CodeWars

# def hydrated(hours):
#     return int(float(0.5)*hours)
# print(hydrated(6.7))



# sum without highest and lowest elements

# def lowHighElement(array):
#     if len(array) == 0 or len(array) == 1:
#         return 0
#     else:
#         array.sort()
#         return sum(array)-array[0]-array[-1]

# print(lowHighElement([6, 2, 1, 8, 10 ]))


# fizzbuz CodeWars

# def fizzbuz(n):
#     last_sum = list()
#     for x in range(1, n+1):
#         if x % 5 == 0 and x % 3 == 0:
#             last_sum.append("FizzBuzz")
#         elif x % 3 == 0:
#             last_sum.append("Fizz")
#         elif x % 5 == 0:
#             last_sum.append("Buzz")
#         else:
#             last_sum.append(x)
#     return last_sum

# print(fizzbuz(10))


# nickName Generator CodeWars

# def nickNameGenerator(name):
#     nickName = ''
#     if len(name) < 4:
#         return "Error"
#     elif name[2] not in "aeiou":
#         nickName = name[:3]
#     else:
#         nickName = name[:4]
#     return nickName

# print(nickNameGenerator("Douglas"))



# V A P O R C O D E  CodeWars

# def vapourCode(string):
#     return " ".join([x.upper() for x in string if ord(x) != 32])

# print(vapourCode('Lets go to the movies'))


# not very secure CodeWars


# def alphaNumeric(passwords):
#     if '_' in passwords or " " in passwords:
#         return False
#     return True


# print(alphaNumeric('world'))


# find the calculation type CodeWars

# def calc_type(num1, num2, result):
#     calc_guess_dict = {
#         num1+num2 : "Addition",
#         num1-num2 : "Subtraction",
#         num1/num2 : "Division",
#         num1*num2 : 'Multiplication'
#     }
#     return calc_guess_dict[result]

# print(calc_type(1, 2, 3))



# Longest Word CoderByte

# def longestWord(sentence):
#     str_dict = dict()
#     for words in sentence.split():
#         str_dict[len(words)] = words
#     print(str_dict)

#     return str_dict[max(str_dict.keys())]

# print(longestWord('fun&!! time'))



# List of multiples Edait

# def list_of_multiples(num1, num2):
#     return [num1*multi for multi in range(1, num2+1)]

# print(list_of_multiples(7, 5))


# Duplication in list LeetCode


# def containsDuplicate(array):
#     hash_dict = dict()    
#     for x in sorted(array):
#         if x not in hash_dict:
#             hash_dict[x] = 1
#         else:
#              return True
#     return False


# print(containsDuplicate([1,2, 3, 4, 5, 1, 8, 2, 3]))
    

# Sum of Digits by Recursion

# def sumRecursion(number):
#     if number == 0:
#         return 0
#     return int(number)%10 + sumRecursion(int(number)//10)

# print(sumRecursion(213))


# Power of digits 

# def power(base, exponent):
#     if base == 0 or exponent == 0: return 1
#     return base * power(base, exponent-1)

# print(power(2, 4))


# Longest word in the sentence

# def longestWordSentence(sentence):
#     long_word_dict = dict()
#     for word in sentence.split():
#         long_word_dict[len(word)] = word
#     return long_word_dict[max(long_word_dict.keys())]

# print(longestWordSentence('arsh ergon hey how are you boomboom'))


# Try to know if its divisionable by 3 or not Codewars

# def division_by_three(numbers):
#     sum_of_digits = sum(int(num) for num in numbers)
#     return True if sum_of_digits % 3 == 0 else False

# print(division_by_three('123456'))


# find_outliners

# def find_outliners(numbers):
#     for x in numbers:
#         if x % 2 == 0 or x % 2 !=0 :
#             return numbers[x]




# print(find_outliners([2, 4, 0, 100, 4, 11, 2602, 36]))


# search a 2D matrix leetCode I

# def searchMatrix(matrix, target):
#     col = len(matrix[0])-1
#     for index in range(len(matrix)):
#         while matrix[index][col] > target and col >= 0:
#             col -= 1
#         if matrix[index][col] == target:
#             return True
#     return False
# print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60))


# search a target in a 2D matrix leetCode II

# def seachMatrixII(matrix, target):
#     col = len(matrix[0]) - 1
#     for items in range(len(matrix)):
#         while matrix[items][col] > target and col >= 0:
#             col -= 1
#         if matrix[items][col] == target:
#             return True
#     return False

# print(seachMatrixII([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 30))


# Reversing an Integer LeetCode

# def reverseInt(integerToReversed):
#     str_val = str(abs(integerToReversed))[::-1]
#     if int(str_val) > 2**31-1:
#         str_val = 0

#     return -int(str_val) if '-' in str(integerToReversed) else int(str_val)


# print(reverseInt(-1233456789))


# string into integer Atoi like C and C++

# def myAtoi(stringToConvert):
#     string_stored = str()
#     if ord(str(stringToConvert[0]).lower()) in range(97, 123):
#         return 0
#     if chr(32) in stringToConvert[0] or stringToConvert[0] is int or str(stringToConvert[0]=='-'):
#         for item in stringToConvert.lower():
#             if item == chr(32) or ord(item) in range(97, 123) or ord(item) in ['+', '-', '.']:
#                 continue
#             else:
#                 string_stored += item
#         try:
#             if (int(string_stored)) < -2**31:
#                 string_stored = -2**31
#             elif int(string_stored) > 2**31-1:
#                 string_stored = 2**31-1
#             return int(string_stored) 
#         except ValueError:
#             return int((string_stored))

#     return 0



# print(myAtoi("3.14"))


# reverse the words of the string if it has more than 5 words codewars

# def reverse_words(string):
#     return " ".join(x[::-1] if len(x) > 4 else x for x in string.split())

# print(reverse_words('Hey fellow warriors'))



# returning the shortest length word

# def short_word(string):
#     return min(len(word) for word in string.split())

# print(short_word('Lets all go on holiday somewhere very cold'))


# # leap year program CodeWars


# def isLeapYear(year):
#     return True if year % 4 == 0 and year % 100 else False

# print(isLeapYear(2000))



# sum of the two lowest positive numbers

# def sum_two_smallest_numbers(numbersArray):
#     return sorted(numbersArray)[0] + sorted(numbersArray)[1]


# print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))



# higher order functional series CodeWars

# def count_language(list_of_things):
#     dict_items = dict();value = 1
#     for item in range(len(list_of_things)):
#         if list_of_things[item]['language'] in dict_items.keys():
#             dict_items[(list_of_things[item]['language'])] += 1
#             # print(list_of_things[item]['language'])
#             print(dict_items, 'if')
#         else:
#             dict_items[(list_of_things[item]['language'])] = value 
#             print(dict_items, 'else')
#             # print(list_of_things[item]['language'], 'else')
#     return dict_items


# print(count_language([
#             { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C' },
#             { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript' },
#             { 'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby' },
#             { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C' },
#             ]))




# returning the sum of a array whose have both negative and positive numbers Codewars

# def sumOfPositiveNumbers(array):
#     return  sum(pos for pos in array if pos > 0)

# print(sumOfPositiveNumbers([1,-4,7,12]))


# reduce but grow (multiplying the numbers of the array)

# def growArray(array):
#     multi_store = 1
#     mid = len(array)-1//2
#     for multi in array[mid:]:
#         multi_store *= multi
#     for multi in array[:mid]:
#         multi_store *= multi
#     return multi_store

# print(growArray([1,2,3,4]))


# finding the unique number in a array

# def find_uniq(array):
#     array = sorted(array)
#     if array[0] != array[-1]:
#         if array[0] == array[1]:
#             return array[-1]
#         else:
#             return array[0]
#     return 0

# print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))


# Middle me program CodeWars

# def middleMe(N, X, Y):
#     Y *=  N
#     midLeng = len(Y)//2
#     if Y[:midLeng] == Y[midLeng:]:
#         return Y[:midLeng] + X + Y[midLeng:]
#     return X

# print(middleMe(11, 'A', '*'))


# Who likes it? CodeWars

# def likes(names):
#     # if len(names) == 0:
#     #     return "No one likes this"
#     # elif len(names) == 2:
#     #     return names[0] + ' and ' + names[1] + "likes this"
#     # elif len(names) > 2:
#     #     return names[0] + ' and ' + names[1] + f' and {len(names)-2} others likes this'
#     # return 0
#     d = {
#         0: 'no one likes this',
#         1 : f'{names[0]} likes this',
#         2 : f'{names[0]} and {names[1]} like this',
#         3 : f'{names[0]}, {names[1]} and {names[2]} like this',
#         4 : f'{names[0]}, {names[1]} and {len(names)-2} like this',
#         00 : f'{names[0]}, {names[1]} and {len(names)-2} like this',

#     }
#     # return d[len(names)] if len(names) in d else d[00]
#     x = len(names)
#     return  x

# print(likes([]))


# # Printer Errors CodeWars

# def printer_Error(color_strings):
#     counter = 0
#     for items in color_strings:
#         if ord(items) not in range((97), (110)):
#             counter += 1
#     return f"{counter}/{len(color_strings)}"

# print(printer_Error('aaaxbbbbyyhwawiwjjjwwm'))



# Your Order Please CodeWars

# def orderByInt(sentence):
#     dict_item = dict()
#     for item in sentence.split():
#         dict_item[int(sorted(item)[0])] = item
#     return " ".join([dict_item[x] for x in range(1, len(dict_item)+1)])

# print(orderByInt('is2 Thi1s T4est 3a'))


# which are in? codewars

# def in_arry(array1, array2):
#     l = list()
#     for a2 in array2:
#         print(a2)
#         if a2 in array1:
#             l.append(a2)
            
        
#     return l

# print(in_arry(["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))


# count the divisors of a number CodeWars

# def divisors(number):
#     return len([x for x in range(1, number+1) if number%x==0])

# print(divisors(4))


# first uique character in a string

# def findUniqueChar(string):
#     d = dict()
#     l = list()
#     for key, value in enumerate(string):
#         if value  in l:
#             l.remove(value)
#         else:
#             l.append(value)
#             d[value] = key

#         print(l, d)
    # return d[l[0]] if d and l else -1


    # for key, value in enumerate(string):
    #     if value in d.keys():
    #         del d[value]
    #     else:
    #         d[value] = key

    # return d[next(iter(d))]

# print(findUniqueChar('aadadaad'))


# the feast of many beast codewars

# def Feast(beast, feast):
#     return  beast[0]  == feast[0] and beast[-1] == feast[-1]

# print(Feast("great blue heron", "garlic naan"))


# Convert string to CamelCase codewars

# def camelCase(sentence):
#     sentence = sentence.replace('-', " ")
#     s = str()
#     for x in sentence.split():
#         s+= (x.capitalize())+' '
#     return s.replace(' ', '_')[0:-1]

# print(camelCase("the-stealth-warrior"))


# first non repeating letter in a string Codewars

# def first_non_repeating_letter(string):
#     d = dict()
#     for key, element in enumerate(string):
#         # print(element, '=', key, string[key::])
#         if element in d:
#             del d[key] 
#         else:
#             d[key] = element
#     return d[0]

# print(first_non_repeating_letter('stress'))


# Disemvolwel trolls codewars

# def remVolwels(string):
#     for ele in string:
#         if ele in 'aeiou':
#             string.replace('', ele)
#     return string

# print(remVolwels('This website is for losers LOL!'))


# sum of all positive numbers from 1 to Nth term

# def SumPosNumbers(nums):
#     return sum(list(range(1, nums+1))) if nums > 0 else False

# print(SumPosNumbers(100))


# find the numbers which are divisible by given number CodeWars

# def divisible_by(number, diviser):
#     return [num for num in number if num % diviser == 0]

# print(divisible_by([1,2,3,4,5,6], 2))


# Move Zero LeetCode

# def swapZero(numbers):
#     j = 0
#     for nums in numbers:
#         if nums!=0:
#             numbers[j] = nums
#             j+=1 
#             print(numbers, j)
        
#     for x in range(j, len(numbers)):
#         # print(numbers)
#         numbers[x] = 0
#         # print(j)

#     # print(numbers)
# swapZero([1, 2, 0, 0, 1, 4])


# Remove Element

# def removeElement(numbers, pop):
#     j = 0; c = 0
#     for x in (numbers):
#         if x != pop:
#             numbers[j] = x
#             j+=1 
#     for i in range(j, len(numbers)):
#         numbers.remove(numbers[j])
#     return sorted(numbers)

# print(removeElement([1, 2, 3, 3, 4, 2], 3))



# finding missing number in  a list

# def missing(numbers):
#     n = len(numbers)
#     sub_sum = (n+1)*(n+2)//2
#     real_sumArray = sum(numbers)
#     return real_sumArray - sub_sum

# print(missing([1,2,3,4,5,6,7,8,9,10]))


# find the majority of number which repeated in array. LeetCode

# def majorityArray(array):
#     hash_map = dict()
#     for i in array:
#         if i in hash_map:
#             hash_map[i] += 1
#         else:
#             hash_map[i] = 1

#     for key in hash_map:
#         if hash_map[key] > len(array) // 2:
#             print(key)
#             return key

# (majorityArray([2,2,1,1,1,2,2]))


# dont give me five codewars

# def dont_give_me_five(start, end):
#     count = 0
#     for x in range(start, end+1):
#         if '5' in str(x):
#             continue
#         else:
#             count+=1
#             print(x)
#     return count

# print(dont_give_me_five(54, 119))


# Regex validate PIN Code Codewars

# import re
# def validate_pin(password):
#     print(re.findall('[|\^&+\-%*/=!>a-zA-Z:]', password))
#     # if re.findall('[a-z][+]', password):
#     #     return False
#     # else:
#     #     return True if len(password) in [4, 6] else False

# print(validate_pin("1234:"))


# Initial of names CodeWars

# def abbrv_name(names):
#     s = str()
#     for name in names.title().replace(' ',''):
#         if name == name.upper():
#             s+= name
#     return '.'.join(s)

# print(abbrv_name("arsh ergon"))



# Two Sum leetCode

# def twoSum(array, target):
#     seen = dict()
#     for key, num in enumerate(array):
#         if target-num in seen:
#             return seen[target-num], key
#         seen[num] = key

        
# print(twoSum([1, 2, 1, 2], 4))


# Count the repeated alphabet in a string HackerRank

# def 


# Digital power codeWars

# def dig_pow(number, power):
#     last_result = 0
#     for x in str(number):
#         last_result += pow(int(x), power)
#         power+=1

#     result = last_result // number

#     return result if result != 0 else -1

# print(dig_pow(46288, 3))


# find the odd int in an array which repeated odd number of time

# def find_it(array):
#     d = dict()
#     for x in array:
#         if x in d:
#             d[x] += 1
#         else:
#             d[x] = 1
#     for i in d.keys():
#         if d[i] % 2 != 0:
#             return i

# print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))


# finding missing number in leet_code

# def missing_number(numbersArray):
#     res = 0
#     c = 0
#     for x in numbersArray:
#         res = res ^ c ^ x
#         c+=1
#         return res ^ c

# print(missing_number([9,6,4,2,3,5,7,0,1]))


# bitStr all possible alpabets

# def bitStr(num, string):
#     if num == 1:
#         return string
#     return [digit + bits for digit in bitStr(1, string) for bits in bitStr(num-1, string)]

# print(bitStr(2, 'ab'))


# Merge sort 

# def mergeSort(array):
#     if len(array) > 1:
#         mid = len(array) // 2
#         left = array[:mid]
#         right = array[mid:]
#         mergeSort(left)
#         mergeSort(right)

#         i = k = j = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i+=1
#             else:
#                 array[k] = right[j]
#                 j+=1
#             k+=1

#         while i < len(left):
#             array[k] = left[i]
#             i+=1
#             k+=1

#         while j < len(right):
#             array[k] = right[j]
#             j+=1
#             k+=1

#     return array

# print(mergeSort([8, 9, 4, 1, 2, 3, 6]))



# LinkedList Python https://blog.learncodeonline.in/linked-list-in-python

# class Node:

# 	def __init__(self, data, next=None):
# 		## data of the node
# 		self.data = data

# 		## next pointer
# 		self.next = next

# class LinkedList:
    
#     def __init__(self):
# 		## initializing the head with None
#         self.head = None

#     def add(self, element):
#         newNode = Node(element, self.head)

#         self.head = newNode


#     def printEle(self):
#         current = self.head
#         linkedList = ''

#         while current!=None:
#             linkedList += str(current.data)+"--->"
#             # print(itr.next)
#             current=current.next

#         return f'Elements: {linkedList}'

#     def length(self):
#         current = self.head
#         leng = 0
#         while current != None:
#             leng +=1

#             current=current.next

#         return f'length {leng}'

#     def maxLink(self):
#         current = self.head
#         maxNode = self.head.data
#         while current:
#             if maxNode < current.data:
#                 maxNode = current.data

#             current = current.next

#         return f'Max: {maxNode}'

    
#     def minLink(self):
#         current = self.head
#         minNode = self.head.data

#         while current:
#             if minNode > current.data:
#                 minNode = current.data
#             current = current.next

#         return f'Min: {minNode}'

    
#     def find(self, target):
#         current = self.head
#         count = 0
#         while current:
#             if current.data == target:
#                 return f'{current.data} index: {count}'
#             current = current.next
#             count+=1
#         return "Not Found"

    
#     def valueByIndex(self, index):
#         current = self.head
#         count = 0
#         while current:
#             if count == index:
#                 return current.data
#             count+=1
#             current = current.next
#         return 0


    
#     def reverse(self):
#         current = self.head
#         prev = None

#         while current:
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next

#         self.head = prev

#         return 0      


#     def findIndex(self, number):
#         current = self.head
#         count = 0
#         while current:
#             if current.data == number:
#                 return count
#             current = current.next
#             count += 1
#         return count


#     def is_present(self, element):
#         if element == 0:
#             self.head = self.head.next
#         current = self.head
#         prevs = self.head
#         while current:
#             if current.data == self.findIndex(element)-1:
#                 current.next = current.next.next
#                 break
#             current = current.next
#         return 0



# obj = LinkedList()
# for x in range(11):
#     (obj.add(x))

# # obj.add(15)

# print(obj.printEle())
# print(obj.length())
# print(obj.maxLink())
# print(obj.minLink())
# print(obj.find(3))
# print(obj.valueByIndex(0))
# print(obj.reverse())
# print(obj.printEle())
# print(obj.is_present(9))
# print(obj.printEle())



# If a string has a unique charaters or not it count whitespaces also

# def isUniqueChar(string):
#     unique_Dict = dict()
#     for letters in string:
#         if letters not in unique_Dict:
#             unique_Dict[letters] = 1
#         else:
#             return False
#     return unique_Dict


# print(isUniqueChar('arsh li egon'))



# the hashtag generator

# def hashTag(string):
#     if len(string) == 0:
#         return string
#     else:
#         return '#'+''.join(s.capitalize() for s in string.split())

# print(hashTag('arsh ergon'))



# def search(nums, target):        
#     right = len(nums)-1
#     left = 0
#     while left <= right:
#         mid = (right+left)//2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left+=1
#         else:
#             right-=1
            
#     return -1


# print(search([-1,0,3,5,9,12], 12))


# first unique charater in a string

# def uniqueString(string):
#     d = dict()
#     for key, element in enumerate(string):
#         if element not in d:
#             d[element] = key
#         else:
#             d.pop(element)
#     return list(d.keys())[0]

# print(uniqueString('loveleetcode'))



# Replace alpabets to their number places

# def alpha_number(string):
#     s = str()
#     for x in string:
#         if x.islower() and x != ' ' and ord(x) in range(97, 122):
#             s+= str(ord(x)-96) + ' '
#         elif x.upper() and x != ' ' and ord(x) in range(65, 91):
#             s+= str(ord(x)-64) + ' '
#         else:
#             continue


#     return str(s)

# print(alpha_number('The sunset sets at twelve o clock.'))

# # 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11



# Binary search
# def binary_search(array, target):
#     first = 0
#     last = len(array) - 1
#     while first <= last:
#         midpoint = (first+last) // 2
#         if array[midpoint] == target:
#             return midpoint
#         elif array[midpoint] < target:
#             first = midpoint + 1
#         else:
#             last = midpoint - 1
#     return -1


# print(binary_search([1,2,3,4,5,7,8,9,10], 5))


# Recursive binary search

# import time

# def recursive_binary_search(array, target):
#     start = time.time()
#     if len(array) == 0:
#         return False
#     else:
#         midpoint = len(array)//2
#         if array[midpoint] == target:
#             return True, start-time.time()
#         else:
#             if array[midpoint] < target:
#                 return recursive_binary_search(array[midpoint+1], target)
#             else:
#                 return recursive_binary_search(array[:midpoint], target)



# print(recursive_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 7))



# Linked list fully working linked list ==============================

# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next



# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = self.head
#         self.length = 0


#     def push(self, data):
#         newNode = Node(data, self.head)
#         self.head = newNode 
#         self.length+=1

#     def append(self, data):
#         newNode = Node(data)
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = newNode


#     def display(self):
#         current = self.head
#         l = ""
#         while current:
#             l+=str(current.data)+'--->'
#             current = current.next

#         return l
            
#     def indexLink(self, index):
#         count = 0
#         current = self.head
#         while count != index:
#             current = current.next
#             count+=1
#         return current


#     def insert(self, index, data):
#         if index >= self.length:
#             return self.push(data)
#         else:
#             newNode = Node(data)
#             leader = self.indexLink(index-1 if index != 0 else index)
#             pointer = leader.next
#             leader.next = newNode
#             newNode.next = pointer
#             self.length+=1


#     def delete(self, index):
#         current = self.head
#         if self.length < index:
#             return False
#         leader = self.indexLink(index-1 if index !=0 else index)
#         unwantedNode = leader.next
#         leader.next = unwantedNode.next
#         self.length-=1


#     # getting index by data or else False

#     def getIndexByData(self, data):
#         current = self.head
#         count = 0
#         while current:
#             if current == data:
#                 return count
#             current = current.next
#             count+=1
#         return count 

    
#     def search(self, data):
#         current = self.head
#         while current:
#             if current.data == data:
#                 return self.getIndexByData(current.data)
#             current = current.next

#     def maxNode(self):
#         current = self.head
#         first = current.data
#         while current:
#             if first < current.data:
#                 first = current.data

#             current = current.next
#             return first

#     def minNode(self):
#         current = self.head
#         last = self.head.data
#         while current:
#             if last > current.data:
#                 last = current.data
#             current = current.next
#         return last

        
#     def repeatingNode(self):
#         repeat_dict = dict()
#         current = self.head
#         while current:
#             if current.data in repeat_dict:
#                 repeat_dict[current.data] += 1
#             else:
#                 repeat_dict[current.data] = 1

#             current = current.next
#         return repeat_dict 

# obj = LinkedList()
# for x in range(10):
#     obj.push(x)

# print(obj.display())
# # print(obj.insert(1, 2))
# # print(obj.indexLink(1))
# obj.delete(2)
# print(obj.display())
# print(obj.search(0))
# print(obj.maxNode())
# print(obj.minNode())
# print(obj.repeatingNode())
# print(obj.append(11))
# obj.push(90)
# print(obj.display())




# Stack 

# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next


# class Stack:
#     def __init__(self):
#         self.top = None
#         self.bottom = None
#         self.length = 0


#     def peek(self):
#         return self.top.data


#     def push(self, data):
#         newNode = Node(data, self.top)
#         self.top = newNode
#         self.bottom = self.top.next
#         self.length += 1

    
#     def display(self):
#         current = self.top
#         s = str()
#         while current:
#             s+= str(current.data)+'--->'
#             current = current.next

#         return s

#     def is_empty(self):
#         return self.length == 0

#     def bottoma(self):
#         prev = ''
#         while self.bottom:
#             if self.bottom == None:
#                 return prev
#             else:
#                 _next = self.bottom.data
#                 prev = _next
#             self.bottom = self.bottom.next
#         return prev


#     def pop(self):
#         self.top = self.bottom.next
#         self.bottom = self.bottom.next
#         self.length-=1




# obj = Stack()

# l = ['google', 'udemy', 'twitter', 'reddit', 'discord']
# for i in l:
#     obj.push(i)
# print(obj.display())
# print(obj.is_empty())
# print(obj.peek())
# print(obj.bottoma())
# print(obj.pop())
# print(obj.display())



#  Stack Implementation by Array

    
# class StackArray:

#     def __init__(self):
#         self.arrayData = []


#     def push(self, data):
#         return self.arrayData.append(data)

#     def display(self):
#         return self.arrayData

#     def length(self):
#         return len(self.arrayData)

#     def pop(self):
#         return self.arrayData.pop()

#     def peek(self):
#         return self.arrayData[-1]

# obj = StackArray()
# print(obj.push(1))
# print(obj.push(2))
# print(obj.push(3))
# print(obj.display())
# print(obj.pop())
# print(obj.display())
# print(obj.peek())



# Queue

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

    
# class Queue:
#     def __init__(self):
#         self.first = None
#         self.last = None
#         self.length = 0

#     def enqueue(self, data):
#         newNode = Node(data)
#         if self.length == 0:
#             self.first = newNode
#             self.last = newNode
#         else:
#             self.last.next = newNode
#             self.last = newNode
#         self.length+=1

#     def display(self):
#         current = self.first
#         s = str()
#         while current:
#             s+=str(current.data)+'--->'
#             current = current.next
#         return s


#     def dequeue(self):
#         if self.length == 0:
#             return None
#         else:
#             self.first = self.first.next
#         self.length -= 1

#     def peek(self):
#         return self.first.data
    
# obj = Queue()
# for i in range(1, 11):
#     obj.enqueue(i)

# for i in range(1, 11):
#     print(obj.peek(), 'next')
#     print(obj.display())
#     obj.dequeue()
       

    
# Implementatin Queue by StackArray

# class QueueArray:
#     def __init__(self):
#         self.stack = []

#     def enqueue(self, data):
#         return self.stack.append(data)

#     def dequeue(self):
#         return self.stack.pop(0)
    
#     def front(self):
#         return self.stack[0]
    
#     def rear(self):
#         return self.stack[-1]

#     def display(self):
#         return self.stack


# obj = QueueArray()
# obj.enqueue(1)
# obj.enqueue(2)
# obj.enqueue(3)
# obj.enqueue(4)

# print(obj.dequeue())
# print(obj.front())
# print(obj.rear())
# print(obj.display())



# Binary Search Tree

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.right = None
#         self.left = None

#     def push(self, data):
#         newNode = Node(data)
#         if self.data:
#             if self.data > data:
#                 if self.left is None:
#                     self.left = newNode
#                 else:
#                     self.left.push(data)
#             elif self.data < data:
#                 if self.right is None:
#                     self.right = newNode
#                 else:
#                     self.right.push(data)
#         else:
#             self.data = data

#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print(self.data)
#         if self.right:
#             self.right.PrintTree()

    
#     def inOrderTraversal(self, root):
#         res = []
#         if root:
#             res = self.inOrderTraversal(root.left)
#             res.append(root.data)
#             res+= self.inOrderTraversal(root.right)
#         return res

    
# obj = Node(13)
# for x in range(1, 21, 2):
#     obj.push(x)

# (obj.PrintTree())

# print(obj.inOrderTraversal(obj))



# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/ LeetCode

# class Find:

#     def searchRange(self, nums, target):
#         if((pos := self.BinarySearch(nums, target)) == -1):
#             return [-1, -1]
#         r=l=pos
#         while nums[l] == target and l>0:l-=1
#         while nums[r] == target and r>len(nums)-1:r+=1
#         if nums[l]!=target:l-=1
#         if nums[r]!=target:r+=1
#         return [l, r]


#     def BinarySearch(data, target):
#         left, right = 0, len(data)-1
#         l = list()
#         while left < right:
#             mid = left+(right+left)//2
#             if data[mid] == target:
#                 return mid
#             elif data[mid] < target:
#                 right += 1
#             else:
#                 left -= 1
        
#         return -1


# obj = Find()
# obj.searchRange([10, 9, 7, 7, 1, 1], None)


# Find the index of a sorted list of two integers leetcode

# def binary(nums, target):
#     try:
#         first = nums.index(target)
#         nums.reverse()
#         second = len(nums) - nums.index(target)-1
#         return [first, second]
#     except:
#         return [-1, -1]


# print(binary([5,7,7,8,8,10], 8))



# Permutation codeWars

# def permutation(data):
#     if len(data) == 0:
#         return []

#     if len(data) == 1:
#         return [data]

#     l = dict()
#     for x in range(len(data)):
#         m = data[x]
#         remlist = data[:x] + data[x+1:]
#         for p in permutation(remlist):
#             # l.append(m+p)
#             l[m+p] = 1
#     return list(l.keys())

# print(permutation('aabb'))



# Polish Alphabet CodeWars


# def correct_translation(string):
#     d = {
#         'ą' :  'a',
#         'ć' :  'c',
#         'ę' :  'e',
#         'ł' :  'l',
#         'ń' :  'n',
#         'ó' :  'o',
#         'ś' :  's',
#         'ź' :  'z',
#         'ż' :  'z',
#     }
#     return "".join(d[x] if x in d  else x for x in string ) 


# print(correct_translation('Jędrzej Błądziński'))


# without 'E' codeWars

# def withOutE(string):
#     if not string:
#         return string
    
#     # count = 0
#     # for x in string:
#     #     if x.lower() == 'e':
#     #         count+=1
#     # return count if count else 'There is no "e".'
#     return (string.lower().count('e') if 'e' in string.lower() else "there is no e")

# print(withOutE("nglish"))


# Snail Code CodeWars

# def snail(snail_code):
#     l = list()
#     for x in range(len(snail_code)):
#         l.extend(snail_code[x])
#     return sorted(l)

# print(snail([[1,2,3],
#          [4,5,6],
#          [7,8,9]]))


# Single Digit codeWars

# def single_digits(numbers):
#     if len(str(numbers)) == 1:
#         return numbers
#     value = bin(numbers)[2:].count('1')
#     return single_digits(value) if len(str(value)) != 1 else value


# print(single_digits(5))


# Count the positive numbers and do the sum of negative numbers. 

# def countPosAndNeg(numbers):
#     if not numbers:
#         return numbers
#     else:
#         mid = len(numbers) - 1 // 2
#         _pos = _neg = 0
#         for pos in numbers[:mid]:
#             if pos >= 0:
#                 _pos += 1
#             else:
#                 _neg += pos

#         for neg in numbers[mid:]:
#             if neg <= 0:
#                 _neg += neg
#             else:
#                 _pos += 1

#     return [_pos, _neg]


# print(countPosAndNeg([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))


# Average Scores CodeWars

# def averageScores(scores):
#     if not scores or len(scores) == 1: return scores
#     else: 
#         return round(sum(scores)/len(scores))

# l = [[5, 78, 52, 900, 1],
#     [5, 25, 50, 75],
#     [2],
#     [1, 1, 1, 1, 9999],
#     [0],
#     ]

# for x in l:
#     print(averageScores(x))


# Coding meetUp CodeWars

# def codingMeetUp(nameList):
#     dict_items = dict()
#     for x in range(len(nameList)):
#         dict_items[x] = nameList[x]['age']
#     return 0


# list1 = [{ 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' }]



# Evenly Spaced integers CodingBat

# def EvenSpace(numbers):
#     if not numbers: return numbers
#     else:
#         return sum(numbers) % 2 == 0


# print(EvenSpace([4, 6, 2]))


# MakeBrick CodingBat

# def MakeBrick(small, big, goal):
#     return small + (big*5) >= goal


# print(MakeBrick(3, 2, 8))


# Blackjack

# def blackJack(num1, num2):
#     if num1 > 21: # or in range(15, 21):
#         return num1
#     elif num2 > 21: # or in range(15, 21):
#         return num2
#     else:
#         return False

# print(blackJack(10, 20))


# Array123, if a sequence is present in a list return True

# def array123(array):
#     x = [1,2,3]
#     for i in range(len(array)):
#         # print(array[i:i+len(x)])
#         if array[i:i+len(x)] == x:
#             return True
#     return False

# print(array123(([1, 1, 2, 3, 1])))


# Product of lists leetCode

# def productAndSum(list1):
#     list_num = list(map(int, str(list1)))
#     int_product = 1
#     print(list_num)
#     for x in list_num:
#         int_product *= x

#     return int_product - sum(list_num)


# print(productAndSum(114))


# Reverse a string CoderByte

# def reverse(string):
#     # s = str()
#     # for x in range(1, len(string)+1):
#     #     s+=string[-x]
#     # return s
#     return string[::-1]

# print(reverse('coderByte'))


# String-Splosion CodingBat

# def stringSplosion(string):
#     leng_str = len(string)
#     s = str()
#     x = 0
#     while x<=leng_str:
#         s += string[:x]
#         x+=1

# print(stringSplosion('Code'))


# Repeated String HackerRank

# def repeatedString(string):
    # dict_alpha = dict()
    # c = 1
    # for letter in string:
    #     if letter == 'a':
    #         dict_alpha[letter] = c
    #         c+=1
    # return dict_alpha['a']

    # if not string:
    #     return string
    # return string.count('a')

# print(repeatedString('abacacaaccddca'))



# Maximum SubArray LeetCode

# def maxSubArray(array):
#     if array == [-1]:
#         return -1
#     lengArray = (len(array)-1) // 2
#     sum_ = array[0]
#     res = array[0]
#     for x in range(0, len(array)):
#         res = sum(array[x:lengArray])
#         sum_ = max(sum_, res)
#         if sum(array) > sum_:
#             sum_ = sum(array)
#         lengArray+=1
#     return sum_


    # lengArray = (len(array)-1) // 2
    # sum_ = array[0]
    # res = array[0]
    # for x in range(1, len(array)):
    #     res = max(array[x], array[x] + res)
    #     sum_ = max(sum_, res)
    # return sum_


# print(maxSubArray([-2, 1]))



# Longest Word CodingBat

# import re

# def longestWord(sentence):
#     regex = ('[@_!#$%^&*()<>?/\|}{~:]')
#     if not sentence:
#         return sentence
#     else:
#         dict_item = list()
#         for words in sentence.split():
#             if not re.search(regex, words):
#                 dict_item = words
#     return (dict_item) if dict_item else []

# print(longestWord('fun&!! time'))




# Intersection CodingBat

# def intersection(array):
#     array_leng = len(array)
#     y = 0;l=[]
#     while y < len(array)[0]:
#         if array[y] == array[y]
#         y+=1
#     return 0



# Sort Array by parity LeetCode

# def sortArrayByParity(arrayList):
#     if not arrayList:
#         return arrayList
#     leng = len(arrayList) // 2
#     i, j = 0, 0
#     while j < len(arrayList):
#         if arrayList[j] % 2 == 0:
#             arrayList[i], arrayList[j] = arrayList[j], arrayList[i]
#             i+=1
#         j+=1

#     return arrayList


# print(sortArrayByParity([3,1,2,4]))



# PhoneBook HackerRank

# n = int(input())
# dict_name = dict()
# while n!=0:
#     b = input()
#     b = b.split()
#     dict_name[b[0]] = int(b[-1])
#     n-=1
# print(dict_name)

# number = input()
# while number:
#     if dict_name[number]:
#         print(f"{number}={dict_name[number]}")
#     else:
#         print('Not Found')
#     number = input()



# Trees

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.Right = None
#         self.Left = None

# class Trees:
#     def __init__(self): 
#         self.Root = None
#         self.length = 0

#     def push(self, data):
#         newNode = Node(data)
#         if self.Root is None:
#             self.Root = newNode
#         else:
#             if data < self.Root.data:
#                 if self.Root.Left is None:
#                     self.Root.Left = newNode
#                 else:
#                     self.push(self.Root.Left, data) 

#             else:
#                 if self.Root.Right is None:
#                     self.Root.Right = newNode
#                 else:
#                     self.push(self.Root.Right, data)
#         self.length+=1

    
#     def displayTree(self, root):
#         if root!=None:
#             self.displayTree(root.Left)
#             print(root.data)
#             self.displayTree(root.Right)



# obj = Trees()
# obj.push(10)
# obj.push(20)
# obj.push(30)
# # obj.push(40)
# # obj.push(50)

# print(obj.displayTree(obj.Root))



# Longest Substring Without Reapting Charaters

# def longestSubstring(string):
#     dict_items = {}
#     maxL = 0
#     startL = 0
#     for letter in range(0, len(string)):
#         if string[letter] in dict_items:
#             startL = max(startL, dict_items[string[letter]]+1)
#         maxL = max(maxL, letter-startL+1)
#         dict_items[string[letter]] = letter
#     return maxL
# print(longestSubstring("aa"))


# Fibonacci Series

# def fibonacciSeries(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     return fibonacciSeries(n-1)+fibonacciSeries(n-2)

# print(fibonacciSeries(4))



# Square Root of a number without pow() or **


# def root(num):
#     if num == 0 or num == 1:
#         return num

#     start = 1
#     end = num
#     while start < end:
#         mid = (start+end)//2
#         if mid*mid == num:
#             return mid
#         elif mid*mid < num:
#             start = mid + 1
#             ans = mid
#         else:
#             end = mid - 1

#     return ans

# print(root(2))



# Multiply numbers strings numbers without using int 

# def multiplyString(num1, num2=0):
#     dict_num = {'1':1, '2':2, '3':3, '4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'0':0}
#     l1 = []; l2 = []
#     for x in num1:
#         l1.append(dict_num[x])
#     for i in num2:
#         l2.append(dict_num[i])
#     return l1, l2

# print(multiplyString('123', '456'))



# # Single Number

# def Number(nums):
#     d = dict()
#     l = list()
#     for x in nums:
#         if x in d:
#             d.pop(d[x])
#         else:
#             d[x] = x
#             l.append(x)

#     return list(d)[0]

# print(Number([2,2,1]))




# Linked List By Baka

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class SingleLinkedList:
#     def __init__(self):
#         self.tail = None
#         self.length = 0

#     def append(self, data):
#         newNode = Node(data)
#         if self.tail is None:
#             self.tail = newNode
#         else:
#             current = self.tail
#             while current.next:
#                 current = current.next
#             current.next = newNode
#         self.length += 1

#     def display(self):
#         current = self.tail
#         s = str()
#         while current:
#             s+= str(current.data)+'--->'
#             current = current.next
#         return s

#     def maxEleANDminEle(self):
#         current = self.tail
#         MAX = current.data
#         MIN = current.data
#         while current:
#             if MAX < current.data:
#                 MAX = current.data
#             current = current.next
#         current = self.tail
#         while current:
#             if MIN > current.data:
#                 MIN = current.data
#             current = current.next
#         return f"MAX: {MAX}, MIN: {MIN}"

#     def increment(self, value, data):
#         current = self.tail
#         while current:
#             if current.data == data:
#                current = (current.data + value)
#                print("Found", current)
#                return
#             current = current.next

#     def index(self, number):
#         pos = 0
#         current = self.tail
#         while current:
#             if current.data == number:
#                 return pos
#             current = current.next
#             pos+=1


#     def search(self, element):
#         current = self.tail
#         while current:
#             if current.data == element:
#                 return f"{current.data} at index {self.index(current.data)}"
#             current = current.next
#         return "Not Found"

#     def lengthList(self):
#         return f"Length: {self.length}"

#     def middle(self, element):
#         newNode = Node(element)
#         numElem = 1
#         mid = self.length // 2
#         current = self.tail
#         while current:
#             if numElem == mid:
#                 newNode.next = current.next # At Any Position
#                 current.next = newNode  # At Any Position
#             numElem += 1
#             current = current.next

#     def remove(self, element):
#         pos = 0
#         current = self.tail
#         while current:
#             if pos == self.index(current.data):
#                 unwantedNode = current
#                 current.next = unwantedNode.next
#             pos+=1
#             current = current.next
#         self.length -= 1


# obj = SingleLinkedList()
# for num in range(1, 21):
#     obj.append(num)


# print(obj.display())
# print(obj.maxEleANDminEle())
# print(obj.increment(3, 1))
# print(obj.display())
# print(obj.search(20))
# print(obj.display())
# print(obj.lengthList())
# (obj.middle(17))
# print(obj.display())
# print(obj.remove(20))
# print(obj.display())


# 4Sum LeetCode

# def Sum(arr, target):
#     _sum = 0
#     d = {}
#     c = 4
#     for x in range(len(arr)):
#         _sum = sum(arr[x:c])
#         if _sum == target:
#             # print(arr[x:c])
#             z= str(arr[x:c])
#             d[z] = 1
#         c+=1
#     return d

# print(Sum([1,0,-1,0,-2,2], 0))



# Search Insert Position LeetCode

# def searchInsertPosition(arr, target):
#     high = len(arr) - 1
#     low = 0
#     if target == 0 or not target:
#         return target
#     while low <= high:
#         mid = (high + low) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#             print(low, arr[low])
#         else:
#             high = mid - 1
#             print(high, arr[high])
#     return low

# print(searchInsertPosition([1, 3, 5, 6], 4))


# Search In rotate array leetCode

# def searchSortedArray(arr, target):
#     arr1 = sorted(arr)
#     high = len(arr1) - 1
#     low = 0
#     while low <= high:
#         mid = (high+low) // 2
#         if arr1[mid] == target:
#             return arr.index(arr1[mid])
#         elif arr1[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1

# print(searchSortedArray([4,5,6,7,0,1,2], 3))


# Find the minium value in a rotated array LeetCode


# def findMinium(numsArr): 
#     MIN = numsArr[0]
#     if not numsArr:
#         return numsArr
#     for x in numsArr:
#         if MIN > x:
#             MIN = x
#     return MIN


# print(findMinium([3,4,5,1,2]))



# Permutation hard one

# def permutation(head, tail=''):
#     if len(head) == 0:
#         print(tail)
#     else:
#         for i in range(len(head)):
#             permutation(head[:i]+head[i+1:], tail+head[i])


# print(permutation('abc'))


# Permutation

# def permutation(string):
#     if len(string) == 0 or len(string) == 1:
#         return string

#     d = dict()
#     for x in range(len(string)):
#         m = string[x]
#         res = string[:x] + string[x + 1:]
#         for p in permutation(res):
#             d[m+p] = 1
#             print(m+p)
#     return list(d.keys()), d

# print(permutation([123]))



# Add Binary Numbers LeetCode

# def binaryAddition(b_num1, b_num2):
#     s = int(b_num1, 2) + int(b_num2, 2)
#     return bin(s)[2:]

# print(binaryAddition("1010", "1011"))



# Jump Game LeetCode

# def jumpGame(arr):
#     m = 0
#     for key, value in enumerate(arr):
#         if key > m:
#             return False
#         m = max(m, key+value)
#     return True


# print(jumpGame([2,0]))


# WeIrD StRiNg CaSe CodeWars

# def to_weird_case(string):
#     leng = len(string)
#     for ele in range(len(string)):
#         if string[ele] == " ":
#             ele= ele -1
#             print('ele', ele)
#         if ele % 2 == 0:
#             string = string.replace(string[ele], string[ele].title())
#     return string

# print(to_weird_case('This is a test'))



# Valid Parenthese LeetCode

# def validParenthese(argv):
#     stack = []
#     d = {'[':']', '{':'}','(':')'}
#     for ele in argv:
#         if ele in d:
#             stack.append(ele)
#         elif len(stack) == 0 or d[stack.pop()] != ele:
#             return False
#     return len(stack) == 0
# print(validParenthese("[(]"))


# Remove Exclamation Marks

# def remove_exclamation_marks(string):
#     s= str()
#     for ele in string:
#         if ele == '!':
#             continue
#         s+= ele
#     return s

# print(remove_exclamation_marks('arsh!'))


# Sort and Star CodeWars

# def sort_star(string):
#     stringArray = string
#     d = dict()
#     stringArrayLen = len(stringArray)
#     for num in range(stringArrayLen):
#         d[ord(stringArray[num][0])] = stringArray[num]
#         print(sorted(list(d.keys()))[0])
#     return "***".join(d[sorted(list(d.keys()))[0]])
# print(sort_star(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]))



# Maximum SubArray Sum CodeWars

# def max_sequence(sequence):
#     max_ = 0
#     mid = len(sequence) // 2
#     for x in range(len(sequence)):
#         max_ = max(max_, sum(sequence[x:mid]))
#         print(sequence[x:mid])
#         mid+=1
#     return max_

#     return 0

# print(max_sequence([1,2,3,4,5,6,7,8]))


# Find the Missing Number Codewars

# def missing_num(num_seq):
#     myNum = sum(list(range(num_seq[-1]+1)))
#     leng = len(num_seq)
#     num_seq_sum = (leng+1)*(leng+2) // 2
#     return num_seq_sum , myNum

# print(missing_num([1,2,4, 5, 6]))


# Happy Number LeetCode Not Solve at now

# def happyNumber(number):
#     s = int()
#     num = str(number)
#     for key, value in enumerate(num):
#         s+=pow(int(num[key]), 2)
#         print(s)

# print(happyNumber(19))



# Is unique: determine if a string has unique characters

# def uniqueString(string):
#     dict_checker = dict()
#     for ele in string.lower():
#         if ele in dict_checker:
#             return False
#         else:
#             dict_checker[ele] = 1
#     return True
# print(uniqueString("Arsh"))



# URLify: write an Algorithm which replace " " with %20

# def urlify(string):
#     return string.replace(" ", "%20")

# print(urlify("Mr John Smith"))


# One away
# pale --> pal -- True
# 

# def oneAway(str1, str2):
#     Flag = True
#     if str1 == str2:
#         return True
#     if len(str1) == len(str2):
#         return False
#     ans = sum(map(ord, str1)) - sum(map(ord, str2))
#     if chr(ans) in str1:
#         return Flag
#     elif ans - sum(map(ord, str1)) == sum(map(ord, str2)):
#         return Flag
#     return False

# print(oneAway("pales", 'pal'))


# Stack Implementation by Node class


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class Stack:
#     def __init__(self):
#         self.top = None
#         self.size = 0

#     def push(self, value):
#         newNode = Node(value)
#         if self.top:
#             newNode.next = self.top
#             self.top = newNode
#         else:
#             self.top = newNode
#         self.size += 1

#     def pop(self):
#         if self.top:
#             data = self.top.data
#             self.size-=1
#             if self.top.next:
#                 self.top = self.top.next
#             else:
#                 self.top = None
#             return data
#         else:
#             return None


#     def peek(self):
#         if self.top:
#             return self.top.data
#         return None



#     def display(self):
#         s = str()
#         current = self.top
#         while current:
#             s+= str(current.data)+'-->'
#             current =  current.next
#         return s


# obj = Stack()
# for x in range(10):
#     obj.push(x)
# print(obj.display())
# print(obj.pop())
# print(obj.display())
# print(obj.peek())




# Squares of a sorted Array LeetCode

# import collections
# def sortedSquares(nums):
#     # l = set()
#     # mid = (len(nums) - 1) // 2
#     # print(nums[mid:])
#     # for ele in nums:
#     #     l.add(ele**2)
#     # return sorted(l)
#     answer = collections.deque()
#     l, r = 0, len(nums)-1
#     while l <= r:
#         left, right = abs(nums[l]), abs(nums[r])
#         if left > right:
#             answer.appendleft(pow(left,2))
#             print(left, l, 'if')
#             l+=1
#         else:
#             answer.appendleft(right*right)
#             print(right, r, 'else')
#             r-=1
        
#     return list(answer)


# print(sortedSquares([-4,-1, 0, 3, 10]))


# Count the digits CodeWars


# def countDigits(num, digit):
#     string = str()
#     for ele in range(num+1):
#         # if '1' in str(pow(ele, 2)):
#         string+=str(pow(ele, 2))
#     return string.count(str(digit))


# print(countDigits(11011, 2))


# Find the Stray Number in an Array CodeWars

# def stray_number(array):
#     dict_item = dict()
#     s = 0
#     for ele in array:
#         if ele in dict_item:
#             dict_item.pop(ele)
#         else:
#             dict_item[ele] = ele

#     return list(dict_item.keys())[0]
#     # return array[0]

# print(stray_number([17, 17, 3, 17, 17, 17, 17]))



# Will you make it? CodeWars

# def car_to_refill(refill_des ,fuel_left, mpg):
#     return True if fuel_left*mpg >= refill_des else False


# print(car_to_refill(100, 50, 1))


# Even or Odd- Which is greater Even or Odd Codewars

# def even_or_odd(arr):
#     odd_list = list()
#     even_list = list()
#     for ele in arr:
#         if int(ele) % 2 == 0:
#             even_list.append(int(ele))
#         else:
#             odd_list.append(int(ele))

#     even_list = sum(even_list)
#     odd_list = sum(odd_list)

#     if even_list > odd_list:
#         return "Even is greater than Odd"
#     elif even_list < odd_list:
#         return "Odd is greater than Even"
#     else:
#         return "Even and Odd are the same"

# print(even_or_odd('12'))


# Trees
# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data
#         self.l = list()

    
#     def preorder(self, node):
#         if node:
#             self.preorder(node.left)
#             print(node.data)
#             self.l.append(node.data)
#             self.preorder(node.right)
#         return self.l

# class Tree:
#     def __init__(self):

    
# root = Node(10)
# root.left = Node(34)
# root.right = Node(67)
# root.left.left = Node(80)
# root.left.right = Node(99)
# # print(root.right.data)
# print(root.preorder(root))



# Delete and Earn LeetCode

# def deleteAndearn(nums):

#     if not nums : return 0
#     house = [0] * (max(nums)+1)
#     for num in nums:
#         house[num] += num
#     dp = [0]*(len(house)+1)
#     for i in range(1,len(house)):
#         dp[i] = max(house[i]+dp[i-2], dp[i-1])
#         print(house[i], dp[i-2], dp[i-1])
#     # return max(dp)


# print(deleteAndearn([3,4,2]))

# Remove the Duplicate from sorted array leetcode

# def sortedArray(array):
#     dict_item = dict()
#     for x in array:
#         if x not in dict_item:
#             dict_item[x] = 1
#         dict_item[x] = 1

#     return list(dict_item.keys())


# print(sortedArray([1,1,2]))


# Valid Palindrome LeetCode

# def validPalindrome(string):
#     s = str()
#     if not string.isalpha():
#         return False
#     for ele in string.lower():
#         if ord(ele) in range(97, 123):
#             s+=ele
#     return s == s[::-1], 'aa'


# print(validPalindrome("arsh11"))


# Count and Say leetcode

# def countAndSay(string):
#     dict_item = dict()
#     s = str()
#     for ele in string:
#         if ele in dict_item:
#             dict_item[ele] += 1
#         else:
#             dict_item[ele] = 1
    
#     for x in dict_item:
#         s+= str(dict_item[x])+x

#     return s

# print(countAndSay("3322251"))


# Missing Number leetcode

# def missingNumber(number):
#     set1 = set(range(sorted(number)[0], len(number)+1))
#     return set1 - set(number)

# print(missingNumber([0,3,1]))



# Two Pointer approach for reversing integers and strings

# import time

# def reverseInt(integer):
#     start = time.time()
#     head = 0
#     tail = len(integer) - 1
#     while head < tail:
#         integer[tail], integer[head] = integer[head], integer[tail]
#         print(integer[head], integer[tail])
#         head+=1
#         tail -= 1
#     return integer, start-time.time()

# print(reverseInt(["h","e","l","l","o"]))
# # print(reverseInt([1,2,3,4,5]))



# First Non-repeating characters in a string LeetCode 

# def nonRepeatingChar(string):
#     for key, value in enumerate(string):
#         # print(string[:key])
#         if value not in string[:key]:
#             return key
#     return -1

# print(nonRepeatingChar(""))



# Valid Anagram LeetCode

# def anagram(s, t):
#     # return True if sorted(t) == sorted(s) else False
#     # return sum(map(ord, s)) == sum(map(ord, t))
#     s = set(s)
#     for ele in t:
#         if ele in s:
#             s.remove(ele)
#     return len(s) == 0

# print(anagram("cat", "rat"))


# Only duplicates CodeWars

# def only_duplicates(string):
#     sets = unique, duplicate = set(), set()
#     for chars in string:
#         sets[chars in unique].add(chars)
#     return "".join(c for c in string if c in duplicate)

# print(only_duplicates("abccdefee"))

# Find all duplicates in an Array  LeetCode

# def findDuplicates(array):
#     res = list()
#     for i in range(len(array)):
#         index = abs(array[i]) - 1
#         if array[index] < 0:
#             res.append(index+1)
#         array[index] = -array[index]
#     return res
# print(findDuplicates(
# [4,3,2,7,8,2,3,1]))


# Find All disappeared numbers in an Array 

# def disapperNumbers(array):
#     res = list()
#     for i in range(0, len(array)):
#         index = abs(array[i])
#         array[index-1] = -abs(array[index-1]) 

#     for i in range(0, len(array)):
#         if array[i] > 0:
#             res.append(i+1)

#     return res

# print(disapperNumbers([4,3,2,7,8,2,3,1]))

  
# Two Sum II LeetCode

# def TwoSumII(numbers, target):
#     seen = dict()
#     for key, value in enumerate(numbers):
#         if target-value in seen:
#             return seen[target-value], key+1
#         seen[value] = key+1


# print(TwoSumII([2, 7, 11, 15], 9))



# Rotating an Array  LeetCode



# # Rotate a linked list 

# class Node:
#     def __init__(self, val, next = None):
#         self.val = val
#         self.next = next



# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def push(self, data):
#         newNode = Node(data, self.head)
#         self.head = newNode

#     def display(self):
#         current = self.head
#         s = str()
#         while current:
#             s+= str(current.val)+'-->'
#             current = current.next
#         return s

#     def reverse(self):
#         current = self.head
#         prev = None
#         while current:
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
#         self.head = prev


# obj = LinkedList()
# for x in range(11):
#     obj.push(x)
# print(obj.display())
# print(obj.reverse())
# print(obj.display())


# Fizz Buzz LeetCode

# class FizzBuzz:
#     def solution(self, value):
#         l = list()
#         for x in range(1, value+1):
#             if x % 3 == 0 and x % 5 ==0:
#                 x = ("FizzBuzz")
#             elif x % 3 == 0:
#                 x = ("Fizz")
#             elif x % 5 == 0:
#                 x = ("Buzz")
#             l.append(f"{x}")
        
#         return l


# obj = FizzBuzz()
# print(obj.solution(15))



# Is a number is multiple of 3 ? leetCode

# import math

# class MultipesOfThree:
#     def solution(self, num):
#         if num > 0:
#             return (math.log10(num) / math.log10(3)) % 1 == 0
#         return False
        


# sol = MultipesOfThree()
# print(sol.solution(-3))




# Prime numbers count them LeetCode

# class PrimeNumber:
#     def solution(self, number):
#         for x in range(2, number):
#             if number % x == 0:
#                 print(number, x)


# sol = PrimeNumber()
# print(sol.solution(10))



# Move Zeros leetcode

# class MoveZero:
#     def solution(self, array):
#         # count = 0
#         # for ele in array:
#         #     if ele == 0:
#         #         array.remove(ele)
#         #         count+=1

#         # for i in range(count):
#         #     array.append(0)

#         # return array
#         r = 0
#         l = len(array)
#         while r < l:
#             if array[r] == 0:
#                 array.append(array.pop(r))
#                 l-=1
#             else:
#                 r+=1
#         return array

# sol = MoveZero()
# print(sol.solution([0,1,0, 3, 12]))




# Boats to save People leetCode

# class SavePeopleByBoat:
#     def solution(self, people, limit ):
#         people.sort()

#         left = 0
#         right = len(people)-1

#         boats_number = 0

#         while(left<=right):
#             if(left==right):
#                 boats_number+=1
#                 break
#             if(people[left]+people[right]<=limit):
#                 left+=1
#             right-=1
#             boats_number+=1
#         return boats_number

# sol = SavePeopleByBoat()
# print(sol.solution([3,2,2,1], 3))



# Valid Mountain Array LeetCode

# class ValidMountainArray:
#     def solution(self, array):
#         i = 1
#         while i < len(array) and array[i] > array[i-1]:  # [0, 2, 3,....]    i > array[i-1] = 2 > 1-1 = 0, 2 > 0 
#             i+=1
        
#         if i == 1 and i == len(array):
#             return False

#         while i < len(array) and array[i-1] > array[i]:
#             i += 1

#         return i == len(array), i, len(array)

# sol = ValidMountainArray()

# print(sol.solution([0,3,2,1]))



# Container with the most water LeetCode

# class ContainerWithMostWater:
#     def solution(self, array):
#         l = 0
#         r = len(array) - 1
#         maxArea = 0
#         while l < r:
#             maxArea = max(maxArea, min(array[l], array[r])*(r-l))

#             if array[l] < array[r]:
#                 l+=1
#             else:
#                 r-=1 
#         return maxArea


# sol = ContainerWithMostWater()
# print(sol.solution([1,8,6,2,5,4,8,3,7]))


# print First Unique Character in a string  LeetCode


# class FirstUniqueChar:
#     def solution(self, string):
#         d = dict()
#         for ele in string:
#             if ele in d:
#                 d[ele] += 1
#             else:
#                 d[ele] = 1

#         for index in range(len(string)):
#             char = string[index]
#             if d[char] == 1:
#                 return index, char
# sol = FirstUniqueChar()
# print(sol.solution('loveleetcode'))




# Shuffle an Array LeetCode

# import random

# class ShuffleArray:
#     def __init__(self, number):
#         self.number = number

#     def shuffle(self):
#         ans = self.number[:]
#         for ele in range(len(ans)-1, 0, -1):
#             j = random.randrange(0, len(ans)-1)
#             self.number[ele], self.number[j] = self.number[j], self.number[ele]
#         return ans

#     def reset(self):
#         return self.number

# sol = ShuffleArray([1,2,3])

# print(sol.shuffle())
# print(sol.reset())


# Min Stack LeetCode

# class MinStack:
#     def __init__(self):
#         self.stack = []

    
#     def push(self, value):
#         self.stack.append(value)
#         # self.stack.reverse()

#     def top(self):
#         return self.stack[-1]

#     def pop(self):
#         return self.stack.pop(-1)

#     def show(self):
#         return self.stack

#     def getMin(self):
#         return min(self.stack)
    
# sol = MinStack()

# sol.push(-2)

# sol.push(0)

# sol.push(-3)


# print(sol.show())

# print(sol.getMin(), 'min')

# print(sol.pop(), 'pop')

# print(sol.top(), 'top')


# print(sol.show())




# Multiply String Integers without using "int()"

# class MultiplyString:
#     def solution(self, number1, number2):
#         num1 =  num2 = 0
#         for i in range(len(number1)):
#             num1 = num1 * 10 + ord(number1[i]) - ord('0')

#         for i in range(len(number2)):
#             num2 = num2 * 10 + ord(number2[i]) - ord('0')
#         return str(num1 * num2)

    
# sol = MultiplyString()

# print(sol.solution('123', '456'))


# Do addition in string Integers without using "int()"


# class StringAddition:
#     def solution(self, num1, num2):
#         res1, res2 = 0, 0

#         for i in range(len(num1)):
#             res1 = res1 * 10 + ord(num1[i]) - ord('0')

#         for i in range(len(num2)):
#             res2 = res2 * 10 + ord(num2[i]) - ord('0')

#         return str(res1+res2)


# sol = StringAddition()

# print(sol.solution('12', '10'))



# Remove duplicates from sorted array leetcode

# class RmDuplicate:
#     def solution(self, array):
#         head = 0
#         tail = 1

#         while head < len(array)-1:
#             if array[head] == array[tail]:
#                 array.pop(head)
#             if array[tail-1] == array[tail]:
#                 array.pop(tail)
#             head+=1
#             tail+=1
#         return array
# sol = RmDuplicate()

# print(sol.solution([0,0,1,1,1,2,2,3,3,4, 5, 5, 9, 9, 10, 10, 11, 11, 11]))


# Factorial Program Recursive and Alternate 

# class AlterFactorial:
#     def solution(self, number):
#         sum_ = 1
#         while number != 0:
#             sum_ *= number
#             number-=1

#         return sum_


# sol = AlterFactorial()

# print(sol.solution(5))


# class RecursiveFactorial:
#     def solution(self, number):
#         if number == 1:
#             return number

#         return number * self.solution(number-1)


# sol = RecursiveFactorial()

# print(sol.solution(5))



# Fibonacci Series with recusion

# class FiboRecursion:
#     def solution(self, number):
#         if number < 2:
#             return number
#         return self.solution(number-1)+ self.solution(number-2)

# sol = FiboRecursion()

# print(sol.solution(4))




# Tress 


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.right = None
#         self.left = None


# class BinarySearchTree:
#     def __init__(self):
#         self.root = None


#     def insert(self, value):
#         newNode = Node(value)
#         if not self.root:
#             self.root = newNode 
#         else:
#             currentNode = self.root
#             while True:
#                 if value > currentNode.value:
#                     if not currentNode.right:
#                         currentNode.right = newNode
#                         return self
#                     else:
#                         currentNode = currentNode.right
#                 else:
#                     if not currentNode.left:
#                         currentNode.left = newNode
#                         return self
#                     else:
#                         currentNode = currentNode.left


#     def lookUp(self, value):
#         currentNode = self.root
#         while currentNode:
#             if value > currentNode.value:
#                 currentNode = currentNode.right
#             elif value < currentNode.value:
#                 currentNode = currentNode.left
#             elif currentNode.value == value:
#                 return currentNode.value         



#     def display(self):
#         current = self.root
#         c = 0
#         while current:
#             current.right
#             print(current.right.right.value)
#             # current.left
#             if c == 10:
#                 break
#             c+=1


#     def maximumNode(self):
#         currentNode = self.root
#         maxNode = currentNode.value
#         while currentNode:
#             maxNode = max(maxNode, currentNode.value)
#             currentNode = currentNode.right
#         return maxNode

    
#     def minimumNode(self):
#         currentNode = self.root
#         minNode = currentNode.value
#         while currentNode:
#             minNode = min(minNode, currentNode.value)
#             currentNode = currentNode.left
        
#         return minNode

    
#     def deletionNode(self, data):
#         currentNode = self.root
#         parentNode = None
#         if not currentNode:
#             return False

#         # while currentNode:
#         #     if currentNode.value == data:
#         #         if currentNode.right:
#         #             print('ya')
#         #             return
#         #     elif currentNode.value < data:
#         #         parentNode = currentNode
#         #         currentNode = currentNode.right
#         #     elif currentNode.value > data:
#         #         parentNode = currentNode
#         #         currentNode = currentNode.left



#         # while currentNode:
#         #     if currentNode.value < data:
#         #         parentNode = currentNode
#         #         currentNode = currentNode.right
#         #     elif currentNode.value > data:
#         #         parentNode = currentNode
#         #         currentNode = currentNode.left

#         #     else:
#         #         if (not currentNode.right and not currentNode.left):
#         #             if currentNode.value > parentNode.value:
#         #                 parentNode.right = None
#         #             else:
#         #                 parentNode.left = None
                
#         #             return self
                
#         #         elif not currentNode.right:
#         #             if parentNode is None:
#         #                 self.root = currentNode.left
#         #             else:




#     # def display(self, root):
#     #     root = self.root
#     #     if root is None:
#     #         return None
        
#     #     self.display(root.left)
#     #     print(root.value, end=' ')
#     #     self.display(root.right)




# obj = BinarySearchTree()

# obj.insert(10)
# obj.insert(12)
# obj.insert(9)
# obj.insert(6)
# obj.insert(45)
# obj.insert(2)
# obj.insert(56)
# obj.insert(90)
# obj.insert(0)



# print(obj.lookUp(12))

# # print(obj.display())

# print(obj.maximumNode())

# print(obj.minimumNode())

# print(obj.deletionNode(12))



# Bubble sort O(n^2)

# class BubbleSort:
#     def __init__(self, data):
#         self.data = data

#     def sorting(self):
#         for i in range(len(self.data)-1):
#             for x in range(len(self.data)-1):
#                 if abs(self.data[x]) > abs(self.data[x+1]):
#                     self.data[x], self.data[x+1] = self.data[x+1], self.data[x]

#         return self.data

# obj = BubbleSort(list(range(-50, -0)))
# print(obj.sorting())



# Selection Sorting O(n^2)

# class SelectionSort:
#     def __init__(self, array):
#         self.array = array

#     def sorting(self):
#         for i in range(len(self.array)-1):
#             for x in range(len(self.array)-1):
#                 if self.array[x] > self.array[x+1]:
#                     self.array[x], self.array[x+1] = self.array[x+1], self.array[x]
#         print(self.array)

# obj = SelectionSort([5,4,3,2,1])

# print(obj.sorting())


# MergeSort recursion

# class MergeSort:

#     def merge(self, left, right):
#         result = list()
#         leftIndex = 0
#         rightIndex = 0

#         while leftIndex < len(left) and rightIndex < len(right):
#             if left[leftIndex] < right[rightIndex]:
#                 result.append(left[leftIndex])
#                 leftIndex += 1
#             else:
#                 result.append(right[rightIndex])
#                 rightIndex += 1

#         return result    

#     def splitArray(self, array):
#         mid = (len(array) - 1) // 2
#         left = array[:mid]
#         right = array[mid:]

#         print(left, right)
#         self.merge(self.splitArray(right), self.splitArray(left))


# obj = MergeSort()

# print(obj.splitArray([9,8,7,6,5,4,3,2,1]))

# print(obj.merge())


# QuickSorting 


# # function to find the partition position
# def partition(array, low, high):

#   # choose the rightmost element as pivot
#   pivot = array[high]

#   # pointer for greater element
#   i = low - 1

#   # traverse through all elements
#   # compare each element with pivot
#   for j in range(low, high):
#     if array[j] <= pivot:
#       # if element smaller than pivot is found
#       # swap it with the greater element pointed by i
#       i = i + 1

#       # swapping element at i with element at j
#       (array[i], array[j]) = (array[j], array[i])

#   # swap the pivot element with the greater element specified by i
#   (array[i + 1], array[high]) = (array[high], array[i + 1])

#   # return the position from where partition is done
#   return i + 1

# # function to perform quicksort
# def quickSort(array, low, high):
#   if low < high:

#     # find pivot element such that
#     # element smaller than pivot are on the left
#     # element greater than pivot are on the right
#     pi = partition(array, low, high)

#     # recursive call on the left of pivot
#     quickSort(array, low, pi - 1)

#     # recursive call on the right of pivot
#     quickSort(array, pi + 1, high)


# data = [8, 7, 2, 1, 0, 9, 6]
# print("Unsorted Array")
# print(data)

# size = len(data)

# quickSort(data, 0, size - 1)

# print('Sorted Array in Ascending Order:')
# print(data) 




#  Reverse the words in a string II LeetCode


# class ReverseWord:
#     def __init__(self, string):
#         self.string = string

#     def reverse(self):
#         return " ".join(x[::-1] for x in self.string.split())


# obj = ReverseWord("Let's take LeetCode contest")
# print(obj.reverse())
# print(obj.reverse()=="s'teL ekat edoCteeL tsetnoc")
# print("s'teL ekat edoCteeL tsetnoc")



# Reverse a string leetCode

# class ReverseString:
#     def __init__(self, string, k):
#         self.string = string
#         self.k = k

#     def reverse(self):
#         self.string = list(self.string)
#         for i in range(0, len(self.string), 2*self.k):
#         #     self.string[i:i+self.k] = reversed(self.string[i:i+self.k])
#             print(self.string[i:i+self.k], i)
#             print(reversed(self.string[i:i+self.k]))
#         # return ''.join(self.string)


# obj = ReverseString("abcdefg", 2)
# print(obj.reverse())




# Find Pivot Index LeetCode

# class PivotIndex:
#     def __init__(self, array):
#         self.array = array

#     def solution(self):
#         totalSum = 0
#         for x in self.array:
#             totalSum+=x
#         print(totalSum)

#         leftSum = 0
#         for x in range(len(self.array)):
#             if totalSum-leftSum-self.array[x] == leftSum:
#                 return x
#             leftSum+=self.array[x]

#         return -1


# obj = PivotIndex([1,7,3,6,5,6])
# print(obj.solution())


# largest number at least twice as others

# class LargestNumber:
#     def __init__(self, array):
#         self.array = array

#     def solution(self):
#         maxNumIndex = self.array.index(max(self.array))
#         for x in range(len(self.array)):
#             if maxNumIndex != x and self.array[maxNumIndex] < 2*self.array[x]:
#                 return -1
#         return maxNumIndex




# # obj = LargestNumber([1,2,3,4])
# obj = LargestNumber([3, 6, 1, 0])

# print(obj.solution())



# Plus One LeetCode

# class PlusOne:
#     def __init__(self, array):
#         self.array = array

#     def solution(self):
#         strInt = str()
#         strInt = strInt.join(str(strNum) for strNum in self.array)
#         return list(str(int(strInt)+1))

# obj = PlusOne([1,2,3])

# print(obj.solution())




# 2D Array and 3D array

# class twoDArray:

#     def solution():
#         l = list()
#         for x in range(10):
#             c = list()
#             for i in range(10):
#                 c.append(i)
#             l.append(c)

#         return l

# obj = twoDArray
# print(obj.solution())


# Array Partition I-> LeetCode

# class ArrayPartition:
#     def __init__(self, array):
#         self.array = array

#     def solution(self):
#         self.array = sorted(self.array)
#         result = 0
#         print(self.array)
#         for i in range(0, len(self.array)-1, 2):
#             # print(self.array[i], end='')
#             result += self.array[i]
#         return result

# obj = ArrayPartition([6,2,6,5,1,2])
# print(obj.solution())



# Two pointer for array

# class TwoPointer:
#     def __init__(self, nums, value):
#         self.nums = nums
#         self.value = value

#     def solution(self):
#         k = 0
#         for i in range(len(self.nums)):
#             if self.nums[i] != self.value:
#                 self.nums[k] = self.nums[i]
#                 k+=1

#         return k, self.nums

        
# sol = TwoPointer([1,2,4,6,7,9,0], 9)        
# print(sol.solution())


# Max Consective Ones LeetCode

# class MaxConsectiveOne:
#     def __init__(self, arrayNum):
#         self.arrayNum = arrayNum

#     def solution(self):
#         current = 0
#         maxRes = 0
#         for i in range(len(self.arrayNum)):
#             if self.arrayNum[i] != 0:
#                 current+=1
#                 maxRes = max(maxRes, current)
#             else:
#                 current = 0

#         return maxRes


# obj = MaxConsectiveOne([1,1,0,1,1,1])

# print(obj.solution())


# Minimum Size Subarray Sum LeetCode

# class MinimumSizeSubarray:
#     def __init__(self, array, target):
#         self.array = array
#         self.target = target

#     def solution(self):
#         i = 0
#         res = len(self.array)+1
#         for j in range(len(self.array)):
#             self.target -= self.array[j]
#             while self.target <= 0:
#                 res = min(res, j-i+1)
#                 self.target += self.array[i]
#                 i+=1
#         return res % (len(self.array)+1)

# obj = MinimumSizeSubarray([2,3,1,2,4,3], 7)

# print(obj.solution())


# Majority element LeetCode

# class MajorityElement:
#     def __init__(self, array):
#         self.array = array
    
#     def solution(self):
#         dict_item = dict()
#         for value in self.array:
#             if value in dict_item:
#                 dict_item[value] += 1
#             else:
#                 dict_item[value] = 1
        

#         for key in dict_item:
#             if dict_item[key] > len(self.array)//2:
#                 return key

# obj = MajorityElement([3,2,3])
# print(obj.solution())


# Find numbers with even number of digits LeetCode

# class NumbersWithEvenDigit:
#     def __init__(self, numArray):
#         self.numsArray = numArray

    
#     def solution(self):
#         count = 0
#         for value in self.numsArray:
#             if len(str(value)) % 2 == 0:
#                 count += 1

#         return count


# obj = NumbersWithEvenDigit([12, 345, 2, 6, 7896])
# print(obj.solution())



# Squares of Sorted array


# class SortedArraySqrt:
#     def __init__(self, numsArr):
#         self.numsArr = numsArr

#     def solution(self):
#         print(self.numsArr)
#         for i in range(len(self.numsArr)):
#             self.numsArr[i] = pow(self.numsArr[i], 2)

#         return sorted(self.numsArr)


# obj = SortedArraySqrt([-4, -1, 0, 3, 10])

# print(obj.solution())


# Remove duplicates from sorted array leetcode

# class RemoveDuplicates:
#     def __init__(self, sortedArr):
#         self.array = sortedArr

#     def solution(self):
#         self.array[:] = sorted(set(self.array))

#         return len(self.array)


# obj = RemoveDuplicates([1,1,2])

# print(obj.solution())


# Check if N and it's Double Exist

# class DoubleExist:
#     def __init__(self, numArr):
#         self.numArr = numArr

#     def solution(self):
#         if self.numArr.count(0) > 1:
#             return True
#         seen = set(self.numArr) - {0}

#         for i in self.numArr:
#             if i * 2 in seen or i % 2 == 0 in seen and i // 2 in seen:
#                 return True
#         return False
  
# obj = DoubleExist([3,1,7,11])

# print(obj.solution())


# Replace elements with greatest element on the right side 

# class GreatestElement:
#     def __init__(self, array):
#         self.array = array

#     def solution(self):
#         maxNum = -1

#         for i in range(len(self.array)-1, -1, -1):
#             self.array[i], maxNum = maxNum, max(maxNum, self.array[i])

#         return self.array


# obj = GreatestElement([17, 18, 5, 4, 6, 1])

# print(obj.solution())




# Height checker LeetCode


# class HeightChecker:
#     def __init__(self, htArr):
#         self.htArr = htArr

#     def solution(self):
#         count = 0
#         exceptedHt = sorted(self.htArr)

#         for i in range(len(self.htArr)):
#             if self.htArr[i] != exceptedHt[i]:
#                 count += 1

#         return count


# obj = HeightChecker([1,1,4,2,1,3])

# print(obj.solution())



# find if a number is strong or not CodeWars

# class StrongNumbers:
#     def __init__(self, number):
#         self.num = number

#     def fact(self, num):
#         if num == 0:
#             return 1
#         return num * self.fact(num-1)

#     def solution(self):
#         res = 0
#         for x in str(self.num):
#             res += self.fact(int(x))
#         print(res)
#         return  "STRONG!!!!" if res == self.num else "Not Strong !!"


# obj = StrongNumbers(40585)

# print(obj.solution())


# Check if number in a sentences are in increasing order LeetCode


# class CheckingNumberInString:
#     def __init__(self, stringWithNumber):
#         self.stringInt = stringWithNumber

#     def solution(self):
#         res = -1

#         for keyInt in self.stringInt.split():
#             if keyInt.isnumeric():
#                 if int(keyInt) > res:
#                     res = int(keyInt)
#                 else:
#                     return False
#         return True

# obj = CheckingNumberInString("hello world 5 x 5")

# print(obj.solution())


# Power of Four LeetCode

# from math import log10
# class PowerOfFour:
#     def __init__(self, number):
#         self.num = number

#     def solution(self):
#         if self.num > 0:
#             return (log10(self.num)/log10(4)) % 1 == 0
#         return False

# obj = PowerOfFour(3)
# print(obj.solution())



# Number of 1 Bits LeetCode

# class NumberOfBits:
#     def __init__(self, bits):
#         self.bits = bits

#     def solution(self):
#         return str(self.bits).count('1')

# obj = NumberOfBits('00000000000000000000000000001011')
# print(obj.solution())


# Is Subsequence LeetCode

# class Subsequence:
#     def __init__(self, s, t):
#         self.s = s
#         self.t = t
    
#     def solution(self):
#         remainder_of_letter = iter(self.t)
#         for i in self.s:
#             if i not in remainder_of_letter:
#                 return False
#         return True

# obj = Subsequence('abc', 'ammbjjc')

# print(obj.solution())



# Linear Queue

# class LinearQueue(object):
#     def __init__(self):
#         self.queue = list()


#     def enqueue(self, data):
#         if data not in self.queue:
#             self.queue.insert(0, data)
#             return True
#         else:
#             return False

#     def dequeue(self):
#         if len(self.queue) > 0:
#             self.queue.pop()
#             return True
#         else:
#             return False

#     def is_empty(self):
#         return len(self.queue) == 0

#     def size(self):
#         return len(self.queue)

#     def show(self):
#         return self.queue


# obj = LinearQueue()

# for x in range(1,10):
#     obj.enqueue(x)

# print(obj.dequeue())
# print(obj.is_empty())
# print(obj.size())
# print(obj.show())




# Circular Queue

# class CircularQueue:
#     def __init__(self, maxSize):
#         self.cirQueue = list()
#         self.maxSize = maxSize
#         self.head = 0
#         self.tail = 0

#     def enqueue(self, data):    
#         if self.size() == self.maxSize-1:
#             return "Queue is Full"
#         self.cirQueue.append(data)

#         self.tail = (self.tail+1) % self.maxSize
#         return True

    
#     def dequeue(self):
#         if self.size == 0:
#             return "Empty Queue"
#         else:
#             data = self.cirQueue[self.head]
#             self.head = (self.head + 1) % self.maxSize

#             return data

        
#     def show(self):
#         return self.cirQueue

#     def size(self):
#         if self.tail >= self.head:
#             qSize = self.tail - self.head
#         else:
#             qSize = self.maxSize - (self.head-self.tail)
#         return qSize


# obj = CircularQueue(4)

# for x in range(1, 11):

#     print(obj.enqueue(x))    

# print(obj.size())
# print(obj.dequeue())
# print(obj.show())



# Find the Smallest Greater than Target Value

# class SmallestGreater:
#     def __init__(self, strArr, target):
#         self.strArr = strArr 
#         self.target = target

#     def solution(self):
#         for letter in self.strArr:
#             if letter > self.target:
#                 return letter
#         return self.target[0]


# obj = SmallestGreater(["c","f","j"], 'c')

# print(obj.solution())


# Search In rotated array II-> LeetCode

# class SearchInRotatedArray:
#     def __init__(self, array, target):
#         self.array  = array
#         self.target = target

#     def solution(self):
#         # self.array[:] = sorted(set(self.array))
#         if self.array.__len__() <= 5:
#             return self.target in self.array
#         l = 0
#         r = len(self.array)

#         while l < r:
#             mid = (l+r) // 2
#             print(self.array[mid])
#             if self.array[mid] == self.target:
#                 return True
#             elif self.array[mid] < self.target:
#                 l = mid + 1
#             else:
#                 r = mid - 1

#         return False


# obj = SearchInRotatedArray([4,5,6,7,0,1,2], 0)

# print(obj.solution())



# Trees BINARY SEARCH TREE

# class Root:
#     def __init__(self, data=None):
#         self.data = data
#         self.right = None
#         self.left = None


# class BinarySearchTree:
#     def __init__(self):
#         self.root = None

 
#     def insert(self, value):
#         newNode = Root(value)
#         if not self.root:
#             self.root = newNode 
#         else:
#             currentNode = self.root
#             while True:
#                 if value > currentNode.data:
#                     if not currentNode.right:
#                         currentNode.right = newNode
#                         return self
#                     else:
#                         currentNode = currentNode.right
#                 else:
#                     if not currentNode.left:
#                         currentNode.left = newNode
#                         return self
#                     else:
#                         currentNode = currentNode.left

#     def maxNode(self):
#         currentNode = self.root
#         maxNum = 0
#         while currentNode:
#             maxNum = max(maxNum, currentNode.data)
#             currentNode = currentNode.right
#         return maxNum


#     def minNode(self):
#         currentNode = self.root
#         minNum = 0
#         while currentNode:
#             minNum = min(minNum, currentNode.data)
#             currentNode = currentNode.left
#         return minNum

#     def indexOf(self, num):
#         count = 0
#         currentNode = self.root
#         if num > currentNode.data:
#             while currentNode:
#                 if currentNode.data == num:
#                     return count
#                 currentNode = currentNode.right
#                 count+=1
#         elif num < currentNode.data:
#             while currentNode:
#                 if currentNode.data == num:
#                     return count
#                 currentNode = currentNode.left
#                 count += 1
#         else:
#             return None

#     def lookUp(self, num):
#         currentNode = self.root
#         if num > currentNode.data:
#             while currentNode:
#                 if currentNode.data == num:
#                     return currentNode.data, self.indexOf(num)
#                 currentNode = currentNode.right

#         elif num < currentNode.data:
#             while currentNode:
#                 if currentNode.data == num:
#                     return currentNode.data, self.indexOf(num)
#                 currentNode = currentNode.left
#         else:
#             return "NOT FOUND!"


#     def pre_order(self):
#         print(self.root.data)

#         if self.root.right:
#             return self.root.right.pre_order()

#         if self.root.left:
#             return self.root.left.pre_order()


#     def in_order(self):
#         if self.root.right:
#             return self.root.right.in_order()

#         print(self.root.data)

#         if self.root.left:
#             return self.root.left.in_order()


#     def post_order(self):
#         if self.root.right:
#             return self.root.right.post_order()
        
#         if self.root.left:
#             return self.root.left.post_order()

#         print(self.root.data)


# obj = BinarySearchTree()

# for x in range(1, 11):
#     obj.insert(x)

# for y in range(12, 21):
#     obj.insert(y)


# print(obj.maxNode())
# print(obj.minNode())

# print(obj.lookUp(14))




# Happy Number leetCode

# class HappyNumber:
#     def __init__(self, number):
#         self.number = number
    
#     def solution(self):
#         seen = set()

#         while self.number not in seen:
#             print(seen, self.number, 'first')
#             seen.add(self.number)
#             self.number = sum((int(x)**2 for x in str(self.number)))
#             print(self.number, 'second')
#         return self.number == 1

# obj = HappyNumber(19)

# print((obj.solution()))



# is Valid Sequence

# class isValidSequnce:
#     def solution(self, array, sequence):
#         seqIndex = 0
#         for value in array:
#             if seqIndex == len(sequence):
#                 break
#             if sequence[seqIndex] == value:
#                 seqIndex+=1
#         return seqIndex == len(sequence) 

# obj = isValidSequnce()
# print(obj.solution([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))


# Sum of first and last digits codechef

# T = int(input())

# for _ in range(T):
#     n = input()
#     print(int(n[0]) + int(n[len(n)-1]))



# Program to reverse an Integer Codechef

# T = int(input())

# for _ in range(T):
#     n = input()
#     n = list(n)
#     right = 0
#     left = len(n)-1
#     while right < left:
#         n[right], n[left] = n[left], n[right]
#         right+=1
#         left-=1
#     print(int("".join(n)))




# Missing Number leetCode

# class MissingNumber:
#     def solution(self, nums):
#         n = len(nums)
#         return n * ((n+1) // 2) - sum(nums)

# obj = MissingNumber()

# print(obj.solution([9,6,4,2,3,5,7,0,1]))


# word to binary Codewars

# class WordToBinary:
#     def __init__(self, stringArr):
#         self.stringArr = stringArr

#     def solution(self):
#         return [format(ord(binWord), 'b') for binWord in self.stringArr]


# obj = WordToBinary('man')
# print(obj.solution())



# Special Series Sum GreeksForGreeks

# class SpecialSeriesSum:
#     def __init__(self, seriesNum):
#         self.seriesNum = seriesNum

#     def solution(self):
#         s = 0
#         for x in range(self.seriesNum+2):
#             s += sum(list(range(1, x)))
#         return s

# obj = SpecialSeriesSum(5)

# print(obj.solution())



# Doubling the value GreeksForGreeks

# def doubleTheValue(array, num):
#     count = 0
#     maxReturn = num

#     for ele in array:
#         if ele == num:
#             maxReturn = ele*2
#             return doubleTheValue(array[count:], maxReturn)
#         count+=1
#     return maxReturn


# print(doubleTheValue([1, 2, 3, 4, 8], 2))



# Maximum Money GreeksForGreeks

# def maximunMoney(n, k):
#     return (n+1//2)*k if n % 2 != 0 else n//2*k


# print(maximunMoney(5, 10))


# Multiply left and right array sum

# def arraySum(array):
#     mid = len(array) // 2
#     return sum(array[:mid]) * sum(array[mid:])

# print(arraySum([1,2]))


# Kth largest Number

# def klargeNum(number, k):
#     hashSet = set()
#     for _ in range(k):
#         hashSet.add(number.pop(number.index(max(number))))
#     return hashSet


# print(klargeNum([12, 15, 787, 1, 23], 3))


# Frequency Game GreeksForGreeks

# def frqGame(arr):
#     hashMap = dict()
#     for ele in arr:
#         hashMap[ele] = 1
#     maxKey = max(hashMap)
#     for key in hashMap:
#         if hashMap[key] < len(arr) // 2:
#             maxKey = max(maxKey, key)

#     return maxKey

# print(frqGame([2,4,5,6,10, 10,1]))



# Simple Balanced Parenthese

# class BalancedParenthe:
#     def solution(self, string):
#         hashMap = {'(':')', '{':'}', '[':']'}
#         l = list()
#         for ele in string:
#             if ele in hashMap:
#                 l.append(ele)
#             elif len(l) == 0 or hashMap[l.pop()] != ele:
#                 return False
#         return len(l) == 0

# obj = BalancedParenthe()

# print(obj.solution('())))'))


# Subarray with given Sum GreeksForGreeks

# def SubarraySum(arr, target):
#     l = 0
#     r = 1
#     while l < len(arr):
#         res = sum(arr[l:r])
#         if res == target:
#             return l+1, r, arr[l:r]
#         elif res > target:
#             l+=1
#             r=0
#             r=l+1
#         else:
#             r+=1
#     return -1

# print(SubarraySum([1,2,3,7,5], 19))



# Min Stack LeetCode

# class MinStack:
#     def __init__(self):
#         self.stack = []

#     def push(self, val):
#         self.stack.append(val)

#     def pop(self):
#         return self.stack.pop(0)

#     def minNum(self):
#         return min(self.stack)

#     def show(self):
#         return self.stack

# obj = MinStack()

# print(obj.push(-3))
# print(obj.push(0))
# print(obj.push(-2))

# print(obj.show())

# print(obj.pop())

# print(obj.minNum())

# print(obj.show())



# Find the largest Kth Integer in the Array LeetCode

# def LargestKthInteger(arr, knum):
#     res = 0
#     if len(arr) < knum:
#         return 0
#     arr = [int(x) for x in arr]
#     while knum != 0:
#         res = arr.pop(arr.index(max(arr)))
#         print(knum, "--", res)
#         knum -= 1
#     return res



# # print(LargestKthInteger(["3","6","7","10"], 4))
# # print(LargestKthInteger(["2","21","12","1"], 3))

# # print(LargestKthInteger(["0", "0"], 2))

# print(LargestKthInteger(["1", '2', '2'], 3))



# find Kth largest Element in an array LeetCode


# def findKthLargestElement(num, k):
#     return sorted(num)[-k]

# print(findKthLargestElement([3,2,1,5,6,4], 2))



# find maximum third number LeetCode

# def thirdMaxNum(arr):
#     if len(set(arr)) == 2:
#         return max(arr)
#     count = 0
#     prev = 0
#     for ele in arr:
#         if ele == prev:
#             count -= 1 
#             print(count, 'if', ele, prev)

#         prev = ele
#         count +=1
#     print(count)
#     try:
#         print(arr[count])
#     except:
#         print(arr[count-1])
# print(thirdMaxNum([5, 2, 2]))



# Second largest Number in a string LeetCode

# def secLargestNum(string):
#     l = list()
#     for i in string:
#         if i.isdigit() and i not in l:
#             l.append(i)

#     if len(l) > 2:
#         return sorted(l)[-2]
#     else:
#         -1

# print(secLargestNum('"dfa12321afd"'))
        


# Largest Odd number in a string LeetCode

# def largestOddNum(strNum):
#     res = 0
#     if int(strNum) % 2 != 0:
#         return strNum
#     else:
#         for i in strNum:
#             if int(i) % 2 != 0:
#                 res = max(res, int(i))
#         return res if res else ""

    # for i in range(len(strNum)-1, -1, -1):
    #     if strNum[i] in '13579':
    #         return strNum[0:i+1]
    #     return ""


# print(largestOddNum('1013389'))


# check if all characters have equal number of occurenece Leetcode


# def equalchr(string):
#     hashMap = dict()
#     for ele in string:
#         if ele in hashMap:
#             hashMap[ele] += 1
#         else:
#             hashMap[ele] = 1

#     if max(hashMap.values()) == min(hashMap.values()):
#         return True
#     return False

# print(equalchr('aaabb'))



# Sum of Digits of String after Convert LeetCode

# def getLucky(string, k):
#     res = str()
#     res += ''.join([str(ord(x)-96) for x in string.lower()])
#     while k != 0:
#         res = split(str(res));k-=1
#     return res

# def split(res):
#     return sum(map(int, res))

# print(getLucky('zbax', 2))



# Digital Sum: Add digits leetcode
# https://en.wikipedia.org/wiki/Digital_root#Congruence_formula

# def digitSum(number):
#     return (number - 1) % 9 + 1

# print(digitSum(38))



# Count the Tailing zeroes LeetCode

# from math import factorial

# def factAndCount(number):
#     Factnum = str(factorial(number))
#     tail = len(Factnum) - 1
#     count = 0
#     while tail != 0:
#         if Factnum[tail] == '0':
#             count += 1
#         else:
#             return count
#         tail -= 1
#     return 0
# print(factAndCount(0))


# Majority of Elements II LeetCode

# def MajorityEle(arr):
#     hashMap = dict()

#     for ele in arr:
#         if ele in hashMap:
#             hashMap[ele] += 1
#         hashMap[ele] =  1

#     for key in hashMap:
#         if hashMap[key] >= len(arr) // 3:
#             return key

# print(MajorityEle([1,2]))


# Find Anagram Cracking the coding the interview

# def checkAnagram(str1, str2):
#     c1 = [0] * 26   
#     c2 = [0] * 26

#     for i in range(len(str1)):
#         pos = ord(str1[i]) - ord('a')
#         c1[pos] = c1[pos] + 1

#         print(c1, '--->', str1[i])
    
#     for i in range(len(str2)):
#         pos = ord(str2[i]) - ord('a')
#         c2[pos] = c2[pos] + 1
        
#         print(c2, '--->', str1[i])



#     j = 0
#     flag = True

#     while j < len(str1) and flag:
#         if c1[j] == c2[j]:
#             j += 1
#             print(c1[j], c2[j])

#         else:
#             flag = False

#     return flag

# print(checkAnagram('heart', 'earth'))



# Valid Palindrome LeetCode

# def validPalindrome(string):
#     s = str()
#     if string in '1234567890':
#         return False
#     else:
#         s += "".join(ele for ele in string.lower() if ord(ele) not in range(48, 58) and ord(ele) in range(97, 123))
#         l = 00
#         r = len(s) - 1
#         count = 0
#         while l < r:
#             if s[l] == s[r]:
#                 l+=1
#                 r-=1
#                 count += 1
#             else:
#                 return False
#     return l == r


# # print(validPalindrome('A man, a plan, a canal: Panama'))
# print(validPalindrome('Ara0'))


# Reversing a string using stack

# def reverseStrByStack(string):
#     stack = []

#     for i in range(len(string)-1, -1, -1):
#         stack.append(string[i])

#     return ''.join(stack)


# print(reverseStrByStack('arsh'))


# Decimal to Binary numbers

# def decToBinNum(num):
#     remainder = str()
#     while num != 0:
#         remainder += str(num%2)
#         num //= 2
#     return remainder[::-1]

# print(decToBinNum(5))



# AlphaNumeric Numbers

# def alphaNumeric(string):
#     c = 0
#     for i in range(len(string)):    
#         c += ord(string[i]) - 96
#         # print(ord(string[i]) - 96)

#     return c


# print(alphaNumeric('four'))



# Unsorted Lists: Linked List A different Approach.


# from typing import NoReturn


# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

#     def getData(self):
#         return self.data
    
#     def getNext(self):
#         return self.next
    
#     def setData(self, newData):
#         self.data = newData

#     def setNext(self, newNext):
#         self.next = newNext



# class UnorderedLinkedList:
#     def __init__(self):
#         self.head = None

#     def isEmpty(self):
#         return self.head == None

#     def push(self, newData):
#         newNode = Node(newData, self.head)
#         newNode.setNext(self.head)
#         self.head = newNode

#     def show(self):
#         current = self.head
#         s = str()
#         while current:
#             s += str(current.getData()) + '--->'
#             current = current.getNext()

#         return s

#     def size(self):
#         current = self.head
#         count = 0
#         while current:
#             count += 1
#             current = current.getNext()

#         return count

#     def maxAndmin(self):
#         current = self.head
#         maxNum = 0
#         minNum = 1

#         current = self.head

#         while current:
#             maxNum = max(maxNum, current.getData())
#             minNum = min(minNum, current.getData())
#             current = current.getNext()

#         return maxNum, minNum

#     def index(self, num):
#         indexOfNum = 0
#         current = self.head

#         while current:
#             if num == current.getData():
#                 return indexOfNum
#             indexOfNum += 1
#             current = current.getNext()
#         return NoReturn

#     def search(self, num):
#         current = self.head

#         while current != None:
#             if current.getData() == num:
#                 return f'{num} at position: {self.index(num)}'
#             current = current.getNext()
#         return "NotFound"

    
#     def remove(self, num):
#         current = self.head
#         prev = None
#         found = False
#         while not found:
#             if current.getData() == num:
#                 found = True
#             else:
#                 prev = current
#                 current = current.getNext()
        
#         if prev == None:
#             self.head = current.getNext()
#         else:
#             prev.setNext(current.getNext())

#     # Getting the middle point of the linkedlist

#     def midPointASlowOne(self):
#         current = self.head
#         count = 0

#         while current != None:
#             count += 1
#             current = current.getNext()

#         count //= 2;loop = 0
#         current = self.head
#         while current:
#             if loop == count:
#                 return current.getData()
#             loop += 1
#             current = current.getNext()

    
#     def midPointAFastOne(self):
#         fast = self.head
#         slow = self.head
#         while fast and fast.getNext():
#             slow = slow.getNext()
#             fast = fast.getNext().getNext()

#         return slow.data


#     def append(self, value):
#         newNode = Node(value)
#         current = self.head
#         prev = None
#         while current != None:
#             current = current.getNext()
#             if current != None:
#                 prev = current
#         prev.setNext(newNode)


#     def reverse(self):
#         prev = None
#         current = self.head
#         while current:
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
        
#         self.head = prev

    
#     def insert(self, pos, data):
#         newNode = Node(data)
#         current = self.head
#         while current:
#             if pos == 0:
#                 print(current.data)
#                 print(prev.data)
#                 tmp = prev.getNext()
#                 prev.setNext(newNode)
#                 prev.next.next = tmp
#             else:
#                 current = current.getNext()
#                 prev = current
#             pos -= 1



# obj = UnorderedLinkedList()

# print(obj.isEmpty())

# for x in range(1, 10):
#     obj.push(x)

# print(obj.show())

# print(obj.size(), ': size')

# print(obj.maxAndmin(), ': Max, Min')

# print(obj.search(7), ': Search')

# print(obj.remove(1), ': remove')

# print(obj.show())

# print(obj.midPointASlowOne(), 'Mid slow')

# print(obj.midPointAFastOne(), 'Mid Fast')

# (obj.append(20))

# print(obj.show())


# obj.reverse()

# print(obj.insert(1, 90))

# print(obj.show())




# Ordered List: linkedList


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

#     def getData(self):
#         return self.data

#     def getNext(self):
#         return self.next

#     def setData(self, newData):
#         self.data = newData

#     def setNext(self, newNext):
#         self.next = newNext


    

# class OrderedLinkedList:
#     def __init__(self):
#         self.head = None
#         self.length = 0

    
#     def add(self, data):
#         current = self.head
#         flag = False
#         prev = None
#         while current != None and not flag:
#             if current.getData() > data:
#                 flag = True

#             else:
#                 prev = current
#                 current = current.getNext()


#         newNode = Node(data)

#         if prev == None:
#             newNode.setNext(self.head)
#             self.head = newNode

#         else:
#             newNode.setNext(current)
#             prev.setNext(newNode)
#         self.length += 1


#     def searching(self, ele):
#         current = self.head

#         while current != None:
#             if current.getData() == ele:
#                 return current.getData()

#             current = current.getNext()

#         return None



#     def show(self):
#         current = self.head
#         s = str()
#         while current != None:
#             s += str(current.getData()) + '----->'
#             current = current.getNext()

#         return s
    
#     def index(self, num):
#         count = 0
#         current = self.head
#         while current != None:
#             if current.getData() == num:
#                 return count + 1

#             count += 1
#             current = current.getNext()
#         return None


#     def maxAndmin(self):
#         current = self.head
#         maxNum = 0
#         minNum = 100

#         while current != None:
#             maxNum = max(maxNum, current.getData())
#             minNum = min(minNum, current.getData())
#             current = current.getNext()

#         return f'Max :{maxNum}, Min :{minNum}'

    
#     def append(self, data):
#         newNode = Node(data)
#         current = self.head
#         prev = None
#         while current != None:
#             if current == None:
#                 break
#             else:
#                 prev = current
#                 current = current.getNext()


#         prev.setNext(newNode)



#     def size(self):
#         return self.length

#     def isEmpty(self):
#         return self.size == 0



# obj = OrderedLinkedList()

# print(obj.add(10))
# print(obj.add(20))
# print(obj.add(30))
# obj.add(1)

# print(obj.isEmpty())

# print(obj.size())

# print(obj.show())

# print(obj.searching(20))

# print(obj.maxAndmin())

# print(obj.index(30))

# print(obj.append(90))

# print(obj.show())




# Suming list without using loops

# def listSum(arr):
#     if len(arr) == 1:
#         return arr[0]

#     else:
#         return arr[0] + listSum(arr[1:])

# print(listSum([1, 2, 3]))



# merge sort

# def mergeSort(arr):
#     for ele in range(len(arr)-1, 0, -1):
#         for i in range(ele):
#             if arr[i] > arr[i+1]:
#                 tmp = arr[i]
#                 arr[i] = arr[i+1]
#                 arr[i+1] = tmp
#     print(arr)
# arr = [5,4,3,21,0,2,7,9]
# obj = mergeSort(arr)





# Sort Characters By Frequency LeetCode

# from collections import Counter 

# def SortCharByFeq(string):
#     res = ''
#     ct = Counter(string)
#     print(ct)
#     ct = ct.most_common()
#     print(ct)
#     for ele in ct:
#         res += str(ele[0] * ele[1])

#     return res

# print(SortCharByFeq("raaeaedere"))



# Top K frequent element LeetCode

# from collections import Counter

# def topKfreq(string, k=0):
#     count = Counter(string).most_common()
#     res = list()
#     for i in range(k):
#         res.append(count[i][0])
#         print(count[i], count[i][0])
#     return res
# print(topKfreq([1,2], 2))


# Top K frequent words

# from collections import Counter

# def topKWords(string, k):
#     count = Counter(string).most_common()
#     print(count)
#     l = list()
#     for i in range(k):
#         l.append(count[i][0])
#     return l 
# print(topKWords(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))




# Nth root equals digit sum CodeWars

# def nthRootOfSum(num):
#     res = list()

#     for x in range(1, 1000):
#         if sum([int(i) for i in str(x**num)]) == x:
#             res.append(x**num)
#     return res

# print(nthRootOfSum(3))



# Consective Letters


# def consectiveLetters(string):
#     return ''.join(sorted(string)) in 'abcdefghijklmnopqrstuvwxyz'

# print(consectiveLetters('abc'))



# Count ones in a segment CodeWars

# def countOnes(left, right):
#     res = int()
#     ra = list(range(left, right+1))
#     return sum([int(bin(x)[2:]) for x in ra])

#     print(res)

# print(countOnes(5, 7))


# is there a vowel in there? CodeWars

# def is_vowel(arr):
#     hashMap = {
#         117 : 'u',
#         97 : 'a',
#         105: 'i',
#         101: 'e',
#         111 : 'o',
#     }
#     l = 0
#     while l != len(arr):
#         if arr[l] in hashMap:
#             arr[l] = hashMap[arr[l]]
#         l += 1
#     return arr

# print(is_vowel([101, 121, 110, 113, 113, 103, 121, 121, 'e', 107, 103] ))



# String compression Cracking the coding interview

# from collections import Counter

# def char_count(input_str):
#     my_dict = Counter(input_str)
#     print(my_dict)
#     output_str = ""
#     for i in input_str:
#         if i not in output_str:
#             output_str += i
#             output_str += str(my_dict[i])
#     return output_str

# result = char_count("aabccccaaa")
# print(result)

# def stringCompress(string, res=str()):
#     l = 0
#     r = len(string) - 1
#     count = 0
#     res = res
#     while l < r:
#         if string[l] == string[l+1]:
#             count += 1
#         elif string[l] != string[l+1]:
#             res += string[l] + str(count)
#             print(res, count, string[l])
#             return stringCompress(string[:count], res)
#         l += 1
#         count = 0
#     return res

# print(stringCompress('aaaabb'))



# is Unique String

# def isUniqueChar(string):
    # hashSet = set()

    # for ele in string:
    #     if ele not in hashSet:
    #         hashSet.add(ele)
    #     else:
    #         return False
    # return True

#     matrix = [0] * 26
#     for i in range(len(string)):
#         pos = ord(string[i]) - ord('a')
#         if not matrix[pos]:
#             matrix[pos] = 1
#             print(matrix)
#         else:
#             return False
#     return True

# print(isUniqueChar('arsh'))


# check Permutation

# def isPermutation(s1, s2):
    # s1 = sorted(s1)
    # s2 = sorted(s2)
    # return s1 == s2, len(s1) == len(s2)

    # matrix1 = [0] * 26
    # matrix2 = [0] * 26
    # count = 0
    # if len(s1) == len(s2):
    #     while count < len(s1) and len(s2):
    #         pos1 = ord(s1[count]) - ord('a')
    #         pos2 = ord(s2[count]) - ord('a')
    #         print(pos1, pos2)
    #         matrix1[pos1] = 1
    #         matrix2[pos2] = 1

    #         count += 1
    #     print(sum(matrix2), sum(matrix1))
    #     if matrix1 == matrix2:
    #         return True
        
    # return False

# print(isPermutation('arsh', 'hrsa'))



# String compression cracking the coding interview

# def stringCompress(string):
#     compressed = []
#     counter = 0

#     for i in range(len(string)):  # noqa
#         # print(i, counter, string[i], string[i-1])
#         if i != 0 and string[i] != string[i - 1]:
#             compressed.append(string[i - 1] + str(counter))
#             counter = 0
#             # print(compressed, string[i - 1], string[i], i)
#         counter += 1

#     # add last repeated character
#     if counter:
#         compressed.append(string[-1] + str(counter))

#     # returns original string if compressed string isn't smaller
#     return min(string, "".join(compressed), key=len)

# print(stringCompress('aaaaaarshaa'))



# string rotation Cracking the coding interview

# def stringRotation(s1, s2):
#     if len(s1) == len(s2) != 0:
#         return s1 in s2 * 2
#     return False

# print(stringRotation('foo', 'bar'))


# Peak Element in an Array 

# def peakElement(arr):
#     MaxNum = arr[0]
#     index = 0

#     for key, value in enumerate(arr):
#         if MaxNum < value:
#             MaxNum = value
#             index = key

#     return index

# print(peakElement([1,2,3]))


# replace 0's with 5's

# def replaceZeroWithFive(number):
#     number = list(str(number))
#     for ele in range(len(number)):
#         if number[ele] == '0':
#             number[ele] = '5'
#     return ''.join(number)

# print(replaceZeroWithFive(1002))



# Multiply Strings

# def multiplyString(num1, num2):
#     intNum1 = 0
#     intNum2 = 0
#     for i in num1:
#         intNum1 = abs(intNum1) * 10 + ord(i) - ord('0')
#     for i in num2:
#         intNum2 = abs(intNum2) * 10 + ord(i) - ord('0')
#     return intNum1 * abs(intNum2), intNum2 , intNum1

# print(multiplyString('4416', '-333'))
# 4416 -333


# Missing number 

# def missingNum(number):
#     return [x for x in range(sorted(number)[0], sorted(number)[-1]) if x not in number]

# print(missingNum([1,2,3,5]))


# Display longest name

# def longestName(string):
#     maxLen = 0
#     name = str()

    # for ele in string:
    #     if len(ele) > maxLen:
    #         maxLen = len(ele);name = ele

    # return name

#     for key, value in enumerate(string):
#         if len(value) > maxLen:
#             maxLen = len(value)
#         else:
#             string.pop(key)

#     return string[key]
        
# print(longestName(['arsh', 'a', 'ergon', 'arshali']))


# Armstrong number

# def armstrong(number):
#     return  'Yes' if sum([pow(int(num), 3) for num in str(number)]) == number else 'No'

# print(armstrong(153))



# Find all Anagrams in a string LeetCode

# my algorithm works but when it comes in huge inputs it's kinda slow

# def findAnagrams(s1, s2):
#     s1Len = len(s1)
#     s2Len = len(s2)
#     l = 0
#     count = 0
#     res = list()
#     while l < s1Len-1:
#         # if sum(map(ord, s2)) == sum(map(ord, s1[count:count+s2Len])):
#         if sorted(s2) == sorted(s1[count:count+s2Len]):

#             # print(count)
#             res.append(count)
#         # print(s1[count:count+3])
#         l += 1
#         count += 1

#     return [] if len(res) == 1 and 0 in res else res[:205]


# # print(findAnagrams("cbaebabacd", 'abc'))

# # print(findAnagrams("abab", 'ab'))

# # print(findAnagrams("af", 'be'))

# print(findAnagrams("eklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmou", "yqrbgjdwtcaxzsnifvhmou"))

# def anagram(s, p):
#     ans = []
#     p_freq = [0] * 26
#     for ch in p:
#         p_freq[ord(ch)-ord('a')] += 1
    
#     s_freq = [0] * 26
    
#     left = 0
#     for right in range(len(s)):
#         s_freq[ord(s[right])-ord('a')] += 1
#         if right-left+1 == len(p):
#             if s_freq == p_freq:
#                 ans.append(left)
#             s_freq[ord(s[left])-ord('a')] -= 1
#             left += 1
#     return ans


# print(anagram('cbaebabacd', 'abc'))



# backSpace string compare


# def backspace(s1, s2=0):
    # def check(s):
    #     stack = []
    #     for i in s1:
    #         if stack and i == '#':
    #             stack.pop()
    #         elif i.isalpha():
    #             stack.append(i)
    #     return stack
    # return check(s1) == check(s2)
    
    # s = []; t = []

#     for i in s1:
#         if i != '#':
#             s.append(i)
#         elif len(s) != 0:
#             (s.pop())

#     for i in s2:
#         if i != '#':
#             t.append(i)
#         elif len(t) != 0:
#             (t.pop())

#     return s == t

# print(backspace('ab#c', 'ad#cd'))


# string to integers LeetCode

# def MyAtoi(number):
#     res = str()
#     number = number.replace(' ', '')
#     if ord(number[0].lower()) in range(97, 123):
#         return 0
#     elif ord(number[0].lower()) not in range(97, 123):
#         for num in number:
#             if ord(num) not in range(97, 123):
#                 res += num

#     return int(res)



# print(MyAtoi('        -45ars'))

# print(MyAtoi('a123'))

# print(MyAtoi('0021'))



# Highest scoring word in a string codewars

# def higestScoringWord(string):
#     hashMap = dict()

#     for word in string.split():
#         hashMap[sum(map(ord, word))-96*len(word)] = word

#     return hashMap[max(hashMap.keys())], hashMap

# print(higestScoringWord('hello there how are you?'))

# print(higestScoringWord('what time are we climbing up the volcano'))


# Arabian String CodeWars

# def arabianString(string):
#     string = string.lower()
#     remove_item = 0
#     for ele in string:
#         if ord(ele) not in range(97, 123):
#             remove_item = ele
#             print(remove_item)
#             string.replace(remove_item, '')

#     return string.title()


# print(arabianString('Ninja-Test--0'))



# Add to Array-Form of Integer LeetCode

# def arrayForm(numList, num):
#     strInt = str()
#     strInt = strInt.join(str(x) for x in numList)
#     return list(str(int(strInt)+num))

# print(arrayForm([1,2,0,0], 34))

# print(arrayForm([2, 7, 4], 181))

# print(arrayForm([9,9,9,9,9,9,9,9,9,9], 1))


# count and say LeetCode


# class CountAndSay:

#     def convert(self, data):
#         if data == 1:
#             return '1'
#         prev = str(data)[0]
#         i = 0
#         ans = str()
#         for ch in str(data):
#             if ch == prev:
#                 i += 1
#             else:
#                 ans += f'{i}{prev}'
#                 prev = ch
#                 i = 1
#         ans += f'{i}{prev}'
#         return ans

#     def sol(self, num):
#         if num == 1:
#             return '1'
#         res = 1
#         for _ in range(num):
#             res = self.convert(res)
        
#         return res


# obj = CountAndSay()
# print(obj.sol(4))



# String compression LeetCode

# from collections import Counter as ct
# def CompressString(strArr):
#     count = ct(strArr)
#     res = list()
#     for x in sorted(set(strArr)):
#         if count[x] == 1:
#             res.append(x)
#         else:
#             res.append(x);res.append(str(count[x]))

#     return res

# print(CompressString(["a","a","b","b","c","c","c"]))


# Mini-Max Sum HackerRank

# def MinAndMax(numArr):
#     minNum, maxNum = 99, 0
#     for i in range(len(numArr)):
#         total = sum(numArr) - numArr[i]
#         maxNum = max(maxNum, total)
#         minNum = min(minNum, total)

#     return maxNum, minNum


# print(MinAndMax([1,3,5,7,9]))



# Check if Number are ascending in a sentences LeetCode

# def AscendingNumbers(string):
#     res = 0

#     for ele in string.split():
#         if ele.isnumeric():
#             if int(ele) > res:res = int(ele)
#             else:return False

#     return True


# print(AscendingNumbers("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))

# print(AscendingNumbers("hello world 5 x 5"))



# Replace all digits with characters LeetCode

# def replaceNumWithChar(string):
    # res = str()
    # for i in range(len(string)):
    #     if i % 2 != 0:
    #         res += chr(ord(string[i-1]) + int(string[i]))
    #     else:
    #         res += string[i]
    # return res

#     l = list(string)

#     for i in range(1, len(l), 2):
#         l[i] = chr(ord(string[i-1]) + int(string[i]))
#     return ''.join(l)
# print(replaceNumWithChar('a1c1e1'))


# Check if the string is a prefix of another leetCode

# def isPrefix(s, word):
#     res = str()
#     word = word.split()
#     for i in range(len(s)-1):
#         res += word[i]
#     if res == s:
#         return True
#     return False

# print(isPrefix( "iloveleetcode", ["i","love","leetcode","apples"]))


# Check if the sentence is Pangram LeetCode

# def isPangram(string):
#     string = set(string.lower())
#     l = list(range(97, 123))
#     for x in string:
#         if ord(x) in l:
#             l.remove(ord(x))
#     return len(l) == 0, l

# print(isPangram("hequickbrownoxjumpsoverthelazydog"))


# Find the common characters LeetCode

# def sortingTheSent(string):
#     hashMap = dict()
#     string = string.split()
#     for i in range(len(string)):
#         hashMap[string[i][-1]] = string[i][:-1]
#     return ' '.join(hashMap[x] for x in sorted(hashMap))

# print(sortingTheSent("is2 sentence4 This1 a3"))



# Merge Strings Alternately #LeetCode

# def mergeString(word1, word2):
#     l1, l2 = len(word1), len(word2)
#     res = str()
#     for i in range(min(l1, l2)):
#         res += f'{word1[i]}{word2[i]}'
#     if l1 > l2:
#         res += word1[i+1:]
#     else:
#         res += word2[i+1:]
#     return res

# print(mergeString('ab', 'pqrs'))


# Find first and last position of an element in sorted array LeetCode

# def searchTarget(arr, target):
#     try:
#         first = arr.index(target)
#         arr.reverse()
#         second = len(arr) - arr.index(target) - 1
#         return [first, second]
#     except:
#         [-1, -1]

# print(searchTarget([5,7,7,8,8,10], 8))



# Seach in rotated Sorted array leetcode

# def searchTarget(nums, target): 
#     nums = sorted(nums)
#     print(nums)
#     l, r = 0, len(nums) - 1
#     while l < r:
#         mid = (r+l) // 2
#         print(nums[mid], mid)
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             l = mid + 1
#         else:
#             r = mid - 1

#     return -1 

# print(searchTarget([4,5,6,7,0,1,2], 0))


# Display longest Name GreeksForGreeks

# def longestName(strArr):
#     maxName = 0
#     name = str()
#     for x in strArr:
#         if len(x) > maxName:
#             maxName = len(x)
#             name = x

#     return name

# print(longestName([ "Geek", "Geeks", "Geeksfor",
#   "GeeksforGeek", "GeeksforGeeks"]))


# Longest Consective of 1's

# def longestConsective(number):
#     binNum = bin(number)[2:]
#     maxNum = 00
#     c = 0
#     for x in binNum:
#         if x == '1':
#             c += 1
#         else:
#             maxNum = max(maxNum, c)
#             c = 0
#     return maxNum

# print(longestConsective(222))


# remove duplicates from a sorted array leetcode


# def removeDup(array):
#     prev = int()
#     l = list()
#     for ele in array:
#         if ele != prev:
#             prev = ele
#             l.append(ele)
#     return l

# print(removeDup([1,1,2]))


# Second largest digit in a string LeetCode

# def SecondLargest(alphaNum):
#     nums = set()

#     for i in alphaNum:
#         if i.isdigit():
#             nums.add(int(i))
#     nums= sorted(nums)

#     if len(nums) == 1 or len(nums) == 0:
#         return -1
#     return nums[-2]
    
# print(SecondLargest("abc1111"))


# Sum of all unique integers in an array LeetCode


# def sumOfUniqInt(intArr):
#     hashMap = dict()

#     res = 0

#     for x in intArr:
#         if x in hashMap:
#             hashMap[x] += 1
#         else:
#             hashMap[x] = 1
    
#     for key in hashMap:
#         if hashMap[key] == 1:
#             res += key

#     return res


# print(sumOfUniqInt([1,2,3,4,5]))


# from collections import Counter as ct

# def freqSort(numArr):
#     Map = ct(numArr)
#     li = list(Map.items())
#     res = list()

#     li.sort(key=lambda x:(x[1], -x[0]))


#     for key, value in li:
#         res += [key] * value
#     return res

# print(freqSort([1,1,2,2,2,3]))



# Find the median in a sorted array leetcode

# def medianSortedArr(nums1, nums2):
#     mid1, mid2, median = 0, 0, 0
#     l = nums1 + nums2
#     l.sort()
#     if len(l) % 2 == 0:
#         mid1 = len(l) // 2
#         mid2 = mid1 - 1
#         median = (l[mid1] + l[mid2]) /  2

#     else:
#         mid = len(l) // 2
#         median = l[mid]

#     return median

# print(medianSortedArr([1,2,3], [4,5,6]))


# find the adjacent elements of largest product CodeSignal


# def adjacentEle(elements):
#     l = 0
#     c = 1
#     maxNum = -100
#     while l < len(elements) - 1:
#         maxNum = max(maxNum, elements[l]*elements[c])
#         print(elements[l]*elements[c])
#         c+=1
#         l+=1
#     return maxNum
# print(adjacentEle([-23, 4, -3, 8, -12]))


# ShapeArea, interesting PolyGon CodeSignal

# def shapeArr(n):
#     return 2 * n * (n - 1) + 1

# print(shapeArr(3))



# Valid Perfect Squares LeetCode


# def validSquares(num):
#     # sq = int(num**(1/2))
#     # return sq*sq == num
#     return pow(int(num**.5), 2) == num

# print(validSquares(2000105819))



# Duplicate Zeros LeetCode

# def ZeroDupli(number):
#     i = 0
#     x = len(number)
#     while i < len(number):
#         if number[i] == 0:
#             number.insert(i, 0)
#             i += 2
#         else:
#             i += 1
#         if len(number) > x:
#             number.pop()
#     return number


# print(ZeroDupli([1,0,2,3,0,4,5,0]))
# print(ZeroDupli([1,2,3]))



# Search Rotated array II LeetCode


# def searchRotated(arr, target):
#     arr[:] = sorted(set(arr))
#     if arr.__len__() <= 5:
#         return target in arr
#     else:
#         l = 0
#         r = len(arr) - 1
#         while l <= r:
#             mid = (l+r) // 2 
#             if arr[mid] == target:
#                 return True
#             elif arr[mid] > target:
#                 r = mid - 1
#             else:
#                 l = mid + 1
#     return False


# print(searchRotated([4,5,6,7,0,1,2], 8))


# Longest Consective Sequence in unsorted Array LeetCode


# def ConsectiveSeq(numArr):
#     count = 1
#     maxNum = 0
#     numArr[:] = sorted(set(numArr))
#     # print(numArr)
#     if len(numArr) == 1:
#         return 1
#     for i in range(len(numArr)-1):
#         temp = numArr[i] + 1
#         if numArr[i+1] == temp:
#             count += 1
#             maxNum = max(maxNum, count)
#         else:
#             maxNum = max(maxNum, count)
#             count = 1
        
#     return maxNum

# print(ConsectiveSeq([100,4,200,1,3,2]))
# print(ConsectiveSeq([0,3,7,2,5,8,4,6,0,1]))
# print(ConsectiveSeq([9,1,4,7,3,-1,0,5,8,-1,6]))
# print(ConsectiveSeq([-6,-1,-1,9,-8,-6,-6,4,4,-3,-8,-1]))
# [1,2,3,4,100,200]


# Product of array without the array[i] value leetcode

# def productOfArray(arrNum):
#     n = len(arrNum) - 1
#     pre = 1
#     pos = 1
#     res = arrNum
#     for i in range(n):
#         res[i] = pre
#         pre *= arrNum[i]
    

#     while n >= 0:
#         res[n] *= pos
#         pos *= arrNum[n]
#         n -= 1

#     return res

# print(productOfArray([1,2,3,4]))
# print(productOfArray([-1,1,0,-3,3]))


# Is a Prime Number CodeWars

# def isPrimeNum(num):
#     flag = False
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 flag = True
#                 break
#     else:
#         return False
        
#     if flag:
#         print('No')
#     else:
#         print('yes')

# print(isPrimeNum(0))


# Find lucky Integer in an Array LeetCode

# def luckyNum(number):
#     hashMap = dict()
#     for ele in number:
#         if ele in hashMap:
#             hashMap[ele] += 1
#         else:
#             hashMap[ele] = 1
#     # maxNum = set()
#     # for key in hashMap:
#     #     if hashMap[key] == key:
#     #         maxNum.add(key)
    
#     # return max(maxNum) if maxNum else -1

#     maxNum = -1
#     for key in sorted(hashMap):
#         if hashMap[key] == key:
#             maxNum = key
    
#     return maxNum

# print(luckyNum([2,2,3,4]))

# print(luckyNum([1,2,2,3,3,3]))

# print(luckyNum([2,3,4]))



# How many numbers are smaller than the current number

# def findingSmallerThanCurrent(numArr):
#     lst = list(sorted(numArr))
#     return [lst.index(i) for i in numArr]

# print(findingSmallerThanCurrent([8,1,2,2,3]))



# Return the smallest string with swaps LeetCode not completed

# def smallestString(string, split):
#     OneArr = len(split[0]) -1 
#     x, y = 0, 0
#     print(OneArr)
#     for i in range(len(string)):

#         # string[split[OneArr][x]], string[split[OneArr[y]]] = string[1], string[0]
#         print(string[split[OneArr][x]]) #, string[split[OneArr[y]]])

# print(smallestString('arsh', [[0,2], [0,3]]))


# Remove one element to make the array strickly increasing leetCode


# def first_bad_pairs(num):
#     for i in range(len(num)-1):
#         if num[i] >= num[i+1]:
#             return i
#     return -1

# def checkIncreasing(numArr):
#     j = first_bad_pairs(numArr)
#     if j == -1:
#         return True
#     if first_bad_pairs(numArr[j-1:j]+numArr[j+1:]) == -1:
#         return True
#     if first_bad_pairs(numArr[j:j+1]+numArr[j+2:]) == -1:
#         return True
#     return False
    

# print(checkIncreasing([1, 3, 2, 1]))
# print(checkIncreasing([1, 3, 2]))
# print(checkIncreasing([123, -17, -5, 1, 2, 3, 12, 43, 45]))


# Longest Substring in a string leetCode


# def longestSubString(string):
#     hashMap = dict()
#     left = 0
#     right = 0
#     ans = 0

#     while left < len(string) and right < len(string):
#         el = string[right]
#         if el in hashMap:
#             left = max(left, hashMap[el]+1)
#         hashMap[el] = right

#         ans = max(ans, right-left+1)
#         right += 1

#     return ans

# print(longestSubString('abcabcbb'))


# first and last occurenece of a number leetcode

# def getFirst(numArr, target):
#     left = 0
#     right = len(numArr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if numArr[mid] == target:
#             if mid == 0 or numArr[mid-1] != target:
#                 return mid
#             right = mid - 1
#         elif numArr[mid] > target:
#             right = mid - 1 
#         else:
#             left = mid + 1

#     return -1 

# def getSecond(numArr, target):
#     left = 0
#     right = len(numArr) -1 
#     while left <= right:
#         mid = (left + right) // 2
#         if numArr[mid] == target:
#             if mid == len(numArr)-1 or numArr[mid+1] != target:
#                 return mid
#             left = mid + 1
#         elif numArr[mid] > target:
#             right = mid - 1 
#         else:
#             left = mid + 1
#     return -1

# def firstAndlast(numArr, target):
#     first =  getFirst(numArr, target)
#     second = getSecond(numArr, target)
#     # print(first)#, second)
#     return [first, second]
    
# print(firstAndlast([5,7,7,8,8,10], 8))
# print(firstAndlast([], 8))
# print(firstAndlast([5,7,7,8,8,10], 6))




# Rotate array leetcode


# def rotate(array, k):

#     for x in range(0, k):
#         temp = array.pop()
#         array.insert(0, temp)

#     return array

# print(rotate([1,2,3,4,5,6,7], 3)) 



# Smallest Index with equal value leetcode

# def smallestEqual(array):
#     for x in range(len(array)):
#         if x % 10 == array[x]:
#             return x
#     return -1



# print(smallestEqual([0, 1, 2]))


# find target indices after sorting the array leetcode

# def targetIndexes(array, target):
#     array.sort()
#     l, r = 0, len(array)
#     result = list()
#     while l <= r:
#         mid = (r+l) // 2
#         if array[mid] == target:
#             result.append(mid)
#             # if array[mid-1] == target:
#             #     result.append(mid-1)
#             # if array[mid+1] == target:
#             #     result.append(mid+1)
#             # print(array.pop(mid), mid)
#         elif array[mid] < target:
#             l = mid + 1
#         else:
#             r = mid - 1
#         return result if result else 0, array, mid
# print(targetIndexes([1, 2, 3,4,5,6,7,8,9], 4))



# Count common words with one occurenece Leetcode

# def countWords(word1, word2):
#     hashMap_word1 = dict()    
#     hashMap_word2 = dict()

#     for word_1 in word1:
#         if word_1 not in hashMap_word1:
#             hashMap_word1[word_1] = 1
#         # else:
#         #     hashMap_word1[word_1] = 1
#     print(hashMap_word1)
#     for word_2 in word2:
#         if word_2 not in hashMap_word2:
#             hashMap_word2[word_2] = 1
#         # else:
#         #     hashMap_word2[word_2]  = 1
#     print(hashMap_word2)

#     for word in hashMap_word2:
#         if word in hashMap_word1:
#             hashMap_word2[word] += 1

#     s1 = len([x for x in hashMap_word1 if hashMap_word1[x] == 2])
#     return s1


# print(countWords(["leetcode","is","amazing","as","is"], ["amazing","leetcode","is"]))



# To lower case LeetCode

# def lowerCase(string):
#     res = str()
#     for x in string:
#         if ord(x) >= 65 and ord(x) <= 90:
#             res+= chr(ord(x)+32)
#         else:
#             res+= x
#     return res

# print(lowerCase("Arsh"))


# Uncommon words from a sentences leetcode


# def uncommonFinder(string):
#     hashMap = dict()

#     for word in string.split():
#         if word in hashMap:
#             hashMap[word] += 1
#         else:
#             hashMap[word] = 1

#     result = list()
#     for key in hashMap:
#         if hashMap[key] == 1:
#             result.append(key)

#     return result


# print(uncommonFinder('this apple is sweet this apple is sour'))



# find words that can be formed by characters Leetcode
# from collections import Counter

# def letterFormed(wordList, chars):
#     result = int()
#     main_c = Counter(chars)    
#     for i in wordList:
#         if Counter(i) & main_c == Counter(i):
#             result += len(i)
#     return result


# print(letterFormed(["cat","bt","hat","tree"], 'atach'))


# reverse only letter Leetcode

# def reverseOnlyLetter(word):
#     onlyWord  = str()

#     for i in word:
#         # if ord(i) in range(65, 123) or ord(i) in range(65, 90):
#         if i.isalpha(): 
#             onlyWord += i
#     onlyWord = onlyWord[::-1]
#     onlyWord = list(onlyWord)
#     # for x in range(len(word)):
#     #     if ord(word[x]) not in range(65, 123) and ord(word[x]) not in range(65, 90):
#     #         onlyWord.insert(x, word[x])

#     for key, value in enumerate(word):
#         if ord(value) not in range(97, 123) and ord(value) not in range(65, 90):
#             onlyWord.insert(key, value)

#     return ''.join(x for x in onlyWord)    

# print(reverseOnlyLetter('a-bC-dEf-ghIj'))


# Student attendance record I leetcode

# def checkRecord(student):
#     absent = 0
#     late = 0

#     for i in student:
#         if i != 'A':
#             absent = 0
#         if i == 'A':
#             absent += 1

#         if i == 'L':
#             late += 1

#         if absent >= 2 or late == 3:
#             return False

#     return True

# print(checkRecord('PPALLL'))
        


# find first palindrome string in the array

# def palindrome(string):
#     # if string == string[::-1]:
#     #     return string
#     return string == string[::-1]

# def firstPalindrome(strArr):
#     for word in strArr:
#          result = palindrome(word)
#          if result:
#              return word
#     return ""

# print(firstPalindrome(["abc","car","ada","racecar","cool"]))


# Valid Palindrome LeetCode

# def validPalindrome(string):
#     res = str()

#     for i in string.lower():
#         if i.isalpha() or i.isdigit():
#             res += i

#     return res == res[::-1], res


# print(validPalindrome('0P'))


# third maximun number leetcode

# def thirdMax(arrNum):
#     arrNum[:] = set(arrNum)
#     if len(arrNum) <= 2:
#         return max(arrNum)

#     count = 3
#     res = int()
#     while count != 0:
#         res = arrNum.pop(arrNum.index(max(arrNum)))
#         count -= 1

#     return res

# print(thirdMax([1,2,2,5,3,5]))


# Shuffle the array LeetCode

# def shuffleArray(numArr, n):
#     new_arr = [0] * len(numArr)
#     count = 0
#     oddIndex = 0
#     while count <= n-1:
#         new_arr[oddIndex] = numArr[count]
#         oddIndex+=2
#         count += 1

#     evenIndex = 1
#     difference = len(numArr) - count
#     i = 1
#     while count <= len(numArr):
#         new_arr[evenIndex] = numArr[count]
#         oddIndex+=1
#         evenIndex += 2
#         count += 1
#         if i == difference:
#             break
#         i+=1

#     return new_arr

# print(shuffleArray([2,5,1,3,4,7], 3))

# print(shuffleArray([2,5,1,3,4,7], 3) == [2,3,5,4,1,7])



# Longest continuours inscreasing subsequence leetcode

# def longestSubsequence(numArr):
#     max_count, res = 1, 1
#     for i in range(1, len(numArr)):
#         if numArr[i] > numArr[i - 1]:
#             res += i
#         else:
#             max_count = max(max_count, res)
#             res = 1
#     return max(max_count, res)


# print(longestSubsequence([1,3,5,4,7]))


# Count common words with one occurence leetcode

# def countWords(word1, word2):
#     new_array = word1 + word2
#     hashMap = dict()

#     for i in new_array:
#         if i in hashMap:
#             hashMap[i] += 1
#         else:
#             hashMap[i] = 1

#     res = 0
#     for key in hashMap:
#         if hashMap[key] == 2:
#             res += 1
#     return res

# print(countWords(['arsh', 'ergon'], ['ergon', 'ali']))


# Maximum number of words found in sentence leetcode

# def maxWordInSen(strSentence):
#     res = int()
#     for i in strSentence:
#         res = max(len(i.split()), res)
#     return res


# print(maxWordInSen(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))


# Rotate string leetcode

# def rotateString(string, goal):
#     for i in range(len(string)):
#         string = string[1:] + string[:1]
#         if string == goal:
#             return True
#     return False

# print(rotateString('abcde', 'cdeab'))


# Kth distinct string in an Array leetcode

# from collections import Counter

# def kthDistinct(strArr, k):
#     freq = Counter(strArr)

#     for x in strArr:
#         if freq[x] == 1:
#             k -= 1
#         if k == 0:
#             return x 
#     return ""

# print(kthDistinct(["d","b","c","b","c","a"], 2))
# print(kthDistinct(["aaa","aa","a"], 1))
# print(kthDistinct(["a","b","a"], 3))
# print(kthDistinct(["joy","pt","yoe","ibria","suvc","d","gua","izen","slt","oe","i","ajcc","gyz","vkx","xy","ktc","i","pgjr","y","qub","wdnu","l","xiu","yv","bdo","gzh","ud","ak","gkz","bsm","w","bgq","zwg","voecw","h","jxjwl","cn","l","uvv","hqy","l","ygpla","gyf","jndji","nm","pabi","wmi","n","c","u","wyy","sze","lgjce","l","eq","hjh","lww","nw","mgf","r","rju","ohcfj","iuo","y","okmx","k","r","rlj","ptw","grniz","youwc","tuox","ib","fqpsi","hteuo","nwgps","dpa","fiksn","dx","zkxvx","wraa","ang","c","fs","kbog","fju","b","guel","alpez","ugahf","uqt","wi","bgvl","sasdu","tbhmj","rnh","litf","tjlp","m","zbtla","tqz","hohg","rad","sba","v","ro","pxj","qf","pv","olku","yhw","ch","vl","iix","nyddk","gh","whpog","lbq","iaz","l","e","mrtv","amru","wu","pcdvm","e","ncal","bvsgi","twl","vysw","bb","pgv","ux","rl","ejt","x","ky","kjdhv","rwit","ko","p","tnvm","tzxar","sfl","y","a","qgdlj","tt","kswr","loos","wg","vzuv","et","pgl","nn","mmwz","qykk","agc","b","wqoc","f","xxp","s","jbew","uggel","gpgc","gmpp","lqcsc","xoym","joni","mfj","p","xhcp","ecxlb","h","y","plt","qm","wvao","qpui","eye","my","q","iwu","shwo","r","pykh","qvia","z","vla","nna","lxzq","frktm","i","tu","eikj","uyfxj","vos","gp","nqm","t","os","asou","qjp","hkwah","rsvxh","a","ywka","lvrq","l","jcgy","snyxu","nuaot","dwjir","bkzgc","nr","o","tclx","g","kx","clog","zbvcs","xmau","upqzf","tngrn","oy","rinwh","mpg","w","kywaj","xge","brg","we","fs","cjby","pyfk","nubf","nautu","h","i","ar","m","a","upbbm","zlmtm","lz","yjia","wze","cjqh","ut","onws","zdlv","wx","vma","ol","cfl","j","htmn","w","f","mdaub","ut","gyqdc","od","yi","tn","xwxh","w","ny","dxis","alhj","dyjq","xrk","kt","xu","ud","ah","am","mcvw","j","bn","jvvk","fc","crc","ubmes","ixf","vzx","rbu","bx","cvif","yif","nb","rb","p","e","wko","pqw","rb","kw","dohos","oxbu","x","swto","yhhz","ci","kvmr","wa","jf","igi","b","rfvik","fs","oz","y","xba","ytobn","ff","drrut","t","p","uij","i","f","boap","oaag","qril","sxor","abwtp","wknu","ix","nmdt","mwran","w","y","owgp","oa","isy","fqran","v","h","lbbbv","fh","bazq","cdqg","iz","yjlyl","sgxj","wjytc","p","mfhn","pdaa","hflf","gg","te","spjp","w","yfgnx","p","lznn","crdvl","mwibr","ggq","i","wunt","nzqp","dd","qpio","ewyy","uqskd","awble","vijg","m","v","ry","irg","yw","rdyk","vdmu","vu","t","c","ac","s","jtse","v","rvfu","e","gna","z","c","swzsy","p","pc","rek","gji","l","ge","bfbux","eh","nks","opq","jso","rmc","opjf","rpyfp","gpvj","jjry","z","yn","gr","et","mftd","m","xrouc","do","yt","geunr","gvitv","szil","f","xttfy","b","ovwbj","h","jix","zg","zs","nnxev","eq","xra","hrby","ylp","czl","fx","ygo","hvzu","nf","vleo","xq","fgua","mhmaj","ysdx","i","xn","gbvbt","kcqi","fccz","jka","eei","nopb","qv","pvorb","g","sgjb","ffwjl","d","ldsd","qmsh","wd","zz","t","qhre","r","ghbs","r","jilcp","tfz","kd","kvog","wi","ybdu","ceo","qeue","be","t","sekeh","ph","yj","swt","vexey","udb","v","x","wy","pf","seuz","ebse","g","rlhbz","p","nfej","rpv","kbje","bbxk","uvnh","nwy","x","ripe","u","tvfml","nql","i","xbtm","w","i","jq","bgjd","osc","tzut","f","xfer","vhusd","dz","mikxe","e","bj","iu","jfjwe","jmv","av","qb","zh","v","lo","lttw","cey","lob","jrlr","hxx","umog","yh","hrdsb","ihax","mfde","kxyu","kc","ssbk","tn","xmz","hpib","am","dvmd","l","lzug","kewq","mfz","gta","ac","m","ds","undj","ynwt","qbr","a","bg","opeti","cbfe","wgoi","gv","iipuo","s","d","cwefs","re","wn","oylg","ehiyg","wwtf","lceat","ialm","xmrxk","qhnh","mouw","peeb","fhu","ralu","k","iouzo","qp","uznab","puyku","uoqe","ych","sc","tlwon","acb","xf","ca","wnqa","um","sbwb","sf","tx","x","dmuj","tc","iby","elj","cuib","tfz","hn","joj","iiqm","ox","dpa","bkrtq","isfc","radjn","wrfuf","kyz","kv","ct","v","axjxb","yt","ohti","io","lewot","wfy","vxb","ijnkw","sluzh","akn","olw","pmf","zca","cv","iitz","xv","o","uii","otcf","zkly","qy","u","rpd","bqlzy","kqz","gept","wurp","gpgx","nj","rz","kyavq","ago","pn","sy","wwpl","k","x","jnr","hnpuv","d","fw","m","qldrq","ntzs","eubps","beuw","rh","t","rwtyp","aivvc","guuuw","fii","qmww","icb","uoa","elwzv","woqij","qtuo","ibsah","ne","trc","jai","v","y","tgpy","huhjx","lu","pvd","irm","iut","mx","aoj","rymh","z","p","mygan","x","xr","bwgu","gnvz","cvol","utnuw","wl","liajp","oadnh","b","y","epv","qczgn","cbi","wtxwb","tg","djjy","nray","sfe","zl","ubk","tzlqt","td","nqqp","kejk","ld","ligej","erih","aj","lcgw","d","lwx","teedd","wrwlh","q","tqzkt","bf","bkj","okgac","f","df","kbimx","jf","s","hkopr","kb","hhud","awxk","xgyc","jso","cotyr","vhoya","x","x","b","yot","tozra","hj","dgq","seexd","d","nlo","o","odbt","cgdhl","nbk","ngfm","s","qbbld","xov","sw","fqc","vfwrb","gba","owrf","enrfi","ipr","ntteh","iu","wzrx","youv","acqq","hchhp","cggns","xs","vilr","lnc","obnr","p","fkkeq","thvih","ol","jq","w","ido","onn","zzao","yzsq","bvhjh","pqae","q","ni","vf","dztl","um","obq","dib","l","d","ksi","lja","qzdp","v","bam","bfulk","e","avks","wawx","z","en","yygo","otmj","b","pyrc","rh","xo","osf","drg","cg","zr","irdkf","cw","a","goqlq","kz","ci","i","hqi","uqhu","x","gw","mlczv","pf","m","qc","r","jtjg","ph","pnwq","tng","b","bct","qwi","kwreq","hk","gxf","yh","xajwe","nirc","dgwz","tq","d","coda","yw","eqows","cxk","pqs","lwxvs","xc","oanm","kf","f","jwaq","dtlw","z","sd","z","ibtb","icqqk","ai","neq","ajjb","uk","fwvi","qws","pnmt","r","rr","ot","btuph","t","uzd","y","qzi","mr","bhnub","c","njapp","h","uavu","jitl","a","vu","m","ar","jaab","doqbt","j","si","wnwfr","ikjs","vtqxj","rh","dp","le","tuyaa","xvoh","tfvfy","rept","k","xgb","bgh","rfse","ev","fzsyv","s","pmj","lgji","m","dhzeg","hr","cwg","jzbts","x","hscu","l","v","qsviy","cbwmw","sus","qx","cd","lzswf","yrebo","kxiji","yzttg","rw","dcutm","q","zc","ls","ypyyx","j","uby","cxi","giz","c","k","mmtsa","rwljp","p","cqyd","gjn","x","z","vxk","da","ewyo","wldqn","x","j","nmth","rcmp","eifm","efakn","hm","k","c","m","bqd","cvz","ob","mbw","zlh","bygh","pobp","bppz","gvbxr","wc","v","wqm","ku","tipun","xlyd","gygp","zg"], 766))



# Count common words with one occurenece leetcode


# from collections import Counter

# def oneOccurence(word1, word2):
#     freq_wrd1 = Counter(word1)
#     freq_wrd2 = Counter(word2)

#     res = int()

#     for key in freq_wrd1:
#         if key in freq_wrd2 and freq_wrd2[key] == 1 and freq_wrd1[key] == 1:
#                 res += 1
#     return res

# print(oneOccurence(["leetcode","is","amazing","as","is"], ["amazing","leetcode","is"]))



# Intersection of two arrays leetcode

# def intersectionArray(array1, array2):
#     array1[:] = set(array1)
#     array2[:] = set(array2)

#     res = list()

#     if len(array1) < len(array2):
#         for i in array1:
#             if i in array2:
#                 res.append(i)
#     else:
#         for i in array2:
#             if i in array1:
#                 res.append(i)

#     return res


# print(intersectionArray([1,2,2,1], [2,2]))


# Valid Palindrome II LeetCode

# def validPalindrome(string):
#     l = 0
#     h = len(string) - 1 
#     res = str()
#     while l <= h:
#         if string[l] != string[h]:
#             return isPalindrome(string[l:h]) or isPalindrome(string[l+1:h+1])
#         l += 1
#         h -= 1
#     return True

# def isPalindrome(word):
#     return word == word[::-1]

# print(validPalindrome('abc'))


# Determine if string havles are alike/same leetcode

# def havlesAreAlike(string):
#     s = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
#     mid = len(string) // 2
#     first = [x for x in string[mid:] if x in s]
#     second = [x for x in string[:mid] if x in s]
#     return len(first) == len(second)
#     # frst_half = string[mid:]    
#     # sec_half = string[:mid]
#     # count_first = 0
#     # count_second = 0

#     # for i in  frst_half:
#     #     if i in s:
#     #         count_first += 1
    
#     # for x in sec_half:
#     #     if x in s:
#     #         count_second += 1

#     # return count_first == count_second


# print(havlesAreAlike('book'))


# Most Common word leecode

# import re

# from collections import Counter

# def mostCommon(string, ban):
#     string = re.sub(r"[^a-zA-Z]", ' ', string).lower()
#     freq = Counter(string.split())
#     if ban in freq:
#         freq.pop(ban)
#         # print(dir(freq))
#     # return freq.get(max(freq.values))
#     return max(freq, key=freq.get)

# print(mostCommon('Bob hit a ball, the hit BALL flew far after it was hit.', 'hit'))



# Remove one element to make the array strickly increasing LeetCode

# import math

# def isIncreasing(numArray):
#     prev = 00
#     flag = False
#     nums = [math.inf]

#     i, n = 0, len(numArray) - 1

#     while i < n:
#         if prev < numArray[i] < numArray[i+1]:
#             prev = numArray[i]
#         else:
#             if flag:
#                 return False
#             flag = True
#             if numArray[i+1] <= prev:
#                 prev = numArray[i]
#                 i+=1
#         i += 1

#     return True

# import math

# def isIncreasing(numArray):
#     prev = 00
#     flag = False
#     nums = [math.inf]

#     i, n = 0, len(numArray) - 1

#     while i < n:
#         if prev < numArray[i] < numArray[i+1]:
#             prev = numArray[i]
#         else:
#             if flag:
#                 return False
#             flag = True
#             if numArray[i+1] <= prev:
#                 prev = numArray[i]
#                 i+=1
#         i += 1

#     return True


# Not solve

# print(isIncreasing([1,2,10,5,7]))
# print(isIncreasing([2,3,1,2]))
# print(isIncreasing([105,924,32,968]))
# print(isIncreasing([1,1,1]))


# Longest Palindromic substring LeetCode

# def longestSubstring(string):
#     res = str()
#     if string == string[::-1]:
#         return string

#     for i in range(len(string)):
#         for x in range(1, len(string)+1):
#             if string[i:x] == string[i:x][::-1] and len(string[i:x]) >= len(res):
#                 res = string[i:x]

#     return res

# Not solved, solved but its not optimized

# print(longestSubstring('babad'))
# print(longestSubstring('cbbd'))


# Delete Character to make string fancy LeetCode

# def makeFancyString(string):
#     t = str()
#     ct = 1
#     ans = str()
#     for i in string:
#         if i == t:
#             ct += 1
#         else:
#             ct = 1

#         if ct <= 2:
#             ans += i
#         t = i
#     return ans

# print(makeFancyString('leeetcode'))



# Largest pair sum in array CodeWars
# def largePair(numArr):
#     numArr.sort()

#     return numArr[-1] + numArr[-2]


# print(largePair([10, 14, 2, 23, 19]))
# print(largePair([1,2,3,4,6,-1,2]))
# print(largePair([99, 2, 2, 23, 19]))
# print(largePair([-10, -8, -16, -18, -19]))


# simple remove duplicates codewars

# def remove(numArr):
#     re = []

#     for i in numArr[::-1]:
#         if i not in re:
#             re.append(i)

#     return re

# print(remove([3, 4, 4, 3, 6, 3]))


# check same case Codewars

# def sameCheck(word1, word2):
#     if word1.isupper() and word1.isalpha() and word2.isupper() and word2.isalpha():
#         return 1
#     if word1.isupper() and word1.isalpha() or word2.isupper() and word2.isalpha():
#         return 0
#     else:
#         return -1

# print(sameCheck('C', 'B'))
# print(sameCheck('b', 'a'))
# print(sameCheck('C', 'b'))


# Identicals elements codewars

# from collections import Counter

# def identicalCheck(word1, word2):
#     if not word1 or not word2:
#         return False
#     freq = Counter(word2)

#     for i in word1:
#         if i in freq:
#             return True

#     return False


# print(identicalCheck([9, 8, 7], [1, 6, 7, 8, 9]))


# First Duplicate codesignal

# def firstDupli(numArr):
#     seen = set()

#     for i in numArr:
#         if i in seen:
#             return i
#         else:
#             seen.add(i)

#     return -1


# print(firstDupli([2, 1, 3, 5, 3, 2]))


# firstNoneRepeating codesignal

# def firstNone(string):
#     hashMap = dict()
#     for i in string:
#         if ord(i) in hashMap:
#             hashMap[ord(i)] += 1
#         else:
#             hashMap[ord(i)] = 1
    
#     for key in hashMap:
#         if hashMap[key] == 1:
#             return chr(key)

#     return '_'


# print(firstNone('abacabad'))
# print(firstNone('abcdefghijklmnopqrstuvwxyziflskecznslkjfabe'))



# RotateImage CodeSignal

# def rotateImage(matrix):
#     matrix.reverse()

#     for i in range(len(matrix)):
#         for j in range(i):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#     return matrix


# print(rotateImage( [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]))


# Factorial Count CodeWars
# from math import floor, log10

# def factorialCount(num):
#     if num < 0:
#         return 0
    
#     if num <= 1:
#         return 1

    
#     digit = 0

#     for i in range(2, num+1):
#         digit += log10(i)

#     return floor(digit) + 1

# print(factorialCount(5))



# isCryptSolution CodeSignal

# def isCrypt(crypt, solution):
#     a = crypt[0]
#     b = crypt[1]
#     c = crypt[2]
#     chr_dict = dict()

#     for i in solution:
#         chr_dict[i[0]] = int(i[1])

#     has_zero = False
#     if chr_dict[a[0]] == 0 or chr_dict[b[0]] == 0 or chr_dict[c[0]] == 0:
#         has_zero = True

#     n1 = ''.join(str(chr_dict[x]) for x in a)
#     n2 = ''.join(str(chr_dict[x]) for x in b)
#     n3 = ''.join(str(chr_dict[x]) for x in c)

#     if int(n1) + int(n2) == int(n3):
#         if has_zero and int(n3) == 0 and len(n3) == len(str(int(n3))):
#             return True

#         elif has_zero:
#             return False

#         else:
#             return True
#     else:
#         return False



# print(isCrypt(["SEND", "MORE", "MONEY"], 
#             [['O', '0'],
#             ['M', '1'],
#             ['Y', '2'],
#             ['E', '5'],
#             ['N', '6'],
#             ['D', '7'],
#             ['R', '8'],
#             ['S', '9']]))


# remove kth element from the linkedList codeSignal

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:

#     def __init__(self):
#         self.head = None

    
#     def add(self, data):
#         newNode  = Node(data)
#         if self.head:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = newNode
#         else:
#             self.head = newNode

        
#     def printNode(self):
#         current = self.head
#         l = str()
#         while current != None:
#             l+=(str(current.data)+ '--->')
#             current = current.next
#         return l 

    
#     def delete(self, data):
#         current = self.head
#         prev = None
#         while current != None:
#             if current.data == data:
#                 prev.next = current.next
#                 current = prev
#             else:
#                 prev = current
#             current = current.next
#         s = str()
#         current = self.head
#         while current != None:
#             s += str(current.data) + '--->'
#             current = current.next

#         return s

# obj = LinkedList()
# for i in range(1, 10):
#     obj.add(i)
# print(obj.printNode())
# print(obj.delete(3))


# def rotateImage(matrix):
#     matrix.reverse()

#     for i in range(len(matrix)):
#         for j in range(i):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#     return matrix


# print(rotateImage( [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]))



# Integer Replacement LeetCode


# def integerReplacement(num, count=0):
#     if num == 1:
#         return count
#     if num % 2 == 0:
#         return integerReplacement(num//2, count+1)
#     if num % 2 != 0 and num + 1 % 4 == 1:
#         return integerReplacement(num-1, count+1)
#     if num % 2 != 0 and num - 1 % 4 == 0:
#         return integerReplacement(num+1, count+1)

#     # count = 0

#     # while num > 1:
#     #     if num % 2 == 0:
#     #         num //= 2
        
#     #     elif num == 3 or num % 4 == 0:
#     #         num -= 1
#     #     else:
#     #         num += 1

#     #     count += 1
    
#     # return count

# # print(integerReplacement(65535))
# x = [8,3,65535,1234]

# for i in x:
#     print(integerReplacement(i))



# count number with unique digits leetcode

# def countUniqueDigit(num):
#     choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#     res = 1
#     ans = 1
#     for i in range(num if num <= 10 else 10):
#         ans *= choices[i]
#         res += ans
#     return res

# print(countUniqueDigit(2))


# Fibonacci numbers leetcode

# def fib(n):
#     # if n == 0:
#     #     return 0
#     # if n == 1:
#     #     return 1
#     # return fib(n-1) + fib(n-2)

#     arr = [0, 1]

#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     for i in range(n):
#         arr.append(arr[-1] + arr[-2])

#     return arr[-2]

# print(fib(3))



# Merge Sorted Array LeetCode
 
# def merge(num1, num2, n, m):
#     num1 = num1[:m] + num2[:n]

#     return sorted(num1)

# print(merge([1,2,3,0,0,0], [2,3,4], 3, 3))


# Counting Bits leetCode

# def countingBits(num):
#     ans = list()

#     for i in range(num+1):
#         ans.append(bin(i)[2:].count('1'))

#     return ans

# print(countingBits(2))




# Reverse Bits LeetCode

# def reverseBits(num):
#     res = 0
#     pos = 31
#     while pos >= 0:
#         if num&(1<<(31-pos)):
#             res = res | 1<<pos
#         pos -=1
#     return res



# print(reverseBits(43261596))
# print(reverseBits('00000010100101000001111010011100'))
# print(reverseBits('11111111111111111111111111111101'))


# Maximun product of three numbers LeetCode

# def maxNum(arrNum):
#     arrNum.sort()
#     l = arrNum[0] * arrNum[1] * arrNum[-1]
#     r = arrNum[-1] * arrNum[-2] * arrNum[-3]
#     return max(l, r)

# print(maxNum([1,2,3]))
# print(maxNum([-100,-98,-1,2,3,4]))


# Element Appearing more than 25% in the sorted array

# from collections import Counter 

# def sortedArray(arrayList):
#     freq = Counter(arrayList)
#     for key, value in freq.items():
#         if value > len(arrayList) * 0.25:
#             return key

# print(sortedArray([1,2,2,6,6,6,6,7,10]))
# print(sortedArray([1,1,1,1]))


# Remove one element to make the array strickly increasing Leetcode

# def strickIncreasing(nums):
#         prev = 0
#         flag = False
#         nums.append(math.inf)
#         i, n = 0, len(nums) - 1
#         while i < n:
#             if prev < nums[i] < nums[i+1]:
#                 prev = nums[i]
#             else:  # nums[i] or nums[i+1] should be removed
#                 if flag:
#                     return False
#                 flag = True
#                 if nums[i+1] <= prev:  # remove nums[i+1]
#                     print(prev)
#                     prev = nums[i]
#                     i += 1
#             i += 1
        
#         return True, nums

# print(strickIncreasing([1,2,3,10,5,7]))
# print(strickIncreasing([2,2,2,2,2]))
# print(strickIncreasing([105,924,32,968]))
# print(strickIncreasing([2,3,1,2]))




# Relative sort array LeetCode
# take arr1 and count the occurence of elements in it place it into a freq variable
# create a new_array
# loop through the arr2 with mapping the arr2[i] in freq and multiplying it with the value

# from collections import Counter

# def relativeSortArray(arr1, arr2):
#     freq = Counter(arr1)
#     new1, new2 = set(arr1), set(arr2)
#     arr3 = sorted(new1.difference(new2))
#     result = list()
#     print(arr3, freq)
#     for key in arr2:
#         result += [key] * freq[key]
    
#     for key in arr3:
#         result += [key] * freq[key]

#     return result

# # arr1 = [2,3,1,3,2,4,6,7,9,2,19]
# # arr2 = [2,1,4,3,9,6]

# # arr1 = [28,6,22,8,44,17]
# # arr2 = [22,28,8,6]

# arr1 = [2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31]
# arr2 = [2,42,38,0,43,21]

# print(relativeSortArray(arr1, arr2) == [2,42,38,0,43,21,5,7,12,12,13,23,24,24,27,29,30,31,33,48])



# Check if every row and column contains all numbers leetcode

# def check_valid(matrix):
    # *******************
    # Worked only for rows
    # size = len(matrix) 
    # matrix_n_size = len(matrix[0]) - 1
    # freq = dict()
    # l, r = 0, size
    # # print(matrix[l][matrix_n_size])

    # while l < r:
    #     # print(matrix[l][matrix_n_size], 'res')
    #     # print(matrix[0],matrix[0][matrix_n_size],'a')
        

    #     if matrix[l][matrix_n_size] in freq:
    #         freq[matrix[l][matrix_n_size]] += 1
    #         matrix_n_size -= 1
    #         # print(matrix[l][matrix_n_size])
    #     else:
    #         freq[matrix[l][matrix_n_size]] = 1
    #         matrix_n_size -= 1
    #     if matrix_n_size == -1:
    #         l+=1
    #         matrix_n_size = len(matrix[0]) - 1

    # return max(freq.values()) == min(freq.values()) == size
    # *******************


#     for row, col in zip(matrix, zip(*matrix)):
#         if len(set(row)) != len(matrix) or len(set(col)) != len(matrix):
#             return False
#         return True

# print(check_valid([[1,2,3],[3,1,2],[2,3,1]]))
# print(check_valid([[1,1,1],[1,2,3],[1,2,3]]))
# print(check_valid([[1,1,2], [1,2,3], [2,3,1]]))
# # print(check_valid([[15,7,18,11,19,10,14,16,8,2,3,6,5,1,17,12,9,4,13],[17,15,9,8,11,13,7,6,5,1,3,16,12,19,10,2,4,14,18],[19,14,12,10,8,9,17,16,4,3,13,18,1,5,7,11,2,15,6]]))
# # print(check_valid([[15,7,18,11,19,10,14,16,8,2,3,6,5,1,17,12,9,4,13],[17,15,9,8,11,13,7,6,5,1,3,16,12,19,10,2,4,14,18],[19,14,12,10,8,9,17,16,4,3,13,18,1,5,7,11,2,15,6],[4,2,10,15,19,16,8,9,5,3,1,11,13,14,6,18,12,17,7],[13,19,9,16,5,8,6,12,14,11,18,10,7,2,3,4,15,17,1],[4,7,18,11,17,16,5,12,10,1,15,13,14,6,19,2,3,9,8],[14,5,15,1,18,6,12,7,8,9,3,13,2,10,19,4,11,16,17],[10,3,1,8,14,19,11,18,15,13,9,12,16,17,7,4,5,2,6],[14,13,19,18,7,2,4,8,10,17,12,5,15,1,6,9,11,3,16],[19,8,10,18,16,12,11,17,4,9,7,2,5,13,15,3,6,1,14],[1,10,6,14,7,18,3,9,4,16,5,11,13,17,15,8,19,2,12],[13,10,5,16,1,19,17,3,9,11,7,8,12,6,4,2,14,15,18],[17,2,1,6,9,19,18,14,4,11,12,13,16,5,8,7,3,10,15],[1,4,10,5,13,6,18,11,3,2,15,14,16,12,17,19,8,9,7],[2,14,3,12,16,17,11,9,1,6,5,19,10,13,4,18,7,15,8],[15,9,8,18,14,13,4,12,5,17,6,1,11,16,19,3,7,2,10],[15,8,12,16,13,2,6,19,18,14,10,5,11,9,7,1,3,17,4],[15,6,17,7,5,3,1,9,19,12,10,11,16,14,18,8,2,13,4],[6,11,10,14,2,13,16,1,9,15,8,19,17,3,5,18,7,4,12]]))



# generate string with characters that have odd count_Leetcode

# def genChar(num):
#     return ''.join('a' * (num-1)+'z' if num % 2==0 else 'a' * num)

# print(genChar())


# Reverse a integer without converting them into a string
# 1132 == 2311
# -431 == -134

# def reverseInteger(num):
#     result, num_remainder = 0, abs(num)
#     while num_remainder:
#         result = result * 10 + num_remainder % 10
#         num_remainder //= 10 
#     return -result if num < 0 else result 

# print(reverseInteger(-123))


# Place even numbers first then the odd numbers without any other extra space
# Sort array by parity LeetCode


# def evenAndOddList(numArr):
#     next_even, next_odd = 0, len(numArr)-1

#     while next_even < next_odd:
#         if numArr[next_even] % 2 == 0:
#             next_even += 1
#         else:
#             numArr[next_even], numArr[next_odd] = numArr[next_odd], numArr[next_even]
#             next_odd -= 1
        
#     return numArr

# print(evenAndOddList([2, 5, 9, 6, 3, 4]))


# plus one LeetCode

# def plusOne(numArray):
#     numArray[-1] += 1
#     for i in reversed(range(1, len(numArray))):
#         if numArray[i] != 10:
#             break
#         numArray[i] = 0
#         numArray[i-1] += 1
    
#     if numArray[0] == 10:
#         numArray[0] = 1
#         numArray.append(0)
#     return numArray

# print(plusOne([9,9,9]))


# Delete Duplicates from sorted array

# def deleteDuplicates(arrList):
#     if not arrList:
#         return 0
    
#     write_next = 1
#     for i in range(1, len(arrList)):
#         if arrList[i-1] != arrList[i]:
#             arrList[write_next] = arrList[i]
#             write_next += 1
#     return arrList[:write_next]


# print(deleteDuplicates([1,2,3,4,4,5,5,6,6,7,7,8,8,9,9]))

# first missing postive Leetcode

# def firstMissing(numArr):
#     numArrSet = set(numArr)
#     for i in range(1, len(numArrSet)+2):
#         if i not in numArrSet:
#             return i

# print(firstMissing([1,3,4,5,6]))


# is palindromic string

# def is_plaindromic(string):
#     # return all(string[i] == string[~i] for i in range(len(string) // 2))
#     return all(string[i] == string[~i] for i in range(len(string)//2))


# print(is_plaindromic('raahaar'))


# majority element Leetcode

# [1,1,1,2,2,1]

# def majorityElement(numArr):
#     res, count = 0, 0
#     for n in numArr:
#         if count == 0:
#             res = n
#         count += 1 if n == res else -1
#     return res

# print(majorityElement([1,2,3,1]))


# Find the minimum in the rotated array algo-monster

# def findMin(arrList):
#     l, r, res= 0, len(arrList) - 1, -1
#     count = -1
#     while l <= r:
#         mid = (l+r) // 2
#         if arrList[mid] <= arrList[-1]:
#             count = mid
#             r -= 1
#         else:
#             l += 1
#     return count

# print(findMin([30, 40, 50, 10, 20]))


# Finding the peak element in the montain array AlgoMonster

# def findingPeakEle(arrList):
#     l, r = 0, len(arrList) - 1
#     while l <= r:
#         mid = (l+r) // 2
#         if mid == len(arrList)-1 or arrList[mid] >= arrList[mid+1]:
#             res = mid
#             r-=1
#         else:
#             l += 1
#     return res

# print(findingPeakEle([1,2,3,2,1]))



# is anagram leetcode

# def isAnagram(word1, word2):
#     # ==================
#     # first Approach
#     # word1_index = [0] * 26
#     # word2_index = [0] * 26

#     # if len(word1) != len(word2):
#     #     return False

#     # for i in range(len(word1)):
#     #     word1_index[i] = ord(word1[i].lower()) - ord('a')
#     #     word2_index[i] = ord(word2[i].lower()) - ord('a')

#     # flag = True
#     # for i in range(len(word1_index)):
#     #     if word1_index[i] != word2_index[i]:
#     #         return False
#     # return True
#     # ===================

#     hashMap_word1 = dict()
#     hashMap_word2 = dict()

#     if len(word1) != len(word2):
#         return False

#     word1, word2 = word1.lower(), word2.lower()

#     for i in range(len(word1)):
#         hashMap_word1[word1[i]] = 1 + hashMap_word1.get(word1[i], 0)
#         hashMap_word2[word2[i]] = 1 + hashMap_word2.get(word2[i], 0)

#     for key in hashMap_word1:
#         if hashMap_word1[key] != hashMap_word2.get(key, 0):
#             return False
#     return True


# l = []
# word1 = 'ABC'
# word2 = 'ABc'

# print(isAnagram(word1, word2))



# add string leetcode

# def addString(num1, num2):
#     int_num1, int_num2 = 0, 0
#     for i in num1:
#         int_num1 = int_num1 * 10 + ord(i) - 48
#     for i in num2:
#         int_num2 = int_num2 * 10 + ord(i) - 48
#     return int_num1 + int_num2

# print(addString('11', '123'))


# Remove duplicates from sorted array II leetcode

# def removeDuplicates(nums):
#     c=1
#     x=0
#     i, l = 0, len(nums) - 1
#     while i < l:
#         if nums[i]!=nums[i-1]:
#             c=1
#         elif nums[i]==nums[i-1] and c<2:
#             c+=1
#         elif c>=2 and nums[i]==nums[i-1]:
#             nums.pop(i)
#             l -= 1
#             x+=1
#         else:
#             c=0
#         i += 1
#     for i in range(x):
#         nums.pop(0)
#     return nums

# print(removeDuplicates([1,1,1,2,2,3]))

# # print(removeDuplicates([0,0,1,1,1,1,2,3,3]))


# Sum of two CodeSignal

# def sumOfTwo(numarr1, numarr2, target):
#     setB = set(numarr2)
#     for i in numarr1:
#         if abs(target - i) in setB:
#             return True
#     return False

# print(sumOfTwo([1,2,3,4], [10,20,30,40], 42))


# amend the sentence codesignal

# def amendSen(string):
#     res = string[0].lower()
#     for i in range(1, len(string)):
#         if string[i].isupper():
#             res += ' ' + string[i].lower() 
#         else:
#             res += string[i].lower()
#     return res

# print(amendSen('ArshErgonAli'))


# strstr codesignal

# def strstr(string, target):
#     len1 = len(string)
#     len2 = len(target)
#     if len1 < len2:
#         return -1
#     for i in range(len1-len2+1):
#         if string[i:i+len2] == target:
#             return i
#     return -1
        
# print(strstr('arsh', 'sh'))


# Amazon online assessment Algomonster

# Two Sum unique pairs

# def twoSumUnique(arrNum, target):
#     seen = set()
#     complement = set()
#     for num in arrNum:
#         if target - num in complement:
#             pairs = (num, target-num) if num < target - num else (target-num, num)
#             seen.add(pairs)
#         complement.add(num)
#     return len(seen)

# print(twoSumUnique([1, 1, 2, 45, 46, 46], 48))


# Best time to buy and sell stocks leetcode

# def bestTime(arrList):
#     l, r = 0, 1
#     maxP = 0
#     while r < len(arrList):
#         if arrList[l] < arrList[r]:
#             profit = arrList[r] - arrList[l]
#             maxP = max(maxP, profit)
#         else:
#             l = r
#         r += 1
#     return maxP

# print(bestTime([7,1,5,3,6,4]))


# longest substring length leetcode

# def longestSubstring(string):
#     hashSet = set()
#     l, res = 0, 0
#     for r in range(len(string)):
#         while string[r] in hashSet:
#             hashSet.remove(string[l])
#             l += 1
#         hashSet.add(string[r])
#         res = max(res, r - l + 1)
#     return res

# print(longestSubstring('pwwkew'))


# Minimum distance to the target element leetcode

# def minimumDistance(nums, target, start):
    # if nums[start] == target:
    #         return 0
    # i = start
    # j = start
    
    # while i < len(nums) or j > 0 :
    #     if nums[i] == target :
            
    #         return abs(i - start)
    #     if nums[j] == target:
    #         return abs(start - j)
    #     if i != len(nums) - 1:
    #         i += 1
    #     if j != 0 :
    #         j -= 1

    # return
    
# nums = [3633,7175,8124,9059,3819,5664,3783,3585,7531]
# target = 3819
# start = 0

# nums = [5,8,7]
# target= 5
# start = 2

# print(minimumDistance(nums, target, start))



# Check if one string swap can make string equal leetcode

# def stringSwap(string1, string2):
#     if string1 == string2:return True
#     count = 0;seen = list()
#     if sorted(string1) != sorted(string2):
#         return False
#     for i in range(len(string1)):
#         if string1[i] != string2[i]:
#             seen.append(string1[i]); seen.append(string2[i])
#             count += 1
#         if count > 2: return False
#     return len(set(seen)) == 2

# print(stringSwap('aa', 'ac'))


# Merge two sorted array into one leetcode

# def mergeTwo(arr1, arr2):
#     temp_arr = list()
#     for i in arr1:
#         if i != 0:
#             temp_arr.append(i)
#     for i in arr2:
#         temp_arr.append(i)
    
#     temp_arr.sort()

#     for i in range(len(temp_arr)):
#         arr1[i] = temp_arr[i]
    
#     return arr1


# print(mergeTwo([1,2,3,0,0,0], [2,5,6]))

# def isAnagram(word1, word2):

# def mergeTwo(arr1, arr2):
#     temp_arr = list()
#     for i in arr1:
#         if i != 0:
#             temp_arr.append(i)
#     for i in arr2:
#         temp_arr.append(i)
    
#     temp_arr.sort()

#     for i in range(len(temp_arr)):
#         arr1[i] = temp_arr[i]
    
#     return arr1


# print(mergeTwo([1,2,3,0,0,0], [2,5,6]))

# def isAnagram(word1, word2):
    # ==================
    # first Approach
    # word1_index = [0] * 26
    # word2_index = [0] * 26

    # if len(word1) != len(word2):
    #     return False

    # for i in range(len(word1)):
    #     word1_index[i] = ord(word1[i].lower()) - ord('a')
    #     word2_index[i] = ord(word2[i].lower()) - ord('a')

    # flag = True
    # for i in range(len(word1_index)):
    #     if word1_index[i] != word2_index[i]:
    #         return False
    # return True
    # ===================

#     hashMap_word1 = dict()
#     hashMap_word2 = dict()

#     if len(word1) != len(word2):
#         return False

#     word1, word2 = word1.lower(), word2.lower()

#     for i in range(len(word1)):
#         hashMap_word1[word1[i]] = 1 + hashMap_word1.get(word1[i], 0)
#         hashMap_word2[word2[i]] = 1 + hashMap_word2.get(word2[i], 0)

#     for key in hashMap_word1:
#         if hashMap_word1[key] != hashMap_word2.get(key, 0):
#             return False
#     return True


# l = []
# word1 = 'ABC'
# word2 = 'ABc'

# print(isAnagram(word1, word2))


# Capitalize the title LeetCode

# def capitalizeTitle(string):
#     listString = string.split()
#     res = listString[0].title() + ' ' if len(listString[0]) not in [1, 2] else listString[0].lower() + ' '
#     for i in range(1, len(listString)):
#         if len(listString[i]) not in [1, 2]:
#             res += listString[i].title() + ' '
#         else:
#             res += listString[i].lower()
#     return res

# print(capitalizeTitle('arsh ergon ali al'))
# print(capitalizeTitle('aaa'))
#     hashMap_word1 = dict()
#     hashMap_word2 = dict()

#     if len(word1) != len(word2):
#         return False

#     word1, word2 = word1.lower(), word2.lower()

#     for i in range(len(word1)):
#         hashMap_word1[word1[i]] = 1 + hashMap_word1.get(word1[i], 0)
#         hashMap_word2[word2[i]] = 1 + hashMap_word2.get(word2[i], 0)

#     for key in hashMap_word1:
#         if hashMap_word1[key] != hashMap_word2.get(key, 0):
#             return False
#     return True


# l = []
# word1 = 'ABC'
# word2 = 'ABc'

# print(isAnagram(word1, word2))



# Find all lonely numbers in an array LeetCode

# def lonelyNum(arrList):
#     res = list()
#     hashMap = dict()
#     for i in arrList:
#         hashMap[i] = 1 + hashMap.get(i, 0)
    
#     for key in hashMap:
#         if hashMap[key] == 1 and not key+1 in hashMap and not key-1  in hashMap:
#             res.append(key)

#     return res

# print(lonelyNum([10,6,5,8]))


# Longest Substring Of All Vowels in Order Leetcode

# def longestVowelSub(string):
    # ans = 0
    # cnt, unique = 1, 1
    # for i in range(1, len(string)): 
    #     if string[i-1] <= string[i]: 
    #         cnt += 1
    #         if string[i-1] < string[i]: 
    #             unique += 1
    #     else: 
    #         cnt = unique = 1
    #     if unique == 5: 
    #         ans = max(ans, cnt)
    # return ans 
#     stack = list(string)
#     prev = stack[0]
#     unique, count = 1, 1
#     maxP = 0
#     for i in range(len(stack)):
#         ele = stack.pop(0)
#         stack.append(0)
#         if ele >= prev:
        
#             count += 1
#             if ele > prev:
#                 unique += 1
#         else:
#             count,unique =1, 1
#         if unique == 5:
#             maxP = max(maxP, count)
#         prev = ele
#     return maxP

# print(longestVowelSub('aeeeiiiioooauuuaeiou'))
# print(longestVowelSub('aeiaaioaaaaeiiiiouuuooaauuaeiu'))


# Pascal triangle

# def pascalTriangle(n):
#     pascal = [[1] * (n+1) for i in range(n)]
#     for i in range(n):
#         for j in range(1, i):
#             pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j] 
#     for x in pascal:
#         print(x)

# print(pascalTriangle(6))


# Implement stack using queues

# class Stack:
#     def __init__(self):
#         self.queues = []

#     def push(self, data):
#         self.queues.append(data)

#     def poping(self):
#         return self.queues.pop()
    
#     def isEmpty(self):
#         return len(self.question) == 0

# obj = Stack()
# for x in range(10):
#     print(obj.push(x))

# print(obj.poping())


# Binary tree inorder traversal, preOrder, postOrder leetcode

# class Tree:
#     def __init__(self, data):
#         self.data = data
#         self.left_child = None
#         self.right_child = None

#     def insert(self, data):
#         newNode = Tree(data)
#         if self.data:
#             if self.data > data:
#                 if self.left_child is None:
#                     self.left_child = newNode
#                 else:
#                     self.left_child.insert(data)
#             else:
#                 if self.right_child is None:
#                     self.right_child = newNode
#                 else:
#                     self.right_child.insert(data)
#         else:
#             self.data = data

#     def inOrder(self, root):
#         if root:
#             self.inOrder(root.left_child)
#             print(root.data)
#             self.inOrder(root.right_child)
#         else:
#             return "Root is empty"
    
#     def preOrder(self, root):
#         if root:
#             print(root.data)
#             self.preOrder(root.left_child)
#             self.preOrder(root.left_child)
#         else:
#             print("root is empty")


#     def postOrder(self, root):
#         if root:
#             self.postOrder(root.left_child)
#             self.postOrder(root.right_child)
#             print(root.data)
#         else:
#             print("root is empty")

# root = Tree(10)
# for x in range(1, 21):
#     (root.insert(x))

# print(root.inOrder(root))
# print(root.preOrder(root))
# print(root.postOrder(root))



# kth smallest element in a bst LeetCode

# class BinaryTree:
#     def __init__(self, data):
#         self.data = data
#         self.left_child = None
#         self.right_child = None
    
#     def insert(self, data):
#         newNode = BinaryTree(data)
#         if self.data:
#             if self.data > data:
#                 if self.left_child is None:
#                     self.left_child = newNode
#                 else:
#                     self.left_child.insert(data)
#             else:
#                 if self.right_child is None:
#                     self.right_child = newNode
#                 else:
#                     self.right_child.insert(data)
#         else:
#             self.data = data

    
#     def inOrder(self, res, root):
#         if root:
#             self.inOrder(res, root.left_child)
#             res.append(root.data)
#             self.inOrder(res, root.right_child)
#         return res

#     def findingTheKth(self, root, k):
#         res = list()
#         self.inOrder(res, root)
#         return res[k - 1]


# root = BinaryTree(10)

# for x in range(1, 30):
#     root.insert(x)

# print(root.findingTheKth(root, 3))



# Second minimum node in a BST LeetCode

# class BinaryTree:
#     def __init__(self, data):
#         self.root = data
#         self.right_child = None
#         self.left_child = None 
    
#     def insert(self, data):
#         newNode  = BinaryTree(data)
#         if self.root:
#             if self.root > data:
#                 if self.left_child is None:
#                     self.left_child = newNode
#                 else:
#                     self.left_child.insert(data)
#             else:
#                 if self.right_child is None:
#                     self.right_child = newNode
#                 else:
#                     self.right_child.insert(data)
#         else:
#             self.root = data

    
#     def preOrder(self, root, res):
#         if root:
#             res.add(root.root)
#             self.preOrder(root.left_child, res)
#             self.preOrder(root.right_child, res)

#         return res
    
#     def findingMin(self, root):
#         res = set()
#         self.preOrder(root, res)
#         List = sorted(res)
#         return List[1] if len(res) >= 2 else -1 

# root = BinaryTree(30)
# for x in range(1, 29):
#     root.insert(x)

# print(root.findingMin(root))


# Maximum Depth of a binary tree
# class BinaryTree:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

#     def insertation(self, data):
#         newNode = BinaryTree(data)
#         if self.data:
#             if self.data < data:
#                 if self.left is None:
#                     self.left = newNode
#                 else:
#                     self.left.insertation(data)
#             else:
#                 if self.right is None:
#                     self.right = newNode
#                 else:
#                     self.right.insertation(data)

#         else:
#             self.data = data

    
#     def depthMax(self, root):
#         if not root: return 0
#         # return max(self.depthMax(root.left), self.depthMax(root.right)) + 1
#         queue = [root]
#         level = 0
#         while queue:
#             for x in range(len(queue)):
#                 node = queue.pop(0)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
            
#             level += 1
#         return level

# root = BinaryTree(10)

# for x in range(1, 40):
#     root.insertation(x)

# print(root.depthMax(root))


# search a sorted array for its entry equal to its index

# The most brute force would be looping all the elements and checking if that is equals to its index
# But since array is sorted, we must use binary search for that
# O(N) memory: O(1)

# class Entry:
#     def finding_index_equals_number(self, listData):
#         for key, val in enumerate(listData):
#             if key == val:
#                 return key, val
#         return -1 
# obj = Entry()
# print(obj.finding_index_equals_number([9, 8, 7, 3, 5, 7]))

# Solution with binary search 
# O(logN) memory: O(1)

# class Entry:
#     def finding_index_equals_number(self, listData):
#         left, right = 0, len(listData)-1

#         while left <= right:
#             mid = (left+right) // 2
#             diff = listData[mid] - mid 
#             if diff == 0:
#                 return mid
#             elif diff > 0:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return -1 

# obj = Entry()

# print(obj.finding_index_equals_number([-2, 0, 2, 3, 5, 6]))


# search in a cyclic sorted array the minimum number
# Brute force
# O(N)

# class Cyclic:
#     def findingMin(self, data):
#         minNum = data[0]

#         for i in data:
#             if i < minNum:
#                 minNum = i

#         return minNum

# obj = Cyclic()

# print(obj.findingMin([378, 478, 550, 103, 203, 302]))


# Binary Search O(logN)
# class Cyclic:
#     def findingMin(self, data):
#         left, right = 0, len(data) - 1
#         while left < right:
#             mid = (left+right) // 2
#             if data[mid] > data[right]:
#                 left = mid + 1
#             else:
#                 right = mid 
#         return data[left]

# obj = Cyclic()

# print(obj.findingMin([378, 478, 550, 103, 203, 302]))



# Reorder listNode leetcode


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insertation(self, data):
#         newNode = Node(data)
#         if self.head:
#             cur = self.head
#             while cur.next:
#                 cur = cur.next
#             cur.next = newNode
#         else:
#             self.head = newNode
#         print(data)

    
#     def printShow(self):
#         if self.head:
#             cur = self.head
#             while cur:
#                 print(cur.data, end=' ')
#                 cur = cur.next
#         else:
#             return False

    
#     def looping(self):
#         res = list()
#         cur = self.head
#         print('loop')
#         while cur:
#             res.append(cur.data)
#             cur = cur.next
#         return self.orderList(res)

#     def orderList(self, res):
#         left, right = 0, len(res)-1
#         newList = [0] * len(res)
#         count = 0
#         for i in res:
#             newList[count] = i
#             count += 2
#             if count >= len(newList):
#                 break
#         count = 1 
#         res =  res[::-1]
#         for i in res:
#             if i not in newList:
#                 newList[count] = i
#                 count += 2
#             if count >= len(newList):
#                 break
#         return newList


# obj = LinkedList()
# for x in [1,1,1,1,1,2,1,3,1,1,1,3,3,3,3,2,2,3,2,1,2,1,2,2,2,3,1,3,2,2,1,3,2,1,1,3,3,3,1,2,1,3,1,1,3,1,2,1,1,3,3,3,3,2,3,3,3,3,2,2,1,3,2,2,3,3,1,1,3,1,3,3,2,2,3,3,1,3,1,1,3,2,3,3,2,2,1,1,2,1,1,2,2,1,3,1,1,3,3,2,1,2,2,3,1,2,3,1,3,2,1,2,1,3,1,3,3,3,1,2,3,1,3,2,3,1,1,1,3,2,2,2,1,3,1,1,2,2,2,1,1,1,1,2,1,2,1,2,3,3,3,2,1,1,3,1,1,2,3,3,2,3,1,2,1,1,1,2,1,1,2,1,2,2,2,2,3,1,3,2,1,1,2,3,1,3,1,1,2,2,3,1,1,1,3,1,3,1,1,2,3,2,3,2,1,2,1,1,1,3,1,2,2,3,3,1,3,1,2,3,3,1,2,1,1,3,1,2,2,3,1,2,3,3,2,2,2,1,1,3,1,2,3,2,2,3,3,2,3,2,1,3,3,1,2,2,2,2,1,3,2,1,1,2,1,1,1,1,2,3,3,1,1,2,1,1,1,3,2,3,3,1,2,1,3,3,2,1,3,2,1,3,1,2,2,3,3,2,3,1,3,1,1,3,3,1,3,3,2,2,3,2,3,2,2,2,3,2,2,3,3,3,1,1,2,2,3,3,3,1,3,3,2,2,2,1,3,3,2,2,3,2,1,2,3,1,2,1,3,1,3,1,1,3,3,2,2,1,1,2,2,1,3,2,3,3,1,1,2,1,2,1,1,1,1,1,3,3,2,2,3,2,1,1,1,2,2,2,1,1,1,3,3,1,1,2,2,1,1,2,3,3,2,3,3,2,1,1,3,1,2,3,2,2,2,3,3,1,1,3,3,2,1,1,3,2,3,2,1,3,2,2,1,2,2,2,1,1,3,3,2,2,3,3,1,1,1,1,1,3,1,2,3,3,1,3,3,2,3,2,3,3,3,3,3,3,2,1,3,2,2,3,1,1,3,3,2,2,3,1,2,1,3,1,2,1,2,1,3,2,1,3,3,2,2,2,2,2,1,3]:
#     obj.insertation(x)
# # print(obj.printShow())
# print(obj.looping())



# Permutation on String

# def permutateString(string1, string2):
#     l, count, length_ = 0, 1, len(string1)-1
#     sum_ord = sum(map(ord, string1))
#     for r in range(1, len(string2)):
#         word = string2[l:r]
#         print(word, count)
#         if count == length_:
#             count = 1
#             l = r-1
#             if sum(map(ord, word)) == sum_ord:
#                 return True

#         count += 1
#     return False


# string1 = 'abc'
# string2 = 'dbca'
# print(permutateString(string1, string2))


# Searching in BST leetcode

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insertation(self, data):
        newNode = TreeNode(data)
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = newNode
                else:
                    self.left.insertation(data)
            else:
                if self.right is None:
                    self.right = newNode
                else:
                    self.right.insertation(data)

        else:
            self.data = data

    def printAll(self, root, val, res):
        if not root: return 
        if root:
            if root.data == val:
                res.append(root.data)
                if root.left and root.right:
                    res.append(root.left.data)
                    res.append(root.right.data)
                if root.left and not root.right:
                    res.append(root.left.data)
                if root.right and not root.left:
                    res.append(root.right.data)
            self.printAll(root.left, val, res)
            self.printAll(root.right, val, res)
        return res


root = TreeNode(4)
for x in [2,7,1,3]:
    root.insertation(x)

print(root.printAll(root, 2, []))
