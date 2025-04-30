def compute_bad_character_table(pattern: str) -> dict:
    """
    Compute the bad character table for the Boyer-Moore algorithm.

    Args:
        pattern: The pattern string

    Returns:
        A dictionary with keys as characters and values as the rightmost position
        of the character in the pattern (0-indexed)
    """
    # TODO: Implement the bad character heuristic for Boyer-Moore algorithm
    # This table maps each character to its rightmost occurrence in the pattern
    # For characters not in the pattern, they should not be in the dictionary
    # Remember that this is used to determine how far to shift when a mismatch occurs
    res = {}
    for i in range(len(pattern) - 1, -1, -1):
        if pattern[i] not in res:
            res[pattern[i]] = i

    return res


def compute_good_suffix_table(pattern: str) -> list[int]:
    """
    Compute the good suffix table for the Boyer-Moore algorithm.

    Args:
        pattern: The pattern string

    Returns:
        A list where shift[i] stores the shift required when a mismatch
        happens at position i of the pattern
    """
    m = len(pattern)
    shift = [0] * (m + 1)

    def find_shift(s, i):
        suffix = s[i + 1 :]
        for k in range(i, -1, -1):
            if s[k : k + len(suffix)] == suffix:
                return i - k + 1
        for k in range(1, len(suffix)):
            if suffix[-k:] == s[:k]:
                return len(suffix) - k
        return len(s)

    for i in range(m):
        shift[i] = find_shift(pattern, i)

    shift[m] = 1

    return shift


def boyer_moore_pattern_match(text: str, pattern: str) -> list[int]:
    """
    Implementation of the Boyer-Moore pattern matching algorithm.

    Args:
        text: The text to search in
        pattern: The pattern to search for

    Returns:
        A list of starting positions (0-indexed) where the pattern was found in the text
    """
    # TODO: Implement the Boyer-Moore string matching algorithm
    # 1. Preprocess the pattern to create the bad character and good suffix tables
    # 2. Start matching from the end of the pattern and move backwards
    # 3. When a mismatch occurs, use the maximum shift from both tables
    # 4. Return all positions where the pattern is found in the text

    if not pattern:
        return list(range(len(text) + 1))

    m = len(pattern)
    n = len(text)
    matches = []

    bad_char_table = compute_bad_character_table(pattern)
    good_suffix_table = compute_good_suffix_table(pattern)

    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            matches.append(i)
            i += good_suffix_table[m]
        else:
            bad_char_shift = j - bad_char_table.get(text[i + j], -1)

            i += max(bad_char_shift, good_suffix_table[j])

    return matches
