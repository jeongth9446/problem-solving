import collections
from typing import List, re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub('[^a-z0-9\s]', ' ', paragraph)
        list_paragraph = paragraph.split()

        cnt_list = collections.Counter(list_paragraph)

        cnt = 0
        while True:
            print(cnt_list.most_common()[cnt])
            if cnt_list.most_common()[cnt][0] not in banned:
                return cnt_list.most_common()[cnt][0]
            cnt = cnt + 1
