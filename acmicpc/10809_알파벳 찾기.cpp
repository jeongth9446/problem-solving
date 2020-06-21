#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int func(int);


int main(void) {
	
	char st[101];
	scanf("%s", st);

	int chk['z'+1] = { 0 };
	for (int i = 'a'; i <= 'z'; i++) {
		chk[i] = -1;
	}
	for (int i = 0; i < strlen(st); i++) {
		if(chk[st[i]]== -1)
			chk[st[i]] = i;	
	}
	for (int i = 'a'; i <= 'z'; i++) {
		printf("%d ", chk[i]);
		
	}

	return 0;

}