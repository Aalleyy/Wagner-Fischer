def wagner_fischer(s, t):
    m = len(s)
    n = len(t)
    d = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
        d[i][0] = i
    for j in range(1, n + 1):
        d[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                d[i][j] = d[i - 1][j - 1] 
            else:
                d[i][j] = min(d[i - 1][j] + 1, 
                              d[i][j - 1] + 1,  
                              d[i - 1][j - 1] + 1) 
    return d[m][n]

def spell_checker(word, dictionary):
    min_distance = float('inf')
    closest_word = None
    for dict_word in dictionary:
        distance = wagner_fischer(word, dict_word)
        if distance < min_distance:
            min_distance = distance
            closest_word = dict_word
    return closest_word, min_distance