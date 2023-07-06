from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm
import sys

sys.tracebacklimit = 0

for elem in ft_tqdm(range(333)):
	sleep(0.005)
print()
for elem in tqdm(range(333)):
	sleep(0.005)
print()