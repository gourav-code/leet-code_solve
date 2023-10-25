int max(int a, int b){
    if(a>b) return a;
    else return b;
}
int trap(int* height, int heightSize){
    int l,r;
    l=0;
    r = heightSize-1;

    int leftMax=height[l];
    int rightMax = height[r];
    int ans = 0;
    while(l<r){
        if(leftMax<rightMax){
            l++;
            leftMax = max(leftMax, height[l]);
            ans += leftMax-height[l];
        }
        else{
            r--;
            rightMax = max(rightMax, height[r]);
            ans += rightMax-height[r];
        }
    }
    return ans;

}