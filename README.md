# Setup Database

- Install Mysql on your OS (for linux(Debian) refer this guide :(Install Mysql on Antix Linux)[https://keshav.is-a.dev/FreqKnow/linux/mysql-setup-on-antix/] )
- create a Database with the name `delivery_management_system`

```sql
create database delivery_management_system
```

- Sync Database Schema (Tables, etc) Specified in the Django Project to the Mysqldb installed on OS

```sh
uv run manage.py migrate
```

or

```sh
python manage.py migrate
```

for More Setup instruction, refer the Text file at `docs/setup.md`
