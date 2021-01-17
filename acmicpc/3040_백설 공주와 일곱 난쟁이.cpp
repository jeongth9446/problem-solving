
#include <stdio.h>

int main(void) {

	int sum = 0;

	int nan[10];
	for (int i = 0; i < 9; i++) {
		scanf("%d", &nan[i]);
		sum += nan[i];
	}
	for (int i = 0; i < 9; i++) {
		for (int j = i + 1; j < 9; j++) {
			if (sum - nan[i] - nan[j] == 100) {
				for (int k = 0; k < 9; k++) {
					if (k != i && k != j) {
						printf("%d\n", nan[k]);
					}

				}
				return 0;
			}
		}
	}

	return 0;


}