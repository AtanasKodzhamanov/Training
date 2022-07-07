def fibDP(n, cache):
  if n in cache.keys():
    return cache[n]
 
  if n < 2:
    cache[n] = n
    return cache[n]
 
  cache[n] = fibDP(n-1,cache) + fibDP(n-2,cache)
  return cache[n]

cache={}
print(fibDP(100,cache))