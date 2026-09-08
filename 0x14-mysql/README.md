# 0x14. MySQL

Setting up a MySQL primary/replica pair and the accounts needed to monitor and
back it up.

## Key files

| File | What it does |
| --- | --- |
| `setup_mysql` | Adds the MySQL 5.7 APT repository and its signing key, then installs the client, server and community server packages |
| `1-setup_user.sql` | Creates `holberton_user@localhost` and grants it `REPLICATION CLIENT` on `*.*` so replication status can be checked |
| `2-mysql.sql` | Creates the `tyrell_corp` database with a `nexus6` table, inserts one row (`Leon`) and grants `SELECT` on it to `holberton_user` |

## Usage

```bash
sudo ./setup_mysql
cat 1-setup_user.sql | sudo mysql -uroot -p
cat 2-mysql.sql | sudo mysql -uroot -p
sudo mysql -uroot -p -e "SELECT * FROM tyrell_corp.nexus6"
```

## Notes

`2-mysql.sql` starts with `DROP DATABASE IF EXISTS tyrell_corp`, so re-running
it destroys existing data. `REPLICATION CLIENT` is the minimal privilege for
`SHOW MASTER STATUS` / `SHOW SLAVE STATUS`, which is what a monitoring or
backup agent needs — it grants no access to table data.
