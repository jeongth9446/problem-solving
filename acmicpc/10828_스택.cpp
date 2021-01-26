//10828_스택

#include <stack>
#include <iostream>
using namespace std;

int main(void) {
	stack<int> stk;
	string cmd;
	int num;
	int n;

	cin >> n;
	while (n--) {
		cin >> cmd;
		if (!cmd.compare("push")) {
			cin >> num;
			stk.push(num);
		}
		if (!cmd.compare("pop")) {
			if (stk.size() == 0)
				cout << -1 << endl;
			else {
				cout << stk.top() << endl;
				stk.pop();
			}
		}
		if (!cmd.compare("size")) {
			cout << stk.size() << endl;
		}
		if (!cmd.compare("empty")) {
			cout << stk.empty() << endl;
		}
		if (!cmd.compare("top")) {
			if (stk.size() == 0)
				cout << -1 << endl;
			else
				cout << stk.top() << endl;
		}
	}
	
	return 0;

}