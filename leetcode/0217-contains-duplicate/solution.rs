use std:: collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut s = HashSet::with_capacity(nums.len());
        nums.into_iter().any(|i| !s.insert(i))
    }
}
