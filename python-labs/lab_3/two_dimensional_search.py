from typing import List, Tuple

from .aho_corasick_algorithm import AhoCorasick


def transpose(matrix: List[str]) -> List[str]:
    return ["".join(row[i] for row in matrix) for i in range(len(matrix[0]))]


def find_pattern_in_column(text_column: str, pattern_columns: list[str]) -> list[tuple[int, int]]:
    """
    Wyszukuje wszystkie kolumny wzorca w kolumnie tekstu.

    Args:
        text_column: Kolumna tekstu
        pattern_columns: Lista kolumn wzorca

    Returns:
        Lista krotek (pozycja, indeks kolumny), gdzie znaleziono kolumnę wzorca
    """
    # TODO: Zaimplementuj wyszukiwanie kolumn wzorca w kolumnie tekstu
    # TODO: Dla każdej kolumny wzorca, przeszukaj kolumnę tekstu
    # TODO: Zwróć listę krotek (pozycja, indeks kolumny) dla znalezionych dopasowań
    ac = AhoCorasick(pattern_columns)
    matches = ac.search(text_column)
    return [(i, k) for (i, p) in matches for k, pat in enumerate(pattern_columns) if pat == p]


def find_pattern_2d(text: list[str], pattern: list[str]) -> list[tuple[int, int]]:
    """
    Wyszukuje wzorzec dwuwymiarowy w tekście dwuwymiarowym.

    Args:
        text: Tekst dwuwymiarowy (lista ciągów znaków tej samej długości)
        pattern: Wzorzec dwuwymiarowy (lista ciągów znaków tej samej długości)

    Returns:
        Lista krotek (i, j), gdzie (i, j) to współrzędne lewego górnego rogu wzorca w tekście
    """
    # TODO: Zaimplementuj wyszukiwanie wzorca dwuwymiarowego
    # TODO: Obsłuż przypadki brzegowe (pusty tekst/wzorzec, wymiary)
    # TODO: Sprawdź, czy wszystkie wiersze mają taką samą długość
    # TODO: Zaimplementuj algorytm wyszukiwania dwuwymiarowego
    # TODO: Zwróć listę współrzędnych lewego górnego rogu dopasowanego wzorca
    if not text or not pattern or not text[0] or not pattern[0]:
        return []

    H, W = len(text), len(text[0])
    h, w = len(pattern), len(pattern[0])
    if h > H or w > W:
        return []

    text_cols = transpose(text)
    pattern_cols = transpose(pattern)

    T = [[-1] * W for _ in range(H)]

    for j, col_text in enumerate(text_cols):
        matches = find_pattern_in_column(col_text, pattern_cols)
        for i, pattern_col_idx in matches:
            if 0 <= i <= H - h:
                T[i][j] = pattern_col_idx

    result = []
    expected_sequence = list(range(w))

    for i in range(H - h + 1):
        row = T[i]
        for j in range(W - w + 1):
            if row[j : j + w] == expected_sequence:
                result.append((i, j))
    return result
