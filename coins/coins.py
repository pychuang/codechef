#! /usr/bin/env python
# http://www.codechef.com/problems/COINS
import sys

def change(n):
	if n == 0:
		return 0

	x = change(n / 2)
	y = change(n / 3)
	z = change(n / 4)
	if n < x + y + z:
		return x + y + z
	else:
		return n

def main():
	for line in sys.stdin:
		(n, ) = map(int, line.split())
		print change(n)

if __name__ == '__main__':
	main()
