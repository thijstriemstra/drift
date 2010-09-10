#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
# Copyright (c) Collab.
# See LICENSE.txt for details.

import sys

from PySide.QtCore import QUrl, QSize
from PySide.QtGui import QApplication
from PySide.QtWebKit import QWebView, QWebSettings

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

web = QWebView()
web.load(QUrl("http://collab.com"))
web.show()

sys.exit(app.exec_())
