import sys
import os

p1, p2 = sys.version_info[:2]

build_dir = os.path.abspath( os.path.join(os.path.dirname(sys.argv[0]), "lzo", "build") )
if not os.path.isdir(build_dir):
    build_dir = os.path.abspath( os.path.join(os.path.dirname(sys.argv[0]), "..", "lzo", "build") )

dirs = os.listdir(build_dir)
for d in dirs:
    if d.find("-%s.%s" % (p1, p2)) != -1 and d.find("lib.") != -1:
#        cwd = os.getcwd()
#        os.chdir( os.path.join(build_dir, d) )
        sys.path.insert(0, os.path.join(build_dir, d) )
        import imp
        fp, pathname, description = imp.find_module("lzo")
        module = imp.load_module("lzo", fp, pathname, description)

        compress = module.compress
        decompress = module.decompress
        set_block_size = module.set_block_size

#        os.chdir(cwd)
        break
