from optparse import OptionParser

def convert_edges(input_file):
    try:
        ifs = open(input_file, 'r')
        base, ext = input_file.split('.')
        ofs = open(base + '-weighted.' + ext, 'w')
        try:
            ofs.write(ifs.readline())
            for line in ifs:
                source_id, target_id = line.strip().split(',')
                source_id = int(source_id)
                target_id = int(target_id)
                if source_id < target_id:
                    ofs.write('%d,%d\n' % (source_id, target_id))
                else:
                    ofs.write('%d,%d\n' % (target_id, source_id))
        finally:
            ifs.close()
            ofs.close()
    except IOError:
        print 'Error in opening edges file ' + input_file

if __name__ == "__main__":
    parser = OptionParser()
    parser.set_defaults(input_file='edges.csv')
    parser.add_option('-f', '--file', dest='input_file',
                        help='Input file (csv) with directed edges')              
    (options, args) = parser.parse_args()

    convert_edges(options.input_file)
