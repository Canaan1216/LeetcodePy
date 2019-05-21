# -*- coding:utf-8 -*-
"""
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

class ListNodeHandle(object):
    def __init__(self):
        self.cur_node = None

    def add(self, data):
        #add a new node pointed to previous node
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 若l1或l2有一个为空,则直接返回另一个结果
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        blank = ListNode(0)  # 定义一个链表,唯一的节点为0
        res = blank  # 用于存储两数相加结果
        flag = 0  # 进位标志
        while l1 or l2:  # 判断l1或l2是否已经取到尽头
            tmpsum = 0
            if l1:
                tmpsum = l1.val
                l1 = l1.next
            if l2:
                tmpsum += l2.val
                l2 = l2.next
            tmpres = ((tmpsum + flag) % 10)
            flag = ((tmpsum + flag) // 10)
            res.next = ListNode(tmpres)
            res = res.next
        if flag:  # 最后一次加和若有进位,则末尾需添1
            res.next = ListNode(1)
        res = blank.next  # 因链表第一个节点为0,故从第二个节点之后为结果
     #   del blank
        return res

def print_ListNode(node):
    str = ""
    while node!=None:
        str = str + "%s"%(node.val)
        str = str + '->'
        node = node.next
    str = str[:-2]
    print str

if __name__ == '__main__':
    # do test
    l1 = ListNode()
    l2 = ListNode()
    l1_Res = ListNodeHandle()
    l2_Res = ListNodeHandle()
    l1_list = [2, 4, 3]
    l2_list = [5, 6, 4]

    for i in l1_list:
        l1 = l1_Res.add(i)
    print "L1:"
    print_ListNode(l1)

    for i in l2_list:
        l2 = l2_Res.add(i)
    print "L2:"
    print_ListNode(l2)

    testDemo = Solution()
    twoNumberResult = testDemo.addTwoNumbers(l1,l2)
    print "Two Number Sum Result:"
    print_ListNode(twoNumberResult)