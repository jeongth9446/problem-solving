#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <stack>

int main(void) {

	char a[100], b[100];

	scanf("%s %s", a, b);
	int max = 0;

	for (int i = 0; i <= strlen(b) - strlen(a); i++) {
		int cnt = 0;
		for (int j = 0; j < strlen(a); j++) {
			if (b[i + j] == a[j]) cnt++;
		}
		if (max < cnt) max = cnt;
	}

	printf("%d\n", strlen(a) - max);

	return 0;

}