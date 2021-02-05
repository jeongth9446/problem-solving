
#include <string.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(const string &u, const string &v) {
	if (u.length() < v.length())
		return true;
	else if (u.length() > v.length())
		return false;
	else {
		if (u.compare(v) < 0) return true;
		else return false;
	}
}
int main(void) {
	int n;
	cin >> n;
	vector<string> vt;

	for (int i = 0; i < n; i++) {
		string k;
		cin >> k;
		vt.push_back(k);
	}

	sort(vt.begin(), vt.end(), cmp);

	cout << vt.at(0) << '\n';

	for (int i = 1; i < n; i++) {
		if(vt.at(i).compare(vt.at(i-1)))
			cout << vt.at(i) << '\n';
	}
	return 0;

}