class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        for item in sorted(set(s)):  # 중복 제외 후 정렬
            suffix = s[s.index(item):]

            if set(s) == set(suffix):  # 앞부분을 모두 버려도 된다면
                return item + self.removeDuplicateLetters(suffix.replace(item, ""))

        return ""