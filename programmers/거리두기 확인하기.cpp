#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<vector<string>> places) {
    vector<int> answer;
    
    
    for(int i = 0; i < places.size(); i ++) {
        int flag = 0;
        int map[5][5];
        for(int j = 0; j < places[i].size(); j ++) {
            for(int k = 0; k < places[i][j].size(); k ++) {
                if(places[i][j].at(k) == 'P')
                    map[j][k] = 1;
                else if(places[i][j].at(k) == 'X')
                    map[j][k] = 2;
                else if(places[i][j].at(k) == 'O')
                    map[j][k] = 0;
            }
        }
        printf("test %d\n", i);
        
        for(int  j = 0; j < 5; j ++) {
            for(int k = 0; k < 5; k ++) {
                if(map[j][k] == 1) { //사람이 앉았으면
                    if(j-1 >= 0 && map[j-1][k] == 1) { //옆에 사람이면,
                        flag = 1;
                    }
                    else if(j-1 >= 0 && map[j-1][k] == 0) { //비었으면,
                        if(j-2 >= 0 && map[j-2][k] == 1) {
                            flag = 1;
                        }
                        if(j-1 >= 0 && k-1 >= 0 && map[j-1][k-1] == 1) {
                            flag = 1;
                        }
                        if(j-1 >= 0 && k+1 < 5 && map[j-1][k+1] == 1) {
                            flag = 1;
                        }
                    }
                    if(k-1 >= 0 && map[j][k-1] == 1) { //옆에 사람이면,
                        flag = 1;
                    }
                    else if(k-1 >= 0 && map[j][k-1] == 0) { //비었으면,
                        if(k-2 >= 0 && map[j][k-2] == 1) {
                            flag = 1;
                        }
                        if(j-1 >= 0 && k-1 >= 0 && map[j-1][k-1] == 1) {
                            flag = 1;
                        }
                        if(j+1 < 5 && k-1 >= 0 && map[j+1][k-1] == 1) {
                            flag = 1;
                        }
                    }
                    if(j+1 < 5 && map[j+1][k] == 1) { //옆에 사람이면,
                        flag = 1;
                    }
                    else if(j+1 < 5 && map[j+1][k] == 0) { //비었으면,
                        if(j+2 < 5 && map[j+2][k] == 1) {
                            flag = 1;
                        }
                        if(j+1 < 5 && k-1 >= 0 && map[j+1][k-1] == 1) {

                            flag = 1;
                        }
                        if(j+1 < 5 && k+1 < 5 && map[j+1][k+1] == 1) {
                            flag = 1;
                        }
                    }
                    if(k +1 < 5 && map[j][k+1] == 1) { //옆에 사람이면,
                        flag = 1;
                    }
                    else if(k+1 < 5 && map[j][k+1] == 0) { //비었으면,
                        if(k+2 < 5 && map[j][k+2] == 1) {
                            flag = 1;
                        }
                        if(j+1 < 5 && k+1 < 5 && map[j+1][k+1] == 1) {
                            flag = 1;
                        }
                        if(j-1 >=0 && k+1 < 5 && map[j-1][k+1] == 1) {
                            flag = 1;
                        }
                    }
                }           
            }
        }
        if(flag == 1) answer.push_back(0);
            else answer.push_back(1);
    }
    return answer;
}