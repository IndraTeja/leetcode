package main

import "fmt"

func twoSum(nums []int, target int) []int {
	var answer []int

	for i, val := range nums {

		for j := i + 1; j < len(nums); j++ {

			if val+nums[j] == target {

				answer = append(answer, i, j)
				break

			}
		}
	}

	return answer
}

func main() {

	nums := []int{2, 7, 11, 15}
	target := 9
	fmt.Println(twoSum(nums, target))

}
