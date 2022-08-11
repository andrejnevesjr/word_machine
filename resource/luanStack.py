class Solution:
    def solve(self, ops):
        l = []
        for i in ops:
            if i == 'DUP' and len(l) > 0:
                x = l[len(l)-1]
                l.append(x)
            
            elif i == 'POP' and len(l) > 0:
                l.pop()
                
            elif i == '-' and len(l) > 1:
                n = (l[len(l)-1])
                l.pop()
                lst = (l[len(l)-1])
                l.pop()
                x = (int(n) - int(lst))
                l.append(x)
                
            elif i == '+' and len(l) > 1:
                n = (l[len(l)-1])
                l.pop()
                lst = (l[len(l)-1])
                l.pop()
                x = (int(n) + int(lst))
                l.append(x)
                

            else:
                try:
                    l.append(int(i))
                except ValueError:
                    return -1
                    #l.append(-1)
        return l[-1]
