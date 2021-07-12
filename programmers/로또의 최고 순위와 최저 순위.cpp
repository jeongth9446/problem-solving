#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// lottos_len은 배열 lottos의 길이입니다.
// win_nums_len은 배열 win_nums의 길이입니다.
int* solution(int lottos[], size_t lottos_len, int win_nums[], size_t win_nums_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(1);
    int lolo[46] = {0};
    int zeros = 0;
    int min = 0;
    int max = 0;
    for(int i = 0; i < win_nums_len; i ++) {
        lolo[win_nums[i]] = 1;
    }
    for(int i = 0; i < lottos_len; i ++) {
        if(lottos[i] == 0) {
            zeros ++;
        }
        else {
            if(lolo[lottos[i]] == 1) {
                printf("%d", lottos[i]);
                min++;
                max++;
            }
        }
    }
    answer[1] = 7-min;
    if(answer[1] == 7) answer[1] = 6; 
    answer[0] = 7-(max + zeros);
    if(answer[0] == 7) answer[0] = 6;
    return answer;
    
}