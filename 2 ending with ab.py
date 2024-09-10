def matches_pattern(text):
    state = 'start'
    for char in text:
        if state == 'start' and char == 'a':
            state = 'a'
        elif state == 'a' and char == 'b':
            state = 'ab'
        else:
            state = 'start' if char != 'a' else 'a'
    return state == 'ab'

test_strings = ["cab", "aba", "abab", "abc", "ab"]
for s in test_strings:
    if matches_pattern(s):
        print(f"'{s}' matches the pattern.")
    else:
        print(f"'{s}' does not match the pattern.")
