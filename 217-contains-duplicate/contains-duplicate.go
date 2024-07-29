func containsDuplicate(nums []int) bool {
    counter := make(map[int]int)
    for _, num := range nums {
        counter[num]++
        if counter[num] > 1 {
            return true
        }
    }
    return false
}