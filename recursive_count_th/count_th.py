'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.

U
Inputs:
- string word
Output:
- integer value of how many occurences of "th" in the word
Constraints:
- Can only have one parameter
- The function must use recursion
- Can not contain any loops
P
- My plan will utilize slicing
- It's base case will be when the sliced up string reaches a length of two or less, where it will check it those two characters are th, returning either a 0 or a 1
- If not at base case, we will check if the first two characters are th, if so, return the 1 + count_th(word[2:]) to slice off that th.
- Else if the second character is t, it will return count_th(word[1:]) to slice off the first character
- Otherwise we will slice off the characters without adding to the count and just return count_th(word[2:])
- The return values will pop off the call stack adding up our count.
- This will be O(n) time and space complexity where n is the length of our string


R
- This would use less space with loops.
- I wonder if regex methods do this in similar speed and space complexity.

'''
def count_th(word):
    if len(word) <= 2:
        if word == 'th':
            return 1
        else:
            return 0
    elif word[:2] == 'th':
        return 1 + count_th(word[2:])
    elif word[1] == 't':
        return count_th(word[1:])
    else:
        return count_th(word[2:])


