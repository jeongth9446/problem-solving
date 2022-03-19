
#include <stdio.h>

int main(void) {
	bool chk[151] = { false };
	int arr[8] = { 0 };
	int p;
	int s = 0;
	for (int i = 0; i < 8; i++) {
		int t;
		scanf("%d", &t);
		chk[t] = true;
		arr[i] = t;
	}
	for (int i = 150, k = 0; ; i--) {
		
		if (chk[i]) {
			k++;
			s += i;
		}
		if (k == 5) {
			p = i; break;
		}
	}
	printf("%d\n", s);
	for (int i = 0; i < 8; i++) {
		if (arr[i] >= p) printf("%d ", i+1);
	}

	return 0;

}