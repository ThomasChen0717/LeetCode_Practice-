# Approach 1: Stack
class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for i in range(len(s)): 
            if s[i] == ']': 
                decode_list = []
                while st[-1] != '[': 
                    ch = st.pop() 
                    decode_list.append(ch) 
                decode_list = decode_list[::-1]
                decode_string = ''.join(decode_list)
                st.pop() 
                base = 1
                k = 0
                while st and st[-1].isdigit(): 
                    k = k + int(st.pop()) * base 
                    base *= 10 
                st.append(k * decode_string)
            else: 
                st.append(s[i])
        
        return ''.join(st)

    # Approach 2: Two Stacks
class Solution:
    def decodeString(self, s: str) -> str:
        string_st = [] 
        count_st = []
        curr_str = ""
        k = 0

        for ch in s: 
            if ch.isdigit(): 
                k = k * 10 + int(ch)
            elif ch == '[': 
                string_st.append(curr_str)
                count_st.append(k) 
                k = 0
                curr_str = ""
            elif ch == ']': 
                decoded_str = string_st.pop() 
                for _ in range(count_st.pop(), 0, -1): 
                    decoded_str += curr_str 
                curr_str = decoded_str 
            else: curr_str += ch

        return curr_str

# Approach 3: Recursive
class Solution:
    idx = 0
    def decodeString(self, s: str) -> str:
        res = ""
        while(self.idx < len(s) and s[self.idx] != ']'): 
            if not s[self.idx].isdigit(): 
                res += s[self.idx]
                self.idx += 1
            else: 
                k = 0
                while self.idx < len(s) and s[self.idx].isdigit(): 
                    k = k * 10 + int(s[self.idx]) 
                    self.idx += 1
                self.idx += 1
                decoded_str = self.decodeString(s) 
                self.idx += 1

                while k: 
                    res += decoded_str
                    k -= 1
        
        return res

