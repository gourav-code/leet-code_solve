#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include<stdbool.h>

bool anagram(int* hashTable, char* s, char* t) {
    for (size_t i = 0; i < strlen(s); ++i) {
        if (s[i] == '\0')
            break;
        ++hashTable[((int)s[i]) - 97];
    }

    for (size_t j = 0; j < strlen(t); ++j) {
        if (t[j] == '\0') {
            break;
        }
        hashTable[((int)(t[j])) - 97] = 0;
    }

    for (int k = 0; k < 26; ++k) {
        if (hashTable[k] != 0)
            return false;
    }

    return true;
}

char** findWords(char** words, int wordsSize, int* returnSize) {
    int hashTable[26];
    char** result = NULL;
    *returnSize = 0;
    int resultCapacity = 0;

    char* header[3] = {
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm"
    };

    for (int i = 0; i < wordsSize; ++i) {
        char temp[strlen(words[i]) + 1];

        for (int j = 0; words[i][j] != '\0'; ++j) {
            temp[j] = tolower(words[i][j]);
        }
        temp[strlen(words[i])] = '\0';

        for (int j = 0; j < 3; ++j) {
            memset(hashTable, 0, sizeof(int) * 26);

            if (anagram(hashTable, temp, header[j])) {
                if (*returnSize >= resultCapacity) {
                    resultCapacity += 10;
                    result = realloc(result, sizeof(char*) * resultCapacity);
                }

                result[*returnSize] = malloc(strlen(words[i]) + 1);
                strcpy(result[*returnSize], words[i]);
                ++(*returnSize);
                break;
            }
        }
    }

    return result;
}

int main() {
    char* words[] = {
        "Hello",
        "Alaska",
        "Dad",
        "Peace",
        "Question"
    };

    int returnSize;
    char** result = findWords(words, 5, &returnSize);

    printf("Result:\n");
    for (int i = 0; i < returnSize; ++i) {
        printf("%s\n", result[i]);
        free(result[i]);
    }

    free(result);

    return 0;
}
