# Specific verses to include (if empty, uses all verses except excluded ones)
INCLUDED_VERSES = [(1, 7), (1, 8), (1, 9), (1, 10), (3, 1), (3, 2), (3, 3),
                   (3, 5), (3, 6), (3, 7), (3, 9), (3, 10), (3, 11), (3, 12),
                   (3, 13), (3, 14), (3, 19), (3, 21), (3, 25), (3, 27),
                   (3, 28), (3, 29), (3, 30), (3, 31), (3, 32),
                   (3, 33), (3, 34), (3, 35), (4, 1), (4, 2), (4, 3), (4, 4),
                   (4, 5), (4, 7), (4, 14), (4, 18), (4, 19), (4, 23), (4, 24),
                   (4, 25), (4, 26), (4, 27), (5, 1), (5, 3), (5, 15), (5, 18),
                   (5, 20), (5, 21), (5, 22), (6, 6), (6, 9), (6, 10), (6, 12),
                   (6, 16), (6, 20), (6, 23), (6, 26),
                   (6, 30), (6, 32), (7, 1), (7, 4), (8, 5), (8, 12), (8, 13),
                   (9, 7), (9, 8), (9, 9), (9, 10), (23, 6), (23, 9), (23, 10),
                   (23, 12), (23, 13), (23, 17), (23, 18), (23, 20), (23, 22),
                   (23, 23), (23, 24), (23, 31), (30, 4), (30, 5), (30, 6),
                   (30, 8), (30, 9), (30, 10), (30, 11), (30, 12), (30, 13),
                   (30, 14), (31, 3), (31, 4), (31, 5), (31, 6), (31, 7),
                   (31, 8), (31, 9), (31, 10), (31, 30)]

# Dictionary mapping chapters to their verse counts
CHAPTER_VERSES = {
    10: 32,
    11: 31,
    12: 28,
    13: 25,
    14: 35,
    15: 33,
    16: 33,
    17: 28,
    18: 24,
    19: 29,
    20: 30,
    21: 31,
    22: 29,
    24: 34,
    25: 28,
    26: 28,
    27: 27,
    28: 28,
    29: 27
}

# Verses to exclude (format: (chapter, start_verse, end_verse))
# For single verses, use the same verse number for start and end
EXCLUDED_RANGES = [
    (10, 1, 1),  # Exclude Proverbs 10:1
    (25, 1, 1),  # Exclude Proverbs 25:1
    (22, 17, 21),  # Exclude Proverbs 22:17-21
    (22, 27, 27),  # Exclude Proverbs 22:27
]

# Convert ranges to individual verses for processing
EXCLUDED_VERSES = [(chapter, verse) for chapter, start, end in EXCLUDED_RANGES
                   for verse in range(start, end + 1)]

# Generate verse references combining chapter mapping and specific inclusions
PROVERBS_VERSES = (
    # Add specifically included verses first
    INCLUDED_VERSES +
    # Then add verses from chapter mapping
    [(chapter, verse) for chapter, count in CHAPTER_VERSES.items()
     for verse in range(1, count + 1)
     if (chapter, verse) not in EXCLUDED_VERSES])

# Default translation to use
TRANSLATION = "KJV"
