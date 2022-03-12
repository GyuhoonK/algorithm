# Algorithm
BOJ, Programmers \
Language : Python


## Tip

### 2차원 배열 90도 회전(뒤집기)
```python
list(zip(*arr[::-1]))
```

### 재귀함수 사용 시
```python
import sys
sys.setrecursionlimit(10**6)
```

### nCr
```python
from operator import mul
from functools import reduce

def nCr(n, r):
    r = min(r, n-r)
    numer = reduce(mul, range(n, n-r, -1), 1)
    denomi = reduce(mul, range(1, r+1), 1)
    return numer // denomi

```