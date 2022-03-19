#include <math.h>
#include <stdio.h>
#include <string.h>
int main(void) {
	
	char a[1001], b[1001];
	int achk[130] = { 0 }, bchk[130] = { 0 };

	scanf("%s %s", a, b);

	for (int i = 0; i < strlen(a); i++)
		achk[a[i]] ++;
	for (int i = 0; i < strlen(b); i++)
		bchk[b[i]] ++;
	int cnt = 0;
	for (int i = 'a'; i <= 'z'; i++) {
		cnt += abs(achk[i] - bchk[i]);
	}
	printf("%d\n", cnt);

	return 0;

}