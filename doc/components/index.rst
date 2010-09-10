==========
Components
==========

This is a list of software dependencies, compiled and tested on OS X `10.5.8`_ and `10.6.4`_.


Runtimes
--------

+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Name                    | Description                 | App Version    | System Version(s) | License                 | Dependencies                     |
+=========================+=============================+================+===================+=========================+==================================+
| CPython_                | General-purpose high-level  | 2.7.0          | 2.6.1, 2.5.4      | PSF_                    | N/A                              |
|                         | programming language whose  |                |                   |                         |                                  |
|                         | design philosophy           |                |                   |                         |                                  |
|                         | emphasizes code readability.|                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Java_                   | Programming language that   | N/A            | 1.6.0_20          | `GPL 3.0`_              | N/A                              |
|                         | derives much of its syntax  |                |                   |                         |                                  |
|                         | from C and C++ but has a    |                |                   |                         |                                  |
|                         | simpler object model and    |                |                   |                         |                                  |
|                         | fewer low-level facilities. |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| `Flash Player`_         | Widely distributed          | N/A            | ?                 | `Flash Player EULA`_    | N/A                              |
|                         | proprietary multimedia and  |                |                   |                         |                                  |
|                         | application player.         |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+




User Interface
--------------

+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Name                    | Description                 | App Version    | System Version(s) | License                 | Dependencies                     |
+=========================+=============================+================+===================+=========================+==================================+
| Qt_                     | Cross-platform application  | 4.7.0          | N/A               | `LGPL 2.1`_             | N/A                              |
|                         | and UI framework.		|                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Pylons_                 | Lightweight web framework   | 1.0            | N/A               | BSD_                    | Genshi_, Routes_, WebHelpers_,   |
|                         | emphasizing flexibility and |                |                   |                         | Beaker_, Paste_, PasteDeploy_,   |
|                         | rapid development.          |                |                   |                         | PasteScript_, FormEncode_,       |
|                         |                             |                |                   |                         | simplejson_, decorator, nose_,   |
|                         |                             |                |                   |                         | WebOb_, WebError_, SQLAlchemy_,  |
|                         |                             |                |                   |                         | WebTest_, Tempita_, MarkupSafe_, |
|                         |                             |                |                   |                         | `repoze.bfg`_, Babel_, CPython_  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Genshi_                 | Provides an integrated set  | 0.6            | N/A               | BSD_                    | CPython_                         |
|                         | of components for parsing,  |                |                   |                         |                                  |
|                         | generating, and processing  |                |                   |                         |                                  |
|                         | HTML, XML or other textual  |                |                   |                         |                                  |
|                         | content for output          |                |                   |                         |                                  |
|                         | generation on the web.      |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| WebHelpers_             | Standard function library   | 1.2            | N/A               | BSD_                    |  CPython_, MarkupSafe_           |
|                         | for Pylons_.                |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| MarkupSafe_             | Implements a XML/HTML/XHTML | 0.10           | N/A               | BSD_                    | CPython_                         |
|                         | Markup safe string for      |                |                   |                         |                                  |
|                         | Python.                     |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| FormEncode_             | HTML validation and form    | 1.2.3          | N/A               | PSF_                    | CPython_                         |
|                         | generation package.         |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Beaker_                 | Library for caching and     | 1.5.4          | N/A               | BSD_                    | CPython_                         |
|                         | sessions in web and         |                |                   |                         |                                  |
|                         | stand-alone Python          |                |                   |                         |                                  |
|                         | scripts and applications.   |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Routes_                 | Python URL recognition and  | 1.12.3         | N/A               | BSD_                    | CPython_                         |
|                         | generation system similar to|                |                   |                         |                                  |
|                         | the Rails routing system.   |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Paste_                  | Tools for using a Web Server| ?              | N/A               | MIT_                    | CPython_                         |
|                         | Gateway Interface stack.    |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| PasteDeploy_            | Load, configure, and compose| 1.3.4          | N/A               | MIT_                    | CPython_                         |
|                         | WSGI applications/servers.  |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| PasteScript_            | Tools for managing Paste_,  | 1.7.4          | N/A               | MIT_                    | CPython_                         |
|                         | Pylons_, and other packages.|                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| `zope.interface`_       | Provides an implementation  | ?              | ?                 | `ZPL 2.1`_              | CPython_                         |
|                         | of object interfaces for    |                |                   |                         |                                  |
|                         | Python.                     |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Babel_                  | Collection of tools for     | 0.9.5          | N/A               | BSD_                    | CPython_                         |
|                         | internationalizing Python   |                |                   |                         |                                  |
|                         | applications.               |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+


