def levenshtein_distance(s1: str, s2: str) -> int:
    """
    Oblicza odległość Levenshteina między dwoma ciągami znaków.

    Args:
        s1: Pierwszy ciąg znaków
        s2: Drugi ciąg znaków

    Returns:
        Odległość Levenshteina (minimalna liczba operacji wstawienia, usunięcia
        lub zamiany znaku potrzebnych do przekształcenia s1 w s2)
    """
    m, n = len(s1), len(s2)

    # Przypadki brzegowe
    if m == 0:
        return n
    if n == 0:
        return m

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicjalizacja pierwszego wiersza i kolumny
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        # koszt dodania wszystkich liter z s2[:j]
        dp[0][j] = j

    # Wypełnianie macierzy
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                # usuwanei
                dp[i - 1][j] + 1,
                # wstawienie
                dp[i][j - 1] + 1,
                # zmiana
                dp[i - 1][j - 1] + cost,
            )

    return dp[m][n]
