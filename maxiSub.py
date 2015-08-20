def sol():
    f = open('testData.txt', 'r')
    test = int(f.readline())
    for i in range(test):
        amount = f.readline()
        ele = map(int, f.readline().split())
        maxi = None
        nmaxi = None
        cur_val = None
        if len(ele) <= 0:
            print 0,0
        for j in range(len(ele)):
            if cur_val is None:
                cur_val = ele[j]
                maxi = cur_val
            else:
                if ele[j] >= 0:
                    if cur_val >= 0:
                        cur_val += ele[j]
                    else: 
                        #cur_val < 0
                        cur_val = ele[j]
                    maxi = max(cur_val, maxi)
                else: 
                # now ele[j]  < 0
                    if cur_val >= 0:
                        if cur_val + ele[j] > 0:
                            cur_val += ele[j]
                        else:
                            cur_val = 0
                    else:
                        #cur_val < 0
                        if cur_val < ele[j]:
                            cur_val = ele[j]
                        elif cur_val >= ele[j]:
                            pass
                        maxi = max(maxi, cur_val)

        for j in range(len(ele)):
            if nmaxi is None:
                nmaxi = ele[j]
                #print "None: nmaxi is ",nmaxi
            else:
                if ele[j] >= 0:
                    if nmaxi > 0:
                        nmaxi += ele[j]
                    else:
                        nmaxi = ele[j]
                    #print "ele > 0:nmaxi is ",nmaxi
                else:
                    nmaxi = max(ele[j],nmaxi)
                    #print "ele <0: nmaxi is ",nmaxi
        
        print maxi,nmaxi
        




sol()