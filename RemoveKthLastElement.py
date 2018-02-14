from ListNode import ListNode


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