# -*- coding: UTF-8 -*-
#
# Copyright © 2003 - 2015 Michal Čihař <michal@cihar.com>
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
# generated by wxGlade 0.4.1 on Thu Feb  8 16:46:42 2007
# vim: expandtab sw=4 ts=4 sts=4:
'''
Wammu - Phone manager
Gammu Phone Database Talkback window
'''

import wx
from Wammu.Locales import ugettext as _

# begin wxGlade: dependencies
# end wxGlade

class TalkbackFeaturesDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: TalkbackFeaturesDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.top_label = wx.StaticText(self, -1, _("Select which functionality works without problems on your phone (either in Wammu or in some other tool using Gammu library)."))
        self.top_static_line = wx.StaticLine(self, -1)
        self.feature_info_checkbox = wx.CheckBox(self, -1, _("Phone information"))
        self.feature_sms_checkbox = wx.CheckBox(self, -1, _("Sending and saving SMS"))
        self.feature_mms_checkbox = wx.CheckBox(self, -1, _("Multimedia messaging"))
        self.feature_phonebook_checkbox = wx.CheckBox(self, -1, _("Basic phonebook functions"))
        self.feature_enhancedphonebook_checkbox = wx.CheckBox(self, -1, _("Enhanced phonebook entries"))
        self.feature_calendar_checkbox = wx.CheckBox(self, -1, _("Calendar entries"))
        self.feature_todo_checkbox = wx.CheckBox(self, -1, _("Todos"))
        self.feature_filesystem_checkbox = wx.CheckBox(self, -1, _("Filesystem manipulation"))
        self.feature_call_checkbox = wx.CheckBox(self, -1, _("Reading and making calls"))
        self.feature_logo_checkbox = wx.CheckBox(self, -1, _("Logos"))
        self.feature_ringtone_checkbox = wx.CheckBox(self, -1, _("Ringtones"))
        self.bottom_static_line = wx.StaticLine(self, -1)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        # List of features
        self.__allfeatures = ['info', 'sms', 'mms', 'phonebook', 'enhancedphonebook', 'calendar', 'todo', 'filesystem', 'call', 'logo', 'ringtone']

    def __set_properties(self):
        # begin wxGlade: TalkbackFeaturesDialog.__set_properties
        self.SetTitle(_("Select features"))
        self.feature_phonebook_checkbox.SetToolTipString(_("You can access name and phone number."))
        self.feature_enhancedphonebook_checkbox.SetToolTipString(_("You have access to more phone numbers per entry or additional fields as email."))
        # end wxGlade

    def __do_layout(self):
        self.button_sizer = wx.StdDialogButtonSizer()
        self.button_sizer.AddButton(wx.Button(self, wx.ID_OK))
        self.button_sizer.AddButton(wx.Button(self, wx.ID_CANCEL))
        self.top_label.Wrap(400)
        # begin wxGlade: TalkbackFeaturesDialog.__do_layout
        window_grid_sizer = wx.FlexGridSizer(3, 1, 0, 0)
        features_sizer = wx.BoxSizer(wx.VERTICAL)
        window_grid_sizer.Add(self.top_label, 0, wx.EXPAND, 0)
        window_grid_sizer.Add(self.top_static_line, 0, wx.ALL | wx.EXPAND, 5)
        features_sizer.Add(self.feature_info_checkbox, 0, wx.ADJUST_MINSIZE, 0)
        features_sizer.Add(self.feature_sms_checkbox, 0, wx.ADJUST_MINSIZE, 0)
        features_sizer.Add(self.feature_mms_checkbox, 0, wx.ADJUST_MINSIZE, 0)
        features_sizer.Add(self.feature_phonebook_checkbox, 0, wx.ADJUST_MINSIZE, 0)
        features_sizer.Add(self.feature_enhancedphonebook_checkbox, 0, wx.ADJUST_MINSIZE, 0)
        features_sizer.Add(self.feature_calendar_checkbox, 0, wx.ADJUST_MINSIZE, 0)
        features_sizer.Add(self.feature_todo_checkbox, 0, wx.ADJUST_MINSIZE, 0)
        features_sizer.Add(self.feature_filesystem_checkbox, 0, wx.ADJUST_MINSIZE, 0)
        features_sizer.Add(self.feature_call_checkbox, 0, wx.ADJUST_MINSIZE, 0)
        features_sizer.Add(self.feature_logo_checkbox, 0, wx.ADJUST_MINSIZE, 0)
        features_sizer.Add(self.feature_ringtone_checkbox, 0, wx.ADJUST_MINSIZE, 0)
        window_grid_sizer.Add(features_sizer, 1, wx.EXPAND, 0)
        window_grid_sizer.Add(self.bottom_static_line, 0, wx.ALL | wx.EXPAND, 5)
        self.SetAutoLayout(True)
        self.SetSizer(window_grid_sizer)
        window_grid_sizer.Fit(self)
        window_grid_sizer.SetSizeHints(self)
        window_grid_sizer.AddGrowableRow(1)
        window_grid_sizer.AddGrowableCol(0)
        self.Layout()
        # end wxGlade
        self.button_sizer.Realize()
        window_grid_sizer.Add(self.button_sizer, 0, wx.ALIGN_RIGHT, 0)
        window_grid_sizer.Fit(self)
        self.Layout()

    def GetFeatures(self):
        result = []
        for x in self.__allfeatures:
            if getattr(self, 'feature_%s_checkbox' % x).GetValue():
                result.append(x)
        return result

    def SetFeatures(self, list):
        for x in self.__allfeatures:
            getattr(self, 'feature_%s_checkbox' % x).SetValue(False)
        for x in list:
            getattr(self, 'feature_%s_checkbox' % x).SetValue(True)

# end of class TalkbackFeaturesDialog


