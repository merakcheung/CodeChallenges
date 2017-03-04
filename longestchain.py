

# Complete the function below.



def getUpperBoundMap(keys):
    uB = 0
    uBtmp = 0
    #initialize upper bound map
    uboundmap = {}
    fragments = []
    fragments_ub = []
    frag_begin = 0
    for i in keys:
        uboundmap[i] = 0
    # end initialization
    for i in range(len(keys)):
        if i == 0:
            uBtmp = 1
            frag_begin = i
        else:
            if keys[i] == keys[i-1]+1:
                uBtmp +=1
            else:
                fragments.append((frag_begin,i-1))
                fragments_ub.append(uBtmp)
                frag_begin = i
                uBtmp = 1
        if i == len(keys) - 1:
            fragments.append((frag_begin, i))
            fragments_ub.append(uBtmp)
        uboundmap[keys[i]] = uBtmp
        uB = max(uB, uBtmp)
    return uB,uboundmap, fragments, fragments_ub


def getLengthMap(words):
    mymap = {}
    for i,w in enumerate(words):
        l = len(w)
        if l in mymap.keys():
            mymap[l].append(i)
        else:
            mymap[l] = [i]
    return mymap


def longestChain(words):
    numWords = len(words)
    if numWords == 0:
        return 0
    myLengthMap = getLengthMap(words)
    lenKeys = myLengthMap.keys()
    lenKeys.sort()
    upperBound,upperBoundMap,frags,frags_ub = getUpperBoundMap(lenKeys)
    sortedfrags = [y for (x,y) in sorted(zip(frags_ub,frags))]
    sortedfrags.reverse()
    frags_ub.sort()
    frags_ub.reverse()
    #print sortedfrags, frags_ub
    searchOrder = []


    resultMap = [1]*numWords
    #initialize resultMap
    #for i in range(numWords):
    #    resultMap[i] = 1
    #  index -> max len up to its length

    for f,ub in zip(sortedfrags,frags_ub):
        ct = 0
        ub_0 = ub
        for thisLenInd in range(f[0],f[1]+1):
            ct += 1
            foundNext = False
            #print 'thisLenInd', thisLenInd
            thisLen = lenKeys[thisLenInd]
            #print ' ---  thisLen', thisLen
            words2MatchIndSet = []
            nextLen = thisLen + 1
            if nextLen in lenKeys:
                words2MatchIndSet = myLengthMap[nextLen]
            for thisWordInd in myLengthMap[thisLen]:
                for nextWordInd in words2MatchIndSet:
                    if resultMap[nextWordInd] == min(upperBoundMap[nextLen],ub_0):
                        continue
                    ret = False ## ret: whether thisWord matches nextWord
                    ind = 0 # find ind: the first char that is different
                    while ind < thisLen:
                        if words[thisWordInd][ind] != words[nextWordInd][ind]:
                            break
                        ind += 1
                    ret = (words[thisWordInd][ind:] == words[nextWordInd][ind+1:])
                    if ret == True:
                        foundNext = True
                        resultMap[nextWordInd] = resultMap[thisWordInd]+ret
                    #resultMap[nextWordInd] = max(resultMap[thisWordInd]+ret if ret else 1, resultMap[nextWordInd])
                    if resultMap[nextWordInd] == ub_0:
                        #print 'resultMap', nextWordInd,' ', words[nextWordInd]
                        return ub_0
            if not foundNext:
                ub_0 = ub-ct

    #print resultMap
    return max(resultMap)


if __name__ == '__main__':
    words = ['a','ab', 'abcd','b','d','bd','abdc','abd','']
    words = ['axxx','bxxx','abbxxx','abxxx','a','b','ab','abc']
    #words = ['a','aa','b', 'bb','aabb']
    print longestChain(words)













