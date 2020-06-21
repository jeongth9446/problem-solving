#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main(void) {

	int n, m;
	int arr[1000];
	int s,c;
	double avg;
	scanf("%d", &n);
	while (n--) {
		scanf("%d", &m);
		s = 0;
		c = 0;
		avg = 0.0;
		for (int i = 0; i < m; i++) {
			scanf("%d", &arr[i]);
			s += arr[i];
		}
		avg = (double)s / (double)m;

		for (int i = 0; i < m; i++) {
			if (arr[i] > avg) {
				c++;
			}
		}
		printf("%.3lf%%\n", (double)c / (double)m * 100.0);

			
	}
	return 0;
}
