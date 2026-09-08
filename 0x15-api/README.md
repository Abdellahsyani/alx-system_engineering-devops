# 0x15. API

Python scripts that consume the [JSONPlaceholder](https://jsonplaceholder.typicode.com)
REST API to build employee to-do reports and export them to CSV and JSON. They
illustrate the DevOps side of APIs: turning a remote data source into files
other tools can consume.

## Key files

| File | What it does |
| --- | --- |
| `0-gather_data_from_an_API.py` | Takes an employee ID and prints `Employee NAME is done with tasks(done/total):` followed by each completed task title |
| `1-export_to_CSV.py` | Exports that employee's tasks to `<USER_ID>.csv` with all fields quoted: `id,username,completed,title` |
| `2-export_to_JSON.py` | Exports the same data to `<USER_ID>.json` as `{"USER_ID": [{"task", "completed", "username"}, ...]}` |
| `3-dictionary_of_list_of_dictionaries.py` | Exports every employee's tasks to `todo_all_employees.json`, keyed by user ID |
| `2.csv` | Sample output produced by `1-export_to_CSV.py` for user 2 |

## Usage

```bash
python3 0-gather_data_from_an_API.py 2
python3 1-export_to_CSV.py 2          # writes 2.csv
python3 3-dictionary_of_list_of_dictionaries.py   # writes todo_all_employees.json
```

## Notes

Requires the `requests` library (`pip3 install requests`) and network access.
User data comes from `/users/<id>` and tasks from `/todos?userId=<id>`; the
scripts guard the entry point with `if __name__ == "__main__":` so they can also
be imported. `3-dictionary...` issues one request per user, so it is the
slowest of the four.
