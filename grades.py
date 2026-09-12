"""Grade calculation logic for the HKU grading helper.

A simplified scheme — check your course syllabus for the actual boundaries.
"""

# HKU grade boundaries used by this app.
BOUNDARIES = [
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
    (0, "F"),
]


def compute_average(scores):
    """Return the mean of a list of numeric scores.

    Returns 0 if the list is empty (avoids a division-by-zero crash).
    """
    if not scores:
        return 0
    return sum(scores) / len(scores)


def letter_grade(average):
    """Return a letter grade (with an emoji) for a numeric average.

    Boundaries:
        A: 90+
        B: 80-89
        C: 70-79
        D: 60-69
        F: <60
    """
    EMOJIS = {
        "A": "🌟",
        "B": "👍",
        "C": "📚",
        "D": "📝",
        "F": "💪",
    }
    for cutoff, letter in BOUNDARIES:
        if average >= cutoff:
            return f"{EMOJIS[letter]} {letter}"
    return f"{EMOJIS['F']} F"  # fallback; should not be reached