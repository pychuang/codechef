/*
 * http://www.codechef.com/problems/MARBLES
 */
#include <stdio.h>

/*
 * C(n, k) = C(n, n-k)
 *         = n! / (k! * (n-k)!)
 *
 *            (n)*(n-1)*...*(n+1)
 *         = ---------------------------
 *                    (n-k)!
 */
static long long combinations(unsigned int n, unsigned int k)
{
	unsigned int i;
	long long val = 1;

	/*
	 * C(n, k) = C(n, n-k)
	 * We want a small k
	 */
	k = n-k < k ? n-k : k;

	for (i = 1; i <= k; i++, n--) {
		val *= n;
		val /= i;
	}

	return val;
}

/*
 * H(n, k) = C(n+k-1, k-1)
 */
static long long selections(unsigned int n, unsigned int k)
{
	return combinations(n+k-1, k-1);
}

int main()
{
	unsigned int i;

	scanf("%u", &i);
	for (; i > 0; i--) {
		unsigned int n, k;

		if (scanf("%u %u", &n, &k) != 2) {
			return -1;
		}

		printf("%lld\n", selections(n-k, k));
	}

	return 0;
}
