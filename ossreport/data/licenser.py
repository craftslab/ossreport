# -*- coding: utf-8 -*-

import argparse
import json
import os
import re
import sys
import yaml

SEP = "---"


def dump_json(data, name):
    with open(name, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2))


def update_json(data, update):
    def _helper(data):
        buf = {}
        for index in range(len(data)):
            buf[data[index]["licenseId"]] = index
        return buf

    keys = _helper(data["licenses"])
    for item in update:
        if item["spdx-id"] in keys.keys():
            buf = data["licenses"][keys[item["spdx-id"]]]
            buf["permissions"] = item["permissions"]
            buf["conditions"] = item["conditions"]
            buf["limitations"] = item["limitations"]
            data["licenses"][keys[item["spdx-id"]]] = buf
    return data


def load_json(name):
    with open(name, "r", encoding="utf-8") as f:
        buf = json.load(f)
    return buf


def read_files(dname):
    def _helper(name):
        with open(name, "r", encoding="utf-8") as f:
            buf = f.read().split(SEP)[1]
            return yaml.load(buf, Loader=yaml.FullLoader)

    buf = []
    for root, _, fnames in os.walk(dname):
        for item in fnames:
            buf.append(_helper(os.path.join(root, item)))
    return buf


def validate_args(data):
    if (
        not isinstance(data.choosealicense_dir, str)
        or len(data.choosealicense_dir.strip()) == 0
    ):
        return False
    if not os.path.exists(data.choosealicense_dir):
        return False
    if not isinstance(data.spdx_file, str) or len(data.spdx_file.strip()) == 0:
        return False
    if not data.spdx_file.endswith(".json"):
        return False
    if not os.path.exists(data.spdx_file):
        return False
    if not isinstance(data.output_file, str) or len(data.output_file.strip()) == 0:
        return False
    if not data.output_file.endswith(".json"):
        return False
    if os.path.exists(data.output_file):
        return False
    return True


def build_parser(data):
    parser = argparse.ArgumentParser(description="Licenser")
    parser.add_argument(
        "--choosealicense-dir",
        action="store",
        dest="choosealicense_dir",
        help="choosealicense directory",
        required=True,
    )
    parser.add_argument(
        "--spdx-file",
        action="store",
        dest="spdx_file",
        help="spdx file (.json)",
        required=True,
    )
    parser.add_argument(
        "--output-file",
        action="store",
        dest="output_file",
        help="output file (.json)",
        required=True,
    )
    return parser.parse_args(data)


def main():
    args = build_parser(sys.argv[1:])
    if validate_args(args) is False:
        print("args invalid")
        return -1

    buf = load_json(args.spdx_file)
    if buf is None or len(buf) == 0:
        print("failed to load json")
        return -2

    buf = update_json(buf, read_files(args.choosealicense_dir))
    if buf is None or len(buf) == 0:
        print("failed to update json")
        return -3

    dump_json(buf, args.output_file)

    return 0


if __name__ == "__main__":
    sys.argv[0] = re.sub(r"(-script\.pyw?|\.exe)?$", "", sys.argv[0])
    sys.exit(main())
