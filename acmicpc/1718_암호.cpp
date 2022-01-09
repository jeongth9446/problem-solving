#include <stdio.h>
#include <string.h>

int main()
{
    //printf("Hello World");

    char s[30001];
    char pass[30001];
    
    scanf("%[^\n]s", s);
    scanf("%s", pass);
    
    //printf("%s\n", s);
    //printf("%s\n", pass);
    
    for(int i = 0; i < strlen(s); i ++) {
        if(s[i] == ' ') {
            printf(" ");
            continue;
        }
        else {
            int k1 = s[i]-'a';
            int k2 = pass[i%strlen(pass)] - 'a';
            
            printf("%c", ((k1 + 26)-k2-1)%26+'a');
        }
    }
    
    return 0;
}
