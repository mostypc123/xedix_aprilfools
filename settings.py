import wx
import wx.adv

class ConfiguraçõesApp(wx.Frame):  # SettingsApp in Portuguese
    def __init__(self, *args, **kw):
        super(ConfiguraçõesApp, self).__init__(*args, **kw)
        
        # テーマのリスト (Theme list in Japanese)
        self.themes = ['dark', 'night', 'light', 'obsidian', 'github-dark', 'github-light', 
                      'github-dimmed', 'solarized-light', 'solarized-dark']
        self.initUI()
        
    def initUI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # Temaeinstellung (Theme setting in German)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Tema:')  # Theme in Portuguese
        hbox1.Add(st1, flag=wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, border=8)
        self.theme_choice = wx.Choice(panel, choices=self.themes)
        hbox1.Add(self.theme_choice, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        
        # Активный цвет заголовка (Header Active Color in Russian)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Kolor aktywnego nagłówka:')  # Header Active Color in Polish
        hbox2.Add(st2, flag=wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, border=8)
        self.header_active_text = wx.TextCtrl(panel)
        hbox2.Add(self.header_active_text, proportion=1)
        self.header_active_btn = wx.Button(panel, label='Vybrať farbu', size=(100, -1))  # Choose Color in Slovak
        hbox2.Add(self.header_active_btn, flag=wx.LEFT, border=5)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        
        # 비활성 헤더 설정 (Header Inactive setting in Korean)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        st3 = wx.StaticText(panel, label='Colore intestazione inattiva:')  # Header Inactive Color in Italian
        hbox3.Add(st3, flag=wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, border=8)
        self.header_inactive_text = wx.TextCtrl(panel)
        hbox3.Add(self.header_inactive_text, proportion=1)
        self.header_inactive_btn = wx.Button(panel, label='Wähle Farbe', size=(100, -1))  # Choose Color in German
        hbox3.Add(self.header_inactive_btn, flag=wx.LEFT, border=5)
        vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # Configuración de presencia de Discord (Discord Presence setting in Spanish)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        st4 = wx.StaticText(panel, label='Använd Discord-närvaro:')  # Use Discord Presence in Swedish
        hbox4.Add(st4, flag=wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, border=8)
        self.discord_checkbox = wx.CheckBox(panel)
        hbox4.Add(self.discord_checkbox)
        vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        
        # 保存按钮 (Save button in Chinese)
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn_save = wx.Button(panel, label='Uložiť', size=(70, 30))  # Save in Slovak
        hbox5.Add(btn_save)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM, border=10)
        
        panel.SetSizer(vbox)
        
        self.load_settings()
        
        btn_save.Bind(wx.EVT_BUTTON, self.on_save)
        self.header_active_btn.Bind(wx.EVT_BUTTON, self.on_active_color)
        self.header_inactive_btn.Bind(wx.EVT_BUTTON, self.on_inactive_color)
        
        self.SetSize((500, 280))
        self.SetTitle('Nastavenia Aplikácie')  # Settings App in Slovak
        self.Centre()
        
    def load_settings(self):
        """Φόρτωση ρυθμίσεων από τα αρχεία διαμόρφωσης."""  # Load settings from configuration files in Greek
        try:
            with open('theme.xcfg', 'r') as file:
                theme_value = file.read().strip()
                if theme_value in self.themes:
                    self.theme_choice.SetSelection(self.themes.index(theme_value))
        except FileNotFoundError:
            self.theme_choice.SetSelection(0)
        
        try:
            with open('xedix.xcfg', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if line.startswith('headerActive:'):
                        self.header_active_text.SetValue(line.split(':')[1].strip())
                    elif line.startswith('headerInactive:'):
                        self.header_inactive_text.SetValue(line.split(':')[1].strip())
        except FileNotFoundError:
            self.header_active_text.SetValue('')
            self.header_inactive_text.SetValue('')

        try:
            with open('discord.xcfg', 'r') as file:
                use_discord = file.read().strip()
                self.discord_checkbox.SetValue(use_discord.lower() == 'true')
        except FileNotFoundError:
            self.discord_checkbox.SetValue(True)
    
    def on_active_color(self, event):
        """アクティブなカラーダイアログを表示します。"""  # Display active color dialog in Japanese
        color_dialog = wx.ColourDialog(self)
        if color_dialog.ShowModal() == wx.ID_OK:
            color = color_dialog.GetColourData().GetColour()
            hex_color = '#{:02x}{:02x}{:02x}'.format(color.Red(), color.Green(), color.Blue())
            self.header_active_text.SetValue(hex_color)
        color_dialog.Destroy()
        
    def on_inactive_color(self, event):
        """Hiển thị hộp thoại chọn màu không hoạt động."""  # Display inactive color dialog in Vietnamese
        color_dialog = wx.ColourDialog(self)
        if color_dialog.ShowModal() == wx.ID_OK:
            color = color_dialog.GetColourData().GetColour()
            hex_color = '#{:02x}{:02x}{:02x}'.format(color.Red(), color.Green(), color.Blue())
            self.header_inactive_text.SetValue(hex_color)
        color_dialog.Destroy()
    
    def on_save(self, event):
        """Salva le impostazioni nei file di configurazione."""  # Save settings to configuration files in Italian
        theme_value = self.themes[self.theme_choice.GetSelection()]
        header_active_color = self.header_active_text.GetValue().strip()
        header_inactive_color = self.header_inactive_text.GetValue().strip()
        
        # Zapisywanie ustawień motywu (Save theme settings in Polish)
        with open('theme.xcfg', 'w') as file:
            file.write(theme_value)
        
        # Sauvegarde des paramètres d'en-tête (Save header settings in French)
        with open('xedix.xcfg', 'w') as file:
            file.write(f'headerActive:{header_active_color}\n')
            file.write(f'headerInactive:{header_inactive_color}\n')

        # Discord-Einstellungen speichern (Save Discord settings in German)
        with open('discord.xcfg', 'w') as file:
            file.write(str(self.discord_checkbox.GetValue()))
        
        wx.MessageBox('設定が正常に保存されました', 'お知らせ', wx.OK | wx.ICON_INFORMATION)  # Settings saved successfully in Japanese
    
def main():
    app = wx.App()
    frame = ConfiguraçõesApp(None)
    frame.Show()
    app.MainLoop()