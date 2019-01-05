# This problem was asked by Amazon.

# Run-length encoding is a fast and simple method of encoding strings. 
# The basic idea is to represent repeated successive characters as a single count and character. 
#For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string to be encoded 
#have no digits and consists solely of alphabetic characters. 
#You can assume the string to be decoded is valid.
import unittest

def encode(input):
	count = 0
	output = ''
	prev = ''

	for c in input:
		if c == prev:
			count += 1
		else:
			if count is 0:
				output += c
			else:
				output += str(count + 1) + c
			prev = c
			count = 0

	if count is not 0:
		output += str(count + 1)

	return output



def decode(input):
	output = ''
	prev = ''
	
	for c in input:
		if c.isdigit():
			output += prev * (int(c) - 1)
		else:
			output += c
			prev = c

	return output

def main():
	a = decode('abc3')
	print(a)






class TestLinkedList(unittest.TestCase):
	def test_single_encode(self):
		self.assertEqual(encode('a'), 'a')
		self.assertEqual(encode('abc'), 'abc')
		self.assertEqual(encode('abdefq'), 'abdefq')

	def test_double_encode(self):
		self.assertEqual(encode('aa'), 'a2')
		self.assertEqual(encode('abbc'), 'ab2c')
		self.assertEqual(encode('aabbddeeffq'), 'a2b2d2e2f2q')

	def test_single_decode(self):
		self.assertEqual(decode('a'), 'a')
		self.assertEqual(decode('abc'), 'abc')
		self.assertEqual(decode('abdefq'), 'abdefq')

	def test_double_decode(self):
		self.assertEqual(decode('a2'), 'aa')
		self.assertEqual(decode('a2b2c2'), 'aabbcc')
		self.assertEqual(decode('ab2d2e3fq'), 'abbddeeefq')
		




if __name__ == '__main__':
	#main()
	unittest.main()

