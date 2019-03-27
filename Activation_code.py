import wx
from random import choice

choose_dict = {'一级': ['一级office', 'ps', 'wps'],
               '二级': ['java', 'access', "c++", "二级office", "c", "vb", "MySQL"],
               "三级": ['信息技术', '嵌入', '数据库']}
activationcode_dice = {
    '一级office': ['MSY876843541', 'MSY654654135', 'MSY788974684', 'MSY758465464', 'MSY324254546', 'MSY879879875',
                 'MSY798746854'], 'ps': ['PS5646463546', 'PS6865465462'], 'wps': ['WP8668465465', 'WP5674645646'],

    'java': ['JA587435435', 'JA686866846', 'JA698746245', 'JA657465452', 'JA547684684'],
    'access': ['AC657498546', 'AC687984684', 'AC867964865', 'AC574987464', 'AC687984645'],
    "c++": ['MC879846543', 'MC579846854', 'MC587986465', 'MC544758764', 'MC587968465'],
    "二级office": ['MSB54654351321', 'MSB58765846546', 'MSB68754545132', 'MSB56786942534', 'MSB98754621354',
                 'MSB87984684634', 'MSB87984646613', 'MSB68984641313', 'MSB78987984334'],
    "c": ['MCB8579846464', 'MCB9876846546', 'MCB8797846543', 'MCB7987464641', 'MCB7846465435', 'MCB6879846546',
          'MCB7959564655'], "vb": ['VB987654654', 'VB879456413', 'VB857943541', 'VB879845645', 'VB798465413'],
    "MySQL": ['SQL2837283921', 'SQL3849302938', 'SQL9382347534'],

    '信息技术': ['SA674654135', 'SA456746846', 'SA324324562', 'SA521432152', 'SA342342314'],
    '嵌入': ['QR679845643', 'QR687684353', 'QR687468465', 'QR879874513', 'QR879465413'],
    '数据库': ['SQ876846546', 'SQ897987464', 'SQ465798746', 'SQ987984656', 'SQ897946541']}


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="激活码生成器", size=(400, 200))
        self.Center()  # 设置窗口居中
        # 放一个面板，用于布局其他控件
        panel = wx.Panel(parent=self)

        # 考试级别初始化
        classbox = wx.BoxSizer(wx.HORIZONTAL)
        # 创建静态文本
        statictext = wx.StaticText(panel, label='考试级别：')
        # 考试级别为字典choose__dict的键名，取出键名，转化为列表
        class_list = list(choose_dict.keys())
        # 初始化下拉菜单1，下拉菜单的选项为列表值
        cb1 = wx.ComboBox(panel, -1, choices=class_list, style=wx.CB_SORT)
        # 将静态文本和下拉菜单cb1加入classbox
        classbox.Add(statictext, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        classbox.Add(cb1, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)

        # 考试科目初始化
        subjectbox = wx.BoxSizer(wx.HORIZONTAL)
        statictext = wx.StaticText(panel, label='考试科目：')
        # 初始化下拉菜单2
        cb2 = wx.ComboBox(panel, -1, style=wx.CB_SORT)
        # 将静态文本和下拉菜单cb2加入subjectbox
        subjectbox.Add(statictext, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        subjectbox.Add(cb2, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)

        # 激活码显示 初始化
        codebox = wx.BoxSizer(wx.HORIZONTAL)
        statictext1 = wx.StaticText(panel, label='激活码：')
        statictext2 = wx.StaticText(panel)
        # 将两个静态文本加入subjectbox
        codebox.Add(statictext1, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        codebox.Add(statictext2, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)

        # 将考试级别、考试科目、激活码 控件添加进 vbox
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(classbox, 1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(subjectbox, 1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(codebox, 1, flag=wx.ALL | wx.EXPAND, border=5)

        # 将vbox控件添加到panel
        panel.SetSizer(vbox)

        # 添加事件处理
        self.Bind(wx.EVT_COMBOBOX, self.OnCb1Clicked, cb1)
        self.Bind(wx.EVT_COMBOBOX, self.OnCb2Clicked, cb2)

        # 成功的关键，对就是这个，解决了问题（在一个函数中用另一个函数的值，就这样弄）
        self.__cb2 = cb2
        self.__statictext2 = statictext2

    def OnCb1Clicked(self, event):
        # print下拉菜单1选择结果
        print("\r\n" + "考试级别选择:{}".format(event.GetString()))
        # 从choose_dict中获取键名为currentclass的键值
        currentclass = event.GetString()
        value = choose_dict.__getitem__(currentclass)
        print(value)
        # 将获取的键值作为下拉菜单2的选项
        self.__cb2.SetItems(list(value))

    def OnCb2Clicked(self, event):
        # 获取下拉菜单2选择值的id
        currentindex = self.__cb2.GetSelection()
        # 根据id找到下拉菜单2的选择值
        currentsubject = self.__cb2.GetItems()[currentindex]
        print("\r\n" + "考试科目选择:{}".format(currentsubject))
        # 下拉菜单2的选择值为acyivation_dict的键名，根据键名找到键值
        for i in activationcode_dice.keys():
            if currentsubject == i:
                subject = activationcode_dice.__getitem__(i)
                print(subject)
                # 用random.chioce函数从键值中随机选择一个作为激活码显示
                self.__statictext2.SetLabel(choice(subject))


# 自定以一个应用程序类
class App(wx.App):
    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print("应用程序退出")
        return 0


if __name__ == '__main__':
    app = App()  # 创建自定以对象App
    app.MainLoop()  # 进入事件主循环
