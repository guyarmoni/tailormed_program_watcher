from flask import Flask, render_template
import query_utils as q
app = Flask(__name__)


@app.route('/')
def get_fund_data():
    connection = q.connect_to_db()
    table = q.get_full_table(connection)
    table = list(map(lambda row: [row[0], row[1].split(','), row[2], row[3]], table))
    connection.close()
    return render_template('home_page.html', data=table)


if __name__ == '__main__':
    app.run(port=4444, debug=True)
