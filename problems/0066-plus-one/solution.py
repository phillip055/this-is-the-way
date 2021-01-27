class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        loop_index = len(digits) - 1
        last_amount_was_ten = True
        while loop_index >= 0 and last_amount_was_ten:
            last_amount = digits[loop_index] + 1
            last_amount_was_ten = last_amount == 10
            if (last_amount_was_ten):
                digits[loop_index] = 0
            else:
                digits[loop_index] += 1
        
            loop_index-=1
        
        if last_amount_was_ten:
            new_result = [1]
            new_result.extend(digits)
            return new_result
        return digits
