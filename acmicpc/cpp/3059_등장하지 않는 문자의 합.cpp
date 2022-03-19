//3059_등장하지 않는 문자의 합

#include <stdio.h>
#include <string.h>

int main(void) {
	char str[1001];

	int t;
	scanf("%d", &t);

	while (t--) {
		scanf("%s", str);
		int chk[100] = { 0 };
		for (int i = 0; i < strlen(str); i++) {
			chk[str[i]] ++;
		}
		int sum = 0;
		for (int i = 'A'; i <= 'Z'; i++) {
			if (chk[i] == 0) sum += i;
		}
		printf("%d\n", sum);
	}
	return 0;

}