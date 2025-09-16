import sys
sys.stdin = open('dijkstra_input.txt', 'r')

from heapq import heappop, heappush
INF = int(21e8) #무한대를 가정 (문제의 최대)