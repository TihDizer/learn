impl Solution {
    pub fn reverse_degree(s: String) -> i32 {
        s.bytes()
            .enumerate()
            .map(|(i, ch)| (b'z' + 1 - ch) as i32 * (i as i32 + 1))
            .sum()
    }
}
