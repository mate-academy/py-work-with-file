def create_report(data_file_name: str, report_file_name: str) -> None:
    input_file = open(data_file_name)

    dictionary = {}
    for line in input_file:
        line = line.strip()
        if not line:
            continue

        key, value = line.split(",")
        value = int(value)

        dictionary[key] = dictionary.get(key, 0) + int(value)
    input_file.close()

    with open(report_file_name, "w", newline="") as report:
        for key, value in dictionary.items():
            report.write(f"{key},{value}\n")

    report.close()
