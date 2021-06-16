//1049번_기타줄

#define _CRT_SECURE_NO_WARNINGS
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
struct node {
	int num;
	int idx;
	int zip;
};
bool cmp(const struct node& p1, const struct node& p2) {
	if (p1.num < p2.num) {
		return true;
	}
	else {
		return false;
	}
}
bool cmp2(const struct node& p1, const struct node& p2) {
	if (p1.idx < p2.idx) {
		return true;
	}
	else {
		return false;
	}
}
int main(void) {
	int n;
	struct node arr[1000001];

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i].num);
		arr[i].idx = i;
	}
	sort(arr, arr + n, cmp);

	int cnt = 0;
	for (int i = 0; i < n; i++) {
		if (i == 0)
			arr[i].zip = cnt;
		else {
			if (arr[i].num == arr[i - 1].num)
				arr[i].zip = cnt;
			else {
				arr[i].zip = ++cnt;
			}
		}
	}
	sort(arr, arr + n, cmp2);

	for(int i = 0; i < n; i++) {
		printf("%d ", arr[i].zip);
	}
	return 0;

}