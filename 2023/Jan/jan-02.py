"""
Problem: 520. Detect Capital

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true

Example 2:
Input: word = "FlaG"
Output: false

Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.

"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        is_valid = False
        if word == word.lower() or word == word.upper():
            is_valid = True
        elif len(word) > 1 and word[1:] == word[1:].lower():
            is_valid = True

        return is_valid

if __name__ == "__main__":
    solution = Solution()
    word = "FlaG"
    print(solution.detectCapitalUse(word))
