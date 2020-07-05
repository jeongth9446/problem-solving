#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int min(int, int, int, int);

int main(void) {
	int x, y, w, h;
	int min_dist;
	scanf("%d %d %d %d", &x, &y, &w, &h);

	min_dist = min(x, y, w - x, h - y);

	printf("%d\n", min_dist);

	return 0;

}


int min(int a, int b, int c, int d) {
	int k = 9999;

	if (k > a) k = a;
	if (k > b) k = b;
	if (k > c) k = c;
	if (k > d) k = d;
	return k;
}