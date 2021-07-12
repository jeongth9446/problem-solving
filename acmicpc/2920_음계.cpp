#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
#include <string>
using namespace std;

int main(void) {
	string u;
	getline(cin, u);
	if (u == "1 2 3 4 5 6 7 8") printf("ascending");
	else if (u=="8 7 6 5 4 3 2 1") printf("descending");
	else printf("mixed");

	return 0;

}