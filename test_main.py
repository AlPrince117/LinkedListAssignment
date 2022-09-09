from unittest import TestCase
from main import LinkedList, Node


class TestLinkedList(TestCase):

    def test_reverse_linked_list(self):
        test_linked_list = LinkedList()
        node_1 = Node('1')
        node_2 = Node('2')
        node_3 = Node('3')
        node_4 = Node('4')

        test_linked_list.head = node_1
        node_1.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        test_linked_list.reverse_linkedList()
        self.assertEqual(str(test_linked_list.head), '4')

    def test_is_infinite_is_true(self):
        linked_list = LinkedList()
        node_1 = Node('a')
        linked_list.head = node_1
        node_2 = Node('b')
        node_3 = Node('c')
        node_1.next = node_2
        node_2.next = node_3
        node_3.next = node_2
        self.assertEqual(linked_list.is_infinite(), True)

    def test_is_infinite_is_not_true(self):
        linked_list = LinkedList()
        node_1 = Node('a')
        linked_list.head = node_1
        node_2 = Node('b')
        node_3 = Node('c')
        node_1.next = node_2
        node_2.next = node_3
        self.assertEqual(linked_list.is_infinite(), False)
