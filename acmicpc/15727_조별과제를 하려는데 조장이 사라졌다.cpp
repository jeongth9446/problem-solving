#include <stdio.h>

int main(void) {
	int n;
	scanf("%d", &n);
	int s;
	s = n / 5;
	if (n % 5 != 0) s++;
	printf("%d\n", s);

	return 0;

}