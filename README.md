### Analysis of Algorithm Semester Project
# Wagner-Fischer Algorithm
The Wagner-Fischer algorithm is a dynamic programming technique used to compute the edit distance (also known as Levenshtein distance) between two strings. The edit distance is a measure of how many single-character edits (insertions, deletions, or substitutions) are needed to change one string into the other.

## Time Complexity

The time complexity of the Wagner-Fischer algorithm is `O(m * n)`, where `m` is the length of the first string `s` and `n` is the length of the second string `t`. This is because the algorithm fills a matrix of size `(m + 1) x (n + 1)` and each cell in the matrix requires a constant amount of work to compute.


## Space Complexity

The space complexity of the Wagner-Fischer algorithm is also `O(m * n)` because it requires a 2D list (matrix) of size `(m + 1) x (n + 1)` to store the edit distances between all prefixes of the two strings.

# Example: Spell Checker

The spell checker uses the Wagner-Fischer algorithm to find the closest word in a given dictionary to an input word. The algorithm works as follows:

1. Initialize `min_distance` to infinity and `closest_word` to `None`.
2. For each word in the dictionary, compute the edit distance to the input word using the Wagner-Fischer algorithm.
3. If the computed distance is less than `min_distance`, update `min_distance` and set `closest_word` to the current dictionary word.
4. After checking all dictionary words, return the `closest_word` and `min_distance`.

### Time Complexity

The time complexity of the spell checker function is `O(D * m * n)`, where `D` is the number of words in the dictionary, `m` is the length of the input word, and `n` is the length of the current dictionary word being checked. This is because the Wagner-Fischer algorithm (which has a time complexity of `O(m * n)`) is called for each word in the dictionary.

### Space Complexity

The space complexity of the spell checker function is `O(m * n)` due to the space required by the Wagner-Fischer algorithm to store the matrix.
