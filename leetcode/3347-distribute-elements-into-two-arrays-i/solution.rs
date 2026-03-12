impl Solution {
    pub fn result_array(nums: Vec<i32>) -> Vec<i32> {
        let mut arr1 = vec![nums[0]];
        let mut arr2 = vec![nums[1]];
        let mut i = 2;
        while i < nums.len() {
            if arr2[arr2.len()-1] < arr1[arr1.len()-1] {
                arr1.push(nums[i]);
            } else {
                arr2.push(nums[i]);
            }
            i += 1;
        }
        arr1.extend(arr2);
        arr1
    }
}
