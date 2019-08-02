class Soft:
    name     = None
    cmd      = None
    icon     = None
    generic  = None
    disabled = False

    def __init__(self):
        pass

    def new(self, name, cmd, icon, generic):
        self.name    = name
        self.cmd     = cmd
        self.icon    = icon
        self.generic = generic
    
    def to_dict(self, inc):
        soft_title = 'soft-%s' % inc
        dic = {
            soft_title: {
                'name':    self.name,
                'cmd':     self.cmd
            }
        }
        if self.icon:
            dic[soft_title]['icon']     = self.icon
        if self.generic:
            dic[soft_title]['generic']  = self.generic
        if self.disabled:
            dic[soft_title]['disabled'] = self.disabled
        return dic