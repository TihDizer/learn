use std::collections::HashMap;

impl Solution {
    pub fn first_unique_even(nums: Vec<i32>) -> i32 {
        let mut map = HashMap::new();
        for &num in &nums {
            if let Some(&count) = map.get(&num) {
                map.insert(num, count + 1);
            } else {
                map.insert(num, 1);
            }
        }

        for &num in &nums {
            if *map.get(&num).unwrap() == 1 && num % 2 == 0 {
                return num;
            }
        }
        -1
    }
}
