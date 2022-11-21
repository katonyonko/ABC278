import io
import sys

_INPUT = """\
6
5
3 1 4 1 5
6
3 2
2 3 4
3 3
1 1
2 3 4
3 3
1
1000000000
8
2 1 1000000000
2 1 1000000000
2 1 1000000000
2 1 1000000000
2 1 1000000000
2 1 1000000000
2 1 1000000000
3 1
10
1 8 4 15 7 5 7 5 8 0
20
2 7 0
3 7
3 8
1 7
3 3
2 4 4
2 4 9
2 10 5
1 10
2 4 2
1 10
2 3 1
2 8 11
2 3 14
2 1 9
3 8
3 8
3 1
2 6 5
3 7
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import defaultdict
  N=int(input())
  A=list(map(int,input().split()))
  A={i:A[i] for i in range(N)}
  b=0
  Q=int(input())
  for i in range(Q):
    query=input().split()
    if query[0]=='1':
      b=int(query[1])
      A=defaultdict(int)
    elif query[0]=='2':
      iq,xq=map(int,query[1:])
      A[iq-1]+=xq
    else:
      iq=int(query[1])-1
      if iq in A: print(b+A[iq])
      else: print(b)