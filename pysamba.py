from samba.samdb import SamDB
from samba.auth import system_session
import samba.param
import inspect
import ldb


"https://habrahabr.ru/post/259029/"
lp = samba.param.LoadParm()
lp.load('samba/etc/smb.conf')
lp.set('private directory', 'samba/private/')
sam = SamDB(lp=lp, session_info=system_session())

res = sam.search(
    base='DC=murmangaz,DC=lan',
    scope=ldb.SCOPE_SUBTREE,
    expression='(&(|(objectCategory=person)(objectCategory=computer))(objectClass=user))',
    attrs=['*', 'unicodePwd']
)
print type(res)
for r in res:
    #dn = str(r.dn)
    cat = r['objectCategory']
    print type(cat)
    print cat.__class__.__name__
    print inspect.getfile(cat.__class__)

    print str(cat), str(r.dn)
