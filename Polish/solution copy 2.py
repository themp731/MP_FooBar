#This is code for the google FooBar Project I got

#Using stack class to implement polish calculator
class Stack:
	def __init__(self):
		self.items=[]

	def isEmpty(self):
		return self.items == []

	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

#Function assumes being passed a string
def answer(expression):
    #Dict for order of operations
    opord = {}
    opord["*"] = 3 
    opord["/"] = 3
    opord["+"] = 2
    opord["-"] = 2
    opord["("] = 1
    operator_stack = Stack()
    polish_list = []
    element_list = []
    #Normally runing a .split() should work
    #Check string methods in python 2.7 vs. 3.4
    for j in expression:
        element_list.append(j)
    for i in element_list:
        if i in "0123456789":
            polish_list.append(i)
        elif i == "(":
            operator_stack.push(i)
        elif i == ")":
            top = operator_stack.pop()
            while top != "(":
                polish_list.append(top)
                top = operator_stack.pop()
        else:
            while (not operator_stack.isEmpty()) and (opord[operator_stack.peek()] > opord[i]):
                polish_list.append(operator_stack.pop())
            operator_stack.push(i)
    while not operator_stack.isEmpty():
        polish_list.append(operator_stack.pop())
    return "".join(polish_list)
