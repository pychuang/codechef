/*
 * http://www.codechef.com/problems/MIXTURES
 */
#include <stdio.h>
#include <string.h>

static unsigned int mixtures[100];
static unsigned int n;
static unsigned int smoke_log[100][100];
static unsigned int mix_log[100][100];

static unsigned int min_smoke(int left, int right, unsigned int *best_mix)
{
	int i;
	unsigned int smallest_smoke = -1;

	if (smoke_log[left][right] != 0 || smoke_log[left][right] != 0) {
		*best_mix = mix_log[left][right];
		return smoke_log[left][right];
	}

	if (left == right) {
		*best_mix = mix_log[left][right] = mixtures[left];
		smoke_log[left][right] = 0;
		return 0;
	}

	if (left + 1 == right) {
		unsigned int a = mixtures[left];
		unsigned int b = mixtures[right];
		unsigned int smoke = a * b;

		*best_mix = mix_log[left][right] = (a + b) % 100;
		smoke_log[left][right] = smoke;
		return smoke;
	}

	for (i = left; i < right; i++) {
		unsigned int a;
		unsigned int b;
		unsigned int smoke;

		smoke = min_smoke(left, i, &a) + min_smoke(i+1, right, &b);
		smoke += a * b;
		if (smoke < smallest_smoke) {
			*best_mix = (a + b) % 100;
			smallest_smoke = smoke;
		}
	}

	mix_log[left][right] = *best_mix;
	smoke_log[left][right] = smallest_smoke;
	return smallest_smoke;
}

int main()
{
	while (scanf("%u", &n) != EOF) {
		int i;
		unsigned int s;
		unsigned int m;

		for (i = 0; i < n; i++) {
			unsigned int tmp;

			if (scanf(" %u", &tmp) != 1) {
				return -1;
			}

			mixtures[i] = tmp;
		}

		bzero(smoke_log, sizeof(smoke_log));
		bzero(mix_log, sizeof(mix_log));
		s = min_smoke(0, n-1, &m);
		printf("%u\n", s);
	}

	return 0;
}
