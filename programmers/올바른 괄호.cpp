#include<string>
#include <iostream>
#include <stack>


using namespace std;

bool solution(string s)
{
    bool answer = true;

    stack<int> stk;
    
    for(int i = 0; i < s.size(); i ++) {
        if(s.at(i) == '(') {
            stk.push(1);
        } else {
            if(stk.size() != 0 && stk.top() == 1) {
                stk.pop();
            }
            else
                return false;
        }
    }
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    cout << "Hello Cpp" << endl;

    if(stk.size() == 0)
        return true;
    else return false;
}