#include <math.h>
#include <iostream>

using namespace std;


int main(void) {
	long long  s;
	cin >> s;
	double x;
	x = 0.5 * (sqrt(8 * s + 1) - 1);
	cout << (int)x;

	return 0;

}