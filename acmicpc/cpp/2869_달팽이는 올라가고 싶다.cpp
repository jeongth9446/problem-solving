#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {

	int a, b, v;

	scanf("%d %d %d", &a, &b, &v);

	int k = a - b;
	int s = 0;
	if ((v - a) % k == 0) s = (v - a) / k;
	else s = (v - a) / k + 1;
	
	printf("%d\n", s + 1);

	return 0;
	

}
