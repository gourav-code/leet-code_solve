#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>


bool checkInclusion(char* s1, char* s2) {
    int i=0,j=0;
    int n1=strlen(s1);
    int n2=strlen(s2);
    int arr1[26]={0};
    int arr2[26]={0};
    if(n2<n1){
        return false;
    }
    for(int tmp=0;tmp<n1&&s1[tmp]!='\0';++tmp){
        arr1[s1[tmp]-97]++;
    }
    for(;j<n2&&s2[j]!='\0';++j){
        arr2[s2[j]-97]++;
        for(int tmp=0;tmp<26;++tmp){
            if(j==4){
                printf("i: %d, char: %c, arr1: %d, arr2: %d\n",i,(char)(tmp+97),arr1[tmp],arr2[tmp]);
            }
            if(arr1[tmp]!=arr2[tmp]){
                break;
            }
            if(tmp==25){
                return true;
            }
        }
        if(j-i+1==n1){
            arr2[s2[i]-97]--;
            ++i;

        }
    }
    return false;
}


int main(void){
    char s1[]="ab";
    char s2[]="eidbaooo";
    if(checkInclusion(s1,s2)){
        printf("YES BOSS\n");
    }
    else{
        printf("hell no\n");
    }


return 0;
}