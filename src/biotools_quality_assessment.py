import json


class instance(object):

    def __init__(self, name):

        # TODO: restrict the format of properties

        # TODO: include @id
        self.name = name
        self.description = None # string
        self.version = None
        self.type = None
        self.links =[]
        self.publication =  0 # number of related publications [by now, for simplicity]
        self.download = []  # list of lists: [[type, url], [], ...]
        self.inst_instr = False # boolean // FUTURE: uri or text
        self.test = False # boolean // FUTURE: uri or text
        self.src = [] # string
        self.os = [] # list of strings
        self.input = [] # list of dictionaries biotools-like {'format' : <format> , 'uri' : <uri> , 'data' : <data> , 'uri': <uri>}
        self.output = [] # list of dictionaries biotools-like {'format' : <format> , 'uri' : <uri> }
        self.dependencies = [] # list of strings
        self.documentation = [] # list of lists [[type, url], [type, rul], ...]
        self.license = False # string
        self.termsUse = False #
        self.contribPolicy = False
        self.authors = [] # list of strings
        self.repository = []
        self.description = False
        self.source = [] #string
        self.bioschemas = False
        self.https = False
        self.operational = False
        self.ssl = False



class toolGenerator(object):
    def __init__(self, tools, source):
        self.tools = tools
        self.source = source
        self.instances = []


def cleanVersion(version):
    if version != None:
        if '.' in version:
            return(version.split('.')[0]+'.'+ version.split('.')[1])
        else:
            return(version)
    else:
        return(version)


def lowerInputs(listInputs):
    newList = []
    if len(listInputs)>0:
        for format in listInputs:
            newFormat = {}
            for a in format.keys():
                newInner = {}
                if format[a] != []:
                    if type(format[a]) == list:
                        for eachdict in format[a]:
                            for e in eachdict.keys():
                                newInner[e] = eachdict[e].lower()
                            newFormat[a] = newInner
                    else:
                        for e in format[a].keys():
                            newInner[e] = format[a][e].lower()
                        newFormat[a] = newInner
        newList.append(newFormat)
    else:
        return([])
    return(newList)


class biotoolsToolsGenerator(toolGenerator):

    def __init__(self, tools, source = 'biotools'):

        toolGenerator.__init__(self, tools, source)

        for tool in self.tools:
            name = tool['name'].lower()
            newInst = instance(name)

            newInst.type = tool.get("toolType")
            newInst.version = self.parse_versions(tool)
            newInst.description = tool.get('description')
            newInst.homepage = tool.get('homepage')
            newInst.publication = len(tool['publication'])
            newInst.download = self.parse_download(tool)
            newInst.src = self.parse_src(tool)
            newInst.os = tool.get('operatingSystem')
            newInst.input = self.parse_input(tool)
            newInst.output = self.parse_output(tool)
            newInst.documentation = self.parse_documentation(tool)
            newInst.inst_instr = self.parse_install_instr(tool, newInst)
            newInst.license = tool.get('license')
            newInst.authors = self.parse_authors(tool)
            newInst.repository = self.parse_repositories(tool)

            newInst.source = ['biotools']

            self.instances.append(newInst)
    

    def parse_versions(self, tool):
        versions = []
        if type(tool.get("version")) == list:
            for v in tool.get("version"):
                versions.append(cleanVersion(v))
        return(versions)


    def parse_download(self, tool):
        links = [ [tol['type'], tol['url']] for tol in tool['download'] ]
        return(links)


    def parse_src(self, tool):
        src = []
        for down in [a for a in tool['download'] if a['type'] == 'Source package']:
            src.append(down['url'])
        return(src)
    
    def parse_input(self, tool):
        inputs = []
        if len(tool['function'])>0:
            inputs = [f['input'] for f in tool['function']]
            return(lowerInputs(inputs[0]))
        else:
            return([])

    def parse_output(self, tool):
        outputs = []
        if len(tool['function'])>0:
            outputs = [f['input'] for f in tool['function']]
            return(lowerInputs(outputs[0]))
        else:
            return([])

    def parse_documentation(self, tool):
        doc = [ [tol['type'], tol['url']] for tol in tool['download'] ]
        return(doc)
    
    def parse_install_instr(self, tool, newInst):
        if 'Manual' in [ doc[0] for doc in newInst.documentation ]:
            return(True)
        else:
            return(False)
        
    def parse_authors(self, tool):
        newAuth = []
        for dic in tool['credit']:
            if dic['name'] not in newAuth and dic['name']!=None:
                newAuth.append(dic['name'])
        return(newAuth)
    
    def parse_repositories(self, tool):
        repos = []
        for link in tool['link']:
            if link['type'] == "Repository":
                repos.append(link['url'])
        return(repos)


def parse_biotools_metadata(in_file):
    # open json
    with open(in_file, "r") as infile:
        entries = json.load(infile)    
    
    # parse the set of entries => intances
    tools = biotoolsToolsGenerator(entries).instances 
    return(tools)


def asses_quality(toos):
    # do the assesment of the set of intances
    # compute scores
    return


infile = "topic_3510.json"
l = parse_biotools_metadata(infile)
print(l[0].__dict__)