

# Remove equal adjacent elements
#
# Example input: [1, 2, 2, 3]
# Example output: [1, 2, 3]
def remove_adjacent(lst):
    return [x for i, x in enumerate(lst) if i < 1 or lst[i - 1] != x]


# Merge two sorted lists in one sorted list in linear time
#
# Example input: [2, 4, 6], [1, 3, 5]
# Example output: [1, 2, 3, 4, 5, 6]
def linear_merge(lst1, lst2):
    n, m = len(lst1), len(lst2)
    i1, i2 = 0, 0
    res = []
    while(i1 < n and i2 < m):
        a, b = lst1[i1], lst2[i2]
        if a < b:
            res.append(a)
            i1 += 1
        else:
            res.append(b)
            i2 += 1
    return res + lst1[i1:] + lst2[i2:]

# lst1 = list(map(int, input().split()))
# lst2 = list(map(int, input().split()))

# print(remove_adjacent(lst1))

# print(linear_merge(lst1, lst2))
