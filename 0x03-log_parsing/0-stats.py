#!/usr/bin/python3
import sys
"""Parsing the log"""


def read_input_line():
    """Input line function"""
    try:
        return input().strip()
    except KeyboardInterrupt:
        sys.exit("\nProgram interrupted.")


def parse_line(line):
    """Parse line function"""
    try:
        parts = line.split()
        ip_address = parts[0]
        date = parts[2].strip('[]')
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_address, date, status_code, file_size
    except (IndexError, ValueError):
        return None


def print_statistics(total_file_size, status_code_counts):
    """Print stats function"""
    print(f"Total file size: File size: {total_file_size}")
    for status_code in sorted(status_code_counts.keys()):
        print(f"{status_code}: {status_code_counts[status_code]}")


def main():
    """Main function"""
    total_file_size = 0
    status_code_counts = {}

    try:
        while True:
            line = read_input_line()
            parsed_data = parse_line(line)

            if parsed_data:
                ip_address, date, status_code, file_size = parsed_data
                total_file_size += file_size

                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
                else:
                    if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                        status_code_counts[status_code] = 1

                if len(status_code_counts) == 8:
                    print_statistics(total_file_size, status_code_counts)
                    status_code_counts = {}
    except EOFError:
        if status_code_counts:
            print_statistics(total_file_size, status_code_counts)


if __name__ == "__main__":
    main()
