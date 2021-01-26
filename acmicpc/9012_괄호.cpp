
#include <stack>
#include <iostream>
using namespace std;

int main(void) {
	
	int t;
	cin >> t;
	
	while (t--) {
		int flag = 0;
		string str;
		stack<char> stk;
		cin >> str;
		for (int i = 0; i < str.length(); i++) {
			if (str.at(i) == '(')
				stk.push('(');
			else if (str.at(i) == ')') {
				if (stk.size() == 0) {
					cout << "NO" << endl;
					flag = 1;
					break;
				}
				else if (stk.top() == '(') {
					stk.pop();
				}
				else {
					cout << "NO" << endl;
					flag = 1;
					break;
				}
			}
		}
		if (flag == 0) {
			if (stk.size() == 0)
				cout << "YES" << endl;
			else cout << "NO" << endl;
		}
	}

	return 0;

}