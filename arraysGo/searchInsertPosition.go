package main

import "fmt"
func searchInsert(nums []int, target int) int {
 for i, number := range nums{
	if number >= target{
		return i
	}
	}
	return len(nums)
}
func main(){
array := [4]int{1, 3, 5, 6}
arraySlice := array[:]
fmt.Println(searchInsert(arraySlice, 5))
return
}