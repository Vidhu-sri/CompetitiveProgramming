
import heapq
import sys

def make_adjlist(n, edges):
    adjlist = [[] for _ in range(n + 1)]
    for s, d, c in edges:
        adjlist[s].append((d, c))
    return adjlist


def djikstra(n,adjlist):

    dist = {i:float('inf') for i in range(1,n+1)}
    dist[1] = 0
    
    frontier = [(0,1)]
    

    while frontier:

        curr_dist, current = heapq.heappop(frontier)

        if curr_dist > dist[current]:
            continue

        

        for neighbor,d in adjlist[current]:
            alt_dist = dist[current]+d
            if  alt_dist< dist[neighbor]:
                dist[neighbor] = alt_dist
                heapq.heappush(frontier,(alt_dist, neighbor))
    return dist





def main():

    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    edges = [tuple(map(int, data[i:i+3])) for i in range(2, len(data), 3)]

    adjlist = make_adjlist(n,edges)
    
    dist = djikstra(n,adjlist)

    print(*dist.values())
    



if __name__ == "__main__":
    main()








