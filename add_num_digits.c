#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    while (n) {
        answer += (n % 10);
        n /= 10;
    }
    return answer;
}

int main(void) {
    int answer = 0;
    answer = solution(123);
    printf("answer is %d", answer);

    return 0;
}