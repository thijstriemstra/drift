#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
# Copyright (c) Collab.
# See LICENSE.txt for details.

import sys, os

from PySide.QtCore import QUrl, QSize
from PySide.QtGui import QApplication
from PySide.QtWebKit import QWebView, QWebSettings, QWebPage

os.environ['GDK_NATIVE_WINDOWS']='0'

app = QApplication(sys.argv)

settings = QWebSettings.globalSettings()
settings.setAttribute(QWebSettings.DnsPrefetchEnabled, True)
settings.setAttribute(QWebSettings.JavascriptEnabled, True)
settings.setAttribute(QWebSettings.PluginsEnabled, True)
settings.setAttribute(QWebSettings.AutoLoadImages, True)
settings.setAttribute(QWebSettings.PrivateBrowsingEnabled, False)
settings.setAttribute(QWebSettings.LinksIncludedInFocusChain, True)
settings.setFontSize(QWebSettings.DefaultFontSize, 16)
settings.setFontSize(QWebSettings.DefaultFixedFontSize, 16)

page = QWebPage()
page.setViewportSize(QSize(800, 600))

web = QWebView()
web.setPage(page)
web.load(QUrl("http://collab.com"))
web.show()
web.setFocus()
web.activateWindow()

sys.exit(app.exec_())
