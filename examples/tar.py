import gzip
import sys
import tarfile
from os import scandir, makedirs
from os.path import isdir, splitext

from steganosort.util import list_encode, list_decode


def tar_sort(files):
    # top level sort by file type (extension)
    # sort by pathname for each file type
    files = sorted(files)
    files = sorted(files, key=lambda k: splitext(k)[1])
    return files


def _enumerate_files(*files):
    all_files = []
    for path in files:
        if isdir(path):
            all_files += [entry.path for entry in scandir(path) if entry.is_file()]
        else:
            all_files.append(path)
    return all_files


def pack(stdin, tarpath, *files, **kwargs):
    files = _enumerate_files(*files)
    compress = kwargs.get('compress', True)
    f = gzip.GzipFile(tarpath, 'wb') if compress else open(tarpath, 'wb')
    with f, tarfile.TarFile(mode='w', fileobj=f) as tar:
        for infile in list_encode(files, stdin.read(), tar_sort):
            tar.add(infile)


def extract(stdout, tarpath, target_dir, **kwargs):
    compress = kwargs.get('compress', True)
    f = gzip.GzipFile(tarpath, 'rb') if compress else open(tarpath, 'rb')
    with f, tarfile.TarFile(mode='r', fileobj=f) as tar:
        file_list = tar.getnames()
        stdout.write(list_decode(file_list, tar_sort).decode('utf-8'))

        makedirs(target_dir, exist_ok=True)
        tar.extractall(target_dir)


def main(cmd, *args):
    kw = {
        'compress': 'z' in cmd
    }
    if 'x' in cmd:
        return extract(sys.stdout, *args, **kw)
    else:
        return pack(sys.stdin, *args, **kw)


if __name__ == '__main__':
    print(sys.argv)
    main(*sys.argv[1:])