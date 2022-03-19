#include <stdio.h>
#include <string.h>

int main(void) {
	char str[5][20];
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 16; j++)
			str[i][j] = 0;
	}
	for (int i = 0; i < 5; i++)
		scanf("%s", str[i]);

	
	for (int j = 0; j < 15; j++) {
		for (int i = 0; i < 5; i++) {
			if ((str[i][j] >= 'A' && str[i][j] <= 'Z') || (str[i][j] >= 'a' && str[i][j] <= 'z') || (str[i][j] >= '0'&&str[i][j] <= '9'))
				printf("%c", str[i][j]);
		}
	}
	return 0;
}