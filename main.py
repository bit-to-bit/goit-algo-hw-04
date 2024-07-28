"""Test sorting algoritms"""

import timeit
from data_loader import get_google_play_data, get_uber_data, get_random_data
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from utils import print_dataset_info

print("Stage 1 - # Формуємо масиви даних")
data_google_play = get_google_play_data()
data_uber = get_uber_data()
data_random = get_random_data(100000)

print("Stage 2 - # Сортування вставками")
# Сортування вставками
time_insertion_sort_google_play = timeit.timeit(
    lambda: insertion_sort(data_google_play.copy()), number=1
)
time_insertion_sort_uber = timeit.timeit(
    lambda: insertion_sort(data_uber.copy()), number=1
)
time_insertion_sort_random = timeit.timeit(
    lambda: insertion_sort(data_random.copy()), number=1
)

print("Stage 3 - # Сортування злиттям")
time_merge_sort_google_play = timeit.timeit(
    lambda: merge_sort(data_google_play.copy()), number=1
)
time_merge_sort_uber = timeit.timeit(lambda: merge_sort(data_uber.copy()), number=1)
time_merge_sort_random = timeit.timeit(lambda: merge_sort(data_random.copy()), number=1)

print("Stage 4 - # Сортування Timsort")
time_timsort_sort_google_play = timeit.timeit(
    lambda: sorted(data_google_play.copy()), number=1
)
time_timsort_sort_uber = timeit.timeit(lambda: sorted(data_uber.copy()), number=1)
time_timsort_sort_random = timeit.timeit(lambda: sorted(data_random.copy()), number=1)

print("Stage 5 - # Оцінка алгоритмів")

print_dataset_info(
    "data_google_play",
    data_google_play,
    time_merge_sort_google_play,
    time_insertion_sort_google_play,
    time_timsort_sort_google_play,
)

print_dataset_info(
    "data_uber",
    data_uber,
    time_merge_sort_uber,
    time_insertion_sort_uber,
    time_timsort_sort_uber,
)

print_dataset_info(
    "data_random",
    data_random,
    time_merge_sort_random,
    time_insertion_sort_random,
    time_timsort_sort_random,
)
