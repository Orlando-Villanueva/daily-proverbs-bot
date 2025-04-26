# Verses to exclude (format: (chapter, start_verse, end_verse))
# For single verses, use the same verse number for start and end
EXCLUDED_RANGES = [
    (10, 1, 1),    # Exclude Proverbs 10:1
    (23, 3, 3),    # Exclude Proverbs 23:3
    (23, 28, 30),  # Exclude Proverbs 23:29-30
    (23, 32, 35),  # Exclude Proverbs 23:32-35
    (25, 1, 1),    # Exclude Proverbs 25:1
]

# Convert ranges to individual verses for processing
EXCLUDED_VERSES = [
    (chapter, verse)
    for chapter, start, end in EXCLUDED_RANGES
    for verse in range(start, end + 1)
]

# Special verses that need custom handling
SPECIAL_VERSES = [
    (25, 6),  # First part: Proverbs 25:6-7a
    (25, 7),  # Second part: Proverbs 25:7b-8
]

# Specific verses to include (if empty, uses all verses except excluded ones)
INCLUDED_VERSES = []

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
    23: 35,
    24: 34,
    25: 28,
    26: 28,
    27: 27,
    28: 28,
    29: 27
}

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
