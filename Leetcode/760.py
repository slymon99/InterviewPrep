class Solution(object):
    def anagramMappings(self, a, b):
        b_mapped = [(idx, val) for idx, val in enumerate(b)]
        b_mapped.sort(key = lambda x: x[1])
        print(b_mapped)
        res = [self.b_search(item, b_mapped) for item in a]
        return res

    def b_search(self, num, l):
        lower = 0
        upper = len(l) - 1
        while lower <= upper:
            mid_idx = (upper + lower) // 2
            mid_val = l[mid_idx][1]
            if mid_val == num:
                return l[mid_idx][0]
            elif num < mid_val:
                upper = mid_idx - 1
            else:
                lower = mid_idx + 1