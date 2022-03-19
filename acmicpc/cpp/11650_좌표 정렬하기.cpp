//11650_좌표 정렬하기

#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

struct Point {
	int x;
	int y;
	Point(int x, int y) : x(x), y(y) {}
};

struct cmp {
	bool operator()(Point a, Point b) {
		if(a.x == b.x)
			return a.y < b.y;
		else return a.x < b.x;
	}
}cmp;
int main(void) {
	vector<Point> vec;

	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		Point p(a, b);
		vec.push_back(p);
	}

	sort(vec.begin(), vec.end(), cmp);

	for (int i = 0; i < n; i++) {
		printf("%d %d\n", vec.at(i).x, vec.at(i).y);
	}
	return 0;

}

