import io
import sys

_INPUT = """\
6
3 4 5 2 2
2 2 1 1
3 2 5 3
3 4 4 3
5 6 9 3 4
7 1 5 3 9 5
4 5 4 5 1 2
6 1 6 2 9 7
4 7 1 5 8 8
3 4 3 3 5 3
9 12 30 4 7
2 2 2 2 2 2 2 2 2 2 2 2
2 2 20 20 2 2 5 9 10 9 9 23
2 29 29 29 29 29 28 28 26 26 26 15
2 29 29 29 29 29 25 25 26 26 26 15
2 29 29 29 29 29 25 25 8 25 15 15
2 18 18 18 18 1 27 27 25 25 16 16
2 19 22 1 1 1 7 3 7 7 7 7
2 19 22 22 6 6 21 21 21 7 7 7
2 19 22 22 22 22 21 21 21 24 24 24
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  H,W,N,h,w=map(int,input().split())
  A=[list(map(lambda x: int(x)-1,input().split())) for _ in range(H)]
  res=[0]*N
  for i in range(H):
    for j in range(W):
      res[A[i][j]]+=1
  ans=[[0]*(W-w+1) for _ in range(H-h+1)]
  for i in range(H-h+1):
    for j in range(W-w+1):
      if j==0:
        if i==0:
          tmp=sum([1 if res[k]>0 else 0 for k in range(N)])
          for k in range(h):
            for l in range(w):
              res[A[k][l]]-=1
              if res[A[k][l]]==0: tmp-=1
        else:
          res=res2.copy()
          tmp=tmp2
          for l in range(w):
            if res[A[i-1][l]]==0: tmp+=1
            res[A[i-1][l]]+=1
            res[A[i+h-1][l]]-=1
            if res[A[i+h-1][l]]==0: tmp-=1
        res2=res.copy()
        tmp2=tmp
      else:
        for k in range(h):
          if res[A[i+k][j-1]]==0: tmp+=1
          res[A[i+k][j-1]]+=1
          res[A[i+k][j-1+w]]-=1
          if res[A[i+k][j-1+w]]==0: tmp-=1
      ans[i][j]=tmp
  for i in range(H-h+1): print(*ans[i])