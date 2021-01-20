//1205_등수 구하기
#include <stdio.h>
#include <cmath>

int main(void) {

	int n, p;
	int score;
	int flag = 0; //현재 스코어 판에 자리가 있는지
	int arr[51] = { 0 };
	scanf("%d %d %d", &n, &score, &p);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	if (p > n) flag = 1; //자리가 있다.

	if (n == 0) {
		printf("%d", 1);
		return 0;
	}
	if (!flag) { //자리가 없으면
		if (score <= arr[p - 1]) {
			printf("-1");
			return 0;
		}	
	}
	for (int i = 0; i < p; i++) {
		if (arr[i] <= score) {
			printf("%d", i + 1);
			return 0;
		}
	}
	return 0;

}