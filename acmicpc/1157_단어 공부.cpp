#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {

	char t;
	int chk[26] = { 0 };
	int max = 0;
	int maxc = 0;
	int maxi = 0;

	while (scanf("%c", &t) != EOF) {
		if (t >= 'A' && t <= 'Z')
			chk[t - 'A'] ++;
		else
			chk[t - 'a'] ++;
	}

		

	for (int i = 0; i < 26; i++) {
		if (max < chk[i]) {
			max = chk[i];
			maxi = i;
			maxc = 1;
		}
		else if (max == chk[i]) {
			maxc++;
		}
	}
	
	if (maxc > 1)
		printf("?\n");
	else
		printf("%c\n", 'A' + maxi);
	return 0;
}
