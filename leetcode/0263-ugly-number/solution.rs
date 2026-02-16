impl Solution {
    pub fn is_ugly(mut n: i32) -> bool {
        if n == 0 {return false;}
        for i in [2, 3, 5]{while n % i == 0{n /= i;}}
        n == 1
    }
}
