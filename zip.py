import os
import tarfile

def tardir(path, tar_name):
    with tarfile.open(tar_name, "w:gz") as tar_handle:
        for root, dirs, files in os.walk(path):
            for file in files:
                tar_handle.add(os.path.join(root, file))
tardir('./lips', 'lips.tar.gz')

#windows
#gzip -d < lips.tar.gz | tar xvf -

