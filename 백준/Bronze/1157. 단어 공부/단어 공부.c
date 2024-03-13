#include <stdio.h>
#include <string.h>

int main() {
    char sentence[1000001]; // 단어의 길이는 최대 100만
    int cnt[26]={0, }; // 알파벳이 26개
    int size, max;
    int i, j, select=0, result=0;

    scanf("%s", sentence);
    size = strlen(sentence);

    for(i = 0; i<size; i++)
    {
        for(j='a'; j<='z'; j++) // 소문자 세기
        {
            if(sentence[i] == j)
                cnt[j-'a']++;
        }
        
        for(j='A'; j<='Z'; j++) // 대문자 세기
        {
            if(sentence[i] == j)
                cnt[j-'A']++;
        }
    }

    max = cnt[0];

    // 최댓값 찾기
    for(i=1; i<26; i++)
    {
        if(max < cnt[i])
        {
            max = cnt[i];
            select = i;
        }
    }
    
    // 최댓값을 가진 알파벳이 몇 개인지 찾기
    for(i=0; i<26; i++)
    {
        if(max == cnt[i])
            result++;
    }

    // 최댓값이 같은 알파벳이 여럿이면 ? 출력
    if(result > 1)
        printf("?\n");
    // 하나면 해당 문자를 대문자로 출력
    else
        printf("%c", select+'A');
    return 0;
}