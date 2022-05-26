from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        # 문자 / 숫자를 구분하여 모은다.
        # 모든 로그는 Letter-log 이거나 Digit-logs 이기 때문에 identifier를 제외한 첫 번 째 값만 확인하면 된다.
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits
