//https://www.notion.so/1934-f6a2364ff4b84fd9a60f38440d2ad48d
//1934번 : 최소공배수


#include <stdio.h>

int func_GCD(int, int);

int main(void) {
	int t;
	int a, b;
	scanf("%d", &t);

	while (t--) {
		scanf("%d %d", &a, &b);
		printf("%d\n", a * b / func_GCD(a, b));
	}

	return 0;
}

int func_GCD(int a, int b) {
	if (a % b == 0) return b;
	else return func_GCD(b, a % b);
}