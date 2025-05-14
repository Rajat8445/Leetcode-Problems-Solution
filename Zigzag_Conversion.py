class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        current_row, going_down = 0, False
        for char in s:
            rows[current_row] += char
            if current_row == 0:
                going_down = True
            elif current_row == numRows - 1:
                going_down = False
            current_row += 1 if going_down else -1
        return ''.join(rows)
print(Solution().convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"