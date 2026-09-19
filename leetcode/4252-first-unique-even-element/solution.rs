use std::collections::HashMap;

impl Solution {
    pub fn first_unique_even(nums: Vec<i32>) -> i32 {
        let mut counts = HashMap::new();

        for &num in nums.iter().filter(|&&x| x % 2 == 0) {
            *counts.entry(num).or_insert(0) += 1;
        }

        nums.into_iter()
            .find(|&x| x % 2 == 0 && counts.get(&x) == Some(&1))
            .unwrap_or(-1)
    }
}
