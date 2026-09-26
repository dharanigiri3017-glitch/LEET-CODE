class Solution:
    def slowestKey(self, releaseTimes, keysPressed):
        max_time = releaseTimes[0]
        result = keysPressed[0]

        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i - 1]

            if duration > max_time or (duration == max_time and keysPressed[i] > result):
                max_time = duration
                result = keysPressed[i]

        return result
