import shutil
import time
from time import sleep
from collections.abc import Sized

def ft_tqdm(lst: range) -> None:
    
    total = len(lst)
    start_time = time.time()
    last_update = 0
    terminal_width, _ = shutil.get_terminal_size(fallback=(80, 24))
    progress_width = terminal_width - 41

    for i, item in enumerate(lst):
        yield item
        current_time = time.time()

        if current_time - start_time > 0.1 or i == total - 1:
            elapsed_time = current_time - start_time
            progress = i + 1
            progress_percent = progress / total * 100
            progress_bar_width = int(progress / total * progress_width)
            progress_bar = "█" * progress_bar_width
            iterations_per_sec = progress / elapsed_time
            remaining_time = (total - progress) / iterations_per_sec
            remaining_time_str = time.strftime("%H:%M", time.gmtime(remaining_time))

            # Print the progress bar and information
            print(f"\r{progress_percent:.0f}% |{progress_bar}| {progress}/{total} [{remaining_time_str}<{elapsed_time:.2f}s, {progress / elapsed_time:.2f}it/s]", end="")
            
            last_update = i
            start_time = current_time

    print()  # Print a newline at the end