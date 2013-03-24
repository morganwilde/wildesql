class dbCredentials(object):
    """
    An object to store database connection information
    """
    def __init__(self, host, database, user, port, password, uriTemplate = None):
        self.host       = host
        self.database   = database
        self.user       = user
        self.port       = port
        self.password   = password
        # format of the connection uri
        if uriTemplate == None:
            self.uriTemplate = 'postgres://{0}:{1}@{2}:{3}/{4}'
        else:
            self.uriTemplate = uriTemplate
        
    def __str__(self):
        """
        returns the connection uri as a string
        """
        return self.uriTemplate.format(self.user,
                                       self.password,
                                       self.host,
                                       self.port,
                                       self.database)
    def __repr__(self):
        return object.__repr__(self)
    
    def getDb(self):
        return self.database