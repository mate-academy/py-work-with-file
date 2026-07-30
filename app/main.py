from os.path import exists


def create_report(data_file_name: str, report_file_name: str) -> None:
    if not exists(data_file_name):
        raise FileNotFoundError

    data = {
        "supply": 0,
        "buy": 0,
    }
    with open(data_file_name, "r") as source:
        for line in source:
            if line is not None:
                key = line.split(",")[0]
                value = int(line.split(",")[1].replace("\n", ""))
                data[key] += value

    if not data:
        print(f"File {data_file_name} has no data.")
        return

    with open(report_file_name, "w") as target:
        target.write(f"supply,{data.get('supply')}\n")
        target.write(f"buy,{data.get('buy')}\n")
        target.write(f"result,{data.get('supply') - data.get('buy')}\n")

    return
