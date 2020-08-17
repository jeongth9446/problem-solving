#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void) {

	char str[101];

	scanf("%s", str);

	for (int i = 0; i < strlen(str); i++) {
		if (str[i] != str[strlen(str) - i - 1]) {
			printf("%d\n", 0);
			return 0;
		}
	}
	printf("%d\n", 1);
	return 0;

}