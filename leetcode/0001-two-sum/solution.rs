impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let (mut i, mut j) = (0, 1);
        loop {
            if nums[i] + nums[j] == target {
                return vec![i as i32, j as i32]
            }
            if j != nums.len()-1{
                j += 1;
            } else if j != nums.len() - 2 {
                i += 1;
                j = i + 1;
            } else {
                return vec![]
            }
        }
    }
}
