#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>


int main(void) {
	
	for (int i = 1000; i < 10000; i++) {
		int t;
		int a=0, b=0, c=0;
		t = i;
		while (t != 0) {
			a += t % 10;
			t /= 10;
		}
		t = i;
		while (t != 0) {
			b += t % 12;
			t /= 12;
		}
		t = i;
		while (t != 0) {
			c += t % 16;
			t /= 16;
		}
		if (a == b && b == c && c == a) {
			printf("%d\n", i);
		}

	}
	return 0;

}
