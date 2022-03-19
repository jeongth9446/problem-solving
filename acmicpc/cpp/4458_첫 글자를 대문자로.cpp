//4458_첫 글자를 대문자로

#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <stack>

int main(void) {
	char str[31];

	int n;
	scanf("%d", &n);
	gets(str);
	while (n--) {
		gets(str);

		if (str[0] >= 97) printf("%c", str[0] - 'a'+'A');
		else printf("%c", str[0]);

		for (int i = 1; i < strlen(str); i++)
			printf("%c", str[i]);
			
		printf("\n");
		
	}

	return 0;


}