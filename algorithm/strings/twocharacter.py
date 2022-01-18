d = list(set(s))
    pairs = [[a, b] for a in d for b in d if a != b]
    max_length = 0
    for p in pairs:
        test = ''.join([c for c in s if c == p[0] or c == p[1]])
        if p[0]*2 not in test and p[1]*2 not in test:
            if len(test) > max_length:
                max_length = len(test)
    return max_length