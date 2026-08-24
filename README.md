# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

## Reflection Response

During this assignment, I learned how stacks and queues work and organize data. Stacks use Last in, First Out,
while queues use First in, First Out. I also learned how to use a Python list for a stack and a deque for queue. I
also tested functions like push, pop, peek, enqueue, and dequeue to help me understand how the structures worked.

One challenge I ran into was what should happen when I tried to remove or view something from an empty stack or
queue. I overcame this by adding a check with is_empty() before viewing or removing values. To verify structures,
I made sure they became empty after the item was removed. Running different tests helped me fix the issues.

Stacks and queues are different because they remove data in different orders. A stack is used when the most recent
item needs to be handled first, like taking plates out of your cabinet. A queue is more useful when things need to
be handled in the order they arrived, like at a checkout line in a market. This assignment helped me understand 
when each data structure is useful in the real world.