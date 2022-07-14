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
            if not p and not s:
                return True
            elif not p:
                return False
            elif not s:
                while j + 1 < len(p) and p[j+1] == "*":
                    j += 2
                if j == len(p):
                    return True
                else:
                    return False

            while i < len(s):
                if j == len(p):
                    return False

                if p[j] == s[i] or p[j] == '.':
                    pre = p[j]
                    if j + 1 < len(p) and p[j+1] == "*":
                        if match(s[i:], p[j+2:], pre):
                            return True
                        elif pre == '.':
                            while j + 1 < len(p) and p[j+1] == '*':
                                j += 2
                            if j == len(p):
                                return True
                            if j + 1 < len(p) and '*' in p[j:]:
                                p2 = p[j:]
                                x = p2.index('*') - 1
                                p1 = p2[:x]
                            else:
                                p1 = p[j:]
                            inds = find_sub_list(p1,s[i:])
                            if not inds:
                                return False
                            else:
                                for ind in inds:
                                    if match(s[ind+i:], p[j:], pre):
                                        return True
                                return False
                        else:
                            i += 1
                    else:
                        i += 1
                        j += 1
                elif p[j] != '*':
                    pre = p[j]
                    if j + 1 < len(p) and p[j+1] == '*':
                        return match(s[i:], p[j+2:], pre)
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
                                    if match(s[ind+i:], p[j+1:], pre):
                                        return True
                                return False
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

            if match(s[i:], p[j:], pre):
                return True
            return False
        return match(s, p, '')
