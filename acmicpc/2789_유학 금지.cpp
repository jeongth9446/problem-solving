#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <stack>

int main(void) {

	char str[1001];

	scanf("%s", str);

	for (int i = 0; i < strlen(str); i++) {
		if (str[i] == 'C' || str[i] == 'A' || str[i] == 'M' || str[i] == 'B' || str[i] == 'R' || str[i] == 'I' || str[i] == 'D' || str[i] == 'G' || str[i] == 'E')
			continue;
			
		printf("%c", str[i]);
	}

	printf("\n");
	return 0;

}