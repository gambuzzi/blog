#/bin/env python
# -*- coding: UTF-8 -*-
# 
# (c) 2011 Roberto Gambuzzi
# Creato:          16/03/2011 23.20.35
# Ultima Modifica: 22/03/2011 12.25.16
# 
# v 0.0.1.1
# 
# file: "prove anoto penna.py"
# auth: Roberto Gambuzzi <gambuzzi@gmail.com>
# desc: 
# 
# $Id: "prove anoto penna.py" 22/03/2011 12.25.16 roberto $
# --------------
"""
This program simply extract all available information in a pgc file.

Copyright (C) 2011 Roberto Gambuzzi

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from win32com.client import constants, Dispatch  
from glob import glob
import os

fileI = Dispatch("AnotoUtil.File") 
pr = Dispatch("Anoto.ServiceAPI.PenRequest")
penID = Dispatch("AnotoUtil.PenID")

def little(n, cifre=8):
    if type(n) == str:
        ret = 0 
        while n:
            ret *= 256
            ret += ord(n[0])
            n = n[1:]
    else:
        ret = ''
        while n or cifre:
            ret = chr(n % 256) + ret
            n /= 256
            if cifre:
                cifre -= 1
    return ret

for f in glob(r'*.pgc'):
    bin = fileI.Read(f)     
    pr.Initialize(bin)    
    print 'penna ', pr.PenId
    print 'pagine',pr.Pages.Count
    for page in pr.Pages:
        print page.PageAddress
        print page.AttributeList
        for k in page.AttributeList:
            print k,page.GetAttribute(k) 
        bound = page.Bounds
        print bound.Left
        print bound.Top
        print bound.Right
        print bound.Bottom
        print bound.Height
        print bound.Width
        print page.HasPenStrokes        
        for area in page.PageAreas:
            print area.Name, area.Type, area.AttributeList, 
            for k in area.AttributeList:
                print k,'-->',page.GetAttribute(k), 
            print area.HasPenStrokes
        for penStroke in page.PenStrokes:
            print "Colore %08X" % penStroke.Color
            print "DeltaTime",penStroke.DeltaTime
            print "Duration",penStroke.Duration
            print "Force",[ord(x) for x in penStroke.Force]
            print "LineWidth",penStroke.LineWidth
            print "StartMillisecond",penStroke.StartMillisecond
            print "StartSecond",penStroke.StartSecond
            print "X",penStroke.X
            print "Y",penStroke.Y 
            
        print page.UsesDefaultPAD
        