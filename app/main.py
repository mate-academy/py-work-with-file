def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as input_file,
          open(report_file_name, "w") as output_file):
        final_data = {}
        lines = input_file.readlines()

        for line in lines:
            if line:
                name, value = line.split(",")

                if name in final_data:
                    final_data[name] += int(value)
                else:
                    final_data[name] = int(value)

        final_data["result"] = final_data["supply"] - final_data["buy"]

        output_file.write(
            "\n".join(
                [",".join([key, value])
                 for key, value in final_data.items()
                 ]
            )
        )
