#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include <stdio.h>
#include <string.h>

int main(void) {
	char str[51][51];

	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", str[i]);
	}

	for (int i = 0; i < strlen(str[0]); i++) {
		bool flag = true;
		for (int j = 0; j < n; j++) {
			if (str[j][i] != str[0][i]) {
				printf("?");
				flag = false;
				break;
				
			}
		}
		if (flag) {
			printf("%c", str[0][i]);
		}
	}

	return 0;

}