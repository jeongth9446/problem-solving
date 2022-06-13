class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        if not self.last:
            return None
        k = self.last.item
        self.last = self.last.next
        return k

    def isEmpty(self):
        return self.last == None


class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        for item in list(s):
            if item == '(' or item == '{' or item == '[':
                stack.push(item)
            else:
                t = stack.pop()
                if (t == '(' and item == ')') or (t == '{' and item == '}') or (t == '[' and item == ']'):
                    continue
                else:
                    return False
        return stack.isEmpty()
