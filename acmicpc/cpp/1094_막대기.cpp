#include <stdio.h>

int main(void) {
	int n;
	int s = 0;
	scanf("%d", &n);

	
	while (n != 0) {
		s += n % 2;
		n /= 2;
	}
	printf("%d\n", s);
	return 0;

}