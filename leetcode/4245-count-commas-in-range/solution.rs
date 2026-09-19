impl Solution {
    pub fn count_commas(n: i32) -> i32 {
        if n > 999 { n - 999 } else { 0 }
    }
}
