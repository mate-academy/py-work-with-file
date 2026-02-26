def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r", encoding="utf-8") as data_file:
        data = data_file.read().split("\n")
        counter = {}
        for line in data:
            if not line.strip():
                continue
            name, value = line.split(",")
            counter[name] = counter.get(name, 0) + int(value)
        counter["result"] = counter["supply"] - counter["buy"]
    with open(report_file_name, "w+", encoding="utf-8") as report_file:
        for item in ["supply", "buy", "result"]:
            report_file.write(f'{item}{","}{counter[item]}\n')


if __name__ == "__main__":
    files = ["apples.csv", "bananas.csv", "grapes.csv", "oranges.csv"]

    for file_name in files:
        data_file_path = f"../{file_name}"
        report_file_path = f"../{file_name[:-4]}_report.csv"
        create_report(data_file_path, report_file_path)
