#include <stdio.h>
#include <string.h>
int main(void) {
	char str[1001];
	scanf("%s", str);
	for (int i = 0; i < strlen(str); i++)
		printf("%c", ((str[i] - 'A' + 23) % 26) + 'A');
	printf("\n");
	return 0;
}