class Trie():
    def __init__(self): 
        self.val = 0 
        self.next = dict()
    def __repr__(self): 
        return f'{self.val} {self.next}' 
def makeTrie(words): 
    trie, r_trie = dict(), dict() 
    for word in words: 
        l = len(word) 
        trie[l], r_trie[l] = trie.get(l, dict()), r_trie.get(l, dict()) 
        trie[l][word[0]] = trie[l].get(word[0], Trie()) 
        r_trie[l][word[-1]] = r_trie[l].get(word[-1], Trie()) 
        cur, cur_r = trie[l][word[0]], r_trie[l][word[-1]]
        for c, c_r in zip(word[1:], word[::-1][1:]): 
            cur.val += 1 
            cur_r.val += 1 
            cur.next[c], cur_r.next[c_r] = cur.next.get(c, Trie()), cur_r.next.get(c_r, Trie()) 
            cur, cur_r = cur.next[c], cur_r.next[c_r] 
            cur.val += 1 
            cur_r.val += 1 
            return trie, r_trie 
def searchTrie(trie, r_trie, query): 
    l = len(query) 
    if query[0] != '?': 
        if trie.get(l) is None: return 0, None 
        return trie[l], False 
    elif query[-1] != '?': 
        if r_trie.get(l) is None: return 0, None 
        return r_trie[l], True 
    else: 
        if trie.get(l) is None: return 0, None 
        return sum(v.val for v in trie[l].values()), None 
def countWords(query, cur, isReverse): 
    if isReverse is None: return cur 
    if isReverse: query = query[::-1] 
    for q in query: 
        if q == '?': return sum(v.val for v in cur.values()) 
        if cur.get(q) is None: return 0 
        cur = cur[q].next 
    return 1 
def solution(words, queries): 
    trie, r_trie = makeTrie(words) 
    return [countWords(query, *searchTrie(trie, r_trie, query)) for query in queries]

#출처: https://dobuzi.tistory.com/6 [Dobuzi's coding]