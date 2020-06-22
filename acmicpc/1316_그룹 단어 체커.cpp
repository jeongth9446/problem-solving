#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {

	int n;
	char t[102];
	int chk[150] = { 0 };
	int cnt = 0;
	scanf("%d", &n);

	while (n--) {
		scanf("%s", t);
		for (int i = 0; i < 150; i++) chk[i] = 0;
		int sw = 0;
		chk[t[0]] = 1;
		for (int i = 1; i < strlen(t); i++) {
			if (t[i] != t[i - 1]) {
				if (chk[t[i]] != 0) {
					sw = 1;
					break;
				}
			}
			chk[t[i]] = 1;

		}
		if (!sw) {
			cnt++;
		}
	}
	printf("%d\n", cnt);
	return 0;
}
