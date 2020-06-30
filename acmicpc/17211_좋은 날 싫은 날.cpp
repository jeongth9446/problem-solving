#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {

	float y = 0.0, n = 0.0;
	float yt, nt;
	int day, s;
	float yy, yn, ny, nn;

	scanf("%d %d", &day, &s);
	scanf("%f %f %f %f", &yy, &yn, &ny, &nn);
	if (s == 1) n = 1;
	else y = 1;

	for(int i = 1; i <= day; i ++) {
		yt = y * yy + n * ny;
		nt = n * nn + y * yn;
		y = yt, n = nt;
	}

	printf("%d\n%d\n", (int)round(y * 1000), (int)round(n * 1000));

	return 0;

}
