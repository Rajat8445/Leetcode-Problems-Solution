class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, n = 0, len(s)
        sign, result = 1, 0
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        # Step 1: Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check for sign
        if i < n and s[i] in "+-":
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 3: Convert digits to integer
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

            # Step 4: Handle 32-bit integer overflow
            if sign * result > INT_MAX:
                return INT_MAX
            if sign * result < INT_MIN:
                return INT_MIN

        return sign * result
print(Solution().myAtoi("   -42"))  # Output: -42
print(Solution().myAtoi("4193 with words"))  # Output: 4193
print(Solution().myAtoi("words and 987"))  # Output: 0