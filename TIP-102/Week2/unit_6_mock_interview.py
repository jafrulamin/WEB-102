class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def findMidIndex(head: Node):
    length = 0
    current = head
    while current != None:
        length += 1
        current = current.next
    # print(length)
    
    midIndex = length // 2
    # print(midIndex)

    current = head

    for _ in range(midIndex):
        current = current.next
    return current.value
def main():
    linked_list = Node(1,Node(2, Node(3, Node(4, Node(5)))))
    print(findMidIndex(linked_list))
    pass

if __name__ == "__main__":
    main()