#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define LETTER 26


typedef struct {
    char element;
    unsigned int freq;
} character;

character hashTable[LETTER];


// memset(hashTable, -1 , sizeof(character) * LETTER);
bool isAnagram(char * s, char * t){
    int n = strlen(s);
    int m = strlen(t);
    if(n != m)
        return false;
    
    for(int i=0;i<n;++i){
        hashTable[((int)s[i])-97].element = s[i];
        
        ++hashTable[((int)s[i])-97].freq;
    }
    
    for(int j=0;j<n;++j){
        if(hashTable[((int)(t[j]))-97].element == t[j] && hashTable[((int)(t[j]))-97].element != '\0'){
         --hashTable[((int)(t[j]))-97].freq;   
        }
    }
    for(int k=0;k<n;++k){
        if(hashTable[((int)(s[k]))-97].freq != 0)
            return false;
    }

    return true;
}

int main(){
    
    char* s = "ab";
    char* t = "ba";

    
    if(isAnagram(s,t)){
        printf("Yes\n");
    }
    else{
        printf("no");
    }
    
    return 0;
}

