# -*- coding: UTF-8 -*-
# vim: expandtab sw=4 ts=4 sts=4:
'''
Wammu - Phone manager
Some static data like bitmaps, category mappings etc.
Many of them might be moved to python-gammu later
'''
__author__ = 'Michal Čihař'
__email__ = 'michal@cihar.com'
__license__ = '''
Copyright © 2003 - 2008 Michal Čihař

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License version 2 as published by
the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License along with
this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
'''

import sys
from gammu.Data import Connections, MemoryValueTypes, CalendarTypes, CalendarValueTypes, TodoPriorities, TodoValueTypes, InternationalPrefixes


# When support for sound will be implemented, here should be sounds
PredefinedSounds = [
        (_('Chimes high'),''),
        (_('Chimes low'),''),
        (_('Ding'),''),
        (_('TaDa'),''),
        (_('Notify'),''),
        (_('Drum'),''),
        (_('Claps'),''),
        (_('Fanfare'),''),
        (_('Chord high'),''),
        (_('Chord low'),''),
        ]

# Wanted somebody who will draw nicer icons :-)

Note = [
    '16 16 2 1',
    'x c Black',
    '  c None',
    '      xx        ',
    '      xxx  xxx  ',
    '      xxxxxxxxx ',
    '      xx  xx  xx',
    '      xx        ',
    '      xx        ',
    '      xx        ',
    '      xx        ',
    '  xxxxxx        ',
    ' xxxxxxx        ',
    'xxxxxxxx        ',
    'xxxxxxxx        ',
    'x  xxxxx        ',
    'x   xxxx        ',
    ' x  xxx         ',
    '  xxxx          ']

UnknownPredefined = [
    '16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '    x      x    ',
    '   x  xxxx  x   ',
    '   x x    x x   ',
    '    x     x x   ',
    '          x x   ',
    '         x x    ',
    '        x x     ',
    '       x x      ',
    '       x x      ',
    '       xx       ',
    '                ',
    '       xx       ',
    '      xxxx      ',
    '      x xx      ',
    '       xx       ']

