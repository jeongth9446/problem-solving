#include <stdio.h>
#include <string.h>
int main(void) {

	char joiioi[10001];
	int ioi = 0, joi = 0;
	scanf("%s", joiioi);

	for (int i = 0; i < strlen(joiioi) - 2; i++) {
		if (joiioi[i + 1] == 'O' && joiioi[i + 2] == 'I') {
			if (joiioi[i] == 'I') ioi++;
			else if (joiioi[i] == 'J') joi++;
		}
	}
	printf("%d\n%d\n", joi, ioi);
	return 0;
}