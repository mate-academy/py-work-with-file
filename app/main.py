import re


def to_int(value: str) -> int:
    match = re.search(r"-?\d+", value.strip())
    return int(match.group()) if match else 0


def create_report(data_file_name: str, report_file_name: str) -> None:

    source, destination = data_file_name, report_file_name

    with (open(source, "r") as file_in, open(destination, "w") as file_out):
        supply = 0
        buy = 0
        for line in file_in:

            line = line.replace("\n", "")
            line_list = line.split(",")
            if "buy" in line:
                buy += to_int(line_list[1])
            if "supply" in line:
                supply += to_int(line_list[1])

        result = supply - buy

        file_out.write(f"supply,{supply}\n")
        file_out.write(f"buy,{buy}\n")
        file_out.write(f"result,{result}\n")