PredefinedAnimations = [
    (_("I'm ironic, flirty"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x   x      x   x',
    ' x   x    x   x ',
    ' x    x  x    x ',
    '  x    xx    x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("I am glad"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x   x      x   x',
    ' x   x    x   x ',
    ' x    xxxx    x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("I am skeptic"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x   xxxxx      x',
    ' x       x    x ',
    ' x        x   x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("I am sad"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x     xxxx     x',
    ' x   x    x   x ',
    ' x  x      x  x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("WOW"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x     xxxx     x',
    'x    x    x    x',
    ' x   x    x   x ',
    ' x    xxxx    x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("I am crying"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x     x    x   x',
    'x              x',
    'x              x',
    'x     xxxx     x',
    ' x   x    x   x ',
    ' x    xxxx    x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("I am winking"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x       xx   x ',
    'x  xxxx  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x   x      x   x',
    ' x   xxxxxx   x ',
    ' x            x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("I am laughing"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x   x      x   x',
    ' x   xxxxxx   x ',
    ' x    xxxx    x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("I am indifferent"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x              x',
    ' x            x ',
    ' x   xxxxxx   x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("I am in love"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxx xx xx ',
    '   xx    x  x  x',
    '  x       x   x ',
    ' x         x x  ',
    ' x  xx   xx x x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x              x',
    ' x   x    x   x ',
    ' x    xxxx    x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("I am confused"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx xx  ',
    '   xx      x  x ',
    '  x           x ',
    ' x           x  ',
    ' x  xx   xx    x',
    'x   x x  x x x x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x              x',
    ' x   xxxxx    x ',
    ' x            x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("Tongue hanging out"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x              x',
    ' x         x  x ',
    ' x    xxxxx x x ',
    '  x     xx   x  ',
    '   xx     x   x ',
    '     xxxxxxxxx  ']),
    (_("I am angry"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x x        x x ',
    ' x  xx   xxx  x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x     xxxx     x',
    ' x   x    x   x ',
    ' x  x      x  x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("Wearing glases"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    '     xxxxxx     ',
    '   xx      xx   ',
    '  x          x  ',
    ' x            x ',
    'xxxxxxxxxxxxxxxx',
    'x   xxx  xxx   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x              x',
    'x              x',
    ' x  x      x  x ',
    ' x   xxxxxx   x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    (_("Devil"),
    ['16 16 2 1',
    'x c Black',
    '  c None',
    'x    xxxxxx    x',
    'xxxxx      xxxxx',
    ' xx          xx ',
    ' x            x ',
    ' x  xx   xx   x ',
    'x   x x  x x   x',
    'x    xx   xx   x',
    'x              x',
    'x              x',
    'x   xxxxxxxx   x',
    'x   x x  x x   x',
    ' x   x    x   x ',
    ' x    xxxx    x ',
    '  x          x  ',
    '   xx      xx   ',
    '     xxxxxx     ']),
    ]

# First is used as default
Models = [
    'auto',
    'at',
    'alcatel',
    'nauto',
    'obex',
    'seobex',
    ]

Conn_Generic = [
    'at19200',
    'at115200',
    'obex',
    ]
Conn_Cable = [
    'at19200',
    'at115200',
    'fbusdlr3',
    'fbus',
    'mbus',
    'fbuspl2303',
    'phonetblue',
    'fbusblue',
    ]
Conn_IrDA_Win = [
    'irdaphonet',
    'irdaat',
    ]
Conn_IrDA_Other = [
    'irdaphonet',
    'at19200',
    ]
Conn_BlueRF = [
    'at19200',
    ]
Conn_Bluetooth_All = [
    'bluephonet',
    'bluefbus',
    'bluerfgnapbus',
    'blueat',
    'blueobex',
    ]
Conn_Bluetooth_Nokia = [
    'bluephonet',
    'bluefbus',
    'bluerfgnapbus',
    'blueat',
    'blueobex',
    ]
Conn_Bluetooth_Standard = [
    'blueat',
    'blueobex',
    'bluerfgnapbus',
    ]
Conn_Bluetooth = {
    'Sony-Ericsson' : Conn_Bluetooth_Standard,
    'Siemens' : Conn_Bluetooth_Standard,
    'BenQ' : Conn_Bluetooth_Standard,
    'Samsung' : Conn_Bluetooth_Standard,
    'LG' : Conn_Bluetooth_Standard,
    'Motorola' : Conn_Bluetooth_Standard,
    'Nokia' : Conn_Bluetooth_Nokia,
    'Alcatel' : Conn_Bluetooth_Standard,
    }
if sys.platform == 'win32':
    Devices = [
        '',
        'com1:',
        'com2:',
        'com3:',
        'com4:',
        'com5:',
        'com6:',
        ]
    AllDevices = [
        (Conn_IrDA_Win, '', None, ['irda']),
        (Conn_Cable, 'com%d:', (1,6), ['irda', 'usb', 'serial', 'bluetooth']),
        ]
# FIXME: support more platforms?
else:
    Devices = [
        '/dev/ttyS0',
        '/dev/ttyS1',
        '/dev/ttyUSB0',
        '/dev/ttyUSB1',
        '/dev/ttyACM0',
        '/dev/ttyACM1',
        '/dev/ircomm0',
        '/dev/rfcomm0',
        '/dev/usb/tts/0',
        ]
    AllDevices = [
        (Conn_Cable, '/dev/ttyS%d', (0, 3), ['serial']),
        (Conn_Cable, '/dev/ttyUSB%d', (0, 3), ['serial', 'usb']),
        (Conn_Cable, '/dev/ttyACM%d', (0, 3), ['serial', 'usb']),
        (Conn_BlueRF, '/dev/rfrcomm%d', (0, 1), ['bluetooth']),
        (Conn_IrDA_Other, '/dev/ircomm%d', (0, 1), ['irda']),
        (Conn_Cable, '/dev/usb/tts/%d', (0, 3), ['serial', 'usb']),
        ]

ContactMemoryTypes = ['ME', 'SM']

SMSIDs = {
    'Text':                 [
        'Text',
        'ConcatenatedTextLong',
        'ConcatenatedAutoTextLong',
        'ConcatenatedTextLong16bit',
        'ConcatenatedAutoTextLong16bit',
        'NokiaVCARD21Long',
        'NokiaVCALENDAR10Long'
        ],
    'Sound':                [
        'NokiaProfileLong',
        'NokiaRingtone',
        'NokiaRingtoneLong',
        'EMSSound10',
        'EMSSound12',
        'EMSSonyEricssonSound',
        'EMSSound10Long',
        'EMSSound12Long',
        'EMSSonyEricssonSoundLong',
        ],
    'Animation':            [
        'NokiaProfileLong',
        'EMSAnimation',
        'AlcatelMonoAnimationLong',
        'NokiaScreenSaverLong',
        ],
    'File':                 [
        'SiemensFile',
        ],
    'Bitmap':               [
        'NokiaProfileLong',
        'NokiaPictureImageLong',
        'NokiaOperatorLogo',
        'NokiaOperatorLogoLong',
        'NokiaCallerLogo',
        'EMSFixedBitmap',
        'EMSVariableBitmap',
        'EMSVariableBitmapLong',
        'AlcatelMonoBitmapLong',
        'AlcatelSMSTemplateName',
        ],
    'PredefinedAnimation':  [
        'EMSPredefinedAnimation',
        ],
    'PredefinedSound':      [
        'EMSPredefinedSound',
        ],
    }

TextFormats = [
    [(_('Alignment'), _('None')),
        ('Left', _('Left'), '<div align="left">%s</div>'),
        ('Right', _('Right'), '<div align="right">%s</div>'),
        ('Center', _('Center'), '<div align="center">%s</div>'),
        ],
    [(_('Text Size'), _('Normal')),
        ('Large', _('Large'), '<font size="+2">%s</font>'),
        ('Small', _('Small'), '<font size="-2">%s</font>'),
        ],
    ['', ('Bold', _('Bold'), '<b>%s</b>')],
    ['', ('Italic', _('Italic'), '<i>%s</i>')],
    ['', ('Underlined', _('Underlined'), '<u>%s</u>')],
    ['', ('Strikethrough', _('Strikethrough'), '<strike>%s</strike>')],
]

# dump from Gammu Phone Database
ManufacturerMap = {
    'Alcatel': 1,
    'Nokia': 2,
    'Siemens': 3,
    'Sony Ericsson': 4,
    'Sagem': 5,
    'Motorola': 6,
    'Falcom': 7,
    'Samsung': 8,
    'LG': 9,
    'Sharp': 10,
    'Mitsubishi': 11,
    'PalmOne': 12,
    'BenQ-Siemens': 13,
    'Philips': 14,
    'Elson': 15,
    'Toshiba': 16,
    'Option': 17,
    'Onda': 18,
    'Teltonika': 19,
    'HTC': 20,
    'Apple': 21,
    'Huawei': 22,
    'Wavecom': 23,
    'Sierra Wireless': 24,
    'Lenovo': 25,
}
GarbleMap = {
    0: 'atdot',
    1: 'nospam',
    2: 'none',
    3: 'hide',
}

# Generated from http://standards.ieee.org/regauth/oui/oui.txt
MAC_Prefixes = {
        'Sony-Ericsson' : [
            '00:01:EC',
            '00:0A:D9',
            '00:0E:07',
            '00:0F:DE',
            '00:12:EE',
            '00:15:E0',
            '00:16:20',
            '00:16:B8',
            '00:18:13',
            '00:19:63',
            '00:1A:75',
            '00:1B:59',
            '00:1C:A4',
            '00:1D:28',
            '00:1E:45',
            '00:80:37',
            ],
        'Nokia' : [
            '00:02:EE',
            '00:0B:E1',
            '00:0E:ED',
            '00:0F:BB',
            '00:10:B3',
            '00:11:9F',
            '00:12:62',
            '00:13:70',
            '00:13:FD',
            '00:14:A7',
            '00:15:2A',
            '00:15:A0',
            '00:15:DE',
            '00:16:4E',
            '00:16:BC',
            '00:17:4B',
            '00:17:B0',
            '00:18:0F',
            '00:18:42',
            '00:18:8D',
            '00:18:C5',
            '00:19:2D',
            '00:19:4F',
            '00:19:79',
            '00:19:B7',
            '00:1A:16',
            '00:1A:89',
            '00:1A:DC',
            '00:1B:33',
            '00:1B:AF',
            '00:1B:EE',
            '00:1C:35',
            '00:1C:9A',
            '00:1C:D4',
            '00:1C:D6',
            '00:1D:3B',
            '00:1D:6E',
            '00:1D:98',
            '00:1D:E9',
            '00:1D:FD',
            '00:1E:3A',
            '00:1E:3B',
            '00:1E:A3',
            '00:1E:A4',
            '00:40:43',
            '00:A0:8E',
            '00:E0:03',
            ],
        'Siemens' : [
            '00:01:E3',
            '00:05:19',
            '00:0B:23',
            '00:0B:A3',
            '00:0D:41',
            '00:0E:8C',
            '00:0F:BB',
            '00:11:06',
            '00:11:33',
            '00:13:A3',
            '00:18:D1',
            '00:19:28',
            '00:19:99',
            '00:1A:D0',
            '00:1A:E8',
            '00:1B:1B',
            '00:1C:06',
            '00:30:05',
            '00:50:07',
            '00:90:40',
            '00:C0:E4',
            '08:00:06',
            ],
        'Samsung' : [
            '00:00:F0',
            '00:02:78',
            '00:09:18',
            '00:0D:AE',
            '00:0D:E5',
            '00:0F:73',
            '00:12:47',
            '00:12:FB',
            '00:13:77',
            '00:15:99',
            '00:15:B9',
            '00:16:32',
            '00:16:6B',
            '00:16:6C',
            '00:16:DB',
            '00:17:C9',
            '00:17:D5',
            '00:18:AF',
            '00:1A:8A',
            '00:1B:98',
            '00:1C:43',
            '00:1D:25',
            '00:1D:F6',
            '00:1E:7D',
            '00:E0:64',
            ],
        'LG' : [
            '00:05:C9',
            '00:0B:29',
            '00:12:56',
            '00:14:80',
            '00:19:A1',
            '00:1C:62',
            '00:1E:75',
            '00:1E:B2',
            '00:50:CE',
            '00:E0:91',
            ],
        'BenQ' : [
            '00:03:9D',
            '00:17:CA',
            ],
        'Motorola' : [
            '00:01:AF',
            '00:04:56',
            '00:04:BD',
            '00:08:0E',
            '00:0A:28',
            '00:0B:06',
            '00:0C:E5',
            '00:0E:5C',
            '00:0E:C7',
            '00:0F:9F',
            '00:11:1A',
            '00:11:80',
            '00:11:AE',
            '00:12:25',
            '00:12:8A',
            '00:12:C9',
            '00:13:71',
            '00:14:04',
            '00:14:9A',
            '00:14:E8',
            '00:15:2F',
            '00:15:9A',
            '00:15:A8',
            '00:16:26',
            '00:16:75',
            '00:16:B5',
            '00:17:00',
            '00:17:84',
            '00:17:E2',
            '00:17:EE',
            '00:18:A4',
            '00:18:C0',
            '00:19:2C',
            '00:19:5E',
            '00:19:A6',
            '00:19:C0',
            '00:1A:1B',
            '00:1A:66',
            '00:1A:77',
            '00:1A:AD',
            '00:1A:DB',
            '00:1A:DE',
            '00:1B:52',
            '00:1B:DD',
            '00:1C:11',
            '00:1C:12',
            '00:1C:C1',
            '00:1C:FB',
            '00:1D:6B',
            '00:1D:BE',
            '00:1E:46',
            '00:1E:5A',
            '00:1E:8D',
            '00:20:40',
            '00:20:75',
            '00:A0:BF',
            '00:C0:F9',
            '00:E0:0C',
            ],
        'Alcatel' : [
            '00:07:72',
            '00:08:9A',
            '00:0E:86',
            '00:0F:62',
            '00:11:3F',
            '00:11:8B',
            '00:15:3F',
            '00:16:4D',
            '00:17:CC',
            '00:19:8F',
            '00:1A:F0',
            '00:1C:8E',
            '00:1D:4C',
            '00:20:32',
            '00:20:60',
            '00:20:DA',
            '00:80:21',
            '00:80:39',
            '00:80:9F',
            '00:A0:81',
            '00:C0:BE',
            '00:D0:95',
            '00:D0:F6',
            '00:E0:B1',
            '00:E0:DA',
            ],
        }

