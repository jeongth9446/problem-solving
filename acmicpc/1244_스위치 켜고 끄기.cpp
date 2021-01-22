//1244_스위치 켜고 끄기
//https://www.notion.so/1244-092b1c9beaf0427da4e41b04c1289507


#include <stdio.h>
#include <string.h>

int main(void) {
	int sw[101] = { 0 };

	int n;
	int student_cnt;
	int sex, light;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &sw[i]);
		if (sw[i] == 0) sw[i] = -1;
	}
	scanf("%d", &student_cnt);
	for (int i = 0; i < student_cnt; i++) {
		scanf("%d %d", &sex, &light);
		if (sex == 1) { //남자
			for (int j = light; j <= n; j += light) {
				sw[j] *= -1;
			}
		}
		else if (sex == 2) { //여자
			sw[light] *= -1;
			for (int j = 1; j <= n; j++) {
				if (sw[light + j] == sw[light - j]) {
					sw[light + j] *= -1;
					sw[light - j] *= -1;
				}
				else break;
			}
		}
	}

	for (int i = 1; i <= n; i++) {
		if (sw[i] == -1) printf("0 ");
		else printf("1 ");
		if (i % 20 == 0) printf("\n");
	}
	return 0;

}