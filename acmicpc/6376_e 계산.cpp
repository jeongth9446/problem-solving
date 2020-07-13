#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>


int main(void) {
	
	double e;
	e = 1.0;
	int n = 1;
	printf("n e\n");
	printf("- -----------\n");
	printf("0 1\n");

	for (int i = 1; i < 10; i++) {
		n *= i;
		e += (double)1 / (double)n;
		if(i == 1) printf("%d %.0lf\n", i, e);
		else if(i == 2) printf("%d %.1lf\n", i, e);
		else printf("%d %10.9lf\n", i, e);
	}

	return 0;

}
