import time
import random


_ = input(f"Press enter to start. When you see \"GO{chr(33)}\" hit enter")

reactionTimes = []

totalPlays = 0
maxPlays = 5

while totalPlays < maxPlays:
    time.sleep(random.uniform(2, 5))
    start = time.monotonic()
    _ = input(f"GO{chr(33)}")
    reactionTime = round((time.monotonic() - start) * 1000, 1)
    if reactionTime > 0:
        print(str(reactionTime) + " ms")
        print()
        reactionTimes.append(reactionTime)
        totalPlays += 1
    else:
        print("Try again, reaction time invalid, hit enter after you see GO")

averageReactionTime = 0
fastestReactionTime = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
for reactionTime in reactionTimes:
    averageReactionTime += reactionTime
    if reactionTime < fastestReactionTime:
        fastestReactionTime = reactionTime
averageReactionTime /= maxPlays

print(f"Finished - {round(averageReactionTime, 1)} ms average reaction time and {fastestReactionTime} ms fastest reaction time")