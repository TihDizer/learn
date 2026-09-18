impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        #[inline]
        fn val(byte: u8) -> i32 {
            match byte {
                b'I' => 1,
                b'V' => 5,
                b'X' => 10,
                b'L' => 50,
                b'C' => 100,
                b'D' => 500,
                b'M' => 1000,
                _ => 0,
            }
        }

        let bytes = s.as_bytes();
        let mut sum = 0;

        for w in bytes.windows(2) {
            let curr = val(w[0]);
            let next = val(w[1]);

            if curr < next {
                sum -= curr;
            } else {
                sum += curr;
            }
        }
        sum + val(bytes[bytes.len() - 1])
    }
}
