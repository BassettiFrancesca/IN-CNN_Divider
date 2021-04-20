def find_pairings():
    digits = [6, 7, 4]

    subgroups = []

    for i in range(len(digits)):
        # for j in range(i + 1, len(digits), 1):
        # for k in range(j + 1, len(digits), 1):
        #   for l in range(k + 1, len(digits), 1):
        #    for m in range(l + 1, len(digits), 1):
        subgroups.append([digits[i]])

    groups = []

    for i in range(len(subgroups)):
        for j in range(i + 1, len(subgroups), 1):
            no_repeat = True
            for k in subgroups[i]:
                if k in subgroups[j]:
                    no_repeat = False
            if no_repeat:
                tmp1 = []
                tmp2 = []
                for l in subgroups[i]:
                    tmp1.append(l)
                for m in subgroups[j]:
                    tmp2.append(m)
                groups.append([tmp1, tmp2])

    for group in groups:
        is_d = [False, False, False]
        for g in group:
            for d in g:
                for (i, dig) in enumerate(digits):
                    if d == dig:
                        is_d[i] = True
        for (i, bool_d) in enumerate(is_d):
            if not bool_d:
                digit = digits[i]
        for g in group:
            g.append(digit)

    return groups
