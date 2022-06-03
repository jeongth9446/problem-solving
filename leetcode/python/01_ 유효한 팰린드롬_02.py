# 데크 자료형을 이용한 최적화
import collections
from typing import Deque

def isPalindrome(self, s: str) -> bool:
    # 자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

# deque의 popleft는 O(1) 이기 때문에,리스트에서의 pop(0) 보다 빠르다.
