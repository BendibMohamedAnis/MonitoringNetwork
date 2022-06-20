from pysnmp.hlapi.v1arch import *
from pysnmp.hlapi.asyncore import *

def snmp_req(self,ip,OID):
        try:
            gen = cmdgen.CommandGenerator()
            errorIndication,errorStatus,errorIndex,varBinds = gen.getCmd(
                cmdgen.CommunityData('server',self.community,1),
                cmdgen.UdpTransportTarget((ip,161)),
                printf("===OID=== ")
                '%s'%OID
            )
            res2 = str(varBinds[0][1]) 

        except Exception as exce:
            res2= None
        return res2