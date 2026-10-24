def groupAnagrams(strs):
    res = []
    visited = set()

    for i in range(len(strs)):
        if i in visited:
            continue

        group = [strs[i]]
        visited.add(i)

        for j in range(i + 1, len(strs)):
            if sorted(strs[i]) == sorted(strs[j]):
                group.append(strs[j])
                visited.add(j)

        res.append(group)

    return res


print(groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
