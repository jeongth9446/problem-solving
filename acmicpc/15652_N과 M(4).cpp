
#include <stdio.h>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <iostream>
#include <queue>

using namespace std;

int f(int n, int max, int* chk, int k, int m) {

	if (k > m) {
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= chk[i]; j++) {
				printf("%d ", i);
			}
		}
		printf("\n");
		return 0;
	}
	for (int i = max; i <= n; i++) {
		chk[i] ++;
		f(n, i, chk, k + 1, m);
		chk[i] --;
	}
	return 0;
}
int main(void) {

	int n, m;
	int chk[9] = { 0 };
	scanf("%d %d", &n, &m);

	f(n, 1, chk, 1, m);

	return 0;

}