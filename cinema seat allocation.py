class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        # Store reserved seats for each affected row
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        # All unaffected rows can have 2 groups
        ans = (n - len(rows)) * 2

        for seats in rows.values():
            left = {2, 3, 4, 5}
            middle = {4, 5, 6, 7}
            right = {6, 7, 8, 9}

            left_free = seats.isdisjoint(left)
            middle_free = seats.isdisjoint(middle)
            right_free = seats.isdisjoint(right)

            if left_free and right_free:
                # Both non-overlapping blocks can be used
                ans += 2
            elif left_free or middle_free or right_free:
                # At least one block can be used
                ans += 1

        return ans
