import samba.dcerpc.lsa as lsa
import samba.dcerpc.samr as samr
import samba.dcerpc.winreg as winreg


domname = lsa.String()
domname.string = u'DOMAIN'

con = samr.samr('ncalrpc:', 'samba/etc/smb.conf')
h = con.Connect(0, 0xFFFFFFF)
sid = con.LookupDomain(h, domname)
print sid
con.Close(h)

from samba.tests import RpcInterfaceTestCase
class WinregTests(RpcInterfaceTestCase):
    def setUp(self):
        self.conn = winreg.winreg('ncalrpc:', self.get_loadparm(), self.get_credentials())
    def testhklm(self):
        handle = self.conn.OpenHKLM(None, winreg.KEY_QUERY_VALUE | winreg.KEY_ENUMERATE_SUB_KEYS)
        self.conn.CloseKey(handle)
