impl Solution {
    pub fn find_closest_number(nums: Vec<i32>) -> i32 {
        let mut min = i32::MAX;
        for i in 0..nums.len() {
            if nums[i].abs() < min.abs() || nums[i].abs() == min.abs() && nums[i] > min { min = nums[i] };
        }
        min
    }
}
