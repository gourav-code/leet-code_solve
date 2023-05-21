// #include <string.h>
// #include <stdio.h>
// #include <stdlib.h>

// char * copyString( char s[], int i, int j){
//     char* tmp;
//     tmp = (char*)malloc((i-j+1)*sizeof(char));
//     for(; i<=j && s[i] != '\0'; ++i){
//         // tmp[i] = s[i];
//         printf("%c\n",s[i]);
//         memset(tmp + i, s[i], sizeof(char));
//     }
//     return tmp;
// }

// char * subPart(int l, int r, char * s, char * res){
//     int resLen = strlen(res);

//     while (l>=0 && r<strlen(s) && s[l] == s[r])
//     {
//         /* code */
//         if((r-l+1) > resLen){
//             res = copyString(s,l,r);
//             resLen = strlen(res);
//         }
//         ++r;
//         --l;
//     }
    
    
//     return res;
// }

// char * longestPalindrome(char * s){
//     int stringLen = strlen(s)-1;
//     char* reverseS;
//     reverseS = (char*)malloc(1001*sizeof(char));
//     int l,r;

//     for(int i=0;i<=stringLen;i++){
//         if(stringLen%2 != 0){
//             l = i;
//             r = i;
//             reverseS = subPart(l, r, s, reverseS);

//         }
//         else{
//             l = i;
//             r = i+1;
//             reverseS = subPart(l,r,s,reverseS);
//         }
//     }

//     return reverseS;
// }

#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


// This function prints the longest palindrome substring
// It also returns the length of the longest palindrome
char * longestPalindrome(char* s)
{
	// Get length of input sing
	int n = strlen(s);

	// table[i][j] will be false if substring str[i..j] is
	// not palindrome. Else table[i][j] will be true
	bool table[n][n];

	memset(table, false, sizeof(table));

	// All substrings of length 1 are palindromes
	int maxLength = 1;
	int start = 0;

	for (int i = 0; i < n; ++i)
		table[i][i] = true;

	// Check for sub-string of length 2.
	for (int i = 0; i < n - 1; ++i) {
		if (s[i] == s[i + 1]) {
			table[i][i + 1] = true;
			start = i;
			maxLength = 2;
		}
	}

	// Check for lengths greater than 2.
	for (int k = 3; k <= n; ++k) {
		// Fix the starting index
		for (int i = 0; i < n - k + 1; ++i) {
			// Get the ending index of substring from
			// starting index i and length k
			int j = i + k - 1;

			// Checking for sub-string from ith index to jth
			// index if str[i+1] to str[j-1] is a palindrome
			if (table[i + 1][j - 1] && s[i] == s[j]) {
				table[i][j] = true;

				if (k > maxLength) {
					start = i;
					maxLength = k;
				}
			}
		}
	}
    char* result = malloc((maxLength + 1) * sizeof(char));
    strncpy(result, s + start, maxLength);
    result[maxLength] = '\0';

    return result;
}




void main(){
    int length;
    char s[100];
    //printf("Length a string : %ld",strlen(str));
    char *p;
    fgets(s, 50, stdin);
    length = strlen(s);
    printf("whole string %s",s);
    // printf("lenght of the string = %d",length);
    p=longestPalindrome(s);
    printf("whole palindromic string %s",p);
    
    
}

