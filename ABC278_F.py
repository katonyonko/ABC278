import io
import sys

_INPUT = """\
6
6
enum
float
if
modint
takahashi
template
10
catch
chokudai
class
continue
copy
exec
havoc
intrinsic
static
yucatec
16
mnofcmzsdx
lgeowlxuqm
ouimgdjxlo
jhwttcycwl
jbcuioqbsj
mdjfikdwix
jhvdpuxfil
peekycgxco
sbvxszools
xuuqebcrzp
jsciwvdqzl
obblxzjhco
ptobhnpfpo
muizaqtpgx
jtgjnbtzcl
sivwidaszs
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  S=[input() for _ in range(N)]
  G=[[] for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if i==j: continue
      if S[j][-1]==S[i][0]:
        G[i].append(j)
  dp=[1]*(N*2**N)
  for i in reversed(range(2**N)):
    for j in range(N):
      if (i>>j)&1!=1: continue
      if dp[i*N+j]==1:
        for v in G[j]:
          if (i>>v)&1==1:
            dp[(i-(1<<j))*N+v]=0
  if max([dp[(1<<i)*N+i] for i in range(N)])==1: print('First')
  else: print('Second')