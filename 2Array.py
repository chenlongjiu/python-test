# Enter your code here. Read input from STDIN. Print output to STDOUT
def check():
    t = input()
    rel = []
    #record the total test case number: 
    for i in range(t):
        # start loop run i t times: 
        line1 = raw_input()
        line2 = raw_input()
        line3 = raw_input()
        l1 = line1.split()
        l2 = line2.split()
        l3 = line3.split()
        f1 = map(int, l1)
        f2 = sorted(map(int, l2))
        f3 = sorted(map(int, l3))
        print f1, f2, f3
        if len(f2) != len(f3) or len(f2) != f1[0]:
            rel.append("No")
        else:
            for i in range(f1[0]):
                if (f2[i] + f3[-i-1]) < f1[1]:
                    rel.append("No")
                    break
            else: 
                rel.append("Yes")
    return rel
print check()
