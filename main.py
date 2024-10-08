#!/usr/bin/python3
from collections import defaultdict

def main():
	book_path = "books/frankenstein.txt"
	with open(book_path, 'r') as f:
		file_contents = f.read()
	words = file_contents.split()
	print(file_contents)
	print(f"--- Begin report of {book_path} ---")
	print(f"{len(words)} words found in the document")
	print()
	characters = count_char(file_contents)
	report(characters)
	print("--- End report ---")

def sort_on(dict):
    return dict[int]

def count_char(file_contents):
	characters = defaultdict(int)
	small_case = file_contents.lower()
	for character in small_case:
		if str.isalpha(character):
			characters[character] += 1
	characters = dict(sorted(characters.items()))
	return characters

def report(characters):
	characters = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True))
	for character in characters:
		print(f"The {character} character was found {characters[character]} times")

main()