#include <stdio.h>

int main(void) {
	int p;
	int s = 0;
	scanf("%d", &p);
	for (int i = 0; i < 5; i++) {
		int t;
		scanf("%d", &t);
		if (t == p) s++;
	}
	printf("%d\n", s);

	return 0;

}