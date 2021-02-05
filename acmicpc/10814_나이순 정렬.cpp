#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

struct person {
	int id;
	int age;
	string name;
	person(int a, int b, string c)
		: id(a), age(b), name(c)
	{}
};

bool cmp(const person &a, const person &b) {
	if (a.age < b.age) return true;
	else if (a.age > b.age) return false;
	else {
		if (a.id < b.id) return true;
		else return false;
	}
}

int main(void) {
	int n;
	vector<struct person> p;

	cin >> n;
	for (int i = 0; i < n; i++) {
		int in_age;
		string in_name;
		cin >> in_age >> in_name;
		p.push_back(person(i, in_age, in_name));
	}


	sort(p.begin(), p.end(), cmp);

	for (int i = 0; i < n; i++) {
		cout << p.at(i).age << ' ' << p.at(i).name << '\n';
	}
	return 0;

}