#include <stdio.h>

int main(void) {
	char board[10][10];

	int n;
	int cnt = 0;
	for (int i = 0; i < 8; i++)
		scanf("%s", board[i]);

	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			if((i+j)%2 == 0 && board[i][j] == 'F') {
				cnt++;
			}
		}
	}
	printf("%d\n", cnt);

	return 0;

}