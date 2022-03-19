#include <stdio.h>
#include <string.h>

int main(void) {
	
	
	int t;
	scanf("%d", &t);

	while (t--) {
		int n, m;
		scanf("%d", &n);
		int max = 0;
		char str[21], tmp[21];
		for (int i = 0; i < n; i++) {
			scanf("%d", &m);
			if (max < m) {
				max = m;
				scanf("%s", str);
			}
			else
				scanf("%s", tmp);
		}
	
		printf("%s\n", str);
		
	}
	return 0;

}