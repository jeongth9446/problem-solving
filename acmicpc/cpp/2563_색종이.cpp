
#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int main(void) {
	int n;
	int black = 0;
	bool paper[101][101] = { false };

	cin >> n;

	while (n--) {
		int a, b;
		cin >> a >> b;
		for (int i = a; i < a + 10; i++) {
			for (int j = b; j < b + 10; j++) {
				paper[i][j] = true;
			}
		}
	}

	for (int i = 1; i <= 100; i++) {
		for (int j = 1; j <= 100; j++) {
			if (paper[i][j]) black++;

		}
	}
	cout << black;

	return 0;

}