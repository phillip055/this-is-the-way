# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x1 = ''
        currentNode = l1
        while(currentNode != None):
            x1 += str(currentNode.val)
            currentNode = currentNode.next
        x1 = x1[::-1]
        x2 = ''
        currentNode = l2
        while(currentNode != None):
            x2 += str(currentNode.val)
            currentNode = currentNode.next
        x2 = x2[::-1]

        res = int(x1) + int(x2)
        resString = str(res)
        reversedResString = resString[::-1]
        
        latestNode = None
        firstNode = None
        
        for i in range(len(reversedResString)):
            node = ListNode(int(reversedResString[i]))
            if latestNode == None:
                firstNode = node
                latestNode = node
            else:
                latestNode.next = node
                latestNode = node
        return firstNode
        
