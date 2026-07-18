class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"{item} pushed into stack")

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Stack:", self.items)


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

print("Popped:", stack.pop())
print("Top element:", stack.peek())

stack.display()
