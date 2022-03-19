#include <stdio.h>

int main(void) {
	int chk[5001] = { 0 };

	int n, k;
	int t = 0;
	int p = 0;
	scanf("%d %d", &n, &k);
	printf("<");
	while (t != n) {
		int a = 0;
		while (a < k) {
			p = p % n + 1;
			if (chk[p] == 0) a++;
		}
		chk[p] = 1;
		t++;
		if (t != n)
			printf("%d, ", p);
		else printf("%d>", p);
	}

	return 0;

}