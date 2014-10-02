#! /usr/bin/env python
# http://www.codechef.com/problems/TREERGB
import sys
import itertools

# global variables
N = 0
RLIMIT = 0
GLIMIT = 0
BLIMIT = 0

RED = 0
GREEN = 1
BLUE = 2
COLORS = [RED, GREEN, BLUE]

links = set()

# structure of a tree node:
#	(id, children[])
nodes = {}
tree = None

# add children to the node
def construct_node(parent):
	global links
	global nodes
	global tree

	parent_node = nodes[parent]

	children = [n2 for (n1, n2) in links if n1 == parent]
	for child in children:
		child_node = nodes[child]
		parent_node[1].append(child_node)

		# remove links
		links.remove((parent, child))
		links.remove((child, parent))

		construct_node(child)

def build_tree():
	global N
	global nodes
	global tree

	for i in range(1, N+1):
		nodes[i] = (i, [])

	tree = nodes[1]
	construct_node(1)
#	print tree

def parse_input():
	global N
	global RLIMIT
	global GLIMIT
	global BLIMIT
	global links

	firstline = sys.stdin.readline()
	(N, RLIMIT, GLIMIT, BLIMIT) = map(int, firstline.split())
#	print N, RLIMIT, GLIMIT, BLIMIT

	for line in sys.stdin:
		(n1, n2) = map(int, line.split())
		links.add((n1, n2))
		links.add((n2, n1))

#	print 'LINKS: ', links

def merge_colorsets(colorsets):
#	print 'MERGE: ', colorsets
	count_table = {}
	for (r, g, b, cnt) in colorsets:
		if (r, g, b) in count_table:
			count = count_table[(r, g, b)]
		else:
			count = 0

		count_table[(r, g, b)] = cnt + count

	merged = [(r, g, b, count_table[(r, g, b)]) for (r, g, b) in count_table]
#	print 'MERGED: ', merged
	return merged

# format of lists_of_colorsets:
#	[[(r, g, b, cnt), (r, g, b, cnt), ...], [(r, g, b, cnt), (r, g, b, cnt), ...], ...]
def combine_lists_of_colorsets(lists_of_colorsets):
#	print 'COMBINE SUB: ', lists_of_colorsets
	newlist = []
	for combination in itertools.product(*lists_of_colorsets):
#		print 'PRODUCT: ', combination
		# format of combination
		#	[(r, g, b, cnt), (r, g, b, cnt), ...]

		newr = 0
		newg = 0
		newb = 0
		newcnt = 1
		for (r, g, b, cnt) in combination:
			newr += r
			newg += g
			newb += b
			newcnt *= cnt

		newlist.append((newr, newg, newb, newcnt))

#	print 'COMBINED SUB: ', newlist
	return newlist

def get_colorsets_of_a_subtree(node):
#	print 'GET SUB: ', node
	tmp = []
	for color in COLORS:
		tmp.extend(get_colorsets(node, color))

	return tmp

def get_colorsets_of_subtrees(child_nodes):
	lists_of_colorsets = []

	for child_node in child_nodes:
		tmp = get_colorsets_of_a_subtree(child_node)

		lists_of_colorsets.append(tmp)

	return combine_lists_of_colorsets(lists_of_colorsets)

def update_colorsets_with_parent_color(colorsets, color):
#	print 'UPDATE: ', colorsets
	if color == 0:
		colorsets = [(r + 1, g, b, cnt) for (r, g, b, cnt) in colorsets]
	elif color == 1:
		colorsets = [(r, g + 1, b, cnt) for (r, g, b, cnt) in colorsets]
	elif color == 2:
		colorsets = [(r, g, b + 1, cnt) for (r, g, b, cnt) in colorsets]

#	print 'UPDATED: ', colorsets
	return colorsets

def apply_restriction(colorsets, color):
	global RLIMIT
	global GLIMIT
	global BLIMIT

#	print 'APPLY: ', colorsets
	if color == 0:
		colorsets = [(r, g, b, cnt) for (r, g, b, cnt) in colorsets if r <= RLIMIT]
	elif color == 1:
		colorsets = [(r, g, b, cnt) for (r, g, b, cnt) in colorsets if g <= GLIMIT]
	elif color == 2:
		colorsets = [(r, g, b, cnt) for (r, g, b, cnt) in colorsets if b <= BLIMIT]

#	print 'APPLIED: ', colorsets
	return colorsets

def apply_restriction_then_merge(colorsets, color):
	tmp = apply_restriction(colorsets, color)
	return merge_colorsets(tmp)

# return [(r, g, b, cnt), (r, g, b, cnt), ...]
#	r: red nodes in this subtree
#	g: green nodes in this subtree
#	b: blue nodes in this subtree
#	cnt: possible combinations in this colorset
def get_colorsets(node, color):
	global COLORS

#	print 'GET node ', node[0], ' COLOR ', color
	child_nodes = node[1]
	if not child_nodes:
		colorsets = [(0, 0, 0, 1)]
	else:
		colorsets = get_colorsets_of_subtrees(child_nodes)

	colorsets = update_colorsets_with_parent_color(colorsets, color)
	colorsets = apply_restriction_then_merge(colorsets, color)
#	print 'GOT node ', node[0], ' COLOR ', color, ' COLORSET: ', colorsets
	return colorsets

def count():
	global tree

	colorsets = []
	colorsets.extend(get_colorsets(tree, 0))	# red
	colorsets.extend(get_colorsets(tree, 1))	# green
	colorsets.extend(get_colorsets(tree, 2))	# blue

	count = 0
	for (r, g, b, cnt) in colorsets:
		count += cnt

	return count

def main():
	parse_input()
	build_tree()
	print count()

if __name__ == '__main__':
	main()
