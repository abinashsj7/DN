class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"{item} added to queue")

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Queue:", self.items)


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.display()

print("Dequeued:", queue.dequeue())
print("Front element:", queue.front())

queue.display()
