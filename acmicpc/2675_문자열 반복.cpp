#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {
	
	int n;
	scanf("%d", &n);
	int m;

	for (int i = 0; i < n; i++) {
		char st[21];
		scanf("%d %s", &m, st);
		
		for (int j = 0; j < strlen(st); j++) {
			for (int k = 0; k < m; k++) {
				printf("%c", st[j]);
			}
		}
		
		printf("\n");
	}
	return 0;

}