import os

all = 'paste Path '
print([name for name in os.listdir(all) if os.path.isdir(name)])
print([name for name in os.listdir(all) if os.path.isfile(name)])
