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
    blocks.enqueue([str(i//2)]*file_map.dequeue())
    blocks.enqueue(['.']*(file_map.dequeue() or 0))

# smallest_fail = [100000000000]
last_checked = [0]*10
def find_space(size, max_index):
    # if size >= smallest_fail[0]:
    #     return None
    
    found = 0
    for i in range(last_checked[size], max_index + 1):
        if blocks.items[i] == '.':
            found += 1
            if found == size:
                last_checked[size] = i-size
                return i-size+1
        else:
            found = 0

    # smallest_fail[0] = size
    return None

visited = [1000000000]
def find_block():
    file_id = None
    size = 0
    end = min(visited[0], blocks.size())
    for i in range(end-1, -1, -1):
        if blocks.items[i] != '.':
            file_id = blocks.items[i]
            while True:
                size += 1
                i -= 1
                if blocks.items[i] != file_id:
                    visited[0] = i+1
                    return {'id':file_id, 'index':i+1, 'size':size}
    return None

final = blocks.items
# print(' '.join(final))
# recent = int(final[-1])
while True:
    file = find_block()
    if file is None:
        break
    space = find_space(file['size'], file['index'])
    if space is None:
        continue
    for i in range(file['size']):
        final[space+i] = file['id']
        final[file['index']+i] = '.'
    # if int(file['id']) < recent-500:
    #     print(file['id'])
    #     recent = int(file['id'])

    # print(' '.join(final))

print(sum([i*int(final[i]) for i in range(len(final)) if final[i] != '.']))