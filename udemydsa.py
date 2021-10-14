
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


