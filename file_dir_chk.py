import os

all = 'paste Path '
print([name for name in os.listdir(all) if os.path.isdir(os.path.join(all,name))])
print([name for name in os.listdir(all) if os.path.isfile(os.path.join(all, name))])
