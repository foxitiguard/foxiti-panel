import json
from foxitipanel_version import BUILD, VERSION

class CLMain():
    def __init__(self):
        self.path = '/usr/local/FoxitiCP/version.txt'
        #versionInfo = json.loads(open(self.path, 'r').read())
        self.version = VERSION
        self.build = str(BUILD)

        ipFile = "/etc/foxitipanel/machineIP"
        f = open(ipFile)
        ipData = f.read()
        self.ipAddress = ipData.split('\n', 1)[0]

        self.initialMeta = {
            "result": "ok"
        }
