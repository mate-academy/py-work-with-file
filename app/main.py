def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file_data:
        # text_read = file_data.readlines()
        text_read = file_data.read()
        text = text_read.split()
        for line in text:
            line_splitted = line.split(",")
            match line_splitted[0]:
                case "supply":
                    supply += int(line_splitted[1])
                case "buy":
                    buy += int(line_splitted[1])

    with open(report_file_name, "w") as file_to_write:
        file_to_write.write(f"supply,{supply}\n")
        file_to_write.write(f"buy,{buy}\n")
        file_to_write.write(f"result,{supply - buy}\n")


create_report("file.txt", "report_file_name")
