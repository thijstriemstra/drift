.. toctree::
   :maxdepth: 2
   
========
Welcome!
========

This is the documentation for the **Drift** project.

Code
----

The code is hosted at Github: http://github.com/collab-project/drift.


Dependencies
------------

Drift uses software created by the Open Source community, such as the HTML rendering engine WebKit,
and returns its enhancements to the community.


Mac OS X
--------

Tested on `OS X 10.6.4`_.

GTK+
----

GTK+ is a toolkit for creating graphical user interfaces which boasts cross platform compatibility
and an easy to use API. GTK+ it is written in C, but has bindings to many other popular programming
languages such as C++, Python and C# among others.


+-------------------------+-----------------------------+----------------+-------------------+-------------------------+
| Name                    | Description                 | App Version    | System Version    | License                 |
+=========================+=============================+================+===================+=========================+
| `GTK+`_                 | Toolkit for creating cross  | 2.20.1         | N/A               | `LGPL 2.1`_             |
|                         | platform user interfaces.   |                |                   |                         |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+
| GLib_                   | Provides data structure     | 2.24.2         | N/A               | `LGPL 2.1`_             |
|                         | handling for C, portability |                |                   |                         |
|                         | wrappers and interfaces for |                |                   |                         |
|                         | such run-time functionality |                |                   |                         |
|                         | as an event loop, threads,  |                |                   |                         |
|                         | dynamic loading and an      |                |                   |                         |
|                         | object system.              |                |                   |                         |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+
| libiconv_               | Standard API for converting | 1.13.1         | 1.11              | `LGPL 2.1`_             |
|                         | character strings from one  |                |                   |                         |
|                         | character encoding to       |                |                   |                         |
|                         | another in Unix-like        |                |                   |                         |
|                         | operating systems.          |                |                   |                         |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+
| Pango_                  | Layout and rendering of text| 1.28.1         | N/A               | `LGPL 2.1`_             |
|                         | with an emphasis on         |                |                   |                         |
|                         | internationalization.       |                |                   |                         |         
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+
| Cairo_                  | 2D graphics library with    | 1.8.10         | 1.8.6             | `LGPL 2.1`_/`MPL 1.1`_  |
|                         | support for multiple output |                |                   |                         |
|                         | devices.                    |                |                   |                         |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+
| ATK_                    | Set of interfaces providing | 1.30           | N/A               | `LGPL 2.1`_             |
|                         | accessibility.              |                |                   |                         |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+
| gettext_                | GNU internationalization and| 0.18.1.1       | N/A               | `GPL 3.0`_              |
|                         | localization (i18n) library,|                |                   |                         |
|                         | commonly used for writing   |                |                   |                         |
|                         | multilingual programs.      |                |                   |                         |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+
| Fontconfig_             | Font customization and      | 2.8            | 2.6               | MIT_                    |
|                         | configuration.              |                |                   |                         |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+
| pkg-config_             | Provides a unified interface| 0.25           | 0.23              | `GPL 2.0`_ or later     |
|                         | for querying installed      |                |                   |                         |
|                         | libraries for the purpose of|                |                   |                         |
|                         | compiling software from its |                |                   |                         |
|                         | source code.                |                |                   |                         |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+
| FreeType_               | Used to rasterize characters| 2.4.2          | 2.3.9             | `GPL 2.0`_              |
|                         | into bitmaps and provides   |                |                   |                         |
|                         | support for other           |                |                   |                         |
|                         | font-related operations.    |                |                   |                         |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+
| libjpeg_                | Widely-used implementation  | 0.6b           | 0.6b              | BSD_                    |
|                         | of a JPEG decoder, encoder  |                |                   |                         |
|                         | and other JPEG utilities.   |                |                   |                         |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+
| libpng_                 | Official Portable Network   | 1.2.44         | 1.2.37            | `libpng license`_       |
|                         | Graphics (PNG) reference    |                |                   |                         |
|                         | library.		        |                |                   |                         |            
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+
| libxml2_                | XML C parser and toolkit.   | 2.7.7          | 2.7.3             | MIT_	               |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+
| libxslt_                | Implements XSLT-1.0 for     | 1.1.12         | 1.1.24            | MIT_	               |
|                         | libxml2_.                   |                |                   |                         |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+

