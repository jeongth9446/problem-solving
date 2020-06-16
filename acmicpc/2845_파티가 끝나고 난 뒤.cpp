#include <stdio.h>

int main(void) {
	int L, P;

	scanf("%d %d", &L, &P);

	int people_sk = L * P;

	for (int i = 1; i <= 5; i++) {
		int t;
		scanf("%d", &t);
		printf("%d ", t - people_sk);

	}
	printf("\n");
	return 0;

}