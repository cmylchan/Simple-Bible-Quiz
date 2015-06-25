import random


def shuffle(list_to_shuffle):
	"""
	Shuffles a list of things. 
	"""

	shuffled = []
	list_to_shuffle = list(list_to_shuffle)
	N = len(list_to_shuffle)
	for x in range(0, N):
		idx = int(random.random() * len(list_to_shuffle))
		shuffled.append(list_to_shuffle.pop(idx))
	return shuffled


if __name__ == '__main__':
	booktitle = raw_input("Please specify which book you would like to take a test on:> ")
	book = __import__('books.' + booktitle)
	book = eval('book.' + booktitle)
	book = book.chapters

	print("Please specify what kind of test you would like to take: ")
	print("     1. Identify Chapter From Heading")
	print("     2. List Headings in Chapter")

	mode = raw_input('Type the number of the choice and hit enter to begin:> ')
	mode = int(mode)

	if mode == 1:
		# This means we give a random header and ask them to identify where it's from.
		book_heading_pairs = []
		for chapter in book.keys():
			for heading in book[chapter]:
				book_heading_pairs.append((chapter, heading))
		book_heading_pairs = shuffle(book_heading_pairs)
		score = 0
		for idx, pair in enumerate(book_heading_pairs):
			print("Where is this heading from? (%d/%d)" % (idx + 1, len(book_heading_pairs)))
			print("    " + pair[1])

			attempt = raw_input("    > ")
			if attempt == str(pair[0]):
				score += 1
			else:
				print("        You thought it was from chapter " + str(attempt))
				print("        But it's really from chapter    " + str(pair[0]))

		print("You got " + str(score) + " out of " + str(len(book_heading_pairs)) + " correct.")

	elif mode == 2:
		# This means we pull a random chapter and ask what headers are in it
		chapter_order = shuffle(book.keys())
		chapter_scores = []
		for chapter in chapter_order:
			print("Please list the headings from chapter " + str(chapter))
			chapter_score = 0.0
			for iii in range(0, len(book[chapter])):
				heading = book[chapter][iii]
				attempt = raw_input("    > ")
				if attempt.lower() == heading.lower():
					chapter_score += 1.0
				else:
					print("        You typed: " + attempt)
					print("        Correct:   " + heading)
			chapter_scores.append(chapter_score / len(book[chapter]))

		print("Your final scores by chapter are: ")
		for chapter, score in zip(chapter_order, chapter_scores):
			print("    " + str(chapter) + ": " + str(score))
		print "Average: " + str(sum(chapter_scores) / len(chapter_scores))

	elif mode == 3:
		# This should be for random trivia mode.
		pass