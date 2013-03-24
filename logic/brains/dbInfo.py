from logic.brains.databeam import session, database_0

###
# Helper functions
###
def isNumberic(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

###
# dbInfo functions
###

def dbName():
    return database_0.getDb()

def tableNames(table_schema = 'public'):
    """
    return all table names that have a certain 'table_schema'
    """
    sql = "SELECT table_name FROM information_schema.tables WHERE table_schema = '{0}'".format(table_schema)
    names = session.query("table_name").from_statement(sql).all()
    return names

def columnNames(table):
    """
    returns all table column names
    """
    sql = ("SELECT column_name, character_maximum_length, udt_name "
           "FROM information_schema.columns "
           "WHERE table_name = '{0}' "
           "ORDER BY ordinal_position ASC").format(table)
    names = session.query("column_name", "character_maximum_length", "udt_name").from_statement(sql).all()
    return names

def columnLengths(table):
    """
    returns percentage lengths for each table column
    """
    # get the absolute lengths
    charMaxLengths = columnNames(table)
    columnInfo = {}
    totalLength = 0
    for length in charMaxLengths:
        colInfo = columnInfo[str(length[0])] = {}
        if length[1] != None:
            colInfo['length'] = int(length[1])
        else:
            if length[2] == 'int4':
                colInfo['length'] = 10
        totalLength += colInfo['length']
        
    # get relative lengths
    for column in columnInfo.keys():
        columnInfo[column]['percentage'] = "{0:.1f}".format((columnInfo[column]['length']/float(totalLength))*100)
        
    return columnInfo

def tableConstraints(table, constraint = 'pkey'):
    possibleConstraints = ['pkey', 'key', 'excl', 'idx', 'fkey']
    if not constraint in possibleConstraints:
        raise NameError('constraint not one of: ' + str(possibleConstraints))
    constraintName = str(table) + '_' + str(constraint)
    sql = ("SELECT column_name, constraint_name "
           "FROM information_schema.constraint_column_usage "
           "WHERE table_name = '{0}' AND constraint_name = '{1}'").format(table, constraintName)
    constraints = session.query("column_name", "constraint_name").from_statement(sql).all()
    return constraints

def tablePrimaryKey(table):
    return str(tableConstraints(table)[0][0])

def tableData(table):
    """
    returns all table entries
    """
    # arrange columns
    columns = columnNames(table)
    query = ()
    columnsStr = ''
    for column in columns:
        query += str(column[0]),
        columnsStr += '"' + column[0] + '", '
    if len(columnsStr) > 0:
        columnsStr = columnsStr[:-2]
    
    # query
    sql = "SELECT {0} FROM {1} ORDER BY {2} ASC".format(columnsStr, table, tablePrimaryKey(table))
    data = session.query(*query).from_statement(sql).all()
    
    # add types and structure
    dataStructured = {}
    rowNo = 0
    for row in data:
        columnNo = 0
        dataStructured[rowNo] = {}
        for column in tuple(row):
            value = column
            # float or int?
            if isNumberic(value):
                if float(value) == int(value):
                    value = int(value)
                else:
                    value = float(value)
            dataStructured[rowNo].update({str(columns[columnNo][0]): value})
            columnNo += 1
        rowNo += 1
    return dataStructured