import boto3
from typing import List

config = boto3.client("config")

dynamodb = boto3.client("dynamodb")


def get_tables() -> List[str]:
    table_list :List[str] = []
    for page in dynamodb.get_paginator("list_tables"):
        table_list.extend(page["TableName"])

    return sorted(table_list)


def warmup(table_name:str) ->

def main():
    for table in get_tables():
        warmup(table)


if __name__ == "__main__":
    main()