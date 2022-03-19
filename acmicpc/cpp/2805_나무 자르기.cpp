#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
#include <string>
using namespace std;

int bf(int* arr, int n, int m, int s, int e);

int main(void) {
	int n, m;
	int arr[1000000];
	int longest = 0;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
		if (arr[i] > longest) longest = arr[i];
	}

	printf("%d", bf(arr,n, m, 0, longest));

	return 0;
}



int bf(int* arr,int n, int m, int s, int e) {
	int mid = (s + e) / 2;
	if (s > e) return e;
	long long gap = 0;
	for (int i = 0; i < n; i++) {
		if (arr[i] > mid)
			gap += arr[i] - mid;
	}
	if (gap < m) {
		return bf(arr, n, m, s, mid-1);
	}
	return bf(arr, n, m, mid +1 , e);
	
}