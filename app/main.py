from functools import reduce


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(f"../{data_file_name}", "r") as file:
        dict_counter = {}

        for string in file.readlines():
            key, value = string.split(",")
            dict_counter.setdefault(key, 0)
            dict_counter[key] += int(value.strip())

    with open(report_file_name, "a") as file:
        result_value = abs(reduce(lambda x, y: y - x, dict_counter.values()))
        result_list = [(key, value) for key, value in dict_counter.items()]
        for key, value in sorted(result_list, reverse=True):
            print(f"{key},{value}", file=file)
        print(f"result,{result_value}", file=file)
