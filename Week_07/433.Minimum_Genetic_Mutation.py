# A gene string can be represented by an 8-character long string, with choices f
# rom "A", "C", "G", "T".
#
#  Suppose we need to investigate about a mutation (mutation from "start" to "en
# d"), where ONE mutation is defined as ONE single character changed in the gene s
# tring.
#
#  For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.
#
#  Also, there is a given gene "bank", which records all the valid gene mutation
# s. A gene must be in the bank to make it a valid gene string.
#
#  Now, given 3 things - start, end, bank, your task is to determine what is the
#  minimum number of mutations needed to mutate from "start" to "end". If there is
#  no such a mutation, return -1.
#
#  Note:
#
#
#  Starting point is assumed to be valid, so it might not be included in the ban
# k.
#  If multiple mutations are needed, all mutations during in the sequence must b
# e valid.
#  You may assume start and end string is not the same.
#
#
#
#
#  Example 1:
#
#
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
#
# return: 1
#
#
#
#
#  Example 2:
#
#
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
#
# return: 2
#
#
#
#
#  Example 3:
#
#
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
#
# return: 3
#
#
#
#


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # BFS
        # check change between cur and next mutation must equal one!
        def viable_check(cur, next):
            change = 0
            for i in range(len(cur)):
                if cur[i] != next[i]:
                    change += 1
            return change == 1

        # BFS starts here
        queue = collections.deque()
        queue.append([start, start, 0])
        visited = [start]

        while queue:
            cur, pre, num_step = queue.popleft()
            if cur == end:
                return num_step

            for item in bank:
                # check only one change in each step and chaeck if visited
                if viable_check(cur, item) and item not in visited:
                    visited.append(cur)
                    queue.append([item, cur, num_step+1])

        return -1

        # 双向BFS
        if end not in bank:
            return -1

        front = {start}
        back = {end}
        distance = 0
        bank = set(bank)
        mutation_len = len(start)

        # BFS starts here
        while front and back:
            distance += 1
            new_front = set()

            for item in front:
                for i in range(mutation_len):
                    for c in ["A", "C", "G", "T"]:
                        new_mutation = item[:i] + c + item[i + 1:]

                        if new_mutation in back:
                            return distance
                        if new_mutation in bank:
                            new_front.add(new_mutation)
                            bank.remove(new_mutation)

            front = new_front

            if len(front) > len(back):
                front, back = back, front

        return -1

# leetcode submit region end(Prohibit modification and deletion)
