//1292_쉽게 푸는 문제
//https://www.notion.so/1292-dc73f51da51d4150b3371d2479b9137e

#include <stdio.h>

int main(void) {
	int arr[1001] = { 0 };
	int n = 1, c = 1, s = 0;
	int a, b;
	while (n <= 1000) {
		for (int i = 1; i <= c; i++) {
			arr[n++] = c;
			if (n > 1000) break;
		}
		c++;
	}
	scanf("%d %d", &a, &b);
	for (int i = a; i <= b; i++)
		s += arr[i];
	printf("%d\n", s);
	return 0;

}