#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>


int main(void) {
	
	char num[1001];

	while (1) {
		scanf("%s", num);
		if (num[0] == '0' && strlen(num) == 1) break;
		while (strlen(num) > 1) {
			int c = 0;
			for (int i = 0; i < strlen(num); i++)
				c += num[i] - '0';
			int k = 0;
			while (c != 0) {
				num[k++] = (c % 10) + '0';
				c /= 10;
			}
			num[k] = '\0';
		}
		printf("%s\n", num);
	}
	return 0;

}
