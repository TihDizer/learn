use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::with_capacity(nums.len());

        for (i, num) in nums.into_iter().enumerate() {
            let compliment = target - num;
            if let Some(&prev_idx) = map.get(&compliment) {
                return vec![prev_idx, i as i32];
            }

            map.insert(num, i as i32);
        }

        vec![]
    }
}
