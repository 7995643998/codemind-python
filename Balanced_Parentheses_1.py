def isValid(s):
    opening = "{[("
    closing = "}])"
    brackets = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if len(stack) == 0:
                return False
            if stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0
s=input()
if(isValid(s)):
    print("True")
else:
    print("False")