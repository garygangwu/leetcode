import collections
import heapq

def findCheapestPrice(n, flights, src, dst, K):
  graph = collections.defaultdict(dict)
  for s, d, c in flights:
    graph[s][d] = c

  best = {}
  for node in range(n):
    if node != src:
      best[node] = float('inf')
    else:
      best[node] = 0
  pq = [(0, 0, src)]

  while len(pq) > 0:
    cost, k, node = heapq.heappop(pq)
    if k > K + 1:
      break
    for neighbor, weight in graph[node].iteritems():
      newcost = cost + weight
      if newcost < best[neighbor] and k+1 <= K+1:
        heapq.heappush(pq, (newcost, k+1, neighbor))
        best[neighbor] = newcost
  return best[dst]


n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
K = 1

print findCheapestPrice(n, flights, src, dst, K)

