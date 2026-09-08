# 0x16. API advanced

Python modules that query the public (unauthenticated) Reddit JSON API. Each
file exposes a single function meant to be imported, not executed, and handles
pagination and error responses without raising.

## Key files

| File | Function | Behaviour |
| --- | --- | --- |
| `0-subs.py` | `number_of_subscribers(subreddit)` | Returns the subscriber count from `/r/<sub>/about.json`, or `0` for an invalid subreddit |
| `1-top_ten.py` | `top_ten(subreddit)` | Prints the titles of the first 10 hot posts, or `None` when the subreddit does not exist |
| `2-recurse.py` | `recurse(subreddit, hot_list=[], after="")` | Recursively follows the `after` cursor and returns every hot post title, or `None` |
| `100-count.py` | `get_posts(subreddit, after="")` | Helper returning one page of posts plus the next `after` cursor, used to tally keyword occurrences |

## Usage

```python
from importlib import import_module

number_of_subscribers = import_module('0-subs').number_of_subscribers
print(number_of_subscribers("programming"))
```

## Notes

- Requests set a custom `User-Agent`; Reddit throttles or rejects the default
  `python-requests` agent.
- Redirects are relied upon *not* being followed for invalid subreddits — a
  non-`200` status is treated as "subreddit does not exist" and returns the
  neutral value instead of raising.
- Pagination uses the `after` fullname cursor with `limit=100`, the API maximum.
- `__pycache__/` holds compiled bytecode and can be deleted at any time.
