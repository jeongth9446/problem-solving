#include <stdio.h>

int main(void) {

    int hour, minute;
    int need_time;

    /** input */
    scanf("%d %d", &hour, &minute);
    scanf("%d", &need_time);

    minute += need_time;

    while(minute >= 60) {
        minute -= 60;
        hour ++;
    }
    hour %= 24;

    /** output */
    printf("%d %d\n", hour, minute);

    return 0;
}