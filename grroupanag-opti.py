def groupAnagrams(strs):
    groups = {}

    for s in strs:
        key = "".join(sorted(s))

        if key not in groups:
            groups[key] = []

        groups[key].append(s)

    return list(groups.values())


print(groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
