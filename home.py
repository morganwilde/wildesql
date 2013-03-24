import os, sys
sys.dont_write_bytecode = True
from flask import Flask, render_template, request

###
# wildesql imports
###
from logic.brains.dbInfo import tableNames, columnNames, tableData, tablePrimaryKey, columnLengths, dbName

temvar = {'tableNames': tableNames(),
          'state': {},
          'table': {},
          'action': {}}

app = Flask(__name__)

@app.route('/')
def begin():
    temvar['state']['table'] = None
    temvar['table'] = {}
    return render_template('home.html', temvar = temvar)

@app.route('/table')
@app.route('/table/')
@app.route('/table/<table>')
@app.route('/table/<table>/do-<action>', methods = ['GET', 'POST'])
def tableView(table = None, action = None):
    if table != None:
        table = str(table)
        temvar['state']['db'] = dbName()
        temvar['state']['table'] = table
        temvar['table']['columns'] = columnNames(table)
        temvar['table']['columnsLength'] = columnLengths(table)
        temvar['table']['primary'] = tablePrimaryKey(table)
        temvar['table']['entries'] = tableData(table)
        
        # actions
        if (action != None):
            temvar['action']['name'] = action
            temvar['action']['get'] = request.args
            temvar['action']['post'] = request.form
    else:
        # TODO implement error message for non-existing tables names (or empty ones)
        pass
    return render_template('block.table.html', temvar = temvar)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port, debug = True)
