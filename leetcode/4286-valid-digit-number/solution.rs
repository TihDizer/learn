impl Solution {
    pub fn valid_digit(mut n: i32, x: i32) -> bool {
        let mut ans = false;
        while n > 0 {
            if n % 10 == x {
                ans = true;
            }
            if n < 10 && n % 10 == x {
                ans = false;
            }
            n /= 10;
        }
        ans
    }
}
