import sys

class Tally_Splitter(object):

    def split_file(self, file_data):
        assert len(file_data) > 0
        assert type(file_data[0]) == str

        i = 0
        while i < len(file_data):
            print i
            current_line = file_data[i]
            if current_line.split()[0] == 'tally':         # here begins extraction of data
                tally_name = 'tally' + current_line.split()[1]
                i += 1
                tally_description = file_data[i]

                while True:                             # d, u, s, m, c, et - some lines before data must be skipped
                    i += 1
                    if file_data[i].split()[0] == 'et':
                        break                           # next line is begining of data

                list_of_energies = []
                while True:
                    i += 1
                    if file_data[i].split()[0] == 't':
                        break                           # no more data
                    for energy in file_data[i].split():
                        list_of_energies.append(energy)

                i += 1
                assert file_data[i] == 'vals\n'
                list_of_values = []
                list_of_accuracy = []
                while True:
                    i += 1
                    if file_data[i].split()[0] == 'tfc':
                        break
                    for el in file_data[i].split('  '):
                        if el == '':
                            continue
                        list_of_values.append(el.split()[0])
                        list_of_accuracy.append(el.split()[1])

                print tally_name
                print tally_description
                print list_of_energies
                print list_of_values
                print list_of_accuracy
            i += 1


if __name__ == "__main__":
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print 'Invalid number of arguments\nUsage: mcnp_mtal_splitter filename'
        exit()
    filename = sys.argv[1]

    with open(filename, 'r') as f:
        file_data = f.readlines()
        ts = Tally_Splitter()
        ts.split_file(file_data)


