
#define BDRY 8
#include <iostream>
#include <string.h>

using namespace std;

bool func_chk_boundary(int, int, int, int);
void func_move(int *, int *, int, int);

int main(void) {
	string a, b;
	int n;

	int king_x, king_y;
	int stone_x, stone_y;

	cin >> a >> b >> n;
	king_y = a.at(0) - 'A', king_x = a.at(1) - '1';
	stone_y = b.at(0) - 'A', stone_x = b.at(1) - '1';

	while (n--) {
		string cmd;
		cin >> cmd;
		int x, y;
		if (!cmd.compare("R"))					y = 1, x = 0;
		else if (!cmd.compare("L"))				y = -1, x = 0;
		else if (!cmd.compare("B"))				y = 0, x = -1;
		else if (!cmd.compare("T"))				y = 0, x = 1;
		else if (!cmd.compare("RT"))			y = 1, x = 1;
		else if (!cmd.compare("LT"))			y = -1, x = 1;
		else if (!cmd.compare("RB"))			y = 1, x = -1;
		else if (!cmd.compare("LB"))			y = -1, x = -1;

		if (func_chk_boundary(king_x, king_y, x, y)) continue;
		if (king_x + x == stone_x && king_y + y == stone_y) {
			if (func_chk_boundary(stone_x, stone_y, x, y)) continue;
			func_move(&stone_x, &stone_y, x, y);
		}
		func_move(&king_x, &king_y, x, y);
	}
	printf("%c%c\n%c%c\n", king_y + 'A', king_x + '1', stone_y + 'A', stone_x + '1');
	return 0;
}

bool func_chk_boundary(int n, int m, int x, int y) {
	if (n + x >= BDRY || m + y >= BDRY) return true;
	else if (n + x < 0 || m + y < 0) return true;
	else return false;
}

void func_move(int* n, int* m, int x, int y) {
	*n += x;
	*m += y;
}