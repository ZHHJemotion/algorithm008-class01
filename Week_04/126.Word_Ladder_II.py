# Given two words (beginWord and endWord), and a dictionary's word list, find al
# l shortest transformation sequence(s) from beginWord to endWord, such that:
#
#
#  Only one letter can be changed at a time
#  Each transformed word must exist in the word list. Note that beginWord is not
#  a transformed word.
#
#
#  Note:
#
#
#  Return an empty list if there is no such transformation sequence.
#  All words have the same length.
#  All words contain only lowercase alphabetic characters.
#  You may assume no duplicates in the word list.
#  You may assume beginWord and endWord are non-empty and are not the same.
#
#
#  Example 1:
#
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
#
#
#  Example 2:
#
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: []
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible trans
# formation.
#
#
#
#
#  Related Topics Array String Backtracking Breadth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # BFS
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return []

        # generate all combinations of forms
        l = len(beginWord)
        # dict of words by changing one letter at one time
        all_combination_dict = defaultdict(list)
        for word in wordList:
            for i in range(l):
                all_combination_dict[word[:i] + "*" + word[i + 1:]].append(word)

        # bfs
        queue = [(beginWord, 1)]
        visited = {beginWord: 1}
        pre_work = defaultdict(list)
        res = []
        while queue:
            cur_word, level = queue.pop(0)
            for i in range(l):
                intermediate_word = cur_word[:i] + "*" + cur_word[i + 1:]
                # traverse all sub tree
                for word in all_combination_dict[intermediate_word]:
                    if word not in visited:
                        visited[word] = level + 1
                        queue.append((word, level + 1))
                    if visited[word] == level + 1:
                        pre_work[word].append(cur_word)
            # the target word has been traversed
            if endWord in visited and visited[endWord] < level + 1:
                break

        # output the all path
        if endWord in visited:
            res = [[endWord]]
            while res[0][0] != beginWord:
                res = [[word] + item for item in res for word in pre_work[item[0]]]
            return res
        else:
            return []

# leetcode submit region end(Prohibit modification and deletion)
