import klepto

d = klepto.archives.dir_archive('data', cached=True, serialized=True)
for k, v in d.iteritems():
    print(k)
