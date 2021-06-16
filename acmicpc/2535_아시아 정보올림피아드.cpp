
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct node {
	int cntry;
	int id;
	int score;

	node(int cntry, int id, int score) : cntry(cntry), id(id), score(score) {}

};

bool cmp(const node a, const node b) {
	if (a.score > b.score) return true;
	return false;
}
int main(void) {
	vector<node> vec;
	int n;
	int m;
	int cntry_arr[101] = { 0 };
	cin >> n;
	for (int i = 0; i < n; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		vec.push_back(node(a, b, c));
	}

	sort(vec.begin(), vec.end(), cmp);

	for (int i = 0, m = 3; i < n && m != 0; i++) {
		if (cntry_arr[vec.at(i).cntry] != 2) {
			cout << vec.at(i).cntry << ' ' <<vec.at(i).id << '\n';
			cntry_arr[vec.at(i).cntry] ++;
			m--;
		}
	}

	return 0;


}