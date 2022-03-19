//2711_오타맨 고창영

#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <stack>

int main(void) {
	
	int t;
	scanf("%d", &t);
	while (t--) {
		int m;
		char str[100];
		scanf("%d %s", &m, str);

		for (int i = 0; i < strlen(str); i++) {
			if (i != m - 1) printf("%c", str[i]);
		}
		printf("\n");
	}

	return 0;

}