# TODO решите задачу
import json

def task() -> float:

    with open('input.json', 'r') as fcc_file:
        fcc_data = json.load(fcc_file)
        a=0
        for x in fcc_data:
            a=a + x["score"] * x["weight"]

        return(round(a, 3))

print(task())
