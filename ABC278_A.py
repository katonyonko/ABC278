import io
import sys

_INPUT = """\
6
3 2
2 7 8
3 4
9 9 9
9 5
1 2 3 4 5 6 7 8 9
1 1
1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  A=list(map(int,input().split()))
  for i in range(K):
    A=A[1:]+[0]
  print(*A)