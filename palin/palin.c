/*
 * http://www.codechef.com/problems/PALIN
 */
#include <stdio.h>
#include <string.h>

#define MAX_LENGTH	1000002
static char number[MAX_LENGTH];
enum status { UNCHANGED, LARGER, SMALLER, };

static void next_palindrome(void)
{
	size_t len = strlen(number);
	enum status status = UNCHANGED;
	int i, j;

	for (i = 0, j = len - 1; i < j; i++, j--) {
		char high_digit = number[i];
		char low_digit = number[j];

		number[j] = high_digit;
		if (high_digit > low_digit) {
			status = LARGER;
		} else if (high_digit < low_digit) {
			status = SMALLER;
		}
	}

	if (status == LARGER) {
		return;
	}

	/* increase digit i, j */
	for (; i >=0; i--, j++) {
		char high_digit = number[i];

		if (i > j) {
			continue;
		}

		/* increase digit */
		if (high_digit == '9') {
			/* need to carry in */
			high_digit = '0';
		} else {
			high_digit++;
		}

		number[i] = high_digit;
		number[j] = high_digit;

		if (high_digit != '0') {
			return;
		}
	}

	/* all digits are 9 */
	number[0] = '1';
	number[len] = '1';
	number[len+1] = '\0';
}

int main()
{
	unsigned int i;

	scanf("%u", &i);
	for (; i > 0; i--) {
		if (scanf(" %s", number) == EOF) {
			break;
		}

		next_palindrome();
		printf("%s\n", number);
	}

	return 0;
}
