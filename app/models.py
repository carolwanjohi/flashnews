class Source:
    '''
    Class that defines Source objects
    '''
    def __init__(self,id,name,description):
        '''
        __init__ method to define the properties of a Source object

        Args:
            id : The unique identifier for the news source. 
            name : The display-friendly name of the news source.
            description : A brief description of the news source and what area they specialize in.
        '''
        self.id = id
        self.name = name
        self.description = description
