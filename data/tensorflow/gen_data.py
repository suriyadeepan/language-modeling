import os


METAFILE = 'tf_py_files.txt'
PATH = os.environ['HOME'] + '/_/tf/tensorflow/'


def get_filenames(filename):
    with open(filename) as f:
        return [ line for line in f.read().split('\n')
                if '__init__' not in line and '.py' in line ]

def read_file(filename):
    with open(filename) as f:
        return f.read()

def filter_comments(content):
    lines = []
    # remove single line comments
    for line in content.split('\n'):
        if line.strip():
            # check for multiline comment in single line
            if line[0] != '#' and line.count('"""') != 2:
                lines.append(line)

    # now.. deal with multiline comments
    indices = [ i for i,line in enumerate(lines) 
            if '\"\"\"' in line ]
    try:
        # forbidden indices of lines <- comments
        if len(indices):
            #try:
            indices = [ list(range(indices[i], indices[i+1]+1)) 
                    for i in range(0, len(indices), 2) ]
            # unpack
            indices = [x for l in indices for x in l]
            #except:
            #    return '\n'.join(lines)
            # reiterate through content
            return '\n'.join([ line for i,line in enumerate(lines) if i not in indices])
    except:
        pass

    return '\n'.join(lines)



if __name__ == '__main__':
    filenames = [ PATH + f for f in get_filenames(METAFILE) ]
    print('{} files found'.format(len(filenames)))
    content = ''
    for filename in filenames:
        print('reading file : ' + filename)
        content += filter_comments(read_file(filename))
    # write content to file
    with open('tensorflow.txt', 'w') as f:
        f.write(content)
