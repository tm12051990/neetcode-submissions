class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0

        for i in details:
            detail = i[11:13]
            detail_int = int(detail)
            if detail_int > 60:
                count += 1
        return count