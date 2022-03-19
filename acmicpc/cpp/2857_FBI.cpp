//2857_FBI

#include <stdio.h>
#include <string.h>


int main(void) {
	
	int flag = 0;
	char str[6][11];
	for (int i = 1; i <= 5; i++) {
		scanf("%s", str[i]);
		
	}
	for (int i = 1; i <= 5; i++) {


		for (int j = 0; j < strlen(str[i]) - 2; j++) {
			if (str[i][j] == 'F' && str[i][j + 1] == 'B' && str[i][j + 2] == 'I') {
				printf("%d ", i);
				flag = 1;
				break;
			}
		}
	}
	if (!flag) {
		printf("HE GOT AWAY!");
	}
}