// This is the solution of No.7 problem in LeetCode, https://leetcode.com/problems/reverse-integer/
// This problem seems easy, howerver, it is hard to solve it correctly.

#include <stdio.h>
#include <stdlib.h>

int reverse(int x){
	int flag = 1;
	if(x<0){
		flag = -1;
		x *= -1;
	}
	// the smallest integer is -2 << 31, while the greatest integer is 2 << 31 - 1, but -2 << 31 can't be the result, so we can convert negative numbers to positive ones.
	int i;
	for(i = 1; x / i >= 10; i *= 10)	// wrong code: for(i = 1; x / i < 10; i *= 10) , it gets wrong i when x has 10 digits.
		;

	if(i == 1000000000 && (x % 10) > 3)
		return 0;
	int j = 1;
	int ret = 0;
	while(j != i){
		ret *= 10;
		ret += (x % (j * 10)) / j;
		j *= 10;
	}
	ret *= 10;
	ret += x / j;
	if(ret < 0)
		return 0;
	ret *= flag;
	return ret;
}

int main(int argc, char** argv){
	int x = atoi(argv[1]);

	printf("%d", reverse(x));
}

