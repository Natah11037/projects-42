def f(a):
    def g(b):
        def h(c):
            def i(d):
                x = [a, b, c, d]
                y = []
                for k in x:
                    y.append("".join(chr(n) for n in k))
                print(" ".join(y))
            return i
        return h
    return g

f([84,117])([118,97,115])([114,233,117,115,115,105,114])([108,39,101,120,97,109,32,33,33])
