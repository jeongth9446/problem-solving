#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>


int main(void) {

	char n[100];
	scanf("%s", n);

	for (int i = 0; i < strlen(n); i++) {
		for (int j = i + 1; j < strlen(n); j++) {
			if (n[i] < n[j]) {
				char t = n[i];
				n[i] = n[j];
				n[j] = t;

			}
		}
	}
	printf("%s\n", n);

	return 0;

}