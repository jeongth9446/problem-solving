#include <stdio.h>
#include <string.h>

int main(void) {
	
	int t;
	scanf("%d", &t);
	char str[1001];
	while (t--) {
		scanf("%s", str);
		printf("%c%c\n", str[0], str[strlen(str) - 1]);
	}
	return 0;

}
