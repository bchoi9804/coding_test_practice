#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* s) {
    int answer = 0;
    answer = atoi(s); // atoi()함수는 문자를 정수로 변환해 준다. stdlib.h가 필요하다.
    // printf("%d\n", answer); 테스트
    return answer;
}