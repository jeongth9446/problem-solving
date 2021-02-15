
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct point {
	int x, y;
	point(int a, int b)
		: x(a), y(b)
	{}
};

bool cmp(const struct point& a, const struct point& b) {
	if (a.y < b.y) return true;
	else if (a.y > b.y) return false;
	else {
		if (a.x < b.x) return true;
		else return false;
	}
}
int main(void) {
	vector<struct point> p;
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int x1, y1;
		cin >> x1 >> y1;
		p.push_back(point(x1, y1));
	}

	sort(p.begin(), p.end(), cmp);

	for (int i = 0; i < n; i++)
		cout << p.at(i).x << ' ' << p.at(i).y << '\n';
	return 0;

}