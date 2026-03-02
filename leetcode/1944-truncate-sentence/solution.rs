impl Solution {
    pub fn truncate_sentence(s: String, k: i32) -> String {
        let mut space_count = 0;
        for (i, c) in s.char_indices() {
            if c == ' ' {
                space_count += 1;
                if space_count == k {
                    return s[..i].to_string();
                }
            }
        }
        s
    }
}
