#include <stdio.h>
#include <string.h>

int main(void) {
	
	char str[510];
3
	scanf("%s", str);

	for (int i = 0; i < strlen(str); i++) {
		if (str[i] == '.') continue;
		if (str[i] == 'X' && str[i + 1] == 'X' && str[i + 2] == 'X' && str[i + 3] == 'X') {
			str[i] = 'A';
			str[i+1] = 'A';
			str[i+2] = 'A';
			str[i+3] = 'A';
			i += 3;
		}
		else if (str[i] == 'X' && str[i + 1] == 'X') {
			str[i] = 'B';
			str[i + 1] = 'B';
			i++;
		}
		else {
			printf("%d\n", -1);
			return 0;
		}
	}
	printf("%s\n", str);

	return 0;


}