#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <cmath>
#include <string.h>
#include <stack>

using namespace std;

int main(void) {
	char board[51][51];
	int max = 0;
	int n;

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%s", board[i]);
	}


	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n - 1; j++) {
			if (board[i][j] != board[i][j + 1]) {
				char t = board[i][j];
				board[i][j] = board[i][j + 1];
				board[i][j + 1] = t;

				for (int l = 0; l < n; l++) {
					for (int m = 0; m < n; m++) {

						int cnt = 1;
						for (int k = l - 1; k >= 0; k--) {
							if (board[k][m] == board[l][m])
								cnt++;
							else break;
						}
						for (int k = l + 1; k < n; k++) {
							if (board[k][m] == board[l][m])
								cnt++;
							else break;
						}
						if (max < cnt) max = cnt;

						cnt = 1;
						for (int k = m - 1; k >= 0; k--) {
							if (board[l][k] == board[l][m])
								cnt++;
							else break;
						}
						for (int k = m + 1; k < n; k++) {
							if (board[l][k] == board[l][m])
								cnt++;
							else break;
						}
						if (max < cnt) max = cnt;

					}
				}
				t = board[i][j];
				board[i][j] = board[i][j + 1];
				board[i][j + 1] = t;

			}
			if (board[j][i] != board[j+1][i]) {
				char t = board[j][i];
				board[j][i] = board[j+1][i];
				board[j+1][i] = t;

				for (int l = 0; l < n; l++) {
					for (int m = 0; m < n; m++) {
						int cnt = 1;
						for (int k = l - 1; k >= 0; k--) {
							if (board[k][m] == board[l][m])
								cnt++;
							else break;
						}
						for (int k = l + 1; k < n; k++) {
							if (board[k][m] == board[l][m])
								cnt++;
							else break;
						}
						if (max < cnt) max = cnt;

						cnt = 1;
						for (int k = m - 1; k >= 0; k--) {
							if (board[l][k] == board[l][m])
								cnt++;
							else break;
						}
						for (int k = m + 1; k < n; k++) {
							if (board[l][k] == board[l][m])
								cnt++;
							else break;
						}
						if (max < cnt) max = cnt;

					}
				}
				t = board[j][i];
				board[j][i] = board[j + 1][i];
				board[j + 1][i] = t;
			}
		}
	}

	printf("%d\n", max);


	return 0;
}