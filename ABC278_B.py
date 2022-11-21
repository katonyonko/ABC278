import io
import sys

_INPUT = """\
6
1 23
19 57
20 40
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  H,M=map(int,input().split())
  A,B,C,D=H//10,H%10,M//10,M%10
  def Judge(A,B,C,D):
    if 0<=A*10+C<24 and 0<=B*10+D<60: return True
    else: return False
  while Judge(A,B,C,D)==False:
    D=(D+1)%10
    if D==0:
      C=(C+1)%6
      if C==0:
        A,B=(A*10+B+1)%24//10,(A*10+B+1)%24%10
  print(A*10+B,C*10+D)