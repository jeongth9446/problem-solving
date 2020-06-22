#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {

	int chk[26] = { 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10 };
	int s = 0;
	char input_txt[16];
	scanf("%s", input_txt);

	for (int i = 0; i < strlen(input_txt); i++) {
		s += chk[input_txt[i] - 'A'];
	}
	printf("%d\n", s);
	return 0;


}