Database
--------

+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Name                    | Description                 | App Version    | System Version(s) | License                 | Dependencies                     |
+=========================+=============================+================+===================+=========================+==================================+
| SQLAlchemy_             | SQL toolkit and Object      | 0.6.3          | N/A               | MIT_                    | CPython_                         |
|                         | Relational Mapper.          |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+


Security
--------

+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Name                    | Description                 | App Version    | System Version(s) | License                 | Dependencies                     |
+=========================+=============================+================+===================+=========================+==================================+
| `repoze.what`_          | Authorization framework for | 0.6            | N/A               | BSD_                    | CPython_ , Paste_, `repoze.who`_ |
|                         | WSGI applications.          |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| `repoze.who`_           | Identification and          | 0.6            | N/A               | BSD_                    | CPython_, Paste_,                |
|                         | authentication framework for|                |                   |                         | `zope.interface`_                |
|                         | arbitrary WSGI applications.|                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+


Networking
----------

+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Name                    | Description                 | App Version    | System Version(s) | License                 | Dependencies                     |
+=========================+=============================+================+===================+=========================+==================================+
| PyAMF_                  | Provides Action Message     | 0.6            | N/A               | MIT_                    | CPython_, SQLAlchemy_            |
|                         | Format (AMF) support for    |                |                   |                         |                                  |
|                         | Python that is compatible   |                |                   |                         |                                  |
|                         | with the `Flash Player`_.   |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| RTMPy_                  | Provides Real-time Messaging| 0.1            | N/A               | MIT_                    | CPython_, PyAMF_, Twisted_       |
|                         | Protocol (RTMP) support for |                |                   |                         |                                  |
|                         | Python that is compatible   |                |                   |                         |                                  |
|                         | with the `Flash Player`_.   |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| WebOb_                  | Provides objects for HTTP   | 0.9.8          | N/A               | MIT_                    | CPython_                         |
|                         | requests and responses.     |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Twisted_                | Event-driven networking     | 10.1.0         | ?                 | MIT_                    | CPython_, `zope.interface`_      |
|                         | engine written in Python.   |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+


Bindings
--------

+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Name                    | Description                 | App Version    | System Version(s) | License                 | Dependencies                     |
+=========================+=============================+================+===================+=========================+==================================+
| PySide_                 | Python bindings for the     | 0.4.1          | N/A               | `LGPL 2.1`_             | CPython_, Qt_                    |
|                         | Qt_ framework.              |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+


Deployment
----------

+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Name                    | Description                 | Version        | System Version(s) | License                 | Dependencies                     |
+=========================+=============================+================+===================+=========================+==================================+
| py2app_                 | Allows you to make          | 0.5.2          | ?                 | `MIT`_                  | CPython_, macholib_,             |
|                         | standalone Mac OS X         |                |                   |                         | modulegraph_                     |
|                         | application bundles and     |                |                   |                         |                                  |
|                         | plugins from Python scripts.|                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| macholib_               | Used to analyze and edit    | 1.3.0          | ?                 | `MIT`_                  | CPython_                         |
|                         | Mach-O headers, the         |                |                   |                         |                                  |
|                         | executable format used by   |                |                   |                         |                                  |
|                         | Mac OS X.                   |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| modulegraph_            | Determines a dependency     | 0.8.1          | ?                 |`MIT`_                   | CPython_, altgraph_              |
|                         | graph between Python modules|                |                   |                         |                                  |
|                         | primarily by bytecode       |                |                   |                         |                                  |
|                         | analysis for import         |                |                   |                         |                                  |
|                         | statements.                 |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| altgraph_               | Python graph (network)      | 0.7.1          | ?                 |`MIT`_                   | CPython_                         |
|                         | package.                    |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+


References
----------

- https://bugs.webkit.org/buglist.cgi?short_desc_type=allwordssubstr&short_desc=&product=WebKit&component=Plug-ins&long_desc_type=allwordssubstr&long_desc=&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&field0-0-0=assigned_to&type0-0-0=notequals&value0-0-0=webkit-unassigned@lists.webkit.org&field0-0-1=keywords&type0-0-1=anywords&value0-0-1=QtTriaged&keywords_type=allwords&keywords=Qt&order=Importance
- http://ubuntuforums.org/showthread.php?t=1316071
- http://lists.openbossa.org/pipermail/pyside/2010-September/001005.html
- http://blog.forwardbias.in/2009/12/flash-in-qgraphicsview.html
- http://trac.webkit.org/wiki/QtWebKitPlugins
- http://qt.nokia.com/developer/changes
- http://code.google.com/p/arora



.. _10.6.4: 			http://www.opensource.apple.com/release/mac-os-x-1064/
.. _10.5.8:			http://www.opensource.apple.com/release/mac-os-x-1058/
.. _CPython:			http://python.org
.. _Java:			http://java.sun.com
.. _PyAMF:			http://pyamf.org
.. _RTMPy:			http://rtmpy.org
.. _Pylons:			http://pylonshq.com
.. _SQLAlchemy:			http://www.sqlalchemy.org
.. _Genshi:			http://genshi.edgewall.org
.. _Routes:			http://routes.groovie.org
.. _WebHelpers:			http://webhelpers.groovie.org
.. _Beaker:			http://beaker.groovie.org
.. _Paste:			http://pythonpaste.org
.. _PasteDeploy:		http://pythonpaste.org/deploy
.. _PasteScript:		http://pythonpaste.org/script
.. _WebOb:			http://pythonpaste.org/webob
.. _zope.interface:		http://pypi.python.org/pypi/zope.interface
.. _FormEncode:			http://formencode.org
.. _simplejson:			http://code.google.com/p/simplejson
.. _nose:			http://code.google.com/p/python-nose
.. _Mako:			http://www.makotemplates.org
.. _WebError:			http://pypi.python.org/pypi/WebError
.. _WebTest:			http://pythonpaste.org/webtest
.. _Tempita:			http://pythonpaste.org/tempita
.. _MarkupSafe:			http://pypi.python.org/pypi/MarkupSafe
.. _repoze.bfg:			http://bfg.repoze.org
.. _repoze.bfg.mako:		http://pypi.python.org/pypi/repoze.bfg.mako
.. _repoze.what:		http://what.repoze.org
.. _repoze.who:			http://docs.repoze.org/who
.. _Twisted:			http://twistedmatrix.com
.. _py2app:			http://pypi.python.org/pypi/py2app
.. _macholib:			http://bitbucket.org/ronaldoussoren/macholib
.. _modulegraph:		http://bitbucket.org/ronaldoussoren/modulegraph
.. _altgraph:			http://bitbucket.org/ronaldoussoren/altgraph
.. _Babel:			http://babel.edgewall.org
.. _Qt:				http://qt.nokia.com
.. _PySide:			http://www.pyside.org
.. _Flash Player:		http://adobe.com/products/flashplayer
.. _Flash Player EULA:		http://www.adobe.com/products/eulas/pdfs/PlatformClients_PC_WWEULA_Combined_20100108_1657.pdf
.. _LGPL 2.1:			http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html
.. _LGPL 3.0:			http://www.gnu.org/licenses/lgpl.html
.. _MPL 1.1:			http://www.mozilla.org/MPL/MPL-1.1.txt
.. _GPL 2.0:			http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
.. _GPL 3.0:			http://www.gnu.org/licenses/gpl-3.0.html
.. _MIT:			http://www.opensource.org/licenses/mit-license.php
.. _BSD:			http://www.opensource.org/licenses/bsd-license.php
.. _PSF:			http://www.python.org/psf/license
.. _ZPL 2.1:			http://www.zope.org/Resources/ZPL
