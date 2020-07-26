#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <cmath>
#include <string.h>
#include <stack>

using namespace std;

int main(void) {

	int n;
	int length = 0;
	int ele = 1;
	int div = 10;
	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		if (i % div == 0) {
			ele++;
			div *= 10;
		}
		length += ele;
	}
	printf("%d\n", length);
	return 0;

}