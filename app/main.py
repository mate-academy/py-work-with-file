def create_report(data_file_name: str, report_file_name: str) -> None:
    objects = {}
    with (
        open(data_file_name, "r") as file_in,
        open(report_file_name, "w") as file_out
    ):
        for line in file_in:
            line = line.strip()
            if not line:  # skip all empty lines or empty elements
                continue

            object_name, object_value = line.strip().split(",")

            object_value = object_value.strip()
            if not object_value:
                continue
            object_value = int(object_value)

            if object_name not in objects:
                objects[object_name] = 0
            objects[object_name] += object_value
        objects["result"] = objects.get("supply", 0) - objects.get("buy", 0)
        file_out.write(f"supply,{objects.get('supply', 0)}\n")
        file_out.write(f"buy,{objects.get('buy', 0)}\n")
        file_out.write(f"result,{objects.get('result', 0)}\n")
