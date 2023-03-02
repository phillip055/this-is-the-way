class Solution:
    def compress(self, chars: List[str]) -> int:
        idx0 = 0
        idx1 = 1

        writecursorIdx = 0

        while idx1 < len(chars):
            if chars[idx0] == chars[idx1]:
                idx1 += 1
                continue
            else:
                chars[writecursorIdx] = chars[idx0]
                writecursorIdx += 1
                if idx1 - idx0 > 1:
                    for i in str(idx1-idx0):
                        chars[writecursorIdx] = i
                        writecursorIdx += 1
                idx0 = idx1
                idx1 = idx0 + 1
        

        if writecursorIdx < idx1:
            chars[writecursorIdx] = chars[idx0]
            writecursorIdx += 1
            if idx1 - idx0 > 1:
                for i in str(idx1-idx0):
                    chars[writecursorIdx] = i
                    writecursorIdx += 1
        return writecursorIdx
                    
