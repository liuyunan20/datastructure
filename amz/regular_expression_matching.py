class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:
        def find_sub_list(sl, wl):
            results = []
            sll = len(sl)
            wll = len(wl)
            for i in range(wll-sll+1):
                if match(wl[i:i+sll], sl):
                    results.append(i)
            return results

        def match(s, p):
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

                    if j + 1 < len(p) and p[j+1] == "*":
                        if match(s[i:], p[j+2:]):
                            return True
                        elif p[j] == '.':
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
                            inds = find_sub_list(p1, s[i:])
                            if not inds:
                                return False
                            else:
                                for ind in inds:
                                    if match(s[ind+i:], p[j:]):
                                        return True
                                return False
                        else:
                            i += 1
                    else:
                        i += 1
                        j += 1
                elif p[j] != '*':
                    if j + 1 < len(p) and p[j+1] == '*':
                        return match(s[i:], p[j+2:])
                    else:
                        return False

            return match(s[i:], p[j:])

        return match(string, pattern)
