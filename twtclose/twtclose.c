/*
 * http://www.codechef.com/problems/TWTCLOSE
 */
#include <stdio.h>
#include <string.h>

static int tweets[1000];
static unsigned int open_tweets;

static unsigned int click(unsigned int t)
{
	if (tweets[t] == 0) {	/* was closed */
		tweets[t] = 1;
		open_tweets++;
	} else {		/* was open */
		tweets[t] = 0;
		open_tweets--;
	}

	return open_tweets;
}

static unsigned int closeall(void)
{
	bzero(tweets, sizeof(tweets));
	open_tweets = 0;
	return open_tweets;
}

int main()
{
	unsigned int n, k;

	scanf("%u %u", &n, &k);
	for (; k > 0; k--) {
		static char cmd[10];
		int ret;
		unsigned int t;
		unsigned int ot;

		if ((ret = scanf("%s %u", cmd, &t)) < 1) {
			return -1;
		}

		switch (ret) {
		case 2:
			ot = click(t - 1);
			break;
		case 1:
			ot = closeall();
			break;
		default:
			return -2;
		}

		printf("%u\n", ot);
	}

	return 0;
}
