def isBalanced(s):
    brackets = {"}": "{", "]": "[", ")":"("}
    stack = []
    for char in s:
        if char in ["{", "(", "["]:
            stack.append(char)
        elif len(stack) > 0 and brackets[char] == stack[-1]:
            del stack[-1]
        else:
            return "NO"
    if len(stack):
        return "NO"
    return "YES"
