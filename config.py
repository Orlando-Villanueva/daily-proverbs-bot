# Specific verses to include (format: (chapter, start_verse, end_verse))
INCLUDED_RANGES = [
    (1, 7, 10),  # Proverbs 1:7-10
    (1, 20, 20),  # Proverbs 1:20
    (3, 1, 3),  # Proverbs 3:1-3
    (3, 5, 7),  # Proverbs 3:5-7
    (3, 9, 14),  # Proverbs 3:9-14
    (3, 19, 19),  # Proverbs 3:19
    (3, 21, 21),  # Proverbs 3:21
    (3, 25, 25),  # Proverbs 3:25
    (3, 27, 35),  # Proverbs 3:27-35
    (4, 1, 1),  # Proverbs 4:1
    (4, 3, 3),  # Proverbs 4:3
    (4, 5, 5),  # Proverbs 4:5
    (4, 7, 7),  # Proverbs 4:7
    (4, 14, 14),  # Proverbs 4:14
    (4, 18, 19),  # Proverbs 4:18-19
    (4, 23, 27),  # Proverbs 4:23-27
    (5, 1, 1),  # Proverbs 5:1
    (5, 3, 3),  # Proverbs 5:3
    (5, 15, 15),  # Proverbs 5:15
    (5, 18, 18),  # Proverbs 5:18
    (5, 20, 22),  # Proverbs 5:20-22
    (6, 6, 6),  # Proverbs 6:6
    (6, 9, 10),  # Proverbs 6:9-10
    (6, 12, 12),  # Proverbs 6:12
    (6, 16, 16),  # Proverbs 6:16
    (6, 20, 20),  # Proverbs 6:20
    (6, 23, 23),  # Proverbs 6:23
    (6, 26, 26),  # Proverbs 6:26
    (6, 30, 30),  # Proverbs 6:30
    (6, 32, 32),  # Proverbs 6:32
    (7, 1, 1),  # Proverbs 7:1
    (7, 4, 4),  # Proverbs 7:4
    (8, 5, 5),  # Proverbs 8:5
    (8, 12, 13),  # Proverbs 8:12-13
    (9, 7, 10),  # Proverbs 9:7-10
    (23, 6, 6),  # Proverbs 23:6
    (23, 9, 10),  # Proverbs 23:9-10
    (23, 12, 13),  # Proverbs 23:12-13
    (23, 17, 18),  # Proverbs 23:17-18
    (23, 20, 20),  # Proverbs 23:20
    (23, 22, 24),  # Proverbs 23:22-24
    (23, 31, 31),  # Proverbs 23:31
    (30, 4, 6),  # Proverbs 30:4-6
    (30, 8, 14),  # Proverbs 30:8-14
    (31, 3, 10),  # Proverbs 31:3-10
    (31, 30, 30),  # Proverbs 31:30
]

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
    (23, 5, 5),
    (24, 32, 32)
]

# Convert ranges to individual verses for processing
EXCLUDED_VERSES = [(chapter, verse) for chapter, start, end in EXCLUDED_RANGES
                   for verse in range(start, end + 1)]

# Convert ranges to individual verses for processing
INCLUDED_VERSES = [(chapter, verse) for chapter, start, end in INCLUDED_RANGES
                   for verse in range(start, end + 1)]

# Generate verse references combining chapter mapping and specific inclusions
PROVERBS_VERSES = (
    # Add specifically included verses first
    INCLUDED_VERSES +
    # Then add verses from chapter mapping
    [(chapter, verse) for chapter, count in CHAPTER_VERSES.items()
     for verse in range(1, count + 1)
     if (chapter, verse) not in EXCLUDED_VERSES and
     (chapter, verse) not in INCLUDED_VERSES])
