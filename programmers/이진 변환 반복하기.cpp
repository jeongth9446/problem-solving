#include <string>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    int zeroes = 0;
    int a, b;
    answer.push_back(0);
    answer.push_back(0);
    answer[0] = 0; answer[1] = 0;
    while(s != "1") {
        answer[0] ++;    
        int a = s.size();
        s.erase(remove(s.begin(), s.end(), '0'), s.end());
        int b = s.size();
        int n = a-b;
        zeroes += n;
        s = "";
        while(b != 0) {
            if(b % 2 == 1) s = "1" + s;
            else s = "0" + s;
            b/=2;
        }
        cout << s << endl;
    }
    answer[1] = zeroes;
    
    return answer;
}