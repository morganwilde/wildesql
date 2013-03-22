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
            #postgres://xjdyiagoarqlrs:epix62QOYw9nacR6X8Z6yrsvS9@ec2-23-21-91-29.compute-1.amazonaws.com:5432/dcotsto8k30h0f
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