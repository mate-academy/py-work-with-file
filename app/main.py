# write your code here

def create_report(data_file_name: str, create_file_name: str) -> None:

    supply = 0
    buy = 0
    try:
        with open(data_file_name, "r") as file:

            for line in file.readlines():
                line = line.strip().split(",")
                if line[0] == "supply":
                    supply += int(line[1])
                elif line[0] == "buy":
                    buy += int(line[1])

        with open(create_file_name, "a") as file:
            file.write(f"supply,{supply}\n")
            file.write(f"buy,{buy}\n")
            file.write(f"result,{supply - buy}\n")
    except FileNotFoundError:
        print(f"File {data_file_name} not found.")


if __name__ == "__main__":
    create_report("apples.csv", "report.csv")
