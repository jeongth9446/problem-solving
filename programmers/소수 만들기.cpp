#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// nums_len은 배열 nums의 길이입니다.
int solution(int nums[], size_t nums_len) {
    int answer = 0;
    int prime[3000] = {0};
    prime[0] = 1; prime[1] = 1;
    for(int i = 2; i < 3000; i ++) {
        if(prime[i] == 0) {
            for(int j = i*2; j < 3000; j += i)
                prime[j] = 1;
        }
    }
    for(int i = 0; i < nums_len; i ++) {
        for(int j = i+1; j < nums_len; j ++) {
            for(int k = j+1; k < nums_len; k ++) {
                int c = nums[i] + nums[j] + nums[k];
                if(prime[c] == 0) answer ++;
            }
        }
    }
    
    return answer;
}