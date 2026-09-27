class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = number.replace(" ", "").replace("-", "")
        result = []

        while len(digits) > 4:
            result.append(digits[:3])
            digits = digits[3:]

        if len(digits) == 4:
            result.append(digits[:2])
            result.append(digits[2:])
        else:
            result.append(digits)

        return "-".join(result)
