import sys

class Tally_Splitter(object):

    def split_file(self, file_data, filename):
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


                # saving all to file
                new_file_name = filename[:-3] + '_' + tally_name + '.csv'
                file = open(new_file_name,'w')   # Trying to create a new file or open one

                file.write(tally_name + ';' + tally_description)
                for k in range(len(list_of_energies)):
                    new_line = list_of_energies[k] + ';' + list_of_values[k] + ';' + list_of_accuracy[k] + '\n'
                    file.write(new_line.replace('.',','))
                last_line = 'TOTAL;' + list_of_values[k+1] + ';' + list_of_accuracy[k+1]
                file.write(last_line.replace('.',','))

                file.close()
            i += 1


if __name__ == "__main__":
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print 'Invalid number of arguments\nUsage: mcnp_mtal_splitter filename'
        exit()
    filename = sys.argv[1]

    with open(filename, 'r') as f:
        file_data = f.readlines()
        ts = Tally_Splitter()
        ts.split_file(file_data, filename)