XXX: what about gtk-doc?

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
| Java_                   | Programming language that   | N/A            | ?                 | `GPL 3.0`_              |
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
| PyAMF_                  | Provides Action Message     | 0.6            | N/A               | MIT_                    |                                  |
|                         | Format (AMF) support for    |                |                   |                         |                                  |
|                         | Python that is compatible   |                |                   |                         |                                  |
|                         | with the Adobe Flash Player.|                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| Pylons_                 | Lightweight web framework   | 1.0            | N/A               | BSD_                    |                                  |
|                         | emphasizing flexibility and |                |                   |                         |                                  |
|                         | rapid development.          |                |                   |                         |                                  |
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
| PyGtk_                  | Python binding for the      | 2.21           | N/A               | `LGPL 2.1`_             | PyGObject_, PyCairo_             |
|                         | `GTK+`_ library.            |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| PyGObject_              | Python binding for the GTK+ | 2.21.5         | N/A               | `LGPL 2.1`_             | GLib_, PyCairo_                  |
|                         | library.                    |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| PyCairo_                | Python binding for the GTK+ | 1.8.10         | N/A               | `LGPL 2.1`_             | 				  |
|                         | library.                    |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+
| PyWebKitGtk_            | Python binding for the      | 1.1.8          | N/A               | `LGPL 3.0`_             | libxslt_, PyGTK_, WebKit_        |
|                         | WebKitGtk rendering engine. |                |                   |                         |                                  |
+-------------------------+-----------------------------+----------------+-------------------+-------------------------+----------------------------------+

Note: glib: `./configure --disable-glibtest --without-ffi --disable-introspection`
Note: pygtk: `export PYTHON=/usr/local/bin/python2.7`

References
----------

- http://techbase.kde.org/Getting_Started/Build/KDE4/Mac_OS_X#Required_Third_Party_Tools
- http://library.gnome.org/devel/gtk-faq/stable/c192.html#FAQ-COMPILE
- http://library.gnome.org/devel/gtk/unstable/gtk-building.html
- http://www.gtk.org/api/2.6/glib/glib-building.html
- http://phacker.org/2010/03/21/building-gtk-on-osx-and-problems-with-libiconv/
- http://www.bill.eccles.net/bills_words/2008/12/libiconv-madness.html
- http://old.nabble.com/Compiling-glib-2.20.5-on-SnowLeopard-td25230062.html
- http://letsneverdie.net/blog/?p=75
- http://cairographics.org/end_to_end_build_for_mac_os_x/
- http://osdir.com/ml/pyjamas-dev/2010-03/msg00066.html
- http://www.apple.com/opensource/
- http://git.gnome.org/browse/pygobject/tree/README


.. _OS X 10.6.4: 		http://www.opensource.apple.com/release/mac-os-x-1064/
.. _GTK+: 			http://www.gtk.org
.. _GLib:			http://library.gnome.org/devel/glib/stable
.. _ATK:			http://library.gnome.org/devel/atk/stable
.. _Fontconfig:			http://www.fontconfig.org
.. _libiconv:			http://www.gnu.org/software/libiconv
.. _gettext:			http://www.gnu.org/software/gettext
.. _pkg-config:			http://pkg-config.freedesktop.org
.. _FreeType:			http://www.freetype.org
.. _libjpeg:			http://www.ijg.org
.. _libpng:			http://www.libpng.org
.. _libxml2:			http://www.xmlsoft.org
.. _libxslt:			http://xmlsoft.org/XSLT
.. _Cairo:			http://cairographics.org
.. _Pango:			http://www.pango.org
.. _CPython:			http://python.org
.. _Java:			http://java.sun.com
.. _PyAMF:			http://pyamf.org
.. _Pylons:			http://pylonshq.com
.. _SQLAlchemy:			http://sqlachemy.org
.. _Genshi:			http://genshi.edgewall.org
.. _repoze.what:		http://what.repoze.org
.. _Babel:			http://babel.edgewall.org
.. _PyWebKitGtk:		http://code.google.com/p/pywebkitgtk
.. _PyGTK:			http://www.pygtk.org	
.. _PyGObject:			http://www.pygtk.org
.. _PyCairo:			http://cairographics.org/pycairo
.. _WebKit:			http://webkit.org
.. _Flash Player:		http://adobe.com/products/flashplayer
.. _Flash Player EULA:		http://www.adobe.com/products/eulas/pdfs/PlatformClients_PC_WWEULA_Combined_20100108_1657.pdf
.. _LGPL 2.1:			http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html
.. _LGPL 3.0:			http://www.gnu.org/licenses/lgpl.html
.. _MPL 1.1:			http://www.mozilla.org/MPL/MPL-1.1.txt
.. _GPL 2.0:			http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
.. _GPL 3.0:			http://www.gnu.org/licenses/gpl-3.0.html
.. _MIT:			http://www.opensource.org/licenses/mit-license.php
.. _libpng license:		http://www.libpng.org/pub/png/src/libpng-LICENSE.txt
.. _BSD:			http://www.opensource.org/licenses/bsd-license.php
.. _PSF:			http://www.python.org/psf/license/
