import yaml

with open('./automation/structure.yaml') as file:
    test = yaml.load(file, Loader=yaml.FullLoader)

def get_type(child):
    if 'type' not in child:
        raise Exception('child does not have "type" field set: ' + str(child))
    else:
        return child['type']

def iterate(children, depth=0):
    for child in children:
        print(get_type(child))
        if 'children' in child:
            iterate(child['children'], depth + 1)

iterate(test)

