
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>


using namespace std;

int main(void) {

	map<int, int> m;
	
	int n, k, t;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &t);
		m[t] ++;
	}

	scanf("%d", &k);
	for (int i = 0; i < k; i++) {
		scanf("%d", &t);
		printf("%d ", m[t]);

	}

	return 0;


}