#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main(void) {

	int n;
	int max_score = 0;
	int score[1000] = { 0 };
	double new_score[1000] = { 0.0 };
	double new_avg = 0.0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &score[i]);
		if (max_score < score[i]) max_score = score[i];
	}
	for (int i = 0; i < n; i++) {
		new_score[i] = (double)score[i] / (double)max_score * 100.0;
		new_avg += new_score[i];
	}
	printf("%lf\n", new_avg / n);
	return 0;


}
