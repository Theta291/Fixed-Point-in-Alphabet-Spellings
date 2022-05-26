letter_spellings = {
    'a': "a",
    'b': "bee",
    'c': "cee",
    'd': "dee",
    'e': "e",
    'f': "ef",
    'g': "gee",
    'h': "aitch",
    'i': "i",
    'j': "jay",
    'k': "kay",
    'l': "el",
    'm': "em",
    'n': "en",
    'o': "o",
    'p': "pee",
    'q': "cue",
    'r': "ar",
    's': "es",
    't': "tee",
    'u': "u",
    'v': "vee",
    'w': "doubleu",
    'x': "ex",
    'y': "wy",
    'z': "zee",
}


spelling_letters = {value: key for key, value in letter_spellings.items()}


alphabet = sorted(letter_spellings.keys())


def lexicographic_comparison(ordering):
	def cmp(string1, string2):
		l1 = len(string1)
		l2 = len(string2)
		s1, s2, lt = (string1, string2, True) if l1 <= l2 else (string2, string1, False)
		for char1, char2 in zip(s1, s2):
			i1 = ordering.index(char1)
			i2 = ordering.index(char2)
			if i1 < i2:
				return lt
			elif i1 > i2:
				return not lt
		return lt

	return cmp


def merger(cmp):
	def merge(l1, l2):
		combined = []
		index1 = 0
		index2 = 0
		while index1 < len(l1) and index2 < len(l2):
			a = l1[index1]
			b = l2[index2]
			if cmp(a, b):
				combined.append(a)
				index1 += 1
			else:
				combined.append(b)
				index2 += 1
		if index1 < len(l1):
			combined.extend(l1[index1:])
		else:
			combined.extend(l2[index2:])
		return combined

	return merge


def merge_sorter(cmp):
	merge = merger(cmp)

	def sort(a_list):
		half_size = int(len(a_list) / 2)
		if half_size:
			part_1 = sort(a_list[:half_size])
			part_2 = sort(a_list[half_size:])
			return merge(part_1, part_2)
		else:
			return a_list

	return sort


def permute_to_permute(ordering):
	cmp = lexicographic_comparison(ordering)
	mergesort = merge_sorter(cmp)
	spellings_ordered = mergesort([letter_spellings[letter] for letter in ordering])
	return [spelling_letters[spelling] for spelling in spellings_ordered]


orders = []
curr_order = alphabet.copy()
orders.append(curr_order)
while True:
	new_order = permute_to_permute(curr_order)

	if new_order in orders:
		orders.append(new_order)
		break
	else:
		orders.append(new_order)
		curr_order = new_order

for order in orders:
  print(order)


# takeaways:
# make OOP letters (easier to add functionality, more readable)
# Don't think of things with Python lens (e.g. most other languages have comparison based sorting, don't get too hung up of keyfunc problem)
# avoid dictionary pattern (k: v)
# think more about functions accepting single objects (def func(*posargs))
