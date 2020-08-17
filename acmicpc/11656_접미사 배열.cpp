#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int cmp(const void* a, const void* b) {
	return(strcmp((char*)a, (char*)b));
}

int main(void) {

	char str[1001][1001];
	int n;
	scanf("%s", str[0]);
	n = strlen(str[0]);
	for (int i = 1; i < n; i++)
		strcpy(str[i], &str[0][i]);
	
	qsort((void*)str, n, sizeof(str[0]), cmp);

	for (int i = 0; i < n; i++)
		printf("%s\n", str[i]);
	return 0;


}