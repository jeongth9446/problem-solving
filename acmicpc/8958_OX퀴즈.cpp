#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main(void) {

	char result[80];

	int n;
	
	scanf("%d", &n);

	while (n--) {
		scanf("%s", result);
		int c = 0;
		int s = 0;
		for (int i = 0; i < strlen(result); i++) {
			if (result[i] == 'O') s += ++c;
			else c = 0;
		}
		printf("%d\n", s);

		
	
	}

	return 0;
}
