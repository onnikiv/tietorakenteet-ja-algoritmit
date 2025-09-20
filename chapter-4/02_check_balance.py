def check_balance(text):
    opened = "([{"
    closed = ")]}"
    pairs = {')': '(', ']': '[', '}': '{'}

    stack = Stack() # type: ignore
    count = 0

    # Tää oli kyllä aivan järkyttävää
    for i, char in enumerate(text):
        if char in opened:
            stack.push((char, i))
        elif char in closed:
            if len(stack) == 0:
                return f"Match error at position {i}"
            top, pos = stack.pop()
            if pairs[char] != top:
                return f"Match error at position {i}"
            count += 1

    if len(stack) > 0:
        _, pos = stack.pop()
        return f"Match error at position {pos}"

    return f"Ok - {count}"
