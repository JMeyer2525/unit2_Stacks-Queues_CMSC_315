"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Adding to the end means the most recently added item will be removed first.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek allows us to view the most recently added item without removing it.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New values are added to the back so the oldest value remains at the front.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front allows us to view the oldest value without removing it.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")

    stack = Stack()

    print("Adding 4 values to the stack:")
    for value in [10, 20, 30, 40]:
        stack.push(value)
        print(f"Added {value} to the stack.")

    print("\nDemonstrating LIFO behavior:")
    print(f"Top value before popping: {stack.peek()}")

    while not stack.is_empty():
        print(f"Popped: {stack.pop()}")

    print("\nTesting empty-stack behavior:")
    print(f"Pop from empty stack: {stack.pop()}")
    print(f"Peek at empty stack: {stack.peek()}")

    print("\nTesting a single-item stack:")
    single_stack = Stack()
    single_stack.push("Only Item")
    print(f"Added: {single_stack.peek()}")
    print(f"Removed: {single_stack.pop()}")
    print(f"Is the single-item stack empty? {single_stack.is_empty()}")


    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    queue = Queue()

    print("Adding 4 customers to the queue:")
    for customer in ["Customer 1", "Customer 2", "Customer 3", "Customer 4"]:
        queue.enqueue(customer)
        print(f"Added {customer} to the queue.")

    print("\nDemonstrating FIFO behavior:")
    print(f"First customer in line: {queue.front()}")

    while not queue.is_empty():
        print(f"Dequeued: {queue.dequeue()}")

    print("\nTesting empty-queue behavior:")
    print(f"Dequeue from empty queue: {queue.dequeue()}")
    print(f"Front of empty queue: {queue.front()}")

    print("\nTesting a single-item queue:")
    single_queue = Queue()
    single_queue.enqueue("Only Customer")
    print(f"Added: {single_queue.front()}")
    print(f"Removed: {single_queue.dequeue()}")
    print(f"Is the single-item queue empty? {single_queue.is_empty()}")


if __name__ == "__main__":
    main()
