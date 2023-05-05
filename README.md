### Hexlet tests and linter status:
[![Actions Status](https://github.com/foxy-chay/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/foxy-chay/python-project-52/actions)

### GitHub Actions
[![linter & tests](https://github.com/foxy-chay/python-project-52/actions/workflows/linter&tests.yml/badge.svg)](https://github.com/foxy-chay/python-project-52/actions/workflows/linter&tests.yml)

### Code Climate
[![Maintainability](https://api.codeclimate.com/v1/badges/e38d3f4981df89d41b55/maintainability)](https://codeclimate.com/github/foxy-chay/python-project-52/maintainability)

### Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/e38d3f4981df89d41b55/test_coverage)](https://codeclimate.com/github/foxy-chay/python-project-52/test_coverage)

# Task Manager

Register, create, delete, and modify tasks, labels, and statuses. Assign task executors and filter tasks by tags, statuses, and executors, or view only tasks that you have created!

## Installation

Clone the repository:

`git clone https://github.com/foxy-chay/python-project-52.git`

Go to the project folder:

`cd python-project-52`

[Install Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)

`make install`

## Settings

Create an ".env" file in the root project directory: 

`touch .env`

Add variables:

ROLLBAR_KEY (Rollbar key)
SECRET_KEY (Secter key Django)
DB_URL (Database)

To use simple sqlite database use this record: 
`DB_URL='sqlite:///db.sqlite3'`

### Start project

`make server`

Use this app in browser on http://localhost:8080
