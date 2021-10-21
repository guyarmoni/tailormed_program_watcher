import parse_utils as p
import query_utils as q


def main():
    # connecting to DB if exists, otherwise creating a new one
    connection = q.connect_to_db()
    q.create_table(connection)

    table = q.get_full_table(connection)
    if not table:  # if table is empty, fill it for the first time
        p.fill_table(connection)
    else:
        p.update_table(connection)

    connection.close()


if __name__ == '__main__':
    main()
