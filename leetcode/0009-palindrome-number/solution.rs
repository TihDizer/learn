impl Solution {
    pub fn is_palindrome(mut x: i32) -> bool {
        if x < 0 {
            return false;
        } 
        if x < 10 {
            return true;
        }
        let mut digits = Vec::new();
        while x > 0 {
            digits.push(x % 10);
            x /= 10;
        }
        for i in 0..digits.len()/2 {
            if digits[i] != digits[digits.len() - i - 1] {
                return false;
            }
        }
        true
    }
}
