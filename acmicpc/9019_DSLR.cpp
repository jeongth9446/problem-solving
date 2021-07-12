#include <stdio.h>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <iostream>
#include <queue>

using namespace std;
struct node {
	string instr;
	int n;
};

int main(void) {
	int t;
	scanf("%d", &t);
	while (t--) {
		queue<struct node> que;
		int a, b;
		bool arr[10001] = { false };
		bool arr2[10001] = { false };
		scanf("%d %d", &a, &b);

		arr[(a * 2) % 10000] = true;
		arr[(a+9999)%10000] = true;
		arr[(a % 1000) * 10 + (a / 1000)] = true;
		arr[(a / 10) + (1000 * (a % 10))] = true;

		que.push({ "D", (a * 2) % 10000 });
		que.push({ "S", (a + 9999) % 10000 });
		que.push({ "L", (a % 1000) * 10 + (a / 1000) });
		que.push({ "R", (a / 10) + (1000 * (a % 10)) });
		while (que.size()) {
			a = que.front().n;
			arr2[a] = true;
			string a_str = que.front().instr;
			que.pop();

			if (a == b) {
				cout << a_str << endl;
				break;
			}
			else {
				if (!arr[(a * 2) % 10000]) {
					arr[(a * 2) % 10000] = true;
					que.push({ a_str + "D", (a * 2) % 10000 });
				}
				if (!arr[(a + 9999) % 10000]) {
					arr[(a + 9999) % 10000] = true;
					que.push({ a_str + "S",(a + 9999) % 10000 });
				}
				if (!arr[(a % 1000) * 10 + (a / 1000)]) {
					arr[(a % 1000) * 10 + (a / 1000)] = true;
					que.push({ a_str + "L", (a % 1000) * 10 + (a / 1000) });
				}
				if (!arr[(a / 10) + (1000 * (a % 10))]) {
					arr[(a / 10) + (1000 * (a % 10))] = true;
					que.push({ a_str + "R", (a / 10) + (1000 * (a % 10)) });
				}
			}

		}

	}

	return 0;

}