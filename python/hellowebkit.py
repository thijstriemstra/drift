#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
# Copyright (c) Collab.
# See LICENSE.txt for details.

import sys

from PySide.QtCore import QUrl
from PySide.QtGui import QApplication
from PySide.QtWebKit import QWebView


app = QApplication(sys.argv)

web = QWebView()
web.load(QUrl("http://collab.com"))
web.show()

sys.exit(app.exec_())
