#include<string.h>
char * longestPalindrome(char * s){
    int stringLen = strlen(s)-1;
    char reverseS[1001];
        
    char temp1[1001];
    char temp2[1001];
    int i,j;

    for(int i=0,j=stringLen;i<=stringLen;i++,j--){
        reverseS[i] = s[j];
    }
    i=0;
    while (i<stringLen)
    {
        /* code */
        if(reverseS[i] == s[i]){
            strcat(temp2,reverseS[i]);
            
        }
        else{
            if(strlen(temp1) < strlen(temp2)){
                strcpy(temp1,temp2);
                strcpy(temp2, "");
            }
        }
        ++i;
    }
    return temp1;


}