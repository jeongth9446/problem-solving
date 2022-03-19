#include <stdio.h>

int main(void) {
	int A, l;

	scanf("%d %d", &A, &l);

	printf("%d\n", A * (l - 1) + 1);

	return 0;

}