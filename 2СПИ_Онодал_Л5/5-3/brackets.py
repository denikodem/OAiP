def brackets(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
    for char in s:
        if char in '([{<':
            stack.append(char)
        elif char in ')]}>':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack
