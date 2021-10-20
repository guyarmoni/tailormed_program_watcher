import sqlite3

CREATE_FUNDS_TABLE = """CREATE TABLE IF NOT EXISTS programs (
                        name TEXT,
                        treatments TEXT,
                        status TEXT,
                        grant TEXT
                        )"""

INSERT_FUND = "INSERT INTO programs VALUES (?, ?, ?, ?)"

GET_FUND_STATUS = "SELECT status FROM programs WHERE name=?"

UPDATE_ROW_INFO = "UPDATE programs SET treatments=?, status=?, grant=? WHERE name=?"

SELECT_ROW = "SELECT * FROM programs WHERE name=?"

SELECT_ALL = "SELECT * FROM programs"


def connect_to_db():
    return sqlite3.connect('assistance_program.db')


def create_table(connection):
    with connection:
        connection.execute(CREATE_FUNDS_TABLE)


def add_fund_to_db(connection, program):
    with connection:
        connection.execute(INSERT_FUND, (program.name, program.concat_treatments(),
                                         program.status, program.grant_amount))


def update_fund_in_db(connection, program):
    with connection:
        row = get_row(connection, program.name)
        if not row:
            print("ERROR: Assistance program name on the website has changed")
            # todo - add error
        elif row[0] != program.get_program_as_db_row():
            update_row(connection, program)


def get_status(connection, program):
    with connection:
        return connection.execute(GET_FUND_STATUS, (program.name, )).fetchall()[0][0]


def update_row(connection, program):
    with connection:
        connection.execute(UPDATE_ROW_INFO, (program.concat_treatments(), program.status,
                                             program.grant_amount, program.name))


def get_row(connection, program_name):
    with connection:
        return connection.execute(SELECT_ROW, (program_name, )).fetchall()


def get_full_table(connection):
    with connection:
        return connection.execute(SELECT_ALL).fetchall()
