#include <stdio.h>

int main(void) {
    
	int n, m, k;
	
	while (1) {
		scanf("%d %d %d", &n, &m, &k);
		if (n == 0 && m == 0 && k == 0) break;

		if (n == k) printf("%d\n", 1);
		else {

			if (m == 0) printf("X\n");
			else if (m > 0) {
				if (n > k) printf("X\n");
				else {
					int step = 1;
					while (++step && k > n) {
						n += m;
						if (k == n) printf("%d\n", step);
						else if (n > k) printf("X\n");
					}
				}
			}
			else {
				if (n < k) printf("X\n");
				else {
					int step = 1;
					while (++step && k < n) {
						n += m;
						if (k == n) printf("%d\n", step);
						else if (n < k) printf("X\n");
					}
				}
			}
		}

	}


	return 0;
}