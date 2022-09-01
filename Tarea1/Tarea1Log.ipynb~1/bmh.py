from collections import defaultdict

def bmh(pattern, text):
    m = len(pattern)
    n = len(text)
    pattern = pattern.lower()
    text = text.lower()

    if m > n:
        return -1

    skip = defaultdict(lambda: m)
    results = []

    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1

    k = m - 1
    n_comp = 0

    while k < n:
        j = m - 1
        i = k
        len_results = len(results)
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
            n_comp += 1
        if j == -1:
            results.append(i + 1)

        if len_results - len(results) == 0: # No contar dos veces la misma letra!
            n_comp += 1

        k += skip[ord(text[k])]

    print(f'# comparisons = {n_comp}')
    return results


#### Fuente: https://github.com/jwasham/code-catalog-python/blob/master/catalog/suggested/pattern_matching/boyer-moore-horspool.py