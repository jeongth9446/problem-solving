#include <stdio.h>

int main(void) {
    int inputNumber[3];
    int maxNumber = 0;

    for(int i = 0; i < 3; i ++) {
        scanf("%d", &inputNumber[i]);
        if(inputNumber[i] > maxNumber) maxNumber = inputNumber[i];
    }
    
    if(inputNumber[0] == inputNumber[1] && inputNumber[1] == inputNumber[2]) {
        printf("%d\n", 10000 + inputNumber[0]*1000);
    } else if(inputNumber[0] == inputNumber[1] || inputNumber[1] == inputNumber[2]) {
        printf("%d\n", 1000 + inputNumber[1]*100);
    } else if(inputNumber[0] == inputNumber[2]) {
        printf("%d\n", 1000 + inputNumber[0]*100);
    } else {
        printf("%d\n", maxNumber * 100);
    }   

    return 0;
    
}