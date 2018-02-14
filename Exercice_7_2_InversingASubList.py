import unittest

from InvertSubList import InvertSubList
from ListNode import ListNode


class Test_7_2_InversingASubList(unittest.TestCase):
    def test_should_return_inverted_sublist_when_list_contains_five_items(self):
        firstNode = ListNode(11)
        secondNode = ListNode(3)
        thirdNode = ListNode(5)
        fourthNode = ListNode(7)
        fifthNode = ListNode(2)
        firstNode.next = secondNode
        secondNode.next = thirdNode
        thirdNode.next = fourthNode
        fourthNode.next = fifthNode

        actualList = InvertSubList(firstNode, 2, 4)

        self.assertEqual(actualList.data, 11)
        self.assertEqual(actualList.next.data, 7)
        self.assertEqual(actualList.next.next.data, 5)
        self.assertEqual(actualList.next.next.next.data, 3)
        self.assertEqual(actualList.next.next.next.next.data, 2)

    def test_should_return_inverted_sublist_when_list_contains_ten_items(self):
        firstNode = ListNode(1)
        secondNode = ListNode(2)
        thirdNode = ListNode(3)
        fourthNode = ListNode(4)
        fifthNode = ListNode(5)
        sixthNode = ListNode(6)
        seventhNode = ListNode(7)
        eigthNode = ListNode(8)
        ninethNode = ListNode(9)
        tenthNode = ListNode(10)
        firstNode.next = secondNode
        secondNode.next = thirdNode
        thirdNode.next = fourthNode
        fourthNode.next = fifthNode
        fifthNode.next = sixthNode
        sixthNode.next = seventhNode
        seventhNode.next = eigthNode
        eigthNode.next = ninethNode
        ninethNode.next = tenthNode

        actualList = InvertSubList(firstNode, 2, 9)

        self.assertEqual(actualList.data, 1)
        self.assertEqual(actualList.next.data, 9)
        self.assertEqual(actualList.next.next.data, 8)
        self.assertEqual(actualList.next.next.next.data, 7)
        self.assertEqual(actualList.next.next.next.next.data, 6)
        self.assertEqual(actualList.next.next.next.next.next.data, 5)
        self.assertEqual(actualList.next.next.next.next.next.next.data, 4)
        self.assertEqual(actualList.next.next.next.next.next.next.next.data, 3)
        self.assertEqual(actualList.next.next.next.next.next.next.next.next.data, 2)
        self.assertEqual(actualList.next.next.next.next.next.next.next.next.next.data, 10)