def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {}

    with open(data_file_name, "r") as file_in, \
         open(report_file_name, "w") as file_out:
        for line in file_in.readlines():
            operation, amount = line.split(",")

            if data.get(operation):
                data[operation] += int(amount)
            else:
                data[operation] = int(amount)

        out_content = [f"{key},{value}" for key, value in data.items()]

        file_out.write("\n".join(out_content))
