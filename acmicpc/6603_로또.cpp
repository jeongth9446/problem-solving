#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <cmath>
#include <string.h>

int s[20];
int chk[20];
int n;

int func(int, int);

int main(void) {
	while (scanf("%d", &n) && n != 0) {
		for (int i = 0; i < n; i++) {
			scanf("%d", &s[i]);
			chk[i] = 0;
		}
		func(1, 0);
		printf("\n");
	}

	return 0;

}

int func(int a, int k) {
	if (a > 6)
	{
		for (int i = 0; i < n; i++)
			if (chk[i]) printf("%d ", s[i]);

		printf("\n");
		return 0;
	}
	for (int i = k; i < n; i++) {
		chk[i] = 1;
		func(a + 1, i + 1);
		chk[i] = 0;
	}	

	return 0;

}