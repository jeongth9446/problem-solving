#include <stdio.h>
#include <string.h>

int main(void) {
	
	char a[8], b[8];
	int chk[20] = { 0 };
	int ap, bp, cp = 0;
	scanf("%s %s", a, b);
	ap = strlen(a)-1;
	bp = strlen(b)-1;
	
	while (ap >= 0 || bp >= 0) {
		if (ap >= 0) chk[cp] += a[ap] - '0';
		if (bp >= 0) chk[cp] += b[bp] - '0';
		cp++; ap--; bp--;
	}

	for (int i = cp - 1; i >= 0; i--)
	{
		printf("%d", chk[i]);
	}
	return 0;

}