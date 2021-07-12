
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <stack>
using namespace std;
int main(void) {
	char a[10001];
	char b[10001];

	int len_a, len_b;
	scanf("%s %s", a, b);

	stack<int> stack_a;
	stack<int> stack_b;
	stack<int> stack_c;
	len_a = strlen(a);
	len_b = strlen(b);

	for (int i = 0; i < len_a; i++)
		stack_a.push(a[i] - '0');
	for (int i = 0; i < len_b; i++)
		stack_b.push(b[i] - '0');

	int rem = 0;
	while (stack_a.size() != 0 || stack_b.size() != 0) {
		int aa, bb;
		if (stack_a.size() != 0) {
			aa = stack_a.top();
			stack_a.pop();
		}
		else aa = 0;
		if (stack_b.size() != 0) {
			bb = stack_b.top();
			stack_b.pop();
		}
		else bb = 0;
		stack_c.push((aa + bb + rem) % 10);
		if (aa + bb + rem > 9) 
			rem = 1;
		else 			
			rem = 0;
	}
	if (rem == 1) printf("%d", rem);
	while (stack_c.size() != 0) {
		printf("%d", stack_c.top());
		stack_c.pop();
	}
	
	return 0;

}