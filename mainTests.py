import unittest

from Exercice_4_1_ComputingTheParityOfAWord import Test_4_1_ComputingTheParityOfAWord
from Exercice_6_1_InterconvertStringsAndIntegers import Test_6_1_InterconvertStringsAndIntegers

Test_4_1_ComputingTheParityOfAWord()
Test_6_1_InterconvertStringsAndIntegers()


class ListNode:
    def __init__(self, _data, initlist=None):
        self.data = _data
        self.next = initlist


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


def InvertSubList(firstNode, start, finish):
    dummy_head = sublist_head = ListNode(0, firstNode)

    for _ in range(1, start):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (temp.next, sublist_head.next, temp)

    return dummy_head.next



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

def RemoveKthLastElement(inputList, indexNb):
    DummyHead = ListNode(0, inputList)

    TailDetectorNode = DummyHead.next

    currentNodeIndex = 1
    while currentNodeIndex < indexNb:
        TailDetectorNode = TailDetectorNode.next
        currentNodeIndex += 1

    BeforeNodeToBeRemoved = DummyHead

    while TailDetectorNode.next != None :
        TailDetectorNode = TailDetectorNode.next
        BeforeNodeToBeRemoved = BeforeNodeToBeRemoved.next

    BeforeNodeToBeRemoved.next = BeforeNodeToBeRemoved.next.next

    return DummyHead.next


class Test_7_7_RemovingThekthLatestNode(unittest.TestCase):
    def test_should_remove_the_middle_element_when_a_list_contains_three_nodes(self):
        firstNode = ListNode(1)
        secondNode = ListNode(2)
        thirdNode = ListNode(3)

        firstNode.next = secondNode
        secondNode.next = thirdNode

        actualList = RemoveKthLastElement(firstNode, 2)

        self.assertEqual(actualList.data, 1)
        self.assertEqual(actualList.next.data, 3)
        self.assertEqual(actualList.next.next, None)

    def test_should_return_third_node_before_the_end_when_a_list_of_seven_elements_is_passed(self):
        firstNode = ListNode(1)
        secondNode = ListNode(2)
        thirdNode = ListNode(3)
        fourthNode = ListNode(4)
        fifthNode = ListNode(5)     # node to be removed
        sixthNode = ListNode(6)
        seventhNode = ListNode(7)

        firstNode.next = secondNode
        secondNode.next = thirdNode
        thirdNode.next = fourthNode
        fourthNode.next = fifthNode
        fifthNode.next = sixthNode
        sixthNode.next = seventhNode

        actualList = RemoveKthLastElement(firstNode, 3)

        self.assertEqual(actualList.data, 1)
        self.assertEqual(actualList.next.data, 2)
        self.assertEqual(actualList.next.next.data, 3)
        self.assertEqual(actualList.next.next.next.data, 4)
        self.assertEqual(actualList.next.next.next.next.data, 6)
        self.assertEqual(actualList.next.next.next.next.next.data, 7)
        self.assertEqual(actualList.next.next.next.next.next.next, None)

if __name__ == "__main__":
    unittest.main()
