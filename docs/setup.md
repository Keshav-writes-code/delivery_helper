## Setup to Run this on Your Machine

This guide will walk you through how to setup this project on your Machine to run the dev server successfully

## Install Prerequisites

1. Install these Language Tools according to your OS

- [ Python ](https://www.python.org/)
- [ Nodejs ](https://nodejs.org/en)
- [ Bun ](https://nodejs.org/en)
- [ UV](https://docs.astral.sh/uv/getting-started/installation/)

2. Install Mysql on your OS (for linux(Debian) refer this guide : [Install Mysql on Antix Linux](https://keshav.is-a.dev/FreqKnow/linux/mysql-setup-on-antix/))
3. Clone this Project

   ```sh
   git clone https://github.com/Keshav-writes-code/delivery_helper.git
   cd delivery_helper
   ```

4. Install Python and Node dependencies

   ```sh
   uv sync &&
   cd ./delivery_helper_app/frontend &&
   bun i &&
   cd -
   ```

## Setup Database

Your Database is required to have a user named : `root` with password `root`

1. create a Database with the name `delivery_management_system` on your OS Mysql Application

   ```sql
   create database delivery_management_system
   ```

2. Sync Database Schema (Tables, etc)

   ```sh
   uv run manage.py makemigrations
   uv run manage.py migrate
   ```

## Run Dev Server

1. in the project root, run this for the Django Server

```sh
uv run manage.py runserver
```

2. And also run this in a seperate terminal for the Frontend Dev Server from Vite

```sh
cd ./delivery_helper_app/frontend &&
bun dev

```
