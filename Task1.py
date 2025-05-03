class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Додає елемент на початок списку
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Додає елемент у кінець списку (для формування відсортованих списків)
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортування вставками
    def insertion_sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    # Вставка вузла у відсортований список
    def sorted_insert(self, head_ref, new_node):
        if not head_ref or new_node.data < head_ref.data:
            new_node.next = head_ref
            return new_node
        current = head_ref
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return head_ref

    # Об'єднання двох відсортованих списків
    def merge_sorted_lists(self, l1, l2):
        dummy = Node(0)
        tail = dummy
        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

    # Вивід списку
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(None)

# Приклад використання
print("== Робота з одним списком ==")
linked_list = SinglyLinkedList()
linked_list.push(10)
linked_list.push(20)
linked_list.push(30)
print("Оригінальний список:")
linked_list.print_list()

linked_list.reverse()
print("Реверсований список:")
linked_list.print_list()

linked_list.insertion_sort()
print("Відсортований список:")
linked_list.print_list()

print("\n== Об'єднання двох відсортованих списків ==")
list1 = SinglyLinkedList()
list1.append(10)
list1.append(30)
list1.append(50)

list2 = SinglyLinkedList()
list2.append(20)
list2.append(40)
list2.append(60)

print("Список 1:")
list1.print_list()
print("Список 2:")
list2.print_list()

merged_list = SinglyLinkedList()
merged_list.head = merged_list.merge_sorted_lists(list1.head, list2.head)
print("Об'єднаний відсортований список:")
merged_list.print_list()
