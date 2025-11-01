# Mad Libs Game
# Author: Kunal Tibe
# Description: A fun word game where users fill in blanks to create a silly story.

print("---Let's play Mad Libs!---\n")

noun1 = input("Enter a noun (person or place or thing): ")
adjective1 = input("Enter a adjective (description): ")
noun2 = input("Enter a noun (person or place or thing): ")
verb1 = input("Enter a verb ending with 'ed': ")
adverb1 = input("Enter a adverb ending with 'ly' (modifies verb): ")
adjective2 = input("Enter a adjective (description): ")
noun3 = input("Enter a noun (person or place or thing): ")

story = f"""Today I went to the {noun1}. It was a {adjective1} day!
I saw a {noun2} that {verb1} {adverb1} across the street.
Everyone stopped to look — it was so {adjective2}!
Later, I found a {noun3} that reminded me of the adventure.
What a day!"""

print("\n--- Your Mad Libs Story ---")
print(story)
