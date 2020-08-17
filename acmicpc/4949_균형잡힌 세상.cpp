#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <stack>


int main(void) {

	std::stack<char> stk;

	char str[1001];

	while (1) {
		gets(str);

		if (str[0] == '.' && strlen(str) == 1)
			break;
		int flag = 0;
		for (int i = 0; i < strlen(str); i++) {
			if (str[i] == '(' || str[i] == '[') {
				stk.push(str[i]);
			}
			else if (str[i] == ')' || str[i] == ']') {
				if (stk.empty()) {
					printf("no\n");
					flag = 1;
					break;
				}
				if (str[i] == ')' && stk.top() == '(') {
					stk.pop();
				}
				else if (str[i] == ']' && stk.top() == '[') {
					stk.pop();
				}
				else {
					while (!stk.empty()) stk.pop();
					printf("no\n");
					flag = 1;
					break;
				}
			}
		}
		if (!flag) {
			if (!stk.empty()) {
				while (!stk.empty()) stk.pop();
				printf("no\n");
				flag = 1;
			}
			else {
				printf("yes\n");

			}
		}

	}
	return 0;

}