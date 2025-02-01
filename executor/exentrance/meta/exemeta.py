class ExeMeta:
    def __init__(self, name, builtunitdirstr, dyres, stres, dylogs, stdumps, fileper=None):
        content = f"<<<{name}>>>\n\n"
        content += f"----- Contructed pre directory: -----\n{builtunitdirstr}----- End pre directory -----\n\n\n"
        if fileper != None:
            content += f"----- Change permission: {fileper.to_str()}-----\n\n\n"
        content += f"----- Check dynamic info: {dyres}-----\n"
        content += ('\n\n\n'.join(dylogs))
        content += f"\n\n\n----- Check static info: {stres}-----\n"
        content += ('\n\n'.join(stdumps))
        self.name = name
        self.content = content

    def build():
        pass



