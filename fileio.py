from datetime import datetime

def current_datetime():
    '''Return a string of the current date and time YYYY-MM-DD__HH-MM-SS'''
    return datetime.now().strftime('%Y-%m-%d__%H-%M-%S')

def clear_txt():
    pass

def from_txt(filename, stripwhite=False, stripblank=False):
    '''Read a txt as lines into a list.
    Remove newlines at end.
    Leave whitespace at the ends, empty string lines, duplicates, order.
    filename is a txt file in the directory, not a path.'''
    with open(filename, 'r', encoding='utf-8') as input_file:
        input_lines = input_file.readlines()
        for n, element in enumerate(input_lines):
            input_lines[n] = element.strip('\n')
            # for some reason, URLs with spaces aren't fetched, so be sure to strip the spaces
    # input_lines = list(set(input_lines))
    # input_lines = [f for f in input_lines if '/art/' in f]
    # input_lines.sort()
    return input_lines

def to_txt(output_list, filename):
    '''Write a list to the named txt file, with a newline added to each line.
    Append without overwriting the file.'''
    # output_list = list(set(output_list))
    # output_list.sort()
    with open(filename, 'a', encoding='utf-8') as output_file:
        for line in output_list:
            output_file.write(line + '\n')

def clear_csv():
    pass

def from_csv(path):
    '''Read a CSV into a list of dicts.
    CSV should be tab separated and in UTF-8.
    Labels are on the first row of the CSV.
    Make sure the fields are delimited by tabs. Values need not be enclosed by quotes.'''
    with open(path, 'r', encoding='utf-8') as input_file:
        input_lines = [f.strip(' \n') for f in input_file.readlines()]
    output_lines = []
    labels = input_lines[0].replace('"', '').split('\t')
    for element in input_lines[1:]:
        temp = element.replace('"', '').split('\t')
        line_dict = {}
        for n, label in enumerate(labels):
            line_dict[label] = temp[n]
            '''
            try:
                line_dict[label] = temp[n]
            except:
                line_dict[label] = ''
            '''
        output_lines.append(line_dict)
    return output_lines, labels

def labels_to_csv(labels, filename):
    '''Clear the output CSV
    and write the label row to it.'''
    with open(filename, 'w', encoding='utf-8') as output_file:
        labels_line = labels[:]
        for n, label in enumerate(labels_line):
            labels_line[n] = '"' + label + '"'
        labels_line = '\t'.join(labels_line)
        output_file.write(labels_line + '\n')

def dicts_to_csv(labels, dicts, filename):
    '''Given a list of dicts,
    append them to the output csv.'''
    with open(filename, 'a', encoding='utf-8') as output_file:
        for dict in dicts:
            line = []
            for label in labels:
                line.append('"' + dict[label] + '"')
            line = '\t'.join(line)
            output_file.write(line + '\n')

if __name__ == "__main__":
    sample = from_txt('test.txt')
    to_txt(sample, current_datetime() + ' ' + 'output.txt')

    sample, labels = from_csv('_input csv.csv')
    print(sample)
    labels_to_csv(labels, '_output csv.csv')
    dicts_to_csv(labels, sample, current_datetime() + ' ' + '_output csv.csv')