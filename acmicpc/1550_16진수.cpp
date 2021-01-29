
#include <stdio.h>
#include <string.h>
int main(void) {

	char str[7];

	scanf("%s", str);

	int len = strlen(str);
	int p = 1;
	int s = 0;
	for (int i = 0; i < len; i++) {
		if (str[i] >= '0' && str[i] <= '9') str[i] -= '0';
		else if (str[i] == 'A') str[i] = 10;
		else if (str[i] == 'B') str[i] = 11;
		else if (str[i] == 'C') str[i] = 12;
		else if (str[i] == 'D') str[i] = 13;
		else if (str[i] == 'E') str[i] = 14;
		else if (str[i] == 'F') str[i] = 15;
	}
	for (int i = len - 1; i >= 0; i--) {
		s += str[i] * p;
		p *= 16;
	}

	printf("%d\n", s);
	return 0;

}