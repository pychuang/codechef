#! /usr/bin/env python
# http://www.codechef.com/problems/POUR1
import sys

def check(a, b, target):
	if a == target or b == target:
		return True
	return False

def tryone(a, amax, b, bmax, states, target):
	if (a, b) not in states:
		states.add((a, b))
		steps = find(a, amax, b, bmax, states, target)
		if steps >= 0:
			return steps
	return -1

def find(a, amax, b, bmax, states, target):
	if check(a, b, target):
		return 0

	nextstep = []

	# empty a
	nextstep.append((0, b))

	# empty b
	nextstep.append((a, 0))

	# fill a
	nextstep.append((amax, b))

	# fill b
	nextstep.append((a, bmax))

	# pour a
	bleft = bmax - b
	if a <= bleft:
		anew  = 0
		bnew = b + a
	else:
		bnew = bmax
		anew = a - bleft

	nextstep.append((anew, bnew))

	# pour b
	aleft = amax - a
	if b <= aleft:
		bnew  = 0
		anew = b + a
	else:
		anew = amax
		bnew = b - aleft

	nextstep.append((anew, bnew))

	# try
	stepslog = []
	for (anew, bnew) in nextstep:
		steps = tryone(anew, amax, bnew, bmax, states, target)
		if steps >= 0:
			stepslog.append(steps + 1)

	if not stepslog:
		return -1

	return min(stepslog)

def pour1(amax, bmax, target):

	states = set()
	states.add((0, 0))
	return find(0, amax, 0, bmax, states, target)

def main():
	t = int(raw_input())

	for i in range(t):
		a = int(raw_input())
		b = int(raw_input())
		c = int(raw_input())

		print pour1(a, b, c)

if __name__ == '__main__':
	main()
