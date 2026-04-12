def isStretchy(s, word):
    i, j = 0, 0
    while i < len(s) and j < len(word):
        if s[i] != word[j]:
            return False
        char = s[i]
        start_i = i
        while i < len(s) and s[i] == char:
            i += 1
        s_count = i - start_i
        start_j = j
        while j < len(word) and word[j] == char:
            j += 1
        w_count = j - start_j
        if s_count < 3:
            if s_count != w_count:
                return False
        else:
            if w_count > s_count:
                return False
    return i == len(s) and j == len(word)


def expressiveWords(s, words):
    result = 0
    for i in words:
        result += isStretchy(s, i)
    return result


tests = [
    ("heeellooo", ["hello", "hi", "helo"], 1),
    ("zzzzzyyyyy", ["zzyy", "zy", "zyy"], 3),
    ("abcd", ["abcd", "abc", "abbcd", "abcd"], 2),
    ("aaa", ["a", "aa", "aaa", "aaaa"], 3),
    ("hello", ["hello", "helo", "helloo"], 1),
    ("wwwwaaadexxxxxx", ["wadex", "wwadexxxxxx", "wwwwaaaadexxxxxx"], 2),
    ("aabbcc", ["aabbcc", "abc", "aabbc"], 1),
    ("xxxxx", ["x", "xx", "xxx", "xxxx", "xxxxx"], 5),
]

for i, (s, words, expected) in enumerate(tests, 1):
    result = expressiveWords(s, words)
    status = "PASS" if result == expected else "FAIL"

    print(f"Test {i}")
    print(f"  s:        {s}")
    print(f"  words:    {words}")
    print(f"  Result:   {result}")
    print(f"  Expected: {expected}")
    print(f"  Status:   {status}")
    print("-" * 50)
