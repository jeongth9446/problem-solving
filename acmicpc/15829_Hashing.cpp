#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
#include <string>
using namespace std;

int main(void) {
	int n;
	long long r = 1;
	char z[51];
	long long hash = 0;
	scanf("%d", &n);
	scanf("%s", z);

	for (int i = 0; i < n; i++) {
		hash += r * (z[i] - 'a' + 1);
		hash %= 1234567891;
		r *= 31;
		r %= 1234567891;
	}
	printf("%lld\n", hash);

	return 0;



}