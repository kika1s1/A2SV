func isPalindrome(x int) bool {
    var b int
    var t int = x
    if  x < 0 {
        return false
    }
    for x > 0{
        b = b * 10 + x % 10
        x = x / 10
    }
    if t == b {
        return true
    }else {
        return false
    }
    
}