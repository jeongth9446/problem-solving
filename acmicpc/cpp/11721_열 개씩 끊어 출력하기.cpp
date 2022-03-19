//11721_열 개씩 끊어 출력하기

#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <stack>

int main(void) {
	char str[101];
	scanf("%s", str);

	for (int i = 0; i < strlen(str); i++) {
		printf("%c", str[i]);
		if ((i + 1) % 10 == 0) printf("\n");

	}
	printf("\n");

	return 0;

}