from functools import reduce


def create_report(data_file_name: str, report_file_name: str) -> None:
    counter = {}
    with open(f"{data_file_name}", "r") as data:
        for line in data.readlines():
            key, value = line.strip().split(",")
            counter.setdefault(key, 0)
            counter[key] += int(value)
    counter_list = sorted([(key, value) for key, value in counter.items()],
                          key=lambda x: len(x[0]),
                          reverse=True)
    with open(f"{report_file_name}", "w") as report:
        for key, value in counter_list:
            line = f"{key},{value}\n" # noqa
            report.write(line)

        report.write(f"result,{abs(reduce(lambda x, y: x - y, counter.values()))}\n") # noqa
