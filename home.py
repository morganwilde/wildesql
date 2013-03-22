import os, sys
sys.dont_write_bytecode = True
from flask import Flask, render_template

###
# wildesql imports
###
from logic.brains.dbInfo import tableNames, columnNames, tableData

temvar = {'tableNames': tableNames(),
          'state': {},
          'table': {}}

app = Flask(__name__)

@app.route('/')
def begin():
    temvar['state']['table'] = None
    temvar['table'] = {}
    return render_template('home.html', temvar = temvar)

@app.route('/table')
@app.route('/table/')
@app.route('/table/<table>')
def tableView(table = None):
    if table != None:
        temvar['state']['table'] = table
        temvar['table']['columns'] = columnNames(table)
        temvar['table']['entries'] = tableData(table)
    else:
        # TODO implement error message for non-existing tables names (or empty ones)
        pass
    return render_template('block.table.html', temvar = temvar)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port, debug = True)
