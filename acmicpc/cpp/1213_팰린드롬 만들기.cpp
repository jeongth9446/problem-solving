//1213_팰린드롬 만들기

#include <stdio.h>
#include <string.h>

int main(void) {
	int odd_cnt = 0;

	char input_str[60];
	int str_chk[100] = { 0 };
	char odd_str = NULL;
	scanf("%s", input_str);
	for (int i = 0; i < strlen(input_str); i++) {
		str_chk[input_str[i]]++;
	}
	for (int i = 'A'; i <= 'Z'; i++)
		if (str_chk[i] % 2 != 0) odd_cnt++;
	if ((odd_cnt == 1 && strlen(input_str) % 2 == 1) || odd_cnt == 0) {
		for (int i = 'A'; i <= 'Z'; i++) {
			if (str_chk[i] % 2 == 1)  odd_str = i;
			for (int j = 1; j <= str_chk[i] / 2; j++) {
				printf("%c", i);
			}
		}
		if (odd_str) {
			printf("%c", odd_str);
		}
		for (int i = 'Z'; i >= 'A'; i--) {
			for (int j = 1; j <= str_chk[i] / 2; j++) {
				printf("%c", i);
			}
		}
		printf("\n");
	}
	else {
		printf("I'm Sorry Hansoo\n");
	}

}