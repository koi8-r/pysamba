from os import remove
from os.path import abspath, realpath, dirname, join, exists
from inspect import getabsfile, getmembers
import tdb, ldb
import sys


# Get script dir (follow symlinks)
def mypath():
    if getattr(sys, 'frozen', False):
        sp = abspath(sys.executable)
    else:
        # __file__ alt
        sp = getabsfile(mypath)
    return dirname(realpath(sp))


tb = tdb.Tdb(join(mypath(), 'samba/private/secrets.tdb'))
assert isinstance(tb, tdb.Tdb)
print type(tb)
print dir(tb)
print getattr(tb, 'filename', '<>')
if 10>9999:
    for m in getmembers(tb):
        print m

    print '----'
    for k in tb.iterkeys():
        print '{'
        print "key(%d) = %r" % (len(k), k)
        print "val(%d) = %r" % (len(tb[k]), tb[k])
        print '}'


hdbp = 'hello.ldb'
exists(hdbp) and remove(hdbp)
# Ldb is a LDAP abstraction over tdb database.
lb = ldb.Ldb(hdbp)
lb.add({
    'dn': 'dc=oz,dc=net,dc=ru',
    'hello_attr': 'Hello, World!'
})
for m in lb.search('dc=oz,dc=net,dc=ru'):
    # dir return attributes and methods
    assert isinstance(m, ldb.Message)
    print type(m)
    print dir(m)

    assert isinstance(m.dn, ldb.Dn)
    print type(m.dn)
    print dir(m.dn)
    print str(m.dn)

    assert isinstance(m['hello_attr'], ldb.MessageElement)
    print type(m['hello_attr'])
    print dir(m['hello_attr'])
    print str(m['hello_attr'])


for k in lb.__class__.__dict__:
    print k
