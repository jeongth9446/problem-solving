#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <cmath>

int main(void) {
	int n;
	int x1, y1, x2, y2, r1, r2;
	scanf("%d", &n);
	
	while (n--) {
		scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);

		int power_d = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
		int power_rplus = (r1 + r2) * (r1 + r2);
		int power_rminus = (r1 - r2) * (r1 - r2);

		if (power_d == 0 && power_rminus == 0) printf("-1\n");
		else if (power_rminus < power_d && power_d < power_rplus) printf("2\n");
		else if (power_rplus == power_d || power_rminus == power_d) printf("1\n");
		else printf("0\n");
	}


	return 0;
}