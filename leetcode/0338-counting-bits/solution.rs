impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        let mut res = vec![0; (n+1) as usize];
        for i in 1..=n {
            res[i as usize] = res[(i >> 1) as usize] + (i & 1);
        }
        res
    }
}
