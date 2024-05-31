class Field():
    """Parameters: table_id, datatype, label, name, value, max_length, hidden\n\n
    Each field in every table has properties that allow the user
    to automatically set up input forms, type check the input, limit
    the length of the field and the label for each field
    """
    def __init__(self, **kwargs):
        self.table_id   =   kwargs.get('table_id', 0)
        self.datatype   =   kwargs.get('datatype', None)
        self.label=   kwargs.get('label', None)
        self.name  =   kwargs.get('name', None)
        self.value      =   kwargs.get('value', None)
        self.max_length =   kwargs.get('max_length', None)
        self.hidden     =   kwargs.get('hidden', False)
    def __str__(self):
        return f"{self.name}: {self.value}"
    

    def create_table(self):
        sql = """DROP table field;
            CREATE TABLE field (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'table_id' INTEGER,
            'datatype' TEXT NOT NULL,
            'label' TEXT NOT NULL,
            'name' TEXT NOT NULL,
            'value' TEXT,
            'max_length' INTEGER,
            'hidden' BOOLEAN DEFAULT FALSE
            );
        """
        # add sqlite3 code
    
    
    def add_new_item(self):
        pass


class Fields(Field):
    """This is a list of all of the fields for a model. It may be easier
    to simply make a list in each model.
    """
    def __init__(self, list:Field=[], **kwargs):
        self.list = list
        self.html_input_str = kwargs.get('html_input_str', None)


datatypes = {
            'Integer': {'python': 'int', 'html': 'number', 'sql': 'INTEGER'},
            'Float': {'python': 'float', 'html': 'number', 'sql': 'REAL'},
            'Text':{'python':'str', 'html': 'text', 'sql':''},
            'Email':{'python':'str', 'html': 'email', 'sql':'TEXT'},
            'Phone':{'python':'str', 'html': 'tel', 'sql':'TEXT'},
            'BlockText':{'python':'str', 'html': 'textarea', 'sql':'TEXT'},
            'Boolean':{'python':'bool', 'html': 'checkbox', 'sql':'INTEGER'},
            'Date':{'python':'datetime', 'html': 'datelocal', 'sql':'TEXT'},
            'Password':{'python':'str', 'html': 'password', 'sql':'TEXT'}
            }