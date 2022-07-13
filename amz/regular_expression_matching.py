class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def find_sub_list(sl,l):
            results = []
            sll = len(sl)
            ll = len(l)
            for i in range(ll-sll+1):
                if match(l[i:i+sll], sl, ''):
                    results.append(i)
            return results

        def match(s, p, pre):
            s = list(s)
            p = list(p)
            i = 0
            j = 0

            while i < len(s):
                if j == len(p) or i < 0:
                    return False
                if p[j] == s[i]:
                    pre = s[i]
                    j += 1
                    if j < len(p) and p[j] == "*" and match(s[i:], p[j+1:], pre):
                        return True
                    else:
                        i += 1
                elif p[j] == '.':
                    pre = '.'
                    j += 1
                    if j < len(p) and p[j] == "*":
                        return match(s[i:], p[j:], '.')
                    else:
                        i += 1
                elif p[j] != '*':
                    if j < len(p) - 1 and p[j+1] == '*':
                        j += 2
                    else:
                        return False
                else:
                    while pre != '.' and i < len(s) - (len(p) - j - 1) and s[i] == pre:
                        i += 1
                    if pre == '.':
                        while j + 2 < len(p) and p[j+2] == '*':
                            j += 2
                        if j + 1 < len(p) and '*' in p[j+1:]:
                            p2 = p[j+1:]
                            x = p2.index('*') - 1
                            p1 = p2[:x]
                            inds = find_sub_list(p1,s[i:])
                            if not inds:
                                return False
                            else:
                                for ind in inds:
                                    return match(s[ind+i:], p[j+1:], pre)
                        else:
                            i = len(s) - (len(p) - j - 1)
                            j += 1
                            continue
                    if i == len(s) and j == len(p) - 1:
                        return True
                    elif i == len(s) and j != len(p) - 1:
                        return False
                    else:
                        j += 1
            if j == len(p) or (j == len(p) - 1 and p[j] == '*') or (j == len(p) - 2 and p[j+1] == '*'):
                return True
            return False
        return match(s, p, '')
