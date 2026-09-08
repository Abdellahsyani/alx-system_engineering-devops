# 0x05. Processes and signals

Scripts about PIDs, process listing/lookup, sending signals, and trapping them.
Together they form a small demo: a long-running process, scripts that kill it,
and a variant that refuses to die on `SIGTERM`.

## Key files

| File | What it does |
| --- | --- |
| `0-what-is-my-pid` | Prints the PID of the running script (`$$`) |
| `1-list_your_processes` | Full process listing in a tree format (`ps uf -e`) |
| `2-show_your_bash_pid` | Filters that listing for `bash` |
| `3-show_your_bash_pid_made_easy` | Same via `pgrep bash -l` (PID + name only) |
| `4-to_infinity_and_beyond` | Infinite loop printing `To infinity and beyond` every 2s |
| `5-dont_stop_me_now` | Kills `4-to_infinity_and_beyond` with `kill -SIGTERM` |
| `6-stop_me_if_you_can` | Kills the same process using `pkill` |
| `7-highlander` | Like task 4, but traps `SIGTERM` and prints `I am invincible!!!` |
| `67-stop_me_if_you_can` | `pkill -f "./7-highlander"` |
| `8-beheaded_process` | Kills `7-highlander` with `SIGKILL`, which cannot be trapped |
| `100-process_and_pid_file` | Writes `/var/run/myscript.pid`, handles `SIGINT`/`SIGTERM`/`SIGQUIT` and cleans up the PID file on exit |

## Usage

```bash
./4-to_infinity_and_beyond &   # start the victim
./5-dont_stop_me_now           # terminate it

./7-highlander &
./67-stop_me_if_you_can        # SIGTERM: trapped, keeps running
./8-beheaded_process           # SIGKILL: process dies
```

## Notes

`100-process_and_pid_file` writes to `/var/run`, so it needs root. The
`SIGKILL` vs. trapped-`SIGTERM` pair is the core lesson: `SIGKILL` (9) and
`SIGSTOP` cannot be caught, blocked or ignored.
