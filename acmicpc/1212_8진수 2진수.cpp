/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <string.h>

int main()
{
    char tmp[333335];
    
    scanf("%s", tmp);
    int str_len = strlen(tmp);
    
    if(tmp[0] == '0' && str_len == 1) { //0이 입력된 경우
        printf("0\n");
        return 0;
    }
    
    int idx = -1;
    
    while(tmp[++idx] == '0');
    
    
    for(int i = idx; i < str_len; i ++) {
        if(i == idx) {
            if(tmp[i] == '1') printf("1");
            if(tmp[i] == '2') printf("10");
            if(tmp[i] == '3') printf("11");
        } else {
            if(tmp[i] == '0') printf("000");
            if(tmp[i] == '1') printf("001");
            if(tmp[i] == '2') printf("010");
            if(tmp[i] == '3') printf("011");
        }
        
        if(tmp[i] == '4') printf("100");
        if(tmp[i] == '5') printf("101");
        if(tmp[i] == '6') printf("110");
        if(tmp[i] == '7') printf("111");
    }
    printf("\n");
    return 0;
    
}
