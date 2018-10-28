#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request, url_for, redirect
from flask_bootstrap import Bootstrap
from predefines import host, port, templateFile
from predefines import mpcCommand
import subprocess
import sys, os
import os
import os.path
from luma.oled.device import ssd1306, sh1106
from luma.core.render import canvas
from PIL import ImageFont
from PIL import Image
import graphics
import time, textwrap
from datetime import datetime

app = Flask(__name__,)

@app.route('/', methods=['GET', 'POST']) 


def index (name='Payphone Radio'):
        image = 'BBC' # Just to hold the variable
        if request.method == 'POST':
                image = 'now_playing'
                if request.form['submit'] == 'Radio On':
                        mpcCommand(['mpc', 'play', str('1')])
                        image = 'BBC_Radio_1.png'
                elif request.form['submit'] == 'Radio Off':
                        mpcCommand(['mpc', 'play', str('1')])
                        mpcCommand(['mpc', 'close'])
                        mpcCommand(['mpc', 'stop'])
                        mpcCommand(['mpc', 'close'])
                elif request.form['submit'] == 'BBC Radio 1':
                        mpcCommand(['mpc', 'play', str('1')])
                        image = 'BBC_Radio_1.png'
                        return render_template(templateFile, name=name, image = image)
                elif request.form['submit'] == 'BBC Radio 2':
                        mpcCommand(['mpc', 'play', str('2')])
                        image = 'BBC_Radio_2.png'
                        return render_template(templateFile, name=name, image = image)
                elif request.form['submit'] == 'BBC Radio 3':
                        mpcCommand(['mpc', 'play', str('3')])
                        image = 'BBC_Radio_3.png'
                        return render_template(templateFile, name=name, image = image)
                elif request.form['submit'] == 'BBC Radio 4':
                        mpcCommand(['mpc', 'play', str('4')])
                        image = 'BBC_Radio_4.png'
                elif request.form['submit'] == 'BBC Radio 5':
                        mpcCommand(['mpc', 'play', str('13')])
                        image = 'BBC_Radio_5.png'
                        return render_template(templateFile, name=name, image = image)
                elif request.form['submit'] == 'BBC Radio 6':
                        mpcCommand(['mpc', 'play', str('14')])
                        image = 'BBC_Radio_6.png'
                elif request.form['submit'] == 'BBC World Service':
                        mpcCommand(['mpc', 'play', str('5')])
                        image = 'BBC_World_Service.png'
                elif request.form['submit'] == 'BBC Radio 1Extra':
                        mpcCommand(['mpc', 'play', str('6')])
                        image = 'BBC_Radio_1Extra.png'
                elif request.form['submit'] == 'BBC Radio 4Extra':
                        mpcCommand(['mpc', 'play', str('7')])
                        image = 'BBC_Radio_4Extra.png'
                elif request.form['submit'] == 'Classic FM':
                        mpcCommand(['mpc', 'play', str('15')])
                        image = 'Classic_FM.png'
                elif request.form['submit'] == 'WSHU CT NPR':
                        mpcCommand(['mpc', 'play', str('8')])
                        image = 'WSHU.png'
                elif request.form['submit'] == 'WNYC NYC NPR':
                        mpcCommand(['mpc', 'play', str('9')])
                        image = 'WNYC.png'
                elif request.form['submit'] == '97.9 The Bull':
                        mpcCommand(['mpc', 'play', str('16')])
                        image = 'The_Bull.png'
                elif request.form['submit'] == '98Q Danbury':
                        mpcCommand(['mpc', 'play', str('17')])
                        image = '98Q.png'
                elif request.form['submit'] == 'CBC Radio 1':
                        mpcCommand(['mpc', 'play', str('10')])
                        image = 'CBC_Radio_1.png'
                elif request.form['submit'] == 'CBC Radio 2':
                        mpcCommand(['mpc', 'play', str('11')])
                        image = 'CBC_Radio_2.png'
                elif request.form['submit'] == 'CFRC':
                        mpcCommand(['mpc', 'play', str('12')])
                        image = 'CFRC.png'
              
    
        #Volume = mpcCommand(['mpc', 'volume'])
        return render_template(templateFile, name=name, image = image)

@app.route('/vol_up')
def vol_up():
    #print "Vol Up"
    mpcCommand(['mpc', 'volume', '+5'])
    return "nothing"

@app.route('/vol_down')
def vol_down():
    #print "Vol Down"
    mpcCommand(['mpc', 'volume', '-5'])
    return "nothing"


if __name__ == '__main__': 
    app.run(host=host, port=port, debug=True)
   
