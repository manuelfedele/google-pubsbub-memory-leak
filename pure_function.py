from memory_profiler import profile


@profile
def callback():
    # Memory intensive operation
    x = [n for n in range(int(1e5))]


if __name__ == '__main__':
    callback()
    callback()
    callback()
    callback()
