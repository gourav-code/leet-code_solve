/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize){
    int postfix = 1;
    int prefix = 1;
    int* returnArr = malloc(sizeof(int)*numsSize);

    for(int i=0;i<numsSize;++i){
        returnArr[i] = prefix;
        prefix = nums[i]*prefix;
    }

    for(int k = numsSize-1;k>=0;--k){
        returnArr[k] = postfix*returnArr[k];
        postfix = nums[k]*postfix;
    }

    *returnSize = numsSize;
    return returnArr;
}