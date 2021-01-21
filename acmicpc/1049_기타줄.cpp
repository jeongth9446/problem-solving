#include <stdio.h>


int main(void) {

	int n, m;
	scanf("%d %d", &n, &m);
	int min_price_6strings = 1000, min_price_1string = 1000;

	for (int i = 0; i < m; i++) {
		int t1, t2;
		scanf("%d %d", &t1, &t2);
		if (t1 < min_price_6strings) min_price_6strings = t1;
		if (t2 < min_price_1string) min_price_1string = t2;
	}

	if (min_price_1string * 6 < min_price_6strings) min_price_6strings = min_price_1string * 6;

	if (((n / 6) + 1) * min_price_6strings < (n / 6) * min_price_6strings + (n % 6) * min_price_1string) {
		printf("%d\n", ((n / 6) + 1) * min_price_6strings);
	} else 
	printf("%d\n", (n / 6) * min_price_6strings + (n % 6) * min_price_1string);
	return 0;


}