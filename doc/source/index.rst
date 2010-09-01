.. toctree::
   :maxdepth: 2
   
========
Welcome!
========

This is the documentation for the **Drift** project.

Source
------

The source code and documentation is hosted at Github: http://github.com/collab-project/drift.


Dependencies
------------

Tested on `OS X 10.6.4`_.

Qt
--

+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Name                    | Description                 | App Version    | System Version(s) | License                 | Dependencies                     |
+=========================+=============================+================+===================+=========================+==================================+
| Qt_                     | Cross-platform application  | 4.6.0          | N/A               | `LGPL 2.1`_             | N/A                              |
|                         | and UI framework.		|                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+

Runtimes
--------

+-------------------------+-----------------------------+----------------+-------------------+-------------------------+
| Name                    | Description                 | App Version    | System Version(s) | License                 |
+=========================+=============================+================+===================+=========================+
| CPython_                | General-purpose high-level  | 2.7.0          | 2.6.1, 2.5.4      | PSF_                    |
|                         | programming language whose  |                |                   |                         |
|                         | design philosophy           |                |                   |                         |
|                         | emphasizes code readability.|                |                   |                         |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+
| Java_                   | Programming language that   | N/A            | 1.6.0_20          | `GPL 3.0`_              |
|                         | derives much of its syntax  |                |                   |                         |
|                         | from C and C++ but has a    |                |                   |                         |
|                         | simpler object model and    |                |                   |                         |
|                         | fewer low-level facilities. |                |                   |                         |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+
| `Flash Player`_         | Widely distributed          | N/A            | ?                 | `Flash Player EULA`_    |
|                         | proprietary multimedia and  |                |                   |                         |
|                         | application player.         |                |                   |                         |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+

Python
------

+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Name                    | Description                 | App Version    | System Version(s) | License                 | Dependencies                     |
+=========================+=============================+================+===================+=========================+==================================+
| PyAMF_                  | Provides Action Message     | 0.6            | N/A               | MIT_                    | SQLAlchemy_                      |
|                         | Format (AMF) support for    |                |                   |                         |                                  |
|                         | Python that is compatible   |                |                   |                         |                                  |
|                         | with the `Flash Player`_.   |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Pylons_                 | Lightweight web framework   | 1.0            | N/A               | BSD_                    | Genshi_, Routes_, WebHelpers_,   |
|                         | emphasizing flexibility and |                |                   |                         | Beaker_, Paste_, PasteDeploy_,   |
|                         | rapid development.          |                |                   |                         | PasteScript, FormEncode_,        |
|                         |                             |                |                   |                         | simplejson_, decorator, nose_,   |
|                         |                             |                |                   |                         | Mako_, WebOb_, WebError_,        |
|                         |                             |                |                   |                         | WebTest_, Tempita_, MarkupSafe_, |
|                         |                             |                |                   |                         | `repoze.bfg.mako`_, SQLAlchemy_, |
|                         |                             |                |                   |                         | `repoze.bfg`_                    |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| SQLAlchemy_             | SQL toolkit and Object      | 0.6.3          | N/A               | MIT_                    |                                  |
|                         | Relational Mapper.          |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Genshi_                 | Provides an integrated set  | 0.6            | N/A               | BSD_                    |                                  |
|                         | of components for parsing,  |                |                   |                         |                                  |
|                         | generating, and processing  |                |                   |                         |                                  |
|                         | HTML, XML or other textual  |                |                   |                         |                                  |
|                         | content for output          |                |                   |                         |                                  |
|                         | generation on the web.      |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| `repoze.what`_          | Authorization framework for | 0.6            | N/A               | BSD_                    |                                  |
|                         | WSGI applications.          |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Babel_                  | Collection of tools for     | 0.9.5          | N/A               | BSD_                    |                                  |
|                         | internationalizing Python   |                |                   |                         |                                  |
|                         | applications.               |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| PySide_                 | CPython_ bindings for the   | 0.4.1          | N/A               | `LGPL 2.1`_             |                                  |
|                         | Qt_ framework.              |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+


References
----------

- http://osdir.com/ml/pyjamas-dev/2010-03/msg00066.html
- http://www.apple.com/opensource/


.. _OS X 10.6.4: 		http://www.opensource.apple.com/release/mac-os-x-1064/
.. _CPython:			http://python.org
.. _Java:			http://java.sun.com
.. _PyAMF:			http://pyamf.org
.. _Pylons:			http://pylonshq.com
.. _SQLAlchemy:			http://sqlachemy.org
.. _Genshi:			http://genshi.edgewall.org
.. _Routes:			http://routes.groovie.org
.. _WebHelpers:			http://webhelpers.groovie.org
.. _Beaker:			http://beaker.groovie.org
.. _Paste:			http://pythonpaste.org
.. _PasteDeploy:		http://pythonpaste.org/deploy
.. _PasteScript:		http://pythonpaste.org/script
.. _WebOb:			http://pythonpaste.org/webob
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
.. _PSF:			http://www.python.org/psf/license/
