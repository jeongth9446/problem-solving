#include <stdio.h>
#include <string.h>
int main(void) {
	
	char str[101];
	scanf("%s", str);

	int sum = 0;
	int n = 0;
	for (int i = 0; i <= strlen(str); i++) {
		if (i == strlen(str) || str[i] == ',') {
			sum += n;
			n = 0;
		}
		else {
			n = n * 10 + str[i] - '0';
		}
	}
	printf("%d\n", sum);
	return 0;

}