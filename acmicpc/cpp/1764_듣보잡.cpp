#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int cmp(const void* a, const void* b) {
	return(strcmp((char*)a, (char*)b));
}

int main(void) {
	int n, m;

	char a[500000][21];
	char b[500000][21];
	int cnt = 0;
	char c[500000][21];

	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++) {
		scanf("%s", a[i]);
	}
	for (int i = 0; i < m; i++) {
		scanf("%s", b[i]);
	}
	qsort((void*)a, n, sizeof(a[0]), cmp);
	qsort((void*)b, m, sizeof(b[0]), cmp);


	int ap = 0, bp = 0;

	while (ap < n && bp < m) {
		if (strcmp(a[ap], b[bp]) == 0) {
			strcpy(c[cnt++], a[ap]);
			bp++;
			ap++;
		}
		else if (strcmp(a[ap], b[bp]) < 0) {
			ap++;
		}
		else if (strcmp(a[ap], b[bp]) > 0) {
			bp++;
		}
	}

	printf("%d\n", cnt);

	for (int i = 0; i < cnt; i++) {
		printf("%s\n", c[i]);
	}
	return 0;


}