class deque:
    def __init__(self, items=[]):
        self.items = list(items)
    def empty(self):
        return self.items == []
    def push(self, item):
        if type(item) == list:
            for i in item:
                self.items.insert(0, i)
        else:
            self.items.insert(0, item)
    def enqueue(self, item):
        if type(item) == list:
            for i in item:
                self.items.append(i)
        else:
            self.items.append(item)
    def dequeue(self):
        if self.empty():
            return None
        return self.items.pop(0)
    def pop(self):
        if self.empty():
            return None
        return self.items.pop()
    def size(self):
        return len(self.items)
    
with open('input', 'r') as f:
    file_map = deque(map(int, f.readline()))

blocks = deque()

for i in range(0, file_map.size(), 2):
    # blocks.append([str(i/2)]*file_map.dequeue())
    # blocks.append(['.']*file_map.dequeue())
    blocks.enqueue([str(i//2)]*file_map.dequeue())
    blocks.enqueue(['.']*(file_map.dequeue() or 0))

# print(blocks.items)
final = []
while not blocks.empty():
    x = blocks.dequeue()
    if x == '.':
        while x == '.':
            x = blocks.pop()
            if not x: break
        else: final.append(int(x))
    else:
        final.append(int(x))

# print(''.join(map(str,final)))

print(sum(map(lambda x, i: x*i, final, range(len(final)))))