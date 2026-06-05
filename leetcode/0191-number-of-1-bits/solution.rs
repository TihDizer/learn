impl Solution {
    pub fn hamming_weight(mut n: i32) -> i32 {
        let mut weight = 0;
        while n != 0 {
            weight += n % 2;
            n /= 2;
        }
        weight
    }
}
