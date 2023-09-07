import shutil
import tarfile

for i in range(999):
    file = tarfile.open(f'./{1000 - i}/{1000 - i - 1}.tar')
    file.extractall(f'./{1000 - i - 1}')
    file.close()
    if i < 998:
        shutil.rmtree(f'./{1000 - i}')
