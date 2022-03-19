#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include <stdio.h>

int main(void) {
	char names[101];

	scanf("%s", names);
	
	printf("%c", names[0]);
	for (int i = 1; names[i] != 0; i++) {
		if (names[i] == '-')
			printf("%c", names[i++ + 1]);
		
	}
	printf("\n");
	return 0;

}