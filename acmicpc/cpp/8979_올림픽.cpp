#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


struct cntry {
	int id;
	int gold;
	int silver;
	int bronze;
	int rank;
	cntry(int id, int gold, int silver, int bronze) : id(id), gold(gold), silver(silver), bronze(bronze) {}
};
bool cmp(const cntry a, const cntry b) {
	if (a.gold > b.gold) return true;
	else if (a.gold < b.gold) return false;
	else {
		if (a.silver > b.silver) return true;
		else if (a.silver < b.silver) return false;
		else {
			if (a.bronze > b.bronze) return true;
			else if (a.bronze < b.bronze) return false;
		}
	}
}
int main(void) {
	int n, k;
	vector<cntry> vec;

	cin >> n >> k;

	for (int i = 0; i < n; i++) {
		int a, b, c, d;
		cin >> a >> b >> c >> d;
		vec.push_back(cntry(a, b, c, d));
	}
	sort(vec.begin(), vec.end(), cmp);

	vec.at(0).rank = 1;
	if (vec.at(0).id == k) cout << vec.at(0).rank;
	else {
		for (int i = 1; i < n; i++) {
			if (vec.at(i).gold == vec.at(i - 1).gold && vec.at(i).silver == vec.at(i - 1).silver && vec.at(i).bronze == vec.at(i - 1).bronze)
				vec.at(i).rank = vec.at(i - 1).rank;
			else
				vec.at(i).rank = i + 1;

			if (vec.at(i).id == k) cout << vec.at(i).rank;

		}

	}
	return 0;

}