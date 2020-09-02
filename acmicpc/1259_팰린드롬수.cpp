//1259_팰린드롬수

#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <stack>

int main(void) {
	
	char str[6];

	while (1) {
		int flag = 0;
		scanf("%s", str);
		if (str[0] == '0' && strlen(str) == 1) break;
		
		for (int i = 0; i < strlen(str); i++)
			if (str[i] != str[strlen(str) - i - 1]) flag = 1;
		
		if (flag) printf("no\n");
		else printf("yes\n");
	
	}

	return 0;

}