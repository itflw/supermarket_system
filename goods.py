class good(object):
    __gid = 0
    __gname = ""
    __gprice = ""
    __gnum = 0

    def set_gid(self, gid):
        self.__gid = gid
    
    def get_gid(self):
        return self.__gid

    def set_gname(self, gname):
        self.__gname = gname

    def get_gname(self):
        return self.__gname
    
    def set_gprice(self, gprice):
        self.__gprice = gprice

    def get_gprice(self):
        return self.__gprice

    def set_gnum(self, gnum):
        self.__gnum = gnum
    
    def get_gnum(self):
        return self.__gnum    