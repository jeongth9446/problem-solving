#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void) {

	char txt[101];
	scanf("%s", txt);
	int cnt = 0;
	for (int i = 0; i < strlen(txt); i++) {
		if (txt[i] == 'c' && txt[i + 1] == '=') {
			cnt++; i++;
		}
		else if (txt[i] == 'c' && txt[i + 1] == '-') {
			cnt++; i++;
		}
		else if (txt[i] == 'd' && txt[i + 1] == 'z' && txt[i + 2] == '=') {
			cnt++; i += 2;
		}
		else if (txt[i] == 'd' && txt[i + 1] == '-') {
			cnt++; i++;
		}
		else if (txt[i] == 'l' && txt[i + 1] == 'j') {
			cnt++; i++;
		}
		else if (txt[i] == 'n' && txt[i + 1] == 'j') {
			cnt++; i++;
		}
		else if (txt[i] == 's' && txt[i + 1] == '=') {
			cnt++; i++;
		}
		else if (txt[i] == 'z' && txt[i + 1] == '=') {
			cnt++; i++;
		}
		else cnt++;
	}
	printf("%d\n", cnt);
	return 0;

}
