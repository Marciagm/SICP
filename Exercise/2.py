def count_while(s, value):
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total = total + 1
        index = index + 1
    return total

def count_for(s, value):
    total = 0
    for elem in s:
        if elem == value:
            total = total + 1
    print(elem)
    return total

def divisors(n):
    return [1] + [x for x in range(2, n//2 + 1) if n%x==0]

def apply_to_all(map_fn, s):
    return[map_fn(x) for x in s]