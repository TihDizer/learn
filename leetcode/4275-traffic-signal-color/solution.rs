impl Solution {
    pub fn traffic_signal(timer: i32) -> String {
        match timer {
            0 => "Green".to_string(),
            30 => "Orange".to_string(),
            31..=90 => "Red".to_string(),
            _ => "Invalid".to_string(),
        }
    }
}
