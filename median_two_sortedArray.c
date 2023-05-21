// #include <stdio.h>
// #include <time.h>
// int main() {
// time_t biggest = 0x7FFFFFFF;
// printf("biggest = %s \n", ctime(&biggest) );
// return 0;
// }


double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){
    int total = nums1Size+nums2Size;
    if (total == 1){
        return nums1Size == 1 ? nums1[0] : nums2[0];
    }
    int arr1[total];

    int i=0;
    int j=0;
    int k=0;

    while(i< nums1Size && j<nums2Size){
        if (nums1[i]<= nums2[j]){
            arr1[k] = nums1[i];
            ++i;
        }
        else{
            arr1[k] = nums2[j];
            ++j;
        }
        ++k;
    }

    while(i<nums1Size){
        arr1[k] = nums1[i];
        ++i;
        ++k;
    }

    while (j<nums2Size)
    {
        /* code */
        arr1[k] = nums2[j];
        ++j;
        ++k;
    }
    
    i = total/2;

    //even case
    if (total%2 == 0){
        j = i-1;                 //remove this line
        return (arr1[i] + arr1[j])/2.00;              //replace j with i-1 code will be faster
    }
    else{
        return arr1[i];
    }

}