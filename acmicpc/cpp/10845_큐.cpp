//https://www.notion.so/10845-46078a45e6184da680c3819ef4e6e7e3
//10845_큐

#include <queue>
#include <string>
#include <iostream>
using namespace std;

int main(void) {
	string cmd;

	queue<int> que;

	int n;
	
	cin >> n;

	while (n--) {
		cin >> cmd;
		if (!cmd.compare("push")) {
			int t;
			cin >> t;
			que.push(t);
		}
		else if (!cmd.compare("pop")) {
			if (que.size() == 0) cout << -1 << endl;
			else {
				cout << que.front() << endl;
				que.pop();
			}
		}
		else if (!cmd.compare("size")) {
			cout << que.size() << endl;
		}
		else if (!cmd.compare("empty")) {
			if (que.empty()) cout << 1 << endl;
			else cout << 0 << endl;
		}
		else if (!cmd.compare("front")) {
			if (que.size() == 0) cout << -1 << endl;
			else {
				cout << que.front() << endl;
				
			}
		}
		else if (!cmd.compare("back")) {
			if (que.size() == 0) cout << -1 << endl;
			else {
				cout << que.back() << endl;
			}
		}
	}

	return 0;

}