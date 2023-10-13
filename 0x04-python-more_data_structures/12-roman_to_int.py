#!/usr/bin/python3

def roman_to_int(roman_string):
	roman_num = {
			'I': 1,
			'V': 5,
			'X': 10,
			'L': 50,
			'C': 100,
			'D': 500,
			'M': 1000}
	result = 0

	if not isinstance(roman_string, str) or roman_string is None:
		return 0

	prev_val = 0
	for num in reversed(roman_string):
		val = roman_num.get(num, 0)
		if val >= prev_val:
			result += val
		else:
			result -= val
		prev_val = val

	return result
