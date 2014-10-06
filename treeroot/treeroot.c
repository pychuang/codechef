/*
 * http://www.codechef.com/problems/TREEROOT
 */
#include <stdio.h>

int main()
{
	unsigned int t;

	scanf("%u", &t);
	for (; t > 0; t--) {	/* for each case */
		unsigned int n;
		int count = 0;

		scanf("%u", &n);
		for (; n > 0; n--) {
			unsigned int id;
			unsigned int sum;

			scanf("%u %u", &id, &sum);

			count += id;
			count -= sum;
		}

		printf("%d\n", count);
	}

	return 0;
}
