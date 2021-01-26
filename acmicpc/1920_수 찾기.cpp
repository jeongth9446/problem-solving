//1920_수 찾기


#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
	cin.tie(NULL);
	std::ios_base::sync_with_stdio(false);

	int A[100001] = { 0 };
	int n, m;
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> A[i];

	sort(A, A+n);

	cin >> m;

	for (int i = 0; i < m; i++) {
		int t;
		cin >> t;
		if (binary_search(A, A + n, t))
			cout << 1 << '\n';
		else cout << 0 << '\n';
	}

	return 0;

}