import collections
import unittest
from array import array

from Exercice_4_1_ComputingTheParityOfAWord import Test_4_1_ComputingTheParityOfAWord
from Exercice_6_1_InterconvertStringsAndIntegers import Test_6_1_InterconvertStringsAndIntegers
from Exercice_7_1_MergingTwoSortedLists import Test_7_1_MergingTwoSortedLists
from Exercice_7_2_InversingASubList import Test_7_2_InversingASubList
from Exercice_7_7_RemovingThekthLatestNode import  Test_7_7_RemovingThekthLatestNode
from Exercice_7_10_OddEvenAlgo import  Test_7_10_OddEvenAlgo

from ListNode import ListNode

Test_4_1_ComputingTheParityOfAWord()
Test_6_1_InterconvertStringsAndIntegers()
Test_7_1_MergingTwoSortedLists()
Test_7_2_InversingASubList()
Test_7_7_RemovingThekthLatestNode()
Test_7_10_OddEvenAlgo()


def print_linked_list_in_reverse(headNode):
    sideEffectArray = array('I')

    RecursiveAdd(headNode, sideEffectArray)

    return sideEffectArray


def RecursiveAdd(headNode, sideEffectArray):
    if headNode is not None:
        RecursiveAdd(headNode.next, sideEffectArray)
        sideEffectArray.append(headNode.data)


class Test_StackBootCamp_Print_Linked_List_In_Reverse(unittest.TestCase):
    def test_should_print_the_only_number_in_a_stack_when_only_one_number_is_stored_in_a_linked_list(self):
        headNode = ListNode(1)

        actual = print_linked_list_in_reverse(headNode)

        self.assertSequenceEqual(actual, [1])

    def test_should_store_the_numbers_in_reverse_order_when_a_linked_list_is_unstacked(self):
        headNode = ListNode(1)
        secondNode = ListNode(2)
        thirdNode = ListNode(3)
        fourthNode = ListNode(4)
        fifthNode = ListNode(5)
        sixthNode = ListNode(6)
        seventhNode = ListNode(7)
        eigthNode = ListNode(8)
        ninethNode = ListNode(9)

        headNode.next = secondNode
        secondNode.next = thirdNode
        thirdNode.next = fourthNode
        fourthNode.next = fifthNode
        fifthNode.next = sixthNode
        sixthNode.next = seventhNode
        seventhNode.next = eigthNode
        eigthNode.next = ninethNode

        actual = print_linked_list_in_reverse(headNode)

        self.assertSequenceEqual(actual, [9, 8, 7, 6, 5, 4, 3, 2, 1])


class MyOwnStack:
    _maxValue = None
    _headNode = ListNode(-1)
    _tailNode = _headNode

    def push(self, param):
        if(self._maxValue == None):
            self._maxValue = param

        if(param > self._maxValue):
            self._maxValue = param

        self._tailNode.next = ListNode(param)
        self._tailNode = self._tailNode.next

    def max(self):
        return self._maxValue

    def pop(self):
        pass


class Test_8_1_Implemting_a_stack_wtih_Max_API(unittest.TestCase):
    def test_should_return_max_element_when_a_stack_is_composed_of_one_element(self):
        maxStack = MyOwnStack()
        maxStack.push(4)

        actual = maxStack.max()
        
        self.assertEqual(actual, 4)

    def test_should_return_max_element_when_two_elements_are_pushed_and_one_element_is_popped(self):
        maxStack = MyOwnStack()
        maxStack.push(4)
        maxStack.push(12)

        actual = maxStack.max()

        self.assertEqual(actual, 12)

#        poppedElement = maxStack.pop()

#        self.assertEqual(poppedElement, 12)

#        actual = maxStack.max()

#        self.assertEqual(actual, 4)


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


class Vector(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y

        return Vector(x, y)

class Test_Chapitre_1_The_Python_Data_Model(unittest.TestCase):
    def test_should_return_seven_of_Diamond_when_seven_of_diamonds_is_instanciated(self):
        actual = Card('7', 'diamonds')

        self.assertEqual(actual.rank, '7')
        self.assertEqual(actual.suit, 'diamonds')

    def test_should_return_number_of_cards_in_the_deck_when_a_deck_is_instanciated(self):
        deck = FrenchDeck()

        actual = len(deck)

        self.assertEqual(actual, 52)

    def test_should_return_two_of_spades_when_the_first_card_of_the_deck_is_asked(self):
        deck = FrenchDeck()

        actual = deck[0]

        self.assertEqual(actual.rank, '2')
        self.assertEqual(actual.suit, 'spades')

    def test_should_return_sum_of_vector_when_two_vectors_are_added(self):
        v1 = Vector(2, 4)
        v2 = Vector(2, 1)

        actual = v1 + v2

        self.assertEqual(actual.x, 4)
        self.assertEqual(actual.y, 5)

class Test_Chapitre_2_An_Array_Of_Sequences(unittest.TestCase):
    def test_should_return_correct_ist_of_symbol_values_when_a_list_comprehension_is_used(self):
        symbols = '$ç£€'

        actual = [ord(symbol) for symbol in symbols]

        self.assertEqual(actual, [36, 231, 163, 8364])

    def test_should_unpack_tuple_information_when_a_tuple_is_unpacker(self):
        city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

        self.assertEqual(city, 'Tokyo')
        self.assertEqual(year, 2003)
        self.assertEqual(pop, 32450)
        self.assertEqual(chg, 0.66)
        self.assertEqual(area, 8014)

class Test_EffectivePython_Item7_Use_List_Comprehension_Instead_of_ma_and_filter(unittest.TestCase):
    def test_should_return_same_lists_when_listcomp_and_map_are_used(self):
        a  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        listcompResult = [x**2 for x in a]
        mapResult = list(map(lambda x: x ** 2, a))

        self.assertSequenceEqual(listcompResult, mapResult)

    def test_should_return_same_lists_when_listcomp_andMap_with_filter_are_used(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        listcompResult = [x ** 2 for x in a if x % 2 == 0]
        mapResult = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, a)))

        self.assertSequenceEqual(listcompResult, mapResult)

if __name__ == "__main__":
    unittest.main()
