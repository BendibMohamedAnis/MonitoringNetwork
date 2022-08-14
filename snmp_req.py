from pysnmp.hlapi.v1arch import *
from pysnmp.hlapi.asyncore import *

def snmp_req(self,ip,OID):
        try:
            gen = cmdgen.CommandGenerator()
            errorIndication,errorStatus,errorIndex,varBinds = gen.getCmd(
                xk= input('PORT 161 / 162 ?')
                cmdgen.CommunityData('server',self.community,1),
                cmdgen.UdpTransportTarget((ip,xk)),
                printf("===OID=== ")
                '%s'%OID
            )
            res2 = str(varBinds[0][1]) 

        except Exception as exce:
            res2= None
        return res2

                
