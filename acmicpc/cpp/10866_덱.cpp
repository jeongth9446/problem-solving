//10866_덱


#include <deque>
#include <iostream>

using namespace std;

int main(void) {

	int n, t;
	string cmd;
	deque<int> deq;

	cin >> n;
	while (n--) {
		cin >> cmd;
		if (!cmd.compare("push_front")) {
			cin >> t;
			deq.push_front(t);
		}
		if (!cmd.compare("push_back")) {
			cin >> t;
			deq.push_back(t);
		}
		if (!cmd.compare("pop_front")) {
			if (deq.size() == 0) {
				cout << -1 << endl;
			}
			else {
				cout << deq.front() << endl;
				deq.pop_front();
			}
		}
		if (!cmd.compare("pop_back")) {
			if (deq.size() == 0) {
				cout << -1 << endl;
			}
			else {
				cout << deq.back() << endl;
				deq.pop_back();
			}
		}
		if (!cmd.compare("size")) {
			cout << deq.size() << endl;
		}
		if (!cmd.compare("empty")) {
			if (deq.empty()) {
				cout << 1 << endl;
			}
			else cout << 0 << endl;
		}
		if (!cmd.compare("front")) {
			if (deq.size() == 0) {
				cout << -1 << endl;
			}
			else {
				cout << deq.front() << endl;
			}
		}
		if (!cmd.compare("back")) {
			if (deq.size() == 0) {
				cout << -1 << endl;
			}
			else {
				cout << deq.back() << endl;
			}
		}

	}

	return 0;

}