class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {
            'b':0,
            'a':0,
            'l':0,
            'o':0,
            'n':0
        }
        for el in text:
            if el in 'balloon':
                freq[el] += 1
            else:
                continue

        count = min(freq['b'], freq['a'], freq['l']//2, freq['o']//2, freq['n'])
        return count


  # Thapa's Solution
        # b = a = l = o = n = 0
        # for el in text:
        #     if el == 'b':
        #         b+=1
        #     elif el == 'a':
        #         a +=1
        #     elif el == 'l':
        #         l += 1
        #     elif el == 'o':
        #         o += 1
        #     elif el == 'n':
        #         n+= 1
        #     else:
        #         continue
            
        # min_first = min(b,a,n)
        # min_second = min(l,o)
        # return min(min_first, int(min_second/2))



        