def wagner_fischer(s, t):
    m = len(s)                                                                     # O(1) - Calculate the length of string s
    n = len(t)                                                                     # O(1) - Calculate the length of string t

    # Step 1: Initialize the matrix
    d = [[0] * (n + 1) for i in range(m + 1)]                                      # O(m * n) - Initialize (m+1)x(n+1) matrix with zeros
    
    # Step 2: Initialize the first row and first column
    for i in range(1, m + 1):                                                      # O(m) - Fill the first column
        d[i][0] = i                                                                # O(1) per iteration

    for j in range(1, n + 1):                                                      # O(n) - Fill the first row
        d[0][j] = j                                                                # O(1) per iteration
    
    # Step 3: Populate the rest of the matrix
    for i in range(1, m + 1):                                                      # O(m)
        for j in range(1, n + 1):                                                  # O(n) for each i, so O(m * n) total
            if s[i - 1] == t[j - 1]:                                               # O(1) - Check if characters are the same

    # If characters at this position are the same, take the value from the diagonal
                d[i][j] = d[i - 1][j - 1]  # O(1)
            else:
    # when characters at the position are not same, perform operation accordingly to get the minimum value
                d[i][j] = min(d[i - 1][j] + 1,                                    # O(1) - Calculate deletion cost
                              d[i][j - 1] + 1,                                    # O(1) - Calculate insertion cost
                              d[i - 1][j - 1] + 1)                                # O(1) - Calculate substitution cost
    
    return d[m][n]  # O(1) - Return the edit distance

def spell_checker(word, dictionary):
    min_distance = float('inf')                                                  # O(1) - Initialize minimum distance
    closest_word = None                                                          # O(1) - Initialize closest word
    
    for dict_word in dictionary:                                                 # Let D be the size of the dictionary, so O(D)
        distance = wagner_fischer(word, dict_word)                               # O(m * n) for each dict_word
        
        if distance < min_distance:                                              # O(1) - Compare current distance with min_distance
            min_distance = distance                                              # O(1) - Update min_distance if current distance is smaller
            closest_word = dict_word                                             # O(1) - Update closest_word if current distance is smaller
    
    return closest_word, min_distance                                            # O(1) - Return the closest word and minimum distance
