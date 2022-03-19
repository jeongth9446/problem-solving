#include <stdio.h>
#include <string.h>

int main(void) {
	
	long long sum = 0;
	char a[10002], b[10002];
	scanf("%s %s", a, b);


	for (int i = 0; i < strlen(a); i++) {
		for (int j = 0; j < strlen(b); j++) {
			sum += (a[i] - '0') * (b[j] - '0');
		}
	}
	printf("%ld", sum);
	return 0;

}