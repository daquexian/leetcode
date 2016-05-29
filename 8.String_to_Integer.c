// This is the solution of No.8 problem in LeetCode, https://leetcode.com/problems/string-to-integer-atoi/
// It's soooooooo hard. Many cases must be taken into account.
// Clear logic is needed. Thinking twice before coding is best choice.
#include <stdio.h>

int myAtoi(char *str){
	int integer;
	int sign = 1;
	int i = 0;
	while(str[0] == ' ')
		str++;
	if(str[0] == '-'){
		sign = -1;
		str++;
	}else if(str[0] == '+'){
		str++;
	}
	while(str[0] == '0')
		str++;
	
	if(str[0] == '\0' || (str[0] - '0') < 0 || (str[0] - '0') >= 10){
		return 0;
	}else{
		integer = (str[0] - '0') * sign;
		str++;
	}
	for(i = 0; str[i] != '\0' && (str[i] - '0') >= 0 && (str[i] - '0') < 10; i++){
		integer *= 10;
		integer += (str[i] - '0') * sign;
		printf("i = %d, str[i] = %d\n", i, str[i]);
	}
	if((i == 9 && str[0] >= '3') || i > 9 || (integer < 0 && sign > 0) || (integer > 0 && sign < 0)){
		return sign == 1 ? 2147483647 : -2147483648;
	}else{
		return integer;
	}
}

int main(int argc, char** argv){
	printf("%d", myAtoi(argv[1]));
}
