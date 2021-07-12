#include <string>
#include <vector>

using namespace std;

int solution(vector<int> arr) {
    int answer = 0;
    int max = 0;
    int lcm = 0;
    for(int i = 0; i < arr.size(); i ++) {
        if(max < arr[i]) max = arr[i];
    }
    printf("%d", max);
    lcm = max;
    while(1) {
        int flag = 0;
        for(int i = 0; i < arr.size(); i ++) {
            if(lcm  % arr[i]!= 0) {
                flag = 1;
                break;
            }
        }
        if(flag == 0) {
            return lcm;
        }
        else {
            lcm += max;
        }
    }
    return answer;
}