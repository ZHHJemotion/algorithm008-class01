# Given two words (beginWord and endWord), and a dictionary's word list, find th
# e length of shortest transformation sequence from beginWord to endWord, such tha
# t:
#
#
#  Only one letter can be changed at a time.
#  Each transformed word must exist in the word list.
#
#
#  Note:
#
#
#  Return 0 if there is no such transformation sequence.
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
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog
# " -> "cog",
# return its length 5.
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
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible trans
# formation.
#
#
#
#
#  Related Topics Breadth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
import string
import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0

        # generate intermediate form by changing only one letter each time
        l = len(beginWord)
        all_combination_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(l):
                all_combination_dict[word[:i] + "*" + word[i+1:]].append(word)

        # bfs
        queue = [(beginWord, 1)]
        visited = {beginWord: True}
        while queue:
            cur_word, level = queue.pop(0)
            for i in range(l):
                intermediate_word = cur_word[:i] + "*" + cur_word[i+1:]
                for word in all_combination_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level+1))
                # 遍历完置空
                all_combination_dict[intermediate_word] = []

        return 0

        # 双向BFS
        if endWord not in wordList:
            return 0

        front = {beginWord}
        back = {endWord}
        distance = 1
        wordList = set(wordList)
        word_len = len(beginWord)

        # bfs starts here
        while front and back:
            distance += 1
            new_front = set()

            for word in front:
                for i in range(word_len):
                    for c in string.ascii_lowercase:  # 遍历 a-z
                        if c != word[i]:
                            new_word = word[:i] + c + word[i + 1:]

                            if new_word in back:
                                return distance

                            if new_word in wordList:
                                new_front.add(new_word)
                                wordList.remove(new_word)

            front = new_front

            if len(front) > len(back):
                front, back = back, front

        return 0

# leetcode submit region end(Prohibit modification and deletion)
