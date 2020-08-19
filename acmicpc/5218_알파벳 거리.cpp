#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
	int TestCases;

	char src1[21], src2[21];

	scanf("%d", &TestCases);
	while (TestCases--) {
		scanf("%s %s", src1, src2);
		printf("Distances: ");
		for (int i = 0; i < strlen(src1); i++)
			printf("%d ", (src2[i] - src1[i]+26)%26);
		printf("\n");
	}

	return 0;

}