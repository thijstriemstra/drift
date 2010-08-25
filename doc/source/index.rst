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

GTK+ has been built up to be based on four libraries:

- Pango_: layout and rendering of text with an emphasis on internationalization.
- Cairo_: 2D graphics.
- ATK_: set of interfaces providing accessibility.
- GLib_: provides data structure handling for C, portability wrappers and interfaces for such run-time
         functionality as an event loop, threads, dynamic loading and an object system.

+---------------+---------------+----------------+-------------------------------+
| Name          | App Version   | System Version | License                       |
+===============+===============+================+===============================+
| `GTK+`_       | 2.20.1        | N/A            | `LGPL 2.1`_                   |
+---------------+---------------+----------------+-------------------------------+
| GLib_         | 2.24.2        | N/A            | `LGPL 2.1`_                   |
+---------------+---------------+----------------+-------------------------------+
| libiconv_     | 1.13.1        | 1.11           | `LGPL 2.1`_                   |
+---------------+---------------+----------------+-------------------------------+
| Pango_        | 1.28.1        | N/A            | `LGPL 2.1`_                   |
+---------------+---------------+----------------+-------------------------------+
| Cairo_        | 1.8.10        | 1.8.6          | `LGPL 2.1`_/`MPL 1.1`_        |
+---------------+---------------+----------------+-------------------------------+
| ATK_          | 1.30          | N/A            | `LGPL 2.1`_                   |
+---------------+---------------+----------------+-------------------------------+
| gettext_      | 0.18.1.1      | N/A            | `GPL 3.0`_                    |
+---------------+---------------+----------------+-------------------------------+
| Fontconfig_   | 2.8           | 2.6            | MIT_                          |
+---------------+---------------+----------------+-------------------------------+
| pkg-config_   | 0.25          | 0.23           | `GPL 2.0`_ or later           |
+---------------+---------------+----------------+-------------------------------+
| FreeType_     | 2.4.2         | 2.3.9          | `GPL 2.0`_                    |
+---------------+---------------+----------------+-------------------------------+
| libjpeg_      | 0.6b          | 0.6b           | BSD_                          |
+---------------+---------------+----------------+-------------------------------+
| libpng_       | 1.2.44        | 1.2.37         | `libpng license`_		 |
+---------------+---------------+----------------+-------------------------------+
| libxml2_      | 2.7.7         | 2.7.3          | MIT_		                 |
+---------------+---------------+----------------+-------------------------------+
| libxslt_      | 1.1.12        | 1.1.24         | MIT_		                 |
+---------------+---------------+----------------+-------------------------------+

XXX: what about gtk-doc?

Runtimes
--------

+-----------------+---------------+-------------------+-------------------------------+
| Name            | App Version   | System Version(s) | License                       |
+=================+===============+===================+===============================+
| CPython_        | 2.7.0         | 2.6.1, 2.5.4      | PSF_                          |
+-----------------+---------------+-------------------+-------------------------------+
| Java_           | N/A           | ?                 | `GPL 3.0`_                    |
+-----------------+---------------+-------------------+-------------------------------+
| `Flash Player`_ | N/A           | ?                 | `Flash Player EULA`_          |
+-----------------+---------------+-------------------+-------------------------------+

Python
------

+-----------------+---------------+-------------------+-------------------------------+
| Name            | App Version   | System Version(s) | License                       |
+=================+===============+===================+===============================+
| PyAMF_          | 0.6           | N/A               | MIT_                          |
+-----------------+---------------+-------------------+-------------------------------+


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


.. _OS X 10.6.4: 	http://www.opensource.apple.com/release/mac-os-x-1064/
.. _GTK+: 		http://www.gtk.org
.. _GLib:		http://library.gnome.org/devel/glib/stable
.. _ATK:		http://library.gnome.org/devel/atk/stable
.. _Fontconfig:		http://www.fontconfig.org
.. _libiconv:		http://www.gnu.org/software/libiconv
.. _gettext:		http://www.gnu.org/software/gettext
.. _pkg-config:		http://pkg-config.freedesktop.org
.. _FreeType:		http://www.freetype.org
.. _libjpeg:		http://www.ijg.org
.. _libpng:		http://www.libpng.org
.. _libxml2:		http://www.xmlsoft.org
.. _libxslt:		http://xmlsoft.org/XSLT
.. _Cairo:		http://cairographics.org
.. _Pango:		http://www.pango.org
.. _CPython:		http://python.org
.. _Java:		http://java.sun.com
.. _PyAMF:		http://pyamf.org
.. _Flash Player:	http://adobe.com/products/flashplayer
.. _Flash Player EULA:	http://www.adobe.com/products/eulas/pdfs/PlatformClients_PC_WWEULA_Combined_20100108_1657.pdf
.. _LGPL 2.1:		http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html
.. _MPL 1.1:		http://www.mozilla.org/MPL/MPL-1.1.txt
.. _GPL 2.0:		http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
.. _GPL 3.0:		http://www.gnu.org/licenses/gpl-3.0.html
.. _MIT:		http://www.opensource.org/licenses/mit-license.php
.. _libpng license:	http://www.libpng.org/pub/png/src/libpng-LICENSE.txt
.. _BSD:		http://www.opensource.org/licenses/bsd-license.php
.. _PSF:		http://www.python.org/psf/license/
