#include <stdio.h>
#include <string.h>
int main(void) {
	
	int n, m;
	char str[5];
	scanf("%d", &n);
	sprintf(str, "%d", n);
	scanf("%d", &m);

	if (strlen(str)*n <= m) {
		for (int i = 0; i <n; i++)
			printf("%s", str);
	}
	else{
		for (int i = 0; i < m / strlen(str); i++)
			printf("%s", str);		
		for (int i = 0; i < m - (m / strlen(str)) * strlen(str); i++)
			printf("%c", str[i]);
	}

	return 0;


}