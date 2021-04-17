package main

import "fmt"

func isPalindrome(x int) bool {

	if x < 0 {
		return false
	}

	var rev int = 0
	var temp int = x

	for temp > 0 {

		rev = (rev * 10) + (temp % 10)
		temp = (temp / 10)

	}

	if x == rev {
		return true
	} else {
		return false
	}

}

func main() {

	var x int = 1991
	if isPalindrome(x) {
		fmt.Printf("%d is a palindrome", x)
	} else {
		fmt.Printf("%d is not a palindrome", x)
	}

}
