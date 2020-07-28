#include <stdio.h>
#include <string.h>

int main(void) {
    char str[101];
    int cnt[200] = {0};
    
    scanf("%s", str);
    
    for(int i = 0; i < strlen(str); i ++)
        cnt[str[i]] ++;
    
    for(int i = 'a'; i <= 'z'; i ++)
        printf("%d ", cnt[i]);
    
    return 0;
}