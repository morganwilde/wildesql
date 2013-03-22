from logic.brains.databeam import session

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
    sql = "SELECT column_name FROM information_schema.columns WHERE table_name = '{0}' ORDER BY ordinal_position".format(table)
    names = session.query("column_name").from_statement(sql).all()
    return names

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
    sql = "SELECT {0} FROM {1} ORDER BY id ASC".format(columnsStr, table)
    data = session.query(*query).from_statement(sql).all()
    return data