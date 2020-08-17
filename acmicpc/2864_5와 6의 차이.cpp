#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
using namespace std;

int main(void) {

	char ain[8], bin[8];

	scanf("%s %s", ain, bin);

	for (int i = 0; i < strlen(ain); i++)
		if (ain[i] == '5') ain[i] = '6';
	for (int i = 0; i < strlen(bin); i++)
		if (bin[i] == '5') bin[i] = '6';

	string amax(ain);
	string bmax(bin);
	int max = atoi(amax.c_str()) + atoi(bmax.c_str());
	
	for (int i = 0; i < strlen(ain); i++)
		if (ain[i] == '6') ain[i] = '5';
	for (int i = 0; i < strlen(bin); i++)
		if (bin[i] == '6') bin[i] = '5';

	string amin(ain);
	string bmin(bin);
	int min = atoi(amin.c_str()) + atoi(bmin.c_str());
	printf("%d %d\n", min, max);
	
	return 0;
	
}