#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {

	long long chk[1000001] = { 0 };
	int res[1000002] = { 0 };
	int cnt = 0;

	long long min, max;

	scanf("%lld %lld", &min, &max);

	for (int i = 0; i < 1000000; i++) {
		chk[i] = (long long)(i + 2) * (long long)(i + 2);
		if (chk[i] >= max) break;

	}


	for (long long i = 0; i < 1000000; i++) {
		if (chk[i] > max) break;
		long long k = min / chk[i];

		for (long long j = k*chk[i]; j <= max; j += chk[i]) {
			if (j < min) continue;
			if (res[j - min] != 0) continue;
				
			if (j % chk[i] == 0) {
				res[j - min] = 1;
				cnt++;
			}
			
		}
	}
	printf("%lld\n", max - min + 1 - cnt);


	return 0;

}
