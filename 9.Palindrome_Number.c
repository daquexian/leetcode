// This is the solution of No.9 problem in LeetCode, https://leetcode.com/problems/palindrome-number/
// Inspired by https://leetcode.com/discuss/23563/line-accepted-java-code-without-the-need-handling-overflow

#include <stdio.h>
#include <stdlib.h>

// Use brilliant code in Problem 7, Inverse Number
/*int isPalindrome(int x){
  	if(x < 0) return 0;
	int reverse = 0, tmp, y = x;
	while(x != 0){
		int tail = x % 10;
		tmp = 10 * reverse + tail;
		if((tmp - tail) / 10 != reverse) return 0;
		reverse = tmp;
		x /= 10;
	}
	return reverse == y;
}*/

//less variables and no need to handle overflow
int isPalindrome(int x){
	if(x < 0 || (x != 0 && x % 10 == 0)) return 0; //It's important.
	int reverse = 0;
	while(reverse < x){
		reverse = 10 * reverse + x % 10;
		x /= 10;
	}
	return reverse == x || reverse / 10 == x;
}

	
int main(int argc, char** argv){
	printf("%d", isPalindrome(atoi(argv[1])));
}
