#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <cmath>
#include <string.h>
#include <stack>

int main(void) {
	char s[10];

	int arr[10] = { 0 };
	scanf("%s", s);
	for (int i = 0; i < strlen(s); i++) {
		arr[s[i] - '0'] ++;
	}
	arr[9] = (arr[6] + arr[9] + 1) / 2;
	arr[6] = arr[9];

	int max = 0;
	for (int i = 0; i < 10; i++) {
		if (max < arr[i]) max = arr[i];
	}
	printf("%d\n", max);

	return 0;


}