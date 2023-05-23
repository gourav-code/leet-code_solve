#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char * reverseString(char* s,int n){
    char* result = malloc(n*sizeof(char));

    for(int i=0;i<n-1;++i){
        // strncpy(result+i,s+(n-i-2),1);
        result[i] = s[n-i-2];
    }
    result[n-1] = '\0';
    result[2] = 't';
    return result;
}


int main(){

    char s[50];
    fgets(s,50,stdin);
    int length = strlen(s);

    printf("Before : %s\n",s);
    char* reverseS;

    reverseS = reverseString(s,length);

    printf("After reverse : %s\n",reverseS);
    free(reverseS);

    printf("After new : %s\n",s);

    return 0;
}