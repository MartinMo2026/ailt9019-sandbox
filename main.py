"""HKU grading helper · tiny app for the AILT9019 vibe-coding tutorial.

Run me with: python main.py
Type 'done' when you have entered all your scores.
"""

import grades


def main():
    print("=== HKU Grade Calculator ===")
    print("Enter assignment scores one at a time.")
    print("Type 'done' (or just press Enter on an empty line) when finished.\n")

    scores = []
    while True:
        entry = input("Score (or 'done'): ").strip()
        if entry == "" or entry.lower() == "done":
            break
        try:
            score = float(entry)
            if score < 0:
                print(f"  {score} is negative — scores must be 0 or above. Try again.")
                continue
            scores.append(score)
        except ValueError:
            print(f"  '{entry}' is not a number — try again.")

    if not scores:
        print("\nNo scores entered. Bye.")
        return

    avg = grades.compute_average(scores)
    grade = grades.letter_grade(avg)

    print(f"\nYou entered {len(scores)} score(s).")
    print(f"Average: {avg:.2f}")
    print(f"Final grade: {grade}")


if __name__ == "__main__":
    main()