def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    dict_of_operation = {}
    with open(data_file_name, "r") as file:
        for line in file:
            if "," not in line:
                continue
            operation = line.strip().split(",")[0]
            number = int(line.strip().split(",")[1])
            if operation not in dict_of_operation:
                dict_of_operation[operation] = number
            else:
                dict_of_operation[operation] += number
        file.close()

    with open(report_file_name, "w") as file:
        file.write(f"supply,{dict_of_operation.get("supply")}\n")
        file.write(f"buy,{dict_of_operation.get("buy")}\n")
        file.write(
            f"result,{dict_of_operation.get(
                "supply") - dict_of_operation.get("buy")}\n"
        )
        file.close()


if __name__ == "__main__":
    create_report("bananas.csv", "test.csv")
