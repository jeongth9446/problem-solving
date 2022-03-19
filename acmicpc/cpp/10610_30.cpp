
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

bool cmp(const int a, const int b) {
	if (a > b) return true;
	else return false;
}
int main(void) {
	string k;
	vector<int> vector_k;
	int len_k;
	int kkk = 0;
	bool zero = false;
	cin >> k;
	len_k = k.length();

	for (int i = 0; i < len_k; i++) {
		vector_k.push_back(k.at(i) - '0');
		kkk += vector_k.back();
		if (vector_k.back() == 0) zero = true;
	}

	if (kkk % 3 == 0 && zero) {
		sort(vector_k.begin(), vector_k.end(), cmp);
		for (int i = 0; i < len_k; i++) {
			cout << vector_k.at(i);

		}
		cout << '\n';
	}
	else {
		cout << -1 << '\n';
	}
	return 0;

}