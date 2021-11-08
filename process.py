#! /usr/bin/python3
import os


if __name__ == '__main__':
    data = ''
    hlink = ''
    with open('digest.rst', 'r') as f:
        for line in f:
            if line.startswith('|') and '``fmgr_' in line:
                start_index = line.find('``fmgr_')
                assert(start_index > 0)

                idx = start_index + 7
                end_index = -1

                while idx < len(line):
                    if line[idx] == '`':
                        end_index = idx
                        break
                    idx += 1
                assert(end_index > 0)
                end_index += 1
                assert(line[end_index] == '`')

                origin = line[start_index: end_index + 1]
                module = origin[2:-2]
                data += line.replace(origin, '%s_   ' % (module))

                link = ''
                fpath = 'docgen/%s.rst' % (module)
                if os.path.isfile(fpath):
                    link = '.. _%s: docgen/%s.html\n' % (module, module)
                else:
                    fpath = 'daemon_docgen/%s.rst' % (module)
                    assert(os.path.isfile(fpath))
                    link = '.. _%s: daemon_docgen/%s.html\n' % (module, module)
                hlink += link
            else:
                data += line


    with open('digest.rst', 'w') as f:
        f.write(data)
        f.write('\n\n')
        f.write(hlink)
