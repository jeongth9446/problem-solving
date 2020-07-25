#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <cmath>
#include <string.h>
#include <stack>

using namespace std;

int main(void) {
	stack<int> s;

	int n;

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		int t;
		scanf("%d", &t);

		if (!t)
			s.pop();
		else
			s.push(t);

	}

	int sum = 0;

	while (s.size()) {
		sum += s.top();
		s.pop();
	}
	printf("%d\n", sum);
	return 0;

}