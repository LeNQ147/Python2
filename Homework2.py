import time
import random

print("Готовий? У тебе є 3 секунди, щоб натиснути Enter, як тільки з'явиться повідомлення!")

pause = random.uniform(2, 5)
time.sleep(pause)

print("Натискай Enter!")

start = time.time()

input()

end = time.time()

print("Твоя реакція:", end - start)
