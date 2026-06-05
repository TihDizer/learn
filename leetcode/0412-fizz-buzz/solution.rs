impl Solution {
    pub fn fizz_buzz(n: i32) -> Vec<String> {
        let mut res = vec![String::new(); n as usize]; 
        for i in 0..n {
            if (i + 1) % 3 == 0 && (i + 1) % 5 == 0 {
                res[i as usize] = "FizzBuzz".to_string();
            } else if (i + 1) % 3 == 0 {
                res[i as usize] = "Fizz".to_string();
            } else if (i + 1) % 5 == 0 {
                res[i as usize] = "Buzz".to_string();
            } else {
                res[i as usize] = (i + 1).to_string();
            }
        }
        res 
    }
}
