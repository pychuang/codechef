/*
 * http://www.codechef.com/problems/COINS
 */
#include <stdio.h>

#define MAX_N		1000000000
#define TABLE_SIZE	(1 << 20)

static unsigned int saved[TABLE_SIZE];

static unsigned int change(unsigned int n)
{
	unsigned int x, y, z;
	unsigned int max;

	if (n == 0) {
		return 0;
	}

	if (n < TABLE_SIZE && saved[n] != 0) {
		return saved[n];
	}

	x = change(n / 2);
	y = change(n / 3);
	z = change(n / 4);
	max = n < (x + y + z) ? (x + y + z) : n;

	if (n < TABLE_SIZE) {
		saved[n] = max;
	}

	return max;
}

int main()
{
	unsigned int n;

	while (scanf("%u", &n) != EOF) {
		int ret = change(n);

		printf("%u\n", ret);
	}

	return 0;
}
