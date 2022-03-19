//17608_막대기

#include <stdio.h>

int main(void) {
	int n;
	scanf("%d", &n);
	int stt[100001];
	for (int i = n - 1; i >= 0; i--) {
		scanf("%d", &stt[i]);
	}
	int max = 0;
	int cnt = 0;
	for (int i = 0; i < n; i++) {
		if (max < stt[i]) {
			max = stt[i];
			cnt++;
		}
	}
	printf("%d\n", cnt);

	return 0;


}