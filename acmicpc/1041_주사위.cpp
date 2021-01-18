//1041_주사위

#define _CRT_SECURE_NO_WARNINGS
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include <stdio.h>
#include <cmath>

int main(void) {
	long long arr[6] = { 0 };
	long long n;
	long long threeDice = 200;
	long long twoDice = 200;

	scanf("%lld", &n);
	for (int i = 0; i < 6; i++) {
		scanf("%lld", &arr[i]);
	}

	if (threeDice > arr[0] + arr[1] + arr[2]) threeDice = arr[0] + arr[1] + arr[2];
	if (threeDice > arr[0] + arr[1] + arr[3]) threeDice = arr[0] + arr[1] + arr[3];
	if (threeDice > arr[0] + arr[2] + arr[4]) threeDice = arr[0] + arr[2] + arr[4];
	if (threeDice > arr[0] + arr[3] + arr[4]) threeDice = arr[0] + arr[3] + arr[4];
	if (threeDice > arr[1] + arr[3] + arr[5]) threeDice = arr[1] + arr[3] + arr[5];
	if (threeDice > arr[1] + arr[2] + arr[5]) threeDice = arr[1] + arr[2] + arr[5];
	if (threeDice > arr[3] + arr[4] + arr[5]) threeDice = arr[3] + arr[4] + arr[5];
	if (threeDice > arr[2] + arr[4] + arr[5]) threeDice = arr[2] + arr[4] + arr[5];


	if (twoDice > arr[0] + arr[1]) twoDice = arr[0] + arr[1];
	if (twoDice > arr[0] + arr[4]) twoDice = arr[0] + arr[4];
	if (twoDice > arr[0] + arr[2]) twoDice = arr[0] + arr[2];
	if (twoDice > arr[0] + arr[3]) twoDice = arr[0] + arr[3];
	if (twoDice > arr[2] + arr[1]) twoDice = arr[2] + arr[1];
	if (twoDice > arr[1] + arr[3]) twoDice = arr[1] + arr[3];
	if (twoDice > arr[5] + arr[3]) twoDice = arr[5] + arr[3];
	if (twoDice > arr[4] + arr[3]) twoDice = arr[4] + arr[3];
	if (twoDice > arr[4] + arr[2]) twoDice = arr[4] + arr[2];
	if (twoDice > arr[5] + arr[2]) twoDice = arr[5] + arr[2];
	if (twoDice > arr[4] + arr[5]) twoDice = arr[4] + arr[5];
	if (twoDice > arr[1] + arr[5]) twoDice = arr[1] + arr[5];


	for (int i = 0; i < 6; i++) {
		for (int j = i + 1; j < 6; j++) {
			if (arr[i] > arr[j]) {
				int t;
				t = arr[i];
				arr[i] = arr[j];
				arr[j] = t;
			}
		}
	}
	if (n != 1) {
		printf("%lld\n", 4 * (twoDice) * (2 * n - 3) + (threeDice) * 4 + arr[0] * (5 * n * n - 16 * n + 12));
	}
	else printf("%lld\n", arr[0] + arr[1] + arr[2] + arr[3] + arr[4]);

	return 0;


}