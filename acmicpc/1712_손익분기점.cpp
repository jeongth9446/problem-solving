#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {

	int  a, b, c;
	int x;
	scanf("%d %d %d",  &a, &b, &c);


	x = (int)((double)a / double(c - b));

	if (x < 0) printf("-1\n");
	else printf("%d\n", x + 1);

	return 0;


}
