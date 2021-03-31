def find_pairings():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    subgroups = []

    for i in range(len(digits)):
        for j in range(i + 1, len(digits), 1):
            for k in range(j + 1, len(digits), 1):
                for l in range(k + 1, len(digits), 1):
                    subgroups.append([digits[i], digits[j], digits[k], digits[l]])

    groups = []

    for i in range(len(subgroups)):
        for j in range(i + 1, len(subgroups), 1):
            no_repeat = True
            for k in subgroups[i]:
                if k in subgroups[j]:
                    no_repeat = False
            if no_repeat:
                groups.append([subgroups[i], subgroups[j]])

    return groups
