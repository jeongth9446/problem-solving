#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

string make_sequence(vector<vector<int>> &game_board, int i, int j, int z, int k) {
    game_board[i][j] = k;
    string tmp = "C";
    if(i-1>= 0 && game_board[i-1][j] == z) 
        tmp = tmp + "U" + make_sequence(game_board, i-1, j, z, k) + "B";
    if(j-1>= 0 && game_board[i][j-1] == z) 
        tmp = tmp + "L" + make_sequence(game_board, i, j-1, z, k) + "B";
    if(i+1< game_board.size() && game_board[i+1][j] == z) 
        tmp = tmp + "D" + make_sequence(game_board, i+1, j, z, k) + "B";
    if(j+1< game_board.size() && game_board[i][j+1] == z) 
        tmp = tmp + "R" + make_sequence(game_board, i, j+1, z, k) + "B";
    
    return tmp; 
}
struct node {
    string seq;
    int idx;
}; 
int solution(vector<vector<int>> game_board, vector<vector<int>> table) {
    int answer = 0;
    vector<string> board_seq;
    
    for(int i = 0; i < game_board.size(); i ++) {
        for(int j = 0; j < game_board[i].size(); j ++) {
            if(game_board[i][j] == 0) {
                board_seq.push_back(make_sequence(game_board, i, j, 0, 1));
            }
        }
    }
    sort(board_seq.begin(), board_seq.end());
    
    vector<vector<int>> table1;
    table1 = table;
    
    int n = 4;
    while(n--) {
        int cnt = 0;
        vector<struct node> table_seq1;
        struct node tmp;
        for(int i = 0; i < game_board.size(); i ++) {
            for(int j = 0; j < game_board[i].size(); j ++) {
                if(table1[i][j] == 1) {
                    tmp.seq = make_sequence(table1, i, j, 1, --cnt);
                    tmp.idx = cnt;
                    table_seq1.push_back(tmp);
                }
            }
        }
        table = table1;

        for(int i = 0; i < table_seq1.size(); i ++) {
            for(int j = 0; j < board_seq.size(); j ++) {
                if(table_seq1[i].seq == board_seq[j]) {
                    for(int k = 0; k < board_seq[j].size(); k ++) {
                        if(board_seq[j].at(k) == 'C') answer ++;
                    }
                    for(int l = 0; l < game_board.size(); l ++) {
                        for(int m = 0; m < game_board.size(); m ++) {
                            if(table[l][m] == table_seq1[i].idx) {
                                table[l][m] = 0;
                            }
                        }    
                    }   
                    board_seq.erase(board_seq.begin() + j);
                    break;
                }
            }
        }
        for(int l = 0; l < game_board.size(); l ++) {
            for(int m = 0; m < game_board.size(); m ++) {
                if(table[l][m] < 0) {
                    table[l][m] = 1;
                }
            }    
        }
        for(int i = 0; i < game_board.size(); i ++) {
            for(int j = 0; j < game_board[i].size(); j ++) {
                table1[i][j] = table[j][game_board.size() - i-1];
            }
        }

    }
    return answer;
}