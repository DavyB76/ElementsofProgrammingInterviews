import unittest

from Exercice_4_1_ComputingTheParityOfAWord import Test_4_1_ComputingTheParityOfAWord
from Exercice_6_1_InterconvertStringsAndIntegers import Test_6_1_InterconvertStringsAndIntegers

Test_4_1_ComputingTheParityOfAWord()
Test_6_1_InterconvertStringsAndIntegers()


class ListNode:
    def __init__(self, _data):
        self.data = _data
        self.next = None


def MergingTwoSortedLists(firstList, secondList):
    dummyHead = ListNode(0)
    currentMergedListNode = dummyHead

    firstListCurrentNode = firstList
    secondListCurrentNode = secondList

    while firstListCurrentNode is not None and secondListCurrentNode is not None:
        if firstListCurrentNode.data < secondListCurrentNode.data:
            currentMergedListNode.next = firstListCurrentNode
            firstListCurrentNode = firstListCurrentNode.next
        else:
            currentMergedListNode.next = secondListCurrentNode
            secondListCurrentNode = secondListCurrentNode.next

        currentMergedListNode = currentMergedListNode.next

    if firstListCurrentNode is not None:
        currentMergedListNode.next = firstListCurrentNode

    if secondListCurrentNode is not None:
        currentMergedListNode.next = secondListCurrentNode

    return dummyHead.next


class Test_7_1_MergingTwoSortedLists(unittest.TestCase):
    def test_should_return_merged_sorted_list_when_merging_two_one_element_lists(self):
        firstList = ListNode(3)
        secondList = ListNode(1)

        actualList = MergingTwoSortedLists(firstList, secondList)

        self.assertEqual(actualList.data, 1)
        self.assertEqual(actualList.next.data, 3)

    def test_should_return_merged_sorted_list_when_merging_one_list_of_two_elements_and_one_list_of_one_element(self):
        firstNode = ListNode(3)
        secondNode = ListNode(8)
        firstNode.next = secondNode

        secondList = ListNode(4)

        actualList = MergingTwoSortedLists(firstNode, secondList)

        self.assertEqual(actualList.data, 3)
        self.assertEqual(actualList.next.data, 4)
        self.assertEqual(actualList.next.next.data, 8)

class Test_7_2_InversingASubList(unittest.TestCase):
    def _test_should_return_inverted_sublist_when_list_contains_two_items(self):
        pass

if __name__ == "__main__":
    unittest.main()
