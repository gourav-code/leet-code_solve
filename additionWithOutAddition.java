class Solution {
    public int getSum(int a, int b) {
        while (b != 0){
            int tmp = (a & b) << 1;
            a = a ^ b;
            b = tmp;
        }
        return a;
    }
}
// also works with python but python has integer size problem