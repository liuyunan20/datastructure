class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        i, n = 0, len(words)
        while i < n:
            lines.append([])
            width = 0
            if i == 0:
                lines[-1].append(words[i])
                width += len(words[i])
                i += 1
            while i < n and width + len(words[i]) + len(lines[-1])<= maxWidth:
                lines[-1].append(words[i])
                width += len(words[i])
                i += 1
            lines[-1] = (lines[-1], maxWidth - width)
            width = 0
            if i == n - 1:
                lines.append([])
                lines[-1].append(words[i])
                width += len(words[i])
                i += 1
                lines[-1] = (lines[-1], maxWidth - width)
        i, n = 0, len(lines)
        while i < n - 1:
            line, spaces = lines[i]
            m = len(line)
            if m == 1:
                lines[i] = line[0] + " " * spaces
            else:
                if spaces % (m - 1) == 0:
                    space = " " * (spaces // (m - 1))
                    print(space)
                    lines[i] = space.join(line)
                else:
                    left = " " * ((spaces -  spaces % (m - 1)) // (m - 2))
                    last = " " * (spaces % (m - 1))
                    lines[i] = ""
                    for j in range(m - 1):
                        if j == m - 2:
                            lines[i] += line[j] + last
                        else:
                            lines[i] += line[j] + left
                    lines[i] += line[m - 1]
            i += 1
        lines[n - 1] = " ".join(lines[n - 1][0])
        lines[n - 1] += " " * (maxWidth - len(lines[n - 1]))
        return lines

