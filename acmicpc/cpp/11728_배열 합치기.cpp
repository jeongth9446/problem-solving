#include <stdio.h>

int main(void) {
	int n, m;

	int Vec_A[1000001];
	int Vec_B[1000001];

	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++) {
		scanf("%d", &Vec_A[i]);
	}
	for (int i = 0; i < m; i++) {
		scanf("%d", &Vec_B[i]);
	}
	for (int s_a = 0, s_b = 0; s_a < n || s_b < m; ) {
		if (s_a == n) {
			printf("%d ", Vec_B[s_b]);
			s_b++;
		}
		else if (s_b == m) {
			printf("%d ", Vec_A[s_a]);
			s_a++;
		}
		else if (Vec_A[s_a] < Vec_B[s_b]) {
			printf("%d ", Vec_A[s_a]);
			s_a++;
		}
		else {
			printf("%d ", Vec_B[s_b]);
			s_b++;
		}
	}
	return 0;


}