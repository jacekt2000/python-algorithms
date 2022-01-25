from typing import Any


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self,):
        self.head = None
        self.tail = None

    def push(self, value: Any):
        nexte = Node(value)
        nexte.next = self.head
        self.head = nexte
        if self.tail:
            self.tail = self.head

    def append(self, value: Any):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def __str__(self):
        nnode = self.head
        x = " "
        while nnode.next:
            x += str(nnode.value) + " -> "
            nnode = nnode.next
        x += str(nnode.value)
        return x


    def node(self, at: int):
        cur_node = self.head
        result = 0
        while cur_node:
            if (at == result):
                return cur_node.value
            result += 1
            cur_node = cur_node.next

    def pop(self):
        node = self.head
        self.head = node.next
        return node

    def insert(self, value: Any, after: Node):
        if after is None:
            raise ValueError("nie ma ")
        nnode = Node(value)
        nnode.next = after.next
        after.next = nnode

    def remove_last(self):
        newnode = self.head
        while newnode.next.next:
            newnode = newnode.next
        newnode.next = None
        return newnode

    # def remove(self, after: Node):
    #     node = self.head
    #     if self.head is None:
    #         return
    #     if after == 0:
    #         self.head = node.next
    #         return
    #     if node is None:
    #         return
    #     if node.next is None:
    #         return
    #     next = node.next.next
    #     node.next = None

    def __len__(self):
        tmp = self.head
        sum = 0
        while tmp:
            tmp = tmp.next
            sum += 1
        return sum


class Lifo:

    def __init__(self):
        self.storage = LinkedList()

    def __len__(self):
        return len(self.storage)

    def __str__(self):
        stack = self.storage.head
        x = ""
        while stack.next:
            x += str(stack.value) + " -> "
            stack = stack.next
        x += str(stack.value)
        return x

    def push(self, element: Any) -> None:  # na szczycie stosu
        self.storage.append(element)

    def pop(self) -> Any:  # zwracam  i usuwa wartosc ze szczytu
        if len(self.storage) != 0:
            return self.storage.remove_last().value
        return self.storage.remove_last()


class Fifo:

    def __init__(self):
        self.storage = LinkedList()

    def __len__(self):
        return len(self.storage)

    def enqueue(self, element: Any) -> None:  # dodaje element
        self.storage.append(element)

    def dequeue(self) -> Any:  # usuwa element i zwraca
        if len(self.storage) != 0:
            return self.storage.remove_last().value

    def peek(self) -> Any: # zwraca tylko 1 element
        if len(self.storage) != 0:
            return self.storage.head.value

    def __str__(self):
        queue = self.storage.head
        x = " "
        while queue.next:
            x += str(queue.value) + " -> "
            queue = queue.next
        x += str(queue.value)
        return x

# List = LinkedList()
# List.push(5)
# List.push(4)
# List.push(3)
# List.push(2)
# List.push(1)
# List.append(5)
# List.append(9)
# List.append(10)
# print(List.__str__())
# print(List.node(6))
#
# List.insert(5,List.head.next.next)
# print(List.__str__())
#
# List.remove_last()
# print(List.__str__())
# List.pop()
# print(List.__str__())
# #List.remove(7) # srednio dziala


# stack = Lifo()
#
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# print(stack.__str__())
# print(stack.pop())
# print(stack.__str__())
# print(stack.__len__())
#
queue = Fifo()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.__str__())
print(queue.dequeue())
print(queue.__str__())
print(queue.__len__())
print(queue.peek()) 
