from collections import  deque

queue = deque()
queue.append("Ali")
queue.append("Ayşe")
queue.append("Mehmet")

print(queue)

print(queue.popleft())
print(queue.popleft())
print(queue.popleft())