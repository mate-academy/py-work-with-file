def create_report(input_file: str, output_file: str) -> None:
    supply = 0
    buy = 0

    file_a = open(input_file, "r")
    for line in file_a:
        line = line.strip()

        if not line:
            continue

        parts = line.split(",")
        if len(parts) == 2:
            op_time = parts[0].strip()
            amount = int(parts[1].strip())

            if op_time == "supply":
                supply += amount
            elif op_time == "buy":
                buy += amount

    file_a.close()

    result = supply - buy

    file_a = open(output_file, "w")
    file_a.write(f"supply,{supply}\n")
    file_a.write(f"buy,{buy}\n")
    file_a.write(f"result,{result}\n")
    file_a.close()
