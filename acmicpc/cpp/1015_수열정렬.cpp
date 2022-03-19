//1015번_수열정렬

#define _CRT_SECURE_NO_WARNINGS
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include <stdio.h>
#include <cmath>
#include <string.h>

int main(void) {
	int n;
	int A[50] = { 0 };
	int B[50] = { 0 };
	int chk[50] = { 0 };
	int P[50] = { 0 };
	
	scanf("%d", &n);
	
	for (int i = 0; i < n; i++) {
		scanf("%d", &A[i]);
		B[i] = A[i];
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (B[i] < B[j]) {
				int t = B[i];
				B[i] = B[j];
				B[j] = t;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j =0; j < n; j ++) {
			if (B[j] == A[i] && chk[j] == 0) {
				P[i] = j;
				chk[j] = 1;
				break;
			}
		}
	}

	for (int i = 0; i < n; i++) {
		printf("%d ", P[i]);
	}
	printf("\n");
	return 0;
}