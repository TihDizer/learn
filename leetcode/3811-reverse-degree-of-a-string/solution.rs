impl Solution {
    pub fn reverse_degree(s: String) -> i32 {
        let mut ans = 0;
        for (i, ch) in s.as_bytes().into_iter().enumerate() {
            let r_ch = b'z' + 1 - ch;
            ans += r_ch as i32 * (i as i32 + 1);
        }
        ans
    }
}
