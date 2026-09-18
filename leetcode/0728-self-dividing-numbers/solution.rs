impl Solution {
    pub fn self_dividing_numbers(left: i32, right: i32) -> Vec<i32> {
        let mut ans = Vec::new();
        for num in left..=right {
            let s_num = num.to_string();
            let mut f = false;
            for i in s_num.chars() {
                if i == '0' || num % i.to_digit(10).unwrap() as i32 != 0 {
                    f = true;
                    break;
                }
            }
            if !f {ans.push(num);}
        }
        ans
    }
}
