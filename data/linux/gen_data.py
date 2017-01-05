import os


METAFILE = 'linux_kernel_c_files.txt'
PATH = os.environ['HOME'] + '/_/tf/datasets/lm/linux_kernel/linux-4.9/'


def get_filenames(filename):
    with open(filename) as f:
        return [ line for line in f.read().split('\n')
                if line[-2:] == '.c' ]

def read_file(filename):
    try:
        with open(filename) as f:
            return f.read()
    except:
        return None

def filter_comments(content):
    lines = []
    # remove single line comments
    for line in content.split('\n'):
        if line.strip():
            # check for multiline comment in single line
            if line[0] != '//' and line.count('/*') + line.count('*/') < 2:
                lines.append(line)

    # now.. deal with multiline comments
    indices = [ i for i,line in enumerate(lines) 
            if '/*' in line or '*/' in line ]
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
    for i, filename in enumerate(filenames):
        print('[{}/{}] reading file : {}'.format(i+1, len(filenames), filename))
        raw_content = read_file(filename)
        if raw_content:
            content = filter_comments(raw_content)
        # write content to file
        with open('linux_kernel.txt', 'a') as f:
            f.write('\n')
            f.write(content)
