
#include <stdio.h>

int main(void) {
	int e, s, m;

	scanf("%d %d %d", &e, &s, &m);
	int ee, ss, mm;
	ee = 1, ss = 1, mm = 1;
	int n = 1;

	while (1) {
		if (ee == e && ss == s && mm == m) {
			printf("%d\n", n); 
			break;
		}
		ee = ee % 15 + 1;
		ss = ss % 28 + 1;
		mm = mm % 19 + 1;
		n++;
	}

	return 0;

}