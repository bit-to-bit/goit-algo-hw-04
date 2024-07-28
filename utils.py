"""Utils module"""

DELIMITER = "-" * 80


def print_dataset_info(
    dataset_name, dataset, time_merge_sort, time_insertion_sort, time_timsort_sort
):
    print(f"\nНабір дадних {dataset_name}:")
    print(DELIMITER)
    print(f"Кількість елементів: {len(dataset)}")
    print(f"Кількість унікальних елементів: {len(set(dataset))}")
    print(
        f"Співвідношення унікальних до усіх: {round(len(set(dataset)) / len(dataset)*100,2)}%\n"
    )
    print(f"Час на сортування вставками: {time_insertion_sort}")
    print(f"Час на сортування злиттям: {time_merge_sort}")
    print(f"Час на сортування timsort: {time_timsort_sort}")

    print(
        f"\nСпіввідношення: вставками \ злиттям \ timesort = {round(time_insertion_sort / time_timsort_sort)} \ {round(time_merge_sort / time_timsort_sort)} \ {1}"
    )

    print(DELIMITER + "\n")
