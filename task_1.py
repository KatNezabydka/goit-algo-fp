"""
Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_linked_list(head):
    """
    Reverse a Singly Linked List
    """
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def insertion_sort(head):
    """
    Sorting Algorithm for a Singly Linked List:
    """
    if not head or not head.next:
        return head
    sorted_head = None
    curr = head
    while curr:
        next_node = curr.next
        sorted_head = insert_node(sorted_head, curr)
        curr = next_node
    return sorted_head


def insert_node(sorted_head, node):
    if not sorted_head or node.value < sorted_head.value:
        node.next = sorted_head
        return node
    curr = sorted_head
    while curr.next and curr.next.value < node.value:
        curr = curr.next
    node.next = curr.next
    curr.next = node
    return sorted_head


def merge_sorted_lists(list1, list2):
    """
    Merge Two Sorted Singly Linked Lists
    """
    dummy = ListNode()
    curr = dummy
    while list1 and list2:
        if list1.value < list2.value:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    curr.next = list1 or list2
    return dummy.next
