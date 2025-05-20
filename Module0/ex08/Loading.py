
import shutil


def ft_tqdm(lst):
    total = len(lst)
    columns, rows = shutil.get_terminal_size()
    print(columns)
    bar_length = columns - 41
    for i, item in enumerate(lst):
        progress = (i + 1) / total
        block = int(round(bar_length * progress))
        progress_info = (
            f"{progress * 100:3.0f}%|["
            f"{'=' * block}"
            f"{'>' if block < bar_length else ''}"
            f"{'.' * (bar_length - block)}] {i + 1}/{total}"
        )

        print(f"\r{progress_info:<{bar_length + 41}}", end="", flush=True)

        yield item

    print(f"\r{100}%|[{'=' * bar_length}] {total}/{total}", end="", flush=True)


if __name__ == "__main__":
    ft_tqdm(range(333))
