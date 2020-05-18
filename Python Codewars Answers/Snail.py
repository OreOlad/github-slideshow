def snail(snail_map):
    if not snail_map:
        return snail_map
    res = list()
    n = len(snail_map)
    res += snail_map.pop(0)
    for i in range(1, n - 1):
        res.append(snail_map[i - 1].pop())
    if snail_map:
        res += snail_map.pop()[::-1]
    for i in range(n - 2, 0, -1):
        res.append(snail_map[i - 1].pop(0))
    res += snail(snail_map)
    return res
