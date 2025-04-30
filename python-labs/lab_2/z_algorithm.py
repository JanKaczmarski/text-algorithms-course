def len_of_common_prefix(s: str, t: str) -> int:
    i = 0
    while i < len(s) and i < len(t) and s[i] == t[i]:
        i += 1
    return i


def compute_z_array(s: str) -> list[int]:
    """
    Compute the Z array for a string.

    The Z array Z[i] gives the length of the longest substring starting at position i
    that is also a prefix of the string.

    Args:
        s: The input string

    Returns:
        The Z array for the string
    """
    # TODO: Implement the Z-array computation
    # For each position i:
    # - Calculate the length of the longest substring starting at i that is also a prefix of s
    # - Use the Z-box technique to avoid redundant character comparisons
    # - Handle the cases when i is inside or outside the current Z-box
    z = [0] * len(s)
    for k in range(1, len(s)):
        z[k] = len_of_common_prefix(s[k:], s)
 
    return z


def z_pattern_match(text: str, pattern: str) -> list[int]:
    """
    Use the Z algorithm to find all occurrences of a pattern in a text.

    Args:
        text: The text to search in
        pattern: The pattern to search for

    Returns:
        A list of starting positions (0-indexed) where the pattern was found in the text
    """
    # TODO: Implement pattern matching using the Z algorithm
    # 1. Create a concatenated string: pattern + special_character + text
    # 2. Compute the Z array for this concatenated string
    # 3. Find positions where Z[i] equals the pattern length
    # 4. Convert these positions in the concatenated string to positions in the original text
    # 5. Return all positions where the pattern is found in the text

    if len(pattern) == 0 or len(pattern) > len(text):
        return []

    res = []
    special_char = "|"

    comb = pattern + special_char + text

    arr = compute_z_array(comb)
    for i in range(len(pattern) + len(special_char) - 1, len(comb)):
        if arr[i] == len(pattern):
            res.append(i - len(pattern) - len(special_char))

    return res
