# Design your implementation of the circular double-ended queue (deque).
#
#  Your implementation should support following operations:
#
#
#  MyCircularDeque(k): Constructor, set the size of the deque to be k.
#  insertFront(): Adds an item at the front of Deque. Return true if the operati
# on is successful.
#  insertLast(): Adds an item at the rear of Deque. Return true if the operation
#  is successful.
#  deleteFront(): Deletes an item from the front of Deque. Return true if the op
# eration is successful.
#  deleteLast(): Deletes an item from the rear of Deque. Return true if the oper
# ation is successful.
#  getFront(): Gets the front item from the Deque. If the deque is empty, return
#  -1.
#  getRear(): Gets the last item from Deque. If the deque is empty, return -1.
#  isEmpty(): Checks whether Deque is empty or not.
#  isFull(): Checks whether Deque is full or not.
#
#
#
#
#  Example:
#
#
# MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be
# 3
# circularDeque.insertLast(1);			// return true
# circularDeque.insertLast(2);			// return true
# circularDeque.insertFront(3);			// return true
# circularDeque.insertFront(4);			// return false, the queue is full
# circularDeque.getRear();  			// return 2
# circularDeque.isFull();				// return true
# circularDeque.deleteLast();			// return true
# circularDeque.insertFront(4);			// return true
# circularDeque.getFront();			// return 4
#
#
#
#
#  Note:
#
#
#  All values will be in the range of [0, 1000].
#  The number of operations will be in the range of [1, 1000].
#  Please do not use the built-in Deque library.
#
#  Related Topics Design Queue


# leetcode submit region begin(Prohibit modification and deletion)
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.q = [0] * (k + 1)
        self.len = k + 1
        self.rear = 0
        self.front = 0

    def move_forward(self, pos):
        return (pos + 1) % self.len

    def move_backward(self, pos):
        return (pos - 1) % self.len

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            # 前端插入始终是先插入后移动，self.front始终指向多出来的那个坑
            self.q[self.front] = value
            self.front = self.move_backward(self.front)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            # 后端插入始终是先移动后插入，self.rear始终指向后端最后插入的元素
            self.rear = self.move_forward(self.rear)
            self.q[self.rear] = value
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.front = self.move_forward(self.front)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.rear = self.move_backward(self.rear)
            return True
        else:
            return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.isEmpty():
            return self.q[self.move_forward(self.front)]
        else:
            return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.isEmpty():
            return self.q[self.rear]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if self.front == self.rear:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if self.move_forward(self.rear) == self.front:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# leetcode submit region end(Prohibit modification and deletion)
