#!/usr/bin/env python3


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_decodings = int(s > "")
        prev_num_decodings = 0
        prev_digit = ""
        
        for curr_digit in s:
            prev_num_decodings, num_decodings = num_decodings, (curr_digit > "0") * num_decodings + (9 < int(prev_digit + curr_digit) < 27) * prev_num_decodings
            prev_digit = curr_digit
            
        return num_decodings


if __name__ == "__main__":
    s = Solution()
    s1 = "12"
    result = s.numDecodings(s1)
    print(result)
