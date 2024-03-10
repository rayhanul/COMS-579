

class Key_parser():

    def __init__(self, key_file="keys.txt") :

        self.key_file=key_file

    def parsing_keys(self):

        my_keys = {}
        with open(self.key_file) as myfile:
            for line in myfile:
                key_name, key_value = line.partition("=")[::2]
                my_keys[key_name.strip()] = key_value
        
        return my_keys





if __name__=="__main__":

    key_parser=Key_parser()

    my_keys=key_parser.parsing_keys()

    print(my_keys)

