//9663_N-Queen


#include <stdio.h>

int board[15][15];
int n;
int pp;
void f(int);

int main(void) {
	scanf("%d", &n);
	pp = 0;
	f(0);

	printf("%d\n", pp);
	return 0;

}

void f(int m) {
	if (m >= n) pp++;
	else {
		for (int i = 0; i < n; i++) { //[m, i]
			int flag = 0;
			for (int j = 0; j < n && !flag; j++) {
				if (board[j][i] == 1) {
					flag = 1;
					break;
				}
			}
			for (int j = 0; j < n && !flag; j++) {
				if (m + j > n || i + j > n) break;
				if (board[m + j][i + j] == 1) {
					flag = 1;
					break;
				}
			}
			for (int j = 0; j < n && !flag; j++) {
				if (m - j < 0 || i + j > n) break;
				if (board[m - j][i + j] == 1) {
					flag = 1;
					break;
				}
			}
			for (int j = 0; j < n && !flag; j++) {
				if (m - j < 0 || i - j < 0) break;
				if (board[m - j][i - j] == 1) {
					flag = 1;
					break;
				}
			}
			for (int j = 0; j < n && !flag; j++) {
				if (m + j > n || i - j < 0) break;
				if (board[m + j][i - j] == 1) {
					flag = 1;
					break;
				}
			}
			if (flag == 0) {
				board[m][i] = 1;
				f(m + 1);
				board[m][i] = 0;
			}
		}
	}
}