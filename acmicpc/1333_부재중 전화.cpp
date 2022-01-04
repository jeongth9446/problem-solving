#include <stdio.h>

int main(void) {
	int n, l, d;
	scanf("%d %d %d", &n, &l, &d);

	int song[180 * 21 + 5 * 21 + 1] = { 0 };
	int bell[180 * 21 + 5 * 21 + 1] = { 0 };

	for (int i = 0; i < (l + 5) * n; i += l +5) {
		for (int j = i; j < i + l; j++) {
			song[j] = 1;
		}
	}
	for (int i = 0; i <= (l + 5) * n + 30; i += d) {
		bell[i] = 1;
	}

	for (int i = 0; i <= (l + 5) * n + 30; i++) {
		if (song[i] == 0 && bell[i] == 1) {
			printf("%d\n", i);
			return 0;
		}
	}

	return 0;

}
