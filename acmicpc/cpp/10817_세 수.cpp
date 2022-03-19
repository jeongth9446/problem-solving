#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void) {

	int arr[3] = { 0 };

	for (int i = 0; i < 3; i++)
		scanf("%d", &arr[i]);

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			if (arr[i] < arr[j])
			{
				int tmp;
				tmp = arr[i];
				arr[i] = arr[j];
				arr[j] = tmp;
			}
		}
	}
	printf("%d\n", arr[1]);
	return 0;
}
