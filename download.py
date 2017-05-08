#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import re
import requests
import codecs
import os.path
import os
from HTMLParser import HTMLParser
import json

data = '''<tr>
  <td><a href="./Glide.html" rel="rdf:_1">3dfx Glide License</a></td>
  <td about="./Glide.html" typeof="spdx:License">
  <code property="spdx:licenseId">Glide</code></td>
  <td align="center"></td>
  <td><a href="./Glide.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Abstyles.html" rel="rdf:_2">Abstyles License</a></td>
  <td about="./Abstyles.html" typeof="spdx:License">
  <code property="spdx:licenseId">Abstyles</code></td>
  <td align="center"></td>
  <td><a href="./Abstyles.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./AFL-1.1.html" rel="rdf:_3">Academic Free License v1.1</a></td>
  <td about="./AFL-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">AFL-1.1</code></td>
  <td align="center">Y</td>
  <td><a href="./AFL-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./AFL-1.2.html" rel="rdf:_4">Academic Free License v1.2</a></td>
  <td about="./AFL-1.2.html" typeof="spdx:License">
  <code property="spdx:licenseId">AFL-1.2</code></td>
  <td align="center">Y</td>
  <td><a href="./AFL-1.2.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./AFL-2.0.html" rel="rdf:_5">Academic Free License v2.0</a></td>
  <td about="./AFL-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">AFL-2.0</code></td>
  <td align="center">Y</td>
  <td><a href="./AFL-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./AFL-2.1.html" rel="rdf:_6">Academic Free License v2.1</a></td>
  <td about="./AFL-2.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">AFL-2.1</code></td>
  <td align="center">Y</td>
  <td><a href="./AFL-2.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./AFL-3.0.html" rel="rdf:_7">Academic Free License v3.0</a></td>
  <td about="./AFL-3.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">AFL-3.0</code></td>
  <td align="center">Y</td>
  <td><a href="./AFL-3.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./AMPAS.html" rel="rdf:_8">Academy of Motion Picture Arts and Sciences BSD</a></td>
  <td about="./AMPAS.html" typeof="spdx:License">
  <code property="spdx:licenseId">AMPAS</code></td>
  <td align="center"></td>
  <td><a href="./AMPAS.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./APL-1.0.html" rel="rdf:_9">Adaptive Public License 1.0</a></td>
  <td about="./APL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">APL-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./APL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Adobe-Glyph.html" rel="rdf:_10">Adobe Glyph List License</a></td>
  <td about="./Adobe-Glyph.html" typeof="spdx:License">
  <code property="spdx:licenseId">Adobe-Glyph</code></td>
  <td align="center"></td>
  <td><a href="./Adobe-Glyph.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./APAFML.html" rel="rdf:_11">Adobe Postscript AFM License</a></td>
  <td about="./APAFML.html" typeof="spdx:License">
  <code property="spdx:licenseId">APAFML</code></td>
  <td align="center"></td>
  <td><a href="./APAFML.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Adobe-2006.html" rel="rdf:_12">Adobe Systems Incorporated Source Code License Agreement</a></td>
  <td about="./Adobe-2006.html" typeof="spdx:License">
  <code property="spdx:licenseId">Adobe-2006</code></td>
  <td align="center"></td>
  <td><a href="./Adobe-2006.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./AGPL-1.0.html" rel="rdf:_13">Affero General Public License v1.0</a></td>
  <td about="./AGPL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">AGPL-1.0</code></td>
  <td align="center"></td>
  <td><a href="./AGPL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Afmparse.html" rel="rdf:_14">Afmparse License</a></td>
  <td about="./Afmparse.html" typeof="spdx:License">
  <code property="spdx:licenseId">Afmparse</code></td>
  <td align="center"></td>
  <td><a href="./Afmparse.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Aladdin.html" rel="rdf:_15">Aladdin Free Public License</a></td>
  <td about="./Aladdin.html" typeof="spdx:License">
  <code property="spdx:licenseId">Aladdin</code></td>
  <td align="center"></td>
  <td><a href="./Aladdin.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./ADSL.html" rel="rdf:_16">Amazon Digital Services License</a></td>
  <td about="./ADSL.html" typeof="spdx:License">
  <code property="spdx:licenseId">ADSL</code></td>
  <td align="center"></td>
  <td><a href="./ADSL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./AMDPLPA.html" rel="rdf:_17">AMD's plpa_map.c License</a></td>
  <td about="./AMDPLPA.html" typeof="spdx:License">
  <code property="spdx:licenseId">AMDPLPA</code></td>
  <td align="center"></td>
  <td><a href="./AMDPLPA.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./ANTLR-PD.html" rel="rdf:_18">ANTLR Software Rights Notice</a></td>
  <td about="./ANTLR-PD.html" typeof="spdx:License">
  <code property="spdx:licenseId">ANTLR-PD</code></td>
  <td align="center"></td>
  <td><a href="./ANTLR-PD.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Apache-1.0.html" rel="rdf:_19">Apache License 1.0</a></td>
  <td about="./Apache-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">Apache-1.0</code></td>
  <td align="center"></td>
  <td><a href="./Apache-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Apache-1.1.html" rel="rdf:_20">Apache License 1.1</a></td>
  <td about="./Apache-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">Apache-1.1</code></td>
  <td align="center">Y</td>
  <td><a href="./Apache-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Apache-2.0.html" rel="rdf:_21">Apache License 2.0</a></td>
  <td about="./Apache-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">Apache-2.0</code></td>
  <td align="center">Y</td>
  <td><a href="./Apache-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./AML.html" rel="rdf:_22">Apple MIT License</a></td>
  <td about="./AML.html" typeof="spdx:License">
  <code property="spdx:licenseId">AML</code></td>
  <td align="center"></td>
  <td><a href="./AML.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./APSL-1.0.html" rel="rdf:_23">Apple Public Source License 1.0</a></td>
  <td about="./APSL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">APSL-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./APSL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./APSL-1.1.html" rel="rdf:_24">Apple Public Source License 1.1</a></td>
  <td about="./APSL-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">APSL-1.1</code></td>
  <td align="center">Y</td>
  <td><a href="./APSL-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./APSL-1.2.html" rel="rdf:_25">Apple Public Source License 1.2</a></td>
  <td about="./APSL-1.2.html" typeof="spdx:License">
  <code property="spdx:licenseId">APSL-1.2</code></td>
  <td align="center">Y</td>
  <td><a href="./APSL-1.2.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./APSL-2.0.html" rel="rdf:_26">Apple Public Source License 2.0</a></td>
  <td about="./APSL-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">APSL-2.0</code></td>
  <td align="center">Y</td>
  <td><a href="./APSL-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Artistic-1.0.html" rel="rdf:_27">Artistic License 1.0</a></td>
  <td about="./Artistic-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">Artistic-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./Artistic-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Artistic-1.0-Perl.html" rel="rdf:_28">Artistic License 1.0 (Perl)</a></td>
  <td about="./Artistic-1.0-Perl.html" typeof="spdx:License">
  <code property="spdx:licenseId">Artistic-1.0-Perl</code></td>
  <td align="center">Y</td>
  <td><a href="./Artistic-1.0-Perl.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Artistic-1.0-cl8.html" rel="rdf:_29">Artistic License 1.0 w/clause 8</a></td>
  <td about="./Artistic-1.0-cl8.html" typeof="spdx:License">
  <code property="spdx:licenseId">Artistic-1.0-cl8</code></td>
  <td align="center">Y</td>
  <td><a href="./Artistic-1.0-cl8.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Artistic-2.0.html" rel="rdf:_30">Artistic License 2.0</a></td>
  <td about="./Artistic-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">Artistic-2.0</code></td>
  <td align="center">Y</td>
  <td><a href="./Artistic-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./AAL.html" rel="rdf:_31">Attribution Assurance License</a></td>
  <td about="./AAL.html" typeof="spdx:License">
  <code property="spdx:licenseId">AAL</code></td>
  <td align="center">Y</td>
  <td><a href="./AAL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Bahyph.html" rel="rdf:_32">Bahyph License</a></td>
  <td about="./Bahyph.html" typeof="spdx:License">
  <code property="spdx:licenseId">Bahyph</code></td>
  <td align="center"></td>
  <td><a href="./Bahyph.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Barr.html" rel="rdf:_33">Barr License</a></td>
  <td about="./Barr.html" typeof="spdx:License">
  <code property="spdx:licenseId">Barr</code></td>
  <td align="center"></td>
  <td><a href="./Barr.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Beerware.html" rel="rdf:_34">Beerware License</a></td>
  <td about="./Beerware.html" typeof="spdx:License">
  <code property="spdx:licenseId">Beerware</code></td>
  <td align="center"></td>
  <td><a href="./Beerware.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./BitTorrent-1.0.html" rel="rdf:_35">BitTorrent Open Source License v1.0</a></td>
  <td about="./BitTorrent-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">BitTorrent-1.0</code></td>
  <td align="center"></td>
  <td><a href="./BitTorrent-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./BitTorrent-1.1.html" rel="rdf:_36">BitTorrent Open Source License v1.1</a></td>
  <td about="./BitTorrent-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">BitTorrent-1.1</code></td>
  <td align="center"></td>
  <td><a href="./BitTorrent-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./BSL-1.0.html" rel="rdf:_37">Boost Software License 1.0</a></td>
  <td about="./BSL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">BSL-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./BSL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Borceux.html" rel="rdf:_38">Borceux license</a></td>
  <td about="./Borceux.html" typeof="spdx:License">
  <code property="spdx:licenseId">Borceux</code></td>
  <td align="center"></td>
  <td><a href="./Borceux.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./BSD-2-Clause.html" rel="rdf:_39">BSD 2-clause &quot;Simplified&quot; License</a></td>
  <td about="./BSD-2-Clause.html" typeof="spdx:License">
  <code property="spdx:licenseId">BSD-2-Clause</code></td>
  <td align="center">Y</td>
  <td><a href="./BSD-2-Clause.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./BSD-2-Clause-FreeBSD.html" rel="rdf:_40">BSD 2-clause FreeBSD License</a></td>
  <td about="./BSD-2-Clause-FreeBSD.html" typeof="spdx:License">
  <code property="spdx:licenseId">BSD-2-Clause-FreeBSD</code></td>
  <td align="center"></td>
  <td><a href="./BSD-2-Clause-FreeBSD.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./BSD-2-Clause-NetBSD.html" rel="rdf:_41">BSD 2-clause NetBSD License</a></td>
  <td about="./BSD-2-Clause-NetBSD.html" typeof="spdx:License">
  <code property="spdx:licenseId">BSD-2-Clause-NetBSD</code></td>
  <td align="center"></td>
  <td><a href="./BSD-2-Clause-NetBSD.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./BSD-3-Clause.html" rel="rdf:_42">BSD 3-clause &quot;New&quot; or &quot;Revised&quot; License</a></td>
  <td about="./BSD-3-Clause.html" typeof="spdx:License">
  <code property="spdx:licenseId">BSD-3-Clause</code></td>
  <td align="center">Y</td>
  <td><a href="./BSD-3-Clause.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./BSD-3-Clause-Clear.html" rel="rdf:_43">BSD 3-clause Clear License</a></td>
  <td about="./BSD-3-Clause-Clear.html" typeof="spdx:License">
  <code property="spdx:licenseId">BSD-3-Clause-Clear</code></td>
  <td align="center"></td>
  <td><a href="./BSD-3-Clause-Clear.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./BSD-3-Clause-No-Nuclear-License.html" rel="rdf:_44">BSD 3-Clause No Nuclear License</a></td>
  <td about="./BSD-3-Clause-No-Nuclear-License.html" typeof="spdx:License">
  <code property="spdx:licenseId">BSD-3-Clause-No-Nuclear-License</code></td>
  <td align="center"></td>
  <td><a href="./BSD-3-Clause-No-Nuclear-License.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./BSD-3-Clause-No-Nuclear-License-2014.html" rel="rdf:_45">BSD 3-Clause No Nuclear License 2014</a></td>
  <td about="./BSD-3-Clause-No-Nuclear-License-2014.html" typeof="spdx:License">
  <code property="spdx:licenseId">BSD-3-Clause-No-Nuclear-License-2014</code></td>
  <td align="center"></td>
  <td><a href="./BSD-3-Clause-No-Nuclear-License-2014.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./BSD-3-Clause-No-Nuclear-Warranty.html" rel="rdf:_46">BSD 3-Clause No Nuclear Warranty</a></td>
  <td about="./BSD-3-Clause-No-Nuclear-Warranty.html" typeof="spdx:License">
  <code property="spdx:licenseId">BSD-3-Clause-No-Nuclear-Warranty</code></td>
  <td align="center"></td>
  <td><a href="./BSD-3-Clause-No-Nuclear-Warranty.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./BSD-4-Clause.html" rel="rdf:_47">BSD 4-clause &quot;Original&quot; or &quot;Old&quot; License</a></td>
  <td about="./BSD-4-Clause.html" typeof="spdx:License">
  <code property="spdx:licenseId">BSD-4-Clause</code></td>
  <td align="center"></td>
  <td><a href="./BSD-4-Clause.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./BSD-Protection.html" rel="rdf:_48">BSD Protection License</a></td>
  <td about="./BSD-Protection.html" typeof="spdx:License">
  <code property="spdx:licenseId">BSD-Protection</code></td>
  <td align="center"></td>
  <td><a href="./BSD-Protection.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./BSD-Source-Code.html" rel="rdf:_49">BSD Source Code Attribution</a></td>
  <td about="./BSD-Source-Code.html" typeof="spdx:License">
  <code property="spdx:licenseId">BSD-Source-Code</code></td>
  <td align="center"></td>
  <td><a href="./BSD-Source-Code.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./BSD-3-Clause-Attribution.html" rel="rdf:_50">BSD with attribution</a></td>
  <td about="./BSD-3-Clause-Attribution.html" typeof="spdx:License">
  <code property="spdx:licenseId">BSD-3-Clause-Attribution</code></td>
  <td align="center"></td>
  <td><a href="./BSD-3-Clause-Attribution.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./0BSD.html" rel="rdf:_51">BSD Zero Clause License</a></td>
  <td about="./0BSD.html" typeof="spdx:License">
  <code property="spdx:licenseId">0BSD</code></td>
  <td align="center">Y</td>
  <td><a href="./0BSD.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./BSD-4-Clause-UC.html" rel="rdf:_52">BSD-4-Clause (University of California-Specific)</a></td>
  <td about="./BSD-4-Clause-UC.html" typeof="spdx:License">
  <code property="spdx:licenseId">BSD-4-Clause-UC</code></td>
  <td align="center"></td>
  <td><a href="./BSD-4-Clause-UC.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./bzip2-1.0.5.html" rel="rdf:_53">bzip2 and libbzip2 License v1.0.5</a></td>
  <td about="./bzip2-1.0.5.html" typeof="spdx:License">
  <code property="spdx:licenseId">bzip2-1.0.5</code></td>
  <td align="center"></td>
  <td><a href="./bzip2-1.0.5.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./bzip2-1.0.6.html" rel="rdf:_54">bzip2 and libbzip2 License v1.0.6</a></td>
  <td about="./bzip2-1.0.6.html" typeof="spdx:License">
  <code property="spdx:licenseId">bzip2-1.0.6</code></td>
  <td align="center"></td>
  <td><a href="./bzip2-1.0.6.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Caldera.html" rel="rdf:_55">Caldera License</a></td>
  <td about="./Caldera.html" typeof="spdx:License">
  <code property="spdx:licenseId">Caldera</code></td>
  <td align="center"></td>
  <td><a href="./Caldera.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CECILL-1.0.html" rel="rdf:_56">CeCILL Free Software License Agreement v1.0</a></td>
  <td about="./CECILL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CECILL-1.0</code></td>
  <td align="center"></td>
  <td><a href="./CECILL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CECILL-1.1.html" rel="rdf:_57">CeCILL Free Software License Agreement v1.1</a></td>
  <td about="./CECILL-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">CECILL-1.1</code></td>
  <td align="center"></td>
  <td><a href="./CECILL-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CECILL-2.0.html" rel="rdf:_58">CeCILL Free Software License Agreement v2.0</a></td>
  <td about="./CECILL-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CECILL-2.0</code></td>
  <td align="center"></td>
  <td><a href="./CECILL-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CECILL-2.1.html" rel="rdf:_59">CeCILL Free Software License Agreement v2.1</a></td>
  <td about="./CECILL-2.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">CECILL-2.1</code></td>
  <td align="center">Y</td>
  <td><a href="./CECILL-2.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CECILL-B.html" rel="rdf:_60">CeCILL-B Free Software License Agreement</a></td>
  <td about="./CECILL-B.html" typeof="spdx:License">
  <code property="spdx:licenseId">CECILL-B</code></td>
  <td align="center"></td>
  <td><a href="./CECILL-B.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CECILL-C.html" rel="rdf:_61">CeCILL-C Free Software License Agreement</a></td>
  <td about="./CECILL-C.html" typeof="spdx:License">
  <code property="spdx:licenseId">CECILL-C</code></td>
  <td align="center"></td>
  <td><a href="./CECILL-C.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./ClArtistic.html" rel="rdf:_62">Clarified Artistic License</a></td>
  <td about="./ClArtistic.html" typeof="spdx:License">
  <code property="spdx:licenseId">ClArtistic</code></td>
  <td align="center"></td>
  <td><a href="./ClArtistic.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./MIT-CMU.html" rel="rdf:_63">CMU License</a></td>
  <td about="./MIT-CMU.html" typeof="spdx:License">
  <code property="spdx:licenseId">MIT-CMU</code></td>
  <td align="center"></td>
  <td><a href="./MIT-CMU.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CNRI-Jython.html" rel="rdf:_64">CNRI Jython License</a></td>
  <td about="./CNRI-Jython.html" typeof="spdx:License">
  <code property="spdx:licenseId">CNRI-Jython</code></td>
  <td align="center"></td>
  <td><a href="./CNRI-Jython.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CNRI-Python.html" rel="rdf:_65">CNRI Python License</a></td>
  <td about="./CNRI-Python.html" typeof="spdx:License">
  <code property="spdx:licenseId">CNRI-Python</code></td>
  <td align="center">Y</td>
  <td><a href="./CNRI-Python.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CNRI-Python-GPL-Compatible.html" rel="rdf:_66">CNRI Python Open Source GPL Compatible License Agreement</a></td>
  <td about="./CNRI-Python-GPL-Compatible.html" typeof="spdx:License">
  <code property="spdx:licenseId">CNRI-Python-GPL-Compatible</code></td>
  <td align="center"></td>
  <td><a href="./CNRI-Python-GPL-Compatible.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CPOL-1.02.html" rel="rdf:_67">Code Project Open License 1.02</a></td>
  <td about="./CPOL-1.02.html" typeof="spdx:License">
  <code property="spdx:licenseId">CPOL-1.02</code></td>
  <td align="center"></td>
  <td><a href="./CPOL-1.02.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CDDL-1.0.html" rel="rdf:_68">Common Development and Distribution License 1.0</a></td>
  <td about="./CDDL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CDDL-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./CDDL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CDDL-1.1.html" rel="rdf:_69">Common Development and Distribution License 1.1</a></td>
  <td about="./CDDL-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">CDDL-1.1</code></td>
  <td align="center"></td>
  <td><a href="./CDDL-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CPAL-1.0.html" rel="rdf:_70">Common Public Attribution License 1.0</a></td>
  <td about="./CPAL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CPAL-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./CPAL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CPL-1.0.html" rel="rdf:_71">Common Public License 1.0</a></td>
  <td about="./CPL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CPL-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./CPL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CATOSL-1.1.html" rel="rdf:_72">Computer Associates Trusted Open Source License 1.1</a></td>
  <td about="./CATOSL-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">CATOSL-1.1</code></td>
  <td align="center">Y</td>
  <td><a href="./CATOSL-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Condor-1.1.html" rel="rdf:_73">Condor Public License v1.1</a></td>
  <td about="./Condor-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">Condor-1.1</code></td>
  <td align="center"></td>
  <td><a href="./Condor-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-1.0.html" rel="rdf:_74">Creative Commons Attribution 1.0</a></td>
  <td about="./CC-BY-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-1.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-2.0.html" rel="rdf:_75">Creative Commons Attribution 2.0</a></td>
  <td about="./CC-BY-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-2.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-2.5.html" rel="rdf:_76">Creative Commons Attribution 2.5</a></td>
  <td about="./CC-BY-2.5.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-2.5</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-2.5.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-3.0.html" rel="rdf:_77">Creative Commons Attribution 3.0</a></td>
  <td about="./CC-BY-3.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-3.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-3.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-4.0.html" rel="rdf:_78">Creative Commons Attribution 4.0</a></td>
  <td about="./CC-BY-4.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-4.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-4.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-ND-1.0.html" rel="rdf:_79">Creative Commons Attribution No Derivatives 1.0</a></td>
  <td about="./CC-BY-ND-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-ND-1.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-ND-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-ND-2.0.html" rel="rdf:_80">Creative Commons Attribution No Derivatives 2.0</a></td>
  <td about="./CC-BY-ND-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-ND-2.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-ND-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-ND-2.5.html" rel="rdf:_81">Creative Commons Attribution No Derivatives 2.5</a></td>
  <td about="./CC-BY-ND-2.5.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-ND-2.5</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-ND-2.5.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-ND-3.0.html" rel="rdf:_82">Creative Commons Attribution No Derivatives 3.0</a></td>
  <td about="./CC-BY-ND-3.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-ND-3.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-ND-3.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-ND-4.0.html" rel="rdf:_83">Creative Commons Attribution No Derivatives 4.0</a></td>
  <td about="./CC-BY-ND-4.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-ND-4.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-ND-4.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-NC-1.0.html" rel="rdf:_84">Creative Commons Attribution Non Commercial 1.0</a></td>
  <td about="./CC-BY-NC-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-NC-1.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-NC-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-NC-2.0.html" rel="rdf:_85">Creative Commons Attribution Non Commercial 2.0</a></td>
  <td about="./CC-BY-NC-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-NC-2.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-NC-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-NC-2.5.html" rel="rdf:_86">Creative Commons Attribution Non Commercial 2.5</a></td>
  <td about="./CC-BY-NC-2.5.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-NC-2.5</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-NC-2.5.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-NC-3.0.html" rel="rdf:_87">Creative Commons Attribution Non Commercial 3.0</a></td>
  <td about="./CC-BY-NC-3.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-NC-3.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-NC-3.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-NC-4.0.html" rel="rdf:_88">Creative Commons Attribution Non Commercial 4.0</a></td>
  <td about="./CC-BY-NC-4.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-NC-4.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-NC-4.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-NC-ND-1.0.html" rel="rdf:_89">Creative Commons Attribution Non Commercial No Derivatives 1.0</a></td>
  <td about="./CC-BY-NC-ND-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-NC-ND-1.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-NC-ND-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-NC-ND-2.0.html" rel="rdf:_90">Creative Commons Attribution Non Commercial No Derivatives 2.0</a></td>
  <td about="./CC-BY-NC-ND-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-NC-ND-2.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-NC-ND-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-NC-ND-2.5.html" rel="rdf:_91">Creative Commons Attribution Non Commercial No Derivatives 2.5</a></td>
  <td about="./CC-BY-NC-ND-2.5.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-NC-ND-2.5</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-NC-ND-2.5.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-NC-ND-3.0.html" rel="rdf:_92">Creative Commons Attribution Non Commercial No Derivatives 3.0</a></td>
  <td about="./CC-BY-NC-ND-3.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-NC-ND-3.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-NC-ND-3.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-NC-ND-4.0.html" rel="rdf:_93">Creative Commons Attribution Non Commercial No Derivatives 4.0</a></td>
  <td about="./CC-BY-NC-ND-4.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-NC-ND-4.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-NC-ND-4.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-NC-SA-1.0.html" rel="rdf:_94">Creative Commons Attribution Non Commercial Share Alike 1.0</a></td>
  <td about="./CC-BY-NC-SA-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-NC-SA-1.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-NC-SA-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-NC-SA-2.0.html" rel="rdf:_95">Creative Commons Attribution Non Commercial Share Alike 2.0</a></td>
  <td about="./CC-BY-NC-SA-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-NC-SA-2.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-NC-SA-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-NC-SA-2.5.html" rel="rdf:_96">Creative Commons Attribution Non Commercial Share Alike 2.5</a></td>
  <td about="./CC-BY-NC-SA-2.5.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-NC-SA-2.5</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-NC-SA-2.5.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-NC-SA-3.0.html" rel="rdf:_97">Creative Commons Attribution Non Commercial Share Alike 3.0</a></td>
  <td about="./CC-BY-NC-SA-3.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-NC-SA-3.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-NC-SA-3.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-NC-SA-4.0.html" rel="rdf:_98">Creative Commons Attribution Non Commercial Share Alike 4.0</a></td>
  <td about="./CC-BY-NC-SA-4.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-NC-SA-4.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-NC-SA-4.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-SA-1.0.html" rel="rdf:_99">Creative Commons Attribution Share Alike 1.0</a></td>
  <td about="./CC-BY-SA-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-SA-1.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-SA-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-SA-2.0.html" rel="rdf:_100">Creative Commons Attribution Share Alike 2.0</a></td>
  <td about="./CC-BY-SA-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-SA-2.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-SA-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-SA-2.5.html" rel="rdf:_101">Creative Commons Attribution Share Alike 2.5</a></td>
  <td about="./CC-BY-SA-2.5.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-SA-2.5</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-SA-2.5.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-SA-3.0.html" rel="rdf:_102">Creative Commons Attribution Share Alike 3.0</a></td>
  <td about="./CC-BY-SA-3.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-SA-3.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-SA-3.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC-BY-SA-4.0.html" rel="rdf:_103">Creative Commons Attribution Share Alike 4.0</a></td>
  <td about="./CC-BY-SA-4.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC-BY-SA-4.0</code></td>
  <td align="center"></td>
  <td><a href="./CC-BY-SA-4.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CC0-1.0.html" rel="rdf:_104">Creative Commons Zero v1.0 Universal</a></td>
  <td about="./CC0-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CC0-1.0</code></td>
  <td align="center"></td>
  <td><a href="./CC0-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Crossword.html" rel="rdf:_105">Crossword License</a></td>
  <td about="./Crossword.html" typeof="spdx:License">
  <code property="spdx:licenseId">Crossword</code></td>
  <td align="center"></td>
  <td><a href="./Crossword.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CrystalStacker.html" rel="rdf:_106">CrystalStacker License</a></td>
  <td about="./CrystalStacker.html" typeof="spdx:License">
  <code property="spdx:licenseId">CrystalStacker</code></td>
  <td align="center"></td>
  <td><a href="./CrystalStacker.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./CUA-OPL-1.0.html" rel="rdf:_107">CUA Office Public License v1.0</a></td>
  <td about="./CUA-OPL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">CUA-OPL-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./CUA-OPL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Cube.html" rel="rdf:_108">Cube License</a></td>
  <td about="./Cube.html" typeof="spdx:License">
  <code property="spdx:licenseId">Cube</code></td>
  <td align="center"></td>
  <td><a href="./Cube.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./curl.html" rel="rdf:_109">curl License</a></td>
  <td about="./curl.html" typeof="spdx:License">
  <code property="spdx:licenseId">curl</code></td>
  <td align="center"></td>
  <td><a href="./curl.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./D-FSL-1.0.html" rel="rdf:_110">Deutsche Freie Software Lizenz</a></td>
  <td about="./D-FSL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">D-FSL-1.0</code></td>
  <td align="center"></td>
  <td><a href="./D-FSL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./diffmark.html" rel="rdf:_111">diffmark license</a></td>
  <td about="./diffmark.html" typeof="spdx:License">
  <code property="spdx:licenseId">diffmark</code></td>
  <td align="center"></td>
  <td><a href="./diffmark.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./WTFPL.html" rel="rdf:_112">Do What The F*ck You Want To Public License</a></td>
  <td about="./WTFPL.html" typeof="spdx:License">
  <code property="spdx:licenseId">WTFPL</code></td>
  <td align="center"></td>
  <td><a href="./WTFPL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./DOC.html" rel="rdf:_113">DOC License</a></td>
  <td about="./DOC.html" typeof="spdx:License">
  <code property="spdx:licenseId">DOC</code></td>
  <td align="center"></td>
  <td><a href="./DOC.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Dotseqn.html" rel="rdf:_114">Dotseqn License</a></td>
  <td about="./Dotseqn.html" typeof="spdx:License">
  <code property="spdx:licenseId">Dotseqn</code></td>
  <td align="center"></td>
  <td><a href="./Dotseqn.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./DSDP.html" rel="rdf:_115">DSDP License</a></td>
  <td about="./DSDP.html" typeof="spdx:License">
  <code property="spdx:licenseId">DSDP</code></td>
  <td align="center"></td>
  <td><a href="./DSDP.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./dvipdfm.html" rel="rdf:_116">dvipdfm License</a></td>
  <td about="./dvipdfm.html" typeof="spdx:License">
  <code property="spdx:licenseId">dvipdfm</code></td>
  <td align="center"></td>
  <td><a href="./dvipdfm.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./EPL-1.0.html" rel="rdf:_117">Eclipse Public License 1.0</a></td>
  <td about="./EPL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">EPL-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./EPL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./ECL-1.0.html" rel="rdf:_118">Educational Community License v1.0</a></td>
  <td about="./ECL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">ECL-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./ECL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./ECL-2.0.html" rel="rdf:_119">Educational Community License v2.0</a></td>
  <td about="./ECL-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">ECL-2.0</code></td>
  <td align="center">Y</td>
  <td><a href="./ECL-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./eGenix.html" rel="rdf:_120">eGenix.com Public License 1.1.0</a></td>
  <td about="./eGenix.html" typeof="spdx:License">
  <code property="spdx:licenseId">eGenix</code></td>
  <td align="center"></td>
  <td><a href="./eGenix.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./EFL-1.0.html" rel="rdf:_121">Eiffel Forum License v1.0</a></td>
  <td about="./EFL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">EFL-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./EFL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./EFL-2.0.html" rel="rdf:_122">Eiffel Forum License v2.0</a></td>
  <td about="./EFL-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">EFL-2.0</code></td>
  <td align="center">Y</td>
  <td><a href="./EFL-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./MIT-advertising.html" rel="rdf:_123">Enlightenment License (e16)</a></td>
  <td about="./MIT-advertising.html" typeof="spdx:License">
  <code property="spdx:licenseId">MIT-advertising</code></td>
  <td align="center"></td>
  <td><a href="./MIT-advertising.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./MIT-enna.html" rel="rdf:_124">enna License</a></td>
  <td about="./MIT-enna.html" typeof="spdx:License">
  <code property="spdx:licenseId">MIT-enna</code></td>
  <td align="center"></td>
  <td><a href="./MIT-enna.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Entessa.html" rel="rdf:_125">Entessa Public License v1.0</a></td>
  <td about="./Entessa.html" typeof="spdx:License">
  <code property="spdx:licenseId">Entessa</code></td>
  <td align="center">Y</td>
  <td><a href="./Entessa.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./ErlPL-1.1.html" rel="rdf:_126">Erlang Public License v1.1</a></td>
  <td about="./ErlPL-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">ErlPL-1.1</code></td>
  <td align="center"></td>
  <td><a href="./ErlPL-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./EUDatagrid.html" rel="rdf:_127">EU DataGrid Software License</a></td>
  <td about="./EUDatagrid.html" typeof="spdx:License">
  <code property="spdx:licenseId">EUDatagrid</code></td>
  <td align="center">Y</td>
  <td><a href="./EUDatagrid.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./EUPL-1.0.html" rel="rdf:_128">European Union Public License 1.0</a></td>
  <td about="./EUPL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">EUPL-1.0</code></td>
  <td align="center"></td>
  <td><a href="./EUPL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./EUPL-1.1.html" rel="rdf:_129">European Union Public License 1.1</a></td>
  <td about="./EUPL-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">EUPL-1.1</code></td>
  <td align="center">Y</td>
  <td><a href="./EUPL-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Eurosym.html" rel="rdf:_130">Eurosym License</a></td>
  <td about="./Eurosym.html" typeof="spdx:License">
  <code property="spdx:licenseId">Eurosym</code></td>
  <td align="center"></td>
  <td><a href="./Eurosym.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Fair.html" rel="rdf:_131">Fair License</a></td>
  <td about="./Fair.html" typeof="spdx:License">
  <code property="spdx:licenseId">Fair</code></td>
  <td align="center">Y</td>
  <td><a href="./Fair.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./MIT-feh.html" rel="rdf:_132">feh License</a></td>
  <td about="./MIT-feh.html" typeof="spdx:License">
  <code property="spdx:licenseId">MIT-feh</code></td>
  <td align="center"></td>
  <td><a href="./MIT-feh.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Frameworx-1.0.html" rel="rdf:_133">Frameworx Open License 1.0</a></td>
  <td about="./Frameworx-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">Frameworx-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./Frameworx-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./FreeImage.html" rel="rdf:_134">FreeImage Public License v1.0</a></td>
  <td about="./FreeImage.html" typeof="spdx:License">
  <code property="spdx:licenseId">FreeImage</code></td>
  <td align="center"></td>
  <td><a href="./FreeImage.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./FTL.html" rel="rdf:_135">Freetype Project License</a></td>
  <td about="./FTL.html" typeof="spdx:License">
  <code property="spdx:licenseId">FTL</code></td>
  <td align="center"></td>
  <td><a href="./FTL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./FSFAP.html" rel="rdf:_136">FSF All Permissive License</a></td>
  <td about="./FSFAP.html" typeof="spdx:License">
  <code property="spdx:licenseId">FSFAP</code></td>
  <td align="center"></td>
  <td><a href="./FSFAP.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./FSFUL.html" rel="rdf:_137">FSF Unlimited License</a></td>
  <td about="./FSFUL.html" typeof="spdx:License">
  <code property="spdx:licenseId">FSFUL</code></td>
  <td align="center"></td>
  <td><a href="./FSFUL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./FSFULLR.html" rel="rdf:_138">FSF Unlimited License (with License Retention)</a></td>
  <td about="./FSFULLR.html" typeof="spdx:License">
  <code property="spdx:licenseId">FSFULLR</code></td>
  <td align="center"></td>
  <td><a href="./FSFULLR.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Giftware.html" rel="rdf:_139">Giftware License</a></td>
  <td about="./Giftware.html" typeof="spdx:License">
  <code property="spdx:licenseId">Giftware</code></td>
  <td align="center"></td>
  <td><a href="./Giftware.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./GL2PS.html" rel="rdf:_140">GL2PS License</a></td>
  <td about="./GL2PS.html" typeof="spdx:License">
  <code property="spdx:licenseId">GL2PS</code></td>
  <td align="center"></td>
  <td><a href="./GL2PS.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Glulxe.html" rel="rdf:_141">Glulxe License</a></td>
  <td about="./Glulxe.html" typeof="spdx:License">
  <code property="spdx:licenseId">Glulxe</code></td>
  <td align="center"></td>
  <td><a href="./Glulxe.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./AGPL-3.0.html" rel="rdf:_142">GNU Affero General Public License v3.0</a></td>
  <td about="./AGPL-3.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">AGPL-3.0</code></td>
  <td align="center">Y</td>
  <td><a href="./AGPL-3.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./GFDL-1.1.html" rel="rdf:_143">GNU Free Documentation License v1.1</a></td>
  <td about="./GFDL-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">GFDL-1.1</code></td>
  <td align="center"></td>
  <td><a href="./GFDL-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./GFDL-1.2.html" rel="rdf:_144">GNU Free Documentation License v1.2</a></td>
  <td about="./GFDL-1.2.html" typeof="spdx:License">
  <code property="spdx:licenseId">GFDL-1.2</code></td>
  <td align="center"></td>
  <td><a href="./GFDL-1.2.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./GFDL-1.3.html" rel="rdf:_145">GNU Free Documentation License v1.3</a></td>
  <td about="./GFDL-1.3.html" typeof="spdx:License">
  <code property="spdx:licenseId">GFDL-1.3</code></td>
  <td align="center"></td>
  <td><a href="./GFDL-1.3.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./GPL-1.0.html" rel="rdf:_146">GNU General Public License v1.0 only</a></td>
  <td about="./GPL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">GPL-1.0</code></td>
  <td align="center"></td>
  <td><a href="./GPL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./GPL-2.0.html" rel="rdf:_147">GNU General Public License v2.0 only</a></td>
  <td about="./GPL-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">GPL-2.0</code></td>
  <td align="center">Y</td>
  <td><a href="./GPL-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./GPL-3.0.html" rel="rdf:_148">GNU General Public License v3.0 only</a></td>
  <td about="./GPL-3.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">GPL-3.0</code></td>
  <td align="center">Y</td>
  <td><a href="./GPL-3.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./LGPL-2.1.html" rel="rdf:_149">GNU Lesser General Public License v2.1 only</a></td>
  <td about="./LGPL-2.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">LGPL-2.1</code></td>
  <td align="center">Y</td>
  <td><a href="./LGPL-2.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./LGPL-3.0.html" rel="rdf:_150">GNU Lesser General Public License v3.0 only</a></td>
  <td about="./LGPL-3.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">LGPL-3.0</code></td>
  <td align="center">Y</td>
  <td><a href="./LGPL-3.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./LGPL-2.0.html" rel="rdf:_151">GNU Library General Public License v2 only</a></td>
  <td about="./LGPL-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">LGPL-2.0</code></td>
  <td align="center">Y</td>
  <td><a href="./LGPL-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./gnuplot.html" rel="rdf:_152">gnuplot License</a></td>
  <td about="./gnuplot.html" typeof="spdx:License">
  <code property="spdx:licenseId">gnuplot</code></td>
  <td align="center"></td>
  <td><a href="./gnuplot.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./gSOAP-1.3b.html" rel="rdf:_153">gSOAP Public License v1.3b</a></td>
  <td about="./gSOAP-1.3b.html" typeof="spdx:License">
  <code property="spdx:licenseId">gSOAP-1.3b</code></td>
  <td align="center"></td>
  <td><a href="./gSOAP-1.3b.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./HaskellReport.html" rel="rdf:_154">Haskell Language Report License</a></td>
  <td about="./HaskellReport.html" typeof="spdx:License">
  <code property="spdx:licenseId">HaskellReport</code></td>
  <td align="center"></td>
  <td><a href="./HaskellReport.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./HPND.html" rel="rdf:_155">Historic Permission Notice and Disclaimer</a></td>
  <td about="./HPND.html" typeof="spdx:License">
  <code property="spdx:licenseId">HPND</code></td>
  <td align="center">Y</td>
  <td><a href="./HPND.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./IBM-pibs.html" rel="rdf:_156">IBM PowerPC Initialization and Boot Software</a></td>
  <td about="./IBM-pibs.html" typeof="spdx:License">
  <code property="spdx:licenseId">IBM-pibs</code></td>
  <td align="center"></td>
  <td><a href="./IBM-pibs.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./IPL-1.0.html" rel="rdf:_157">IBM Public License v1.0</a></td>
  <td about="./IPL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">IPL-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./IPL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./ICU.html" rel="rdf:_158">ICU License</a></td>
  <td about="./ICU.html" typeof="spdx:License">
  <code property="spdx:licenseId">ICU</code></td>
  <td align="center"></td>
  <td><a href="./ICU.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./ImageMagick.html" rel="rdf:_159">ImageMagick License</a></td>
  <td about="./ImageMagick.html" typeof="spdx:License">
  <code property="spdx:licenseId">ImageMagick</code></td>
  <td align="center"></td>
  <td><a href="./ImageMagick.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./iMatix.html" rel="rdf:_160">iMatix Standard Function Library Agreement</a></td>
  <td about="./iMatix.html" typeof="spdx:License">
  <code property="spdx:licenseId">iMatix</code></td>
  <td align="center"></td>
  <td><a href="./iMatix.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Imlib2.html" rel="rdf:_161">Imlib2 License</a></td>
  <td about="./Imlib2.html" typeof="spdx:License">
  <code property="spdx:licenseId">Imlib2</code></td>
  <td align="center"></td>
  <td><a href="./Imlib2.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./IJG.html" rel="rdf:_162">Independent JPEG Group License</a></td>
  <td about="./IJG.html" typeof="spdx:License">
  <code property="spdx:licenseId">IJG</code></td>
  <td align="center"></td>
  <td><a href="./IJG.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Info-ZIP.html" rel="rdf:_163">Info-ZIP License</a></td>
  <td about="./Info-ZIP.html" typeof="spdx:License">
  <code property="spdx:licenseId">Info-ZIP</code></td>
  <td align="center"></td>
  <td><a href="./Info-ZIP.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Intel-ACPI.html" rel="rdf:_164">Intel ACPI Software License Agreement</a></td>
  <td about="./Intel-ACPI.html" typeof="spdx:License">
  <code property="spdx:licenseId">Intel-ACPI</code></td>
  <td align="center"></td>
  <td><a href="./Intel-ACPI.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Intel.html" rel="rdf:_165">Intel Open Source License</a></td>
  <td about="./Intel.html" typeof="spdx:License">
  <code property="spdx:licenseId">Intel</code></td>
  <td align="center">Y</td>
  <td><a href="./Intel.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Interbase-1.0.html" rel="rdf:_166">Interbase Public License v1.0</a></td>
  <td about="./Interbase-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">Interbase-1.0</code></td>
  <td align="center"></td>
  <td><a href="./Interbase-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./IPA.html" rel="rdf:_167">IPA Font License</a></td>
  <td about="./IPA.html" typeof="spdx:License">
  <code property="spdx:licenseId">IPA</code></td>
  <td align="center">Y</td>
  <td><a href="./IPA.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./ISC.html" rel="rdf:_168">ISC License</a></td>
  <td about="./ISC.html" typeof="spdx:License">
  <code property="spdx:licenseId">ISC</code></td>
  <td align="center">Y</td>
  <td><a href="./ISC.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./JasPer-2.0.html" rel="rdf:_169">JasPer License</a></td>
  <td about="./JasPer-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">JasPer-2.0</code></td>
  <td align="center"></td>
  <td><a href="./JasPer-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./JSON.html" rel="rdf:_170">JSON License</a></td>
  <td about="./JSON.html" typeof="spdx:License">
  <code property="spdx:licenseId">JSON</code></td>
  <td align="center"></td>
  <td><a href="./JSON.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./LPPL-1.0.html" rel="rdf:_171">LaTeX Project Public License v1.0</a></td>
  <td about="./LPPL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">LPPL-1.0</code></td>
  <td align="center"></td>
  <td><a href="./LPPL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./LPPL-1.1.html" rel="rdf:_172">LaTeX Project Public License v1.1</a></td>
  <td about="./LPPL-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">LPPL-1.1</code></td>
  <td align="center"></td>
  <td><a href="./LPPL-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./LPPL-1.2.html" rel="rdf:_173">LaTeX Project Public License v1.2</a></td>
  <td about="./LPPL-1.2.html" typeof="spdx:License">
  <code property="spdx:licenseId">LPPL-1.2</code></td>
  <td align="center"></td>
  <td><a href="./LPPL-1.2.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./LPPL-1.3a.html" rel="rdf:_174">LaTeX Project Public License v1.3a</a></td>
  <td about="./LPPL-1.3a.html" typeof="spdx:License">
  <code property="spdx:licenseId">LPPL-1.3a</code></td>
  <td align="center"></td>
  <td><a href="./LPPL-1.3a.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./LPPL-1.3c.html" rel="rdf:_175">LaTeX Project Public License v1.3c</a></td>
  <td about="./LPPL-1.3c.html" typeof="spdx:License">
  <code property="spdx:licenseId">LPPL-1.3c</code></td>
  <td align="center">Y</td>
  <td><a href="./LPPL-1.3c.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Latex2e.html" rel="rdf:_176">Latex2e License</a></td>
  <td about="./Latex2e.html" typeof="spdx:License">
  <code property="spdx:licenseId">Latex2e</code></td>
  <td align="center"></td>
  <td><a href="./Latex2e.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./BSD-3-Clause-LBNL.html" rel="rdf:_177">Lawrence Berkeley National Labs BSD variant license</a></td>
  <td about="./BSD-3-Clause-LBNL.html" typeof="spdx:License">
  <code property="spdx:licenseId">BSD-3-Clause-LBNL</code></td>
  <td align="center"></td>
  <td><a href="./BSD-3-Clause-LBNL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Leptonica.html" rel="rdf:_178">Leptonica License</a></td>
  <td about="./Leptonica.html" typeof="spdx:License">
  <code property="spdx:licenseId">Leptonica</code></td>
  <td align="center"></td>
  <td><a href="./Leptonica.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./LGPLLR.html" rel="rdf:_179">Lesser General Public License For Linguistic Resources</a></td>
  <td about="./LGPLLR.html" typeof="spdx:License">
  <code property="spdx:licenseId">LGPLLR</code></td>
  <td align="center"></td>
  <td><a href="./LGPLLR.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Libpng.html" rel="rdf:_180">libpng License</a></td>
  <td about="./Libpng.html" typeof="spdx:License">
  <code property="spdx:licenseId">Libpng</code></td>
  <td align="center"></td>
  <td><a href="./Libpng.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./libtiff.html" rel="rdf:_181">libtiff License</a></td>
  <td about="./libtiff.html" typeof="spdx:License">
  <code property="spdx:licenseId">libtiff</code></td>
  <td align="center"></td>
  <td><a href="./libtiff.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./LAL-1.2.html" rel="rdf:_182">Licence Art Libre 1.2</a></td>
  <td about="./LAL-1.2.html" typeof="spdx:License">
  <code property="spdx:licenseId">LAL-1.2</code></td>
  <td align="center"></td>
  <td><a href="./LAL-1.2.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./LAL-1.3.html" rel="rdf:_183">Licence Art Libre 1.3</a></td>
  <td about="./LAL-1.3.html" typeof="spdx:License">
  <code property="spdx:licenseId">LAL-1.3</code></td>
  <td align="center"></td>
  <td><a href="./LAL-1.3.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./LiLiQ-P-1.1.html" rel="rdf:_184">Licence Libre du Québec – Permissive version 1.1</a></td>
  <td about="./LiLiQ-P-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">LiLiQ-P-1.1</code></td>
  <td align="center">Y</td>
  <td><a href="./LiLiQ-P-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./LiLiQ-Rplus-1.1.html" rel="rdf:_185">Licence Libre du Québec – Réciprocité forte version 1.1</a></td>
  <td about="./LiLiQ-Rplus-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">LiLiQ-Rplus-1.1</code></td>
  <td align="center">Y</td>
  <td><a href="./LiLiQ-Rplus-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./LiLiQ-R-1.1.html" rel="rdf:_186">Licence Libre du Québec – Réciprocité version 1.1</a></td>
  <td about="./LiLiQ-R-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">LiLiQ-R-1.1</code></td>
  <td align="center">Y</td>
  <td><a href="./LiLiQ-R-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./LPL-1.02.html" rel="rdf:_187">Lucent Public License v1.02</a></td>
  <td about="./LPL-1.02.html" typeof="spdx:License">
  <code property="spdx:licenseId">LPL-1.02</code></td>
  <td align="center">Y</td>
  <td><a href="./LPL-1.02.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./LPL-1.0.html" rel="rdf:_188">Lucent Public License Version 1.0</a></td>
  <td about="./LPL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">LPL-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./LPL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./MakeIndex.html" rel="rdf:_189">MakeIndex License</a></td>
  <td about="./MakeIndex.html" typeof="spdx:License">
  <code property="spdx:licenseId">MakeIndex</code></td>
  <td align="center"></td>
  <td><a href="./MakeIndex.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./MTLL.html" rel="rdf:_190">Matrix Template Library License</a></td>
  <td about="./MTLL.html" typeof="spdx:License">
  <code property="spdx:licenseId">MTLL</code></td>
  <td align="center"></td>
  <td><a href="./MTLL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./MS-PL.html" rel="rdf:_191">Microsoft Public License</a></td>
  <td about="./MS-PL.html" typeof="spdx:License">
  <code property="spdx:licenseId">MS-PL</code></td>
  <td align="center">Y</td>
  <td><a href="./MS-PL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./MS-RL.html" rel="rdf:_192">Microsoft Reciprocal License</a></td>
  <td about="./MS-RL.html" typeof="spdx:License">
  <code property="spdx:licenseId">MS-RL</code></td>
  <td align="center">Y</td>
  <td><a href="./MS-RL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./MirOS.html" rel="rdf:_193">MirOS Licence</a></td>
  <td about="./MirOS.html" typeof="spdx:License">
  <code property="spdx:licenseId">MirOS</code></td>
  <td align="center">Y</td>
  <td><a href="./MirOS.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./MITNFA.html" rel="rdf:_194">MIT +no-false-attribs license</a></td>
  <td about="./MITNFA.html" typeof="spdx:License">
  <code property="spdx:licenseId">MITNFA</code></td>
  <td align="center"></td>
  <td><a href="./MITNFA.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./MIT.html" rel="rdf:_195">MIT License</a></td>
  <td about="./MIT.html" typeof="spdx:License">
  <code property="spdx:licenseId">MIT</code></td>
  <td align="center">Y</td>
  <td><a href="./MIT.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Motosoto.html" rel="rdf:_196">Motosoto License</a></td>
  <td about="./Motosoto.html" typeof="spdx:License">
  <code property="spdx:licenseId">Motosoto</code></td>
  <td align="center">Y</td>
  <td><a href="./Motosoto.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./MPL-1.0.html" rel="rdf:_197">Mozilla Public License 1.0</a></td>
  <td about="./MPL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">MPL-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./MPL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./MPL-1.1.html" rel="rdf:_198">Mozilla Public License 1.1</a></td>
  <td about="./MPL-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">MPL-1.1</code></td>
  <td align="center">Y</td>
  <td><a href="./MPL-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./MPL-2.0.html" rel="rdf:_199">Mozilla Public License 2.0</a></td>
  <td about="./MPL-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">MPL-2.0</code></td>
  <td align="center">Y</td>
  <td><a href="./MPL-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./MPL-2.0-no-copyleft-exception.html" rel="rdf:_200">Mozilla Public License 2.0 (no copyleft exception)</a></td>
  <td about="./MPL-2.0-no-copyleft-exception.html" typeof="spdx:License">
  <code property="spdx:licenseId">MPL-2.0-no-copyleft-exception</code></td>
  <td align="center">Y</td>
  <td><a href="./MPL-2.0-no-copyleft-exception.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./mpich2.html" rel="rdf:_201">mpich2 License</a></td>
  <td about="./mpich2.html" typeof="spdx:License">
  <code property="spdx:licenseId">mpich2</code></td>
  <td align="center"></td>
  <td><a href="./mpich2.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Multics.html" rel="rdf:_202">Multics License</a></td>
  <td about="./Multics.html" typeof="spdx:License">
  <code property="spdx:licenseId">Multics</code></td>
  <td align="center">Y</td>
  <td><a href="./Multics.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Mup.html" rel="rdf:_203">Mup License</a></td>
  <td about="./Mup.html" typeof="spdx:License">
  <code property="spdx:licenseId">Mup</code></td>
  <td align="center"></td>
  <td><a href="./Mup.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./NASA-1.3.html" rel="rdf:_204">NASA Open Source Agreement 1.3</a></td>
  <td about="./NASA-1.3.html" typeof="spdx:License">
  <code property="spdx:licenseId">NASA-1.3</code></td>
  <td align="center">Y</td>
  <td><a href="./NASA-1.3.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Naumen.html" rel="rdf:_205">Naumen Public License</a></td>
  <td about="./Naumen.html" typeof="spdx:License">
  <code property="spdx:licenseId">Naumen</code></td>
  <td align="center">Y</td>
  <td><a href="./Naumen.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./NBPL-1.0.html" rel="rdf:_206">Net Boolean Public License v1</a></td>
  <td about="./NBPL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">NBPL-1.0</code></td>
  <td align="center"></td>
  <td><a href="./NBPL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Net-SNMP.html" rel="rdf:_207">Net-SNMP License</a></td>
  <td about="./Net-SNMP.html" typeof="spdx:License">
  <code property="spdx:licenseId">Net-SNMP</code></td>
  <td align="center"></td>
  <td><a href="./Net-SNMP.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./NetCDF.html" rel="rdf:_208">NetCDF license</a></td>
  <td about="./NetCDF.html" typeof="spdx:License">
  <code property="spdx:licenseId">NetCDF</code></td>
  <td align="center"></td>
  <td><a href="./NetCDF.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./NGPL.html" rel="rdf:_209">Nethack General Public License</a></td>
  <td about="./NGPL.html" typeof="spdx:License">
  <code property="spdx:licenseId">NGPL</code></td>
  <td align="center">Y</td>
  <td><a href="./NGPL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./NOSL.html" rel="rdf:_210">Netizen Open Source License</a></td>
  <td about="./NOSL.html" typeof="spdx:License">
  <code property="spdx:licenseId">NOSL</code></td>
  <td align="center"></td>
  <td><a href="./NOSL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./NPL-1.0.html" rel="rdf:_211">Netscape Public License v1.0</a></td>
  <td about="./NPL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">NPL-1.0</code></td>
  <td align="center"></td>
  <td><a href="./NPL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./NPL-1.1.html" rel="rdf:_212">Netscape Public License v1.1</a></td>
  <td about="./NPL-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">NPL-1.1</code></td>
  <td align="center"></td>
  <td><a href="./NPL-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Newsletr.html" rel="rdf:_213">Newsletr License</a></td>
  <td about="./Newsletr.html" typeof="spdx:License">
  <code property="spdx:licenseId">Newsletr</code></td>
  <td align="center"></td>
  <td><a href="./Newsletr.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./NLPL.html" rel="rdf:_214">No Limit Public License</a></td>
  <td about="./NLPL.html" typeof="spdx:License">
  <code property="spdx:licenseId">NLPL</code></td>
  <td align="center"></td>
  <td><a href="./NLPL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Nokia.html" rel="rdf:_215">Nokia Open Source License</a></td>
  <td about="./Nokia.html" typeof="spdx:License">
  <code property="spdx:licenseId">Nokia</code></td>
  <td align="center">Y</td>
  <td><a href="./Nokia.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./NPOSL-3.0.html" rel="rdf:_216">Non-Profit Open Software License 3.0</a></td>
  <td about="./NPOSL-3.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">NPOSL-3.0</code></td>
  <td align="center">Y</td>
  <td><a href="./NPOSL-3.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./NLOD-1.0.html" rel="rdf:_217">Norwegian Licence for Open Government Data</a></td>
  <td about="./NLOD-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">NLOD-1.0</code></td>
  <td align="center"></td>
  <td><a href="./NLOD-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Noweb.html" rel="rdf:_218">Noweb License</a></td>
  <td about="./Noweb.html" typeof="spdx:License">
  <code property="spdx:licenseId">Noweb</code></td>
  <td align="center"></td>
  <td><a href="./Noweb.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./NRL.html" rel="rdf:_219">NRL License</a></td>
  <td about="./NRL.html" typeof="spdx:License">
  <code property="spdx:licenseId">NRL</code></td>
  <td align="center"></td>
  <td><a href="./NRL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./NTP.html" rel="rdf:_220">NTP License</a></td>
  <td about="./NTP.html" typeof="spdx:License">
  <code property="spdx:licenseId">NTP</code></td>
  <td align="center">Y</td>
  <td><a href="./NTP.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Nunit.html" rel="rdf:_221">Nunit License</a></td>
  <td about="./Nunit.html" typeof="spdx:License">
  <code property="spdx:licenseId">Nunit</code></td>
  <td align="center"></td>
  <td><a href="./Nunit.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OCLC-2.0.html" rel="rdf:_222">OCLC Research Public License 2.0</a></td>
  <td about="./OCLC-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">OCLC-2.0</code></td>
  <td align="center">Y</td>
  <td><a href="./OCLC-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./ODbL-1.0.html" rel="rdf:_223">ODC Open Database License v1.0</a></td>
  <td about="./ODbL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">ODbL-1.0</code></td>
  <td align="center"></td>
  <td><a href="./ODbL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./PDDL-1.0.html" rel="rdf:_224">ODC Public Domain Dedication &amp; License 1.0</a></td>
  <td about="./PDDL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">PDDL-1.0</code></td>
  <td align="center"></td>
  <td><a href="./PDDL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OCCT-PL.html" rel="rdf:_225">Open CASCADE Technology Public License</a></td>
  <td about="./OCCT-PL.html" typeof="spdx:License">
  <code property="spdx:licenseId">OCCT-PL</code></td>
  <td align="center"></td>
  <td><a href="./OCCT-PL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OGTSL.html" rel="rdf:_226">Open Group Test Suite License</a></td>
  <td about="./OGTSL.html" typeof="spdx:License">
  <code property="spdx:licenseId">OGTSL</code></td>
  <td align="center">Y</td>
  <td><a href="./OGTSL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OLDAP-2.2.2.html" rel="rdf:_227">Open LDAP Public License  2.2.2</a></td>
  <td about="./OLDAP-2.2.2.html" typeof="spdx:License">
  <code property="spdx:licenseId">OLDAP-2.2.2</code></td>
  <td align="center"></td>
  <td><a href="./OLDAP-2.2.2.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OLDAP-1.1.html" rel="rdf:_228">Open LDAP Public License v1.1</a></td>
  <td about="./OLDAP-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">OLDAP-1.1</code></td>
  <td align="center"></td>
  <td><a href="./OLDAP-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OLDAP-1.2.html" rel="rdf:_229">Open LDAP Public License v1.2</a></td>
  <td about="./OLDAP-1.2.html" typeof="spdx:License">
  <code property="spdx:licenseId">OLDAP-1.2</code></td>
  <td align="center"></td>
  <td><a href="./OLDAP-1.2.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OLDAP-1.3.html" rel="rdf:_230">Open LDAP Public License v1.3</a></td>
  <td about="./OLDAP-1.3.html" typeof="spdx:License">
  <code property="spdx:licenseId">OLDAP-1.3</code></td>
  <td align="center"></td>
  <td><a href="./OLDAP-1.3.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OLDAP-1.4.html" rel="rdf:_231">Open LDAP Public License v1.4</a></td>
  <td about="./OLDAP-1.4.html" typeof="spdx:License">
  <code property="spdx:licenseId">OLDAP-1.4</code></td>
  <td align="center"></td>
  <td><a href="./OLDAP-1.4.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OLDAP-2.0.html" rel="rdf:_232">Open LDAP Public License v2.0 (or possibly 2.0A and 2.0B)</a></td>
  <td about="./OLDAP-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">OLDAP-2.0</code></td>
  <td align="center"></td>
  <td><a href="./OLDAP-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OLDAP-2.0.1.html" rel="rdf:_233">Open LDAP Public License v2.0.1</a></td>
  <td about="./OLDAP-2.0.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">OLDAP-2.0.1</code></td>
  <td align="center"></td>
  <td><a href="./OLDAP-2.0.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OLDAP-2.1.html" rel="rdf:_234">Open LDAP Public License v2.1</a></td>
  <td about="./OLDAP-2.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">OLDAP-2.1</code></td>
  <td align="center"></td>
  <td><a href="./OLDAP-2.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OLDAP-2.2.html" rel="rdf:_235">Open LDAP Public License v2.2</a></td>
  <td about="./OLDAP-2.2.html" typeof="spdx:License">
  <code property="spdx:licenseId">OLDAP-2.2</code></td>
  <td align="center"></td>
  <td><a href="./OLDAP-2.2.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OLDAP-2.2.1.html" rel="rdf:_236">Open LDAP Public License v2.2.1</a></td>
  <td about="./OLDAP-2.2.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">OLDAP-2.2.1</code></td>
  <td align="center"></td>
  <td><a href="./OLDAP-2.2.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OLDAP-2.3.html" rel="rdf:_237">Open LDAP Public License v2.3</a></td>
  <td about="./OLDAP-2.3.html" typeof="spdx:License">
  <code property="spdx:licenseId">OLDAP-2.3</code></td>
  <td align="center"></td>
  <td><a href="./OLDAP-2.3.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OLDAP-2.4.html" rel="rdf:_238">Open LDAP Public License v2.4</a></td>
  <td about="./OLDAP-2.4.html" typeof="spdx:License">
  <code property="spdx:licenseId">OLDAP-2.4</code></td>
  <td align="center"></td>
  <td><a href="./OLDAP-2.4.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OLDAP-2.5.html" rel="rdf:_239">Open LDAP Public License v2.5</a></td>
  <td about="./OLDAP-2.5.html" typeof="spdx:License">
  <code property="spdx:licenseId">OLDAP-2.5</code></td>
  <td align="center"></td>
  <td><a href="./OLDAP-2.5.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OLDAP-2.6.html" rel="rdf:_240">Open LDAP Public License v2.6</a></td>
  <td about="./OLDAP-2.6.html" typeof="spdx:License">
  <code property="spdx:licenseId">OLDAP-2.6</code></td>
  <td align="center"></td>
  <td><a href="./OLDAP-2.6.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OLDAP-2.7.html" rel="rdf:_241">Open LDAP Public License v2.7</a></td>
  <td about="./OLDAP-2.7.html" typeof="spdx:License">
  <code property="spdx:licenseId">OLDAP-2.7</code></td>
  <td align="center"></td>
  <td><a href="./OLDAP-2.7.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OLDAP-2.8.html" rel="rdf:_242">Open LDAP Public License v2.8</a></td>
  <td about="./OLDAP-2.8.html" typeof="spdx:License">
  <code property="spdx:licenseId">OLDAP-2.8</code></td>
  <td align="center"></td>
  <td><a href="./OLDAP-2.8.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OML.html" rel="rdf:_243">Open Market License</a></td>
  <td about="./OML.html" typeof="spdx:License">
  <code property="spdx:licenseId">OML</code></td>
  <td align="center"></td>
  <td><a href="./OML.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OPL-1.0.html" rel="rdf:_244">Open Public License v1.0</a></td>
  <td about="./OPL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">OPL-1.0</code></td>
  <td align="center"></td>
  <td><a href="./OPL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OSL-1.0.html" rel="rdf:_245">Open Software License 1.0</a></td>
  <td about="./OSL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">OSL-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./OSL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OSL-1.1.html" rel="rdf:_246">Open Software License 1.1</a></td>
  <td about="./OSL-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">OSL-1.1</code></td>
  <td align="center"></td>
  <td><a href="./OSL-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OSL-2.0.html" rel="rdf:_247">Open Software License 2.0</a></td>
  <td about="./OSL-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">OSL-2.0</code></td>
  <td align="center">Y</td>
  <td><a href="./OSL-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OSL-2.1.html" rel="rdf:_248">Open Software License 2.1</a></td>
  <td about="./OSL-2.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">OSL-2.1</code></td>
  <td align="center">Y</td>
  <td><a href="./OSL-2.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OSL-3.0.html" rel="rdf:_249">Open Software License 3.0</a></td>
  <td about="./OSL-3.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">OSL-3.0</code></td>
  <td align="center">Y</td>
  <td><a href="./OSL-3.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OpenSSL.html" rel="rdf:_250">OpenSSL License</a></td>
  <td about="./OpenSSL.html" typeof="spdx:License">
  <code property="spdx:licenseId">OpenSSL</code></td>
  <td align="center"></td>
  <td><a href="./OpenSSL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OSET-PL-2.1.html" rel="rdf:_251">OSET Public License version 2.1</a></td>
  <td about="./OSET-PL-2.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">OSET-PL-2.1</code></td>
  <td align="center">Y</td>
  <td><a href="./OSET-PL-2.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./PHP-3.0.html" rel="rdf:_252">PHP License v3.0</a></td>
  <td about="./PHP-3.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">PHP-3.0</code></td>
  <td align="center">Y</td>
  <td><a href="./PHP-3.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./PHP-3.01.html" rel="rdf:_253">PHP License v3.01</a></td>
  <td about="./PHP-3.01.html" typeof="spdx:License">
  <code property="spdx:licenseId">PHP-3.01</code></td>
  <td align="center"></td>
  <td><a href="./PHP-3.01.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Plexus.html" rel="rdf:_254">Plexus Classworlds License</a></td>
  <td about="./Plexus.html" typeof="spdx:License">
  <code property="spdx:licenseId">Plexus</code></td>
  <td align="center"></td>
  <td><a href="./Plexus.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./PostgreSQL.html" rel="rdf:_255">PostgreSQL License</a></td>
  <td about="./PostgreSQL.html" typeof="spdx:License">
  <code property="spdx:licenseId">PostgreSQL</code></td>
  <td align="center">Y</td>
  <td><a href="./PostgreSQL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./psfrag.html" rel="rdf:_256">psfrag License</a></td>
  <td about="./psfrag.html" typeof="spdx:License">
  <code property="spdx:licenseId">psfrag</code></td>
  <td align="center"></td>
  <td><a href="./psfrag.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./psutils.html" rel="rdf:_257">psutils License</a></td>
  <td about="./psutils.html" typeof="spdx:License">
  <code property="spdx:licenseId">psutils</code></td>
  <td align="center"></td>
  <td><a href="./psutils.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Python-2.0.html" rel="rdf:_258">Python License 2.0</a></td>
  <td about="./Python-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">Python-2.0</code></td>
  <td align="center">Y</td>
  <td><a href="./Python-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./QPL-1.0.html" rel="rdf:_259">Q Public License 1.0</a></td>
  <td about="./QPL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">QPL-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./QPL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Qhull.html" rel="rdf:_260">Qhull License</a></td>
  <td about="./Qhull.html" typeof="spdx:License">
  <code property="spdx:licenseId">Qhull</code></td>
  <td align="center"></td>
  <td><a href="./Qhull.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Rdisc.html" rel="rdf:_261">Rdisc License</a></td>
  <td about="./Rdisc.html" typeof="spdx:License">
  <code property="spdx:licenseId">Rdisc</code></td>
  <td align="center"></td>
  <td><a href="./Rdisc.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./RPSL-1.0.html" rel="rdf:_262">RealNetworks Public Source License v1.0</a></td>
  <td about="./RPSL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">RPSL-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./RPSL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./RPL-1.1.html" rel="rdf:_263">Reciprocal Public License 1.1</a></td>
  <td about="./RPL-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">RPL-1.1</code></td>
  <td align="center">Y</td>
  <td><a href="./RPL-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./RPL-1.5.html" rel="rdf:_264">Reciprocal Public License 1.5</a></td>
  <td about="./RPL-1.5.html" typeof="spdx:License">
  <code property="spdx:licenseId">RPL-1.5</code></td>
  <td align="center">Y</td>
  <td><a href="./RPL-1.5.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./RHeCos-1.1.html" rel="rdf:_265">Red Hat eCos Public License v1.1</a></td>
  <td about="./RHeCos-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">RHeCos-1.1</code></td>
  <td align="center"></td>
  <td><a href="./RHeCos-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./RSCPL.html" rel="rdf:_266">Ricoh Source Code Public License</a></td>
  <td about="./RSCPL.html" typeof="spdx:License">
  <code property="spdx:licenseId">RSCPL</code></td>
  <td align="center">Y</td>
  <td><a href="./RSCPL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./RSA-MD.html" rel="rdf:_267">RSA Message-Digest License </a></td>
  <td about="./RSA-MD.html" typeof="spdx:License">
  <code property="spdx:licenseId">RSA-MD</code></td>
  <td align="center"></td>
  <td><a href="./RSA-MD.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Ruby.html" rel="rdf:_268">Ruby License</a></td>
  <td about="./Ruby.html" typeof="spdx:License">
  <code property="spdx:licenseId">Ruby</code></td>
  <td align="center"></td>
  <td><a href="./Ruby.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./SAX-PD.html" rel="rdf:_269">Sax Public Domain Notice</a></td>
  <td about="./SAX-PD.html" typeof="spdx:License">
  <code property="spdx:licenseId">SAX-PD</code></td>
  <td align="center"></td>
  <td><a href="./SAX-PD.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Saxpath.html" rel="rdf:_270">Saxpath License</a></td>
  <td about="./Saxpath.html" typeof="spdx:License">
  <code property="spdx:licenseId">Saxpath</code></td>
  <td align="center"></td>
  <td><a href="./Saxpath.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./SCEA.html" rel="rdf:_271">SCEA Shared Source License</a></td>
  <td about="./SCEA.html" typeof="spdx:License">
  <code property="spdx:licenseId">SCEA</code></td>
  <td align="center"></td>
  <td><a href="./SCEA.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./SWL.html" rel="rdf:_272">Scheme Widget Library (SWL) Software License Agreement</a></td>
  <td about="./SWL.html" typeof="spdx:License">
  <code property="spdx:licenseId">SWL</code></td>
  <td align="center"></td>
  <td><a href="./SWL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./SMPPL.html" rel="rdf:_273">Secure Messaging Protocol Public License</a></td>
  <td about="./SMPPL.html" typeof="spdx:License">
  <code property="spdx:licenseId">SMPPL</code></td>
  <td align="center"></td>
  <td><a href="./SMPPL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Sendmail.html" rel="rdf:_274">Sendmail License</a></td>
  <td about="./Sendmail.html" typeof="spdx:License">
  <code property="spdx:licenseId">Sendmail</code></td>
  <td align="center"></td>
  <td><a href="./Sendmail.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./SGI-B-1.0.html" rel="rdf:_275">SGI Free Software License B v1.0</a></td>
  <td about="./SGI-B-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">SGI-B-1.0</code></td>
  <td align="center"></td>
  <td><a href="./SGI-B-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./SGI-B-1.1.html" rel="rdf:_276">SGI Free Software License B v1.1</a></td>
  <td about="./SGI-B-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">SGI-B-1.1</code></td>
  <td align="center"></td>
  <td><a href="./SGI-B-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./SGI-B-2.0.html" rel="rdf:_277">SGI Free Software License B v2.0</a></td>
  <td about="./SGI-B-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">SGI-B-2.0</code></td>
  <td align="center"></td>
  <td><a href="./SGI-B-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OFL-1.0.html" rel="rdf:_278">SIL Open Font License 1.0</a></td>
  <td about="./OFL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">OFL-1.0</code></td>
  <td align="center"></td>
  <td><a href="./OFL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./OFL-1.1.html" rel="rdf:_279">SIL Open Font License 1.1</a></td>
  <td about="./OFL-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">OFL-1.1</code></td>
  <td align="center">Y</td>
  <td><a href="./OFL-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./SimPL-2.0.html" rel="rdf:_280">Simple Public License 2.0</a></td>
  <td about="./SimPL-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">SimPL-2.0</code></td>
  <td align="center">Y</td>
  <td><a href="./SimPL-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Sleepycat.html" rel="rdf:_281">Sleepycat License</a></td>
  <td about="./Sleepycat.html" typeof="spdx:License">
  <code property="spdx:licenseId">Sleepycat</code></td>
  <td align="center">Y</td>
  <td><a href="./Sleepycat.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./SNIA.html" rel="rdf:_282">SNIA Public License 1.1</a></td>
  <td about="./SNIA.html" typeof="spdx:License">
  <code property="spdx:licenseId">SNIA</code></td>
  <td align="center"></td>
  <td><a href="./SNIA.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Spencer-86.html" rel="rdf:_283">Spencer License 86</a></td>
  <td about="./Spencer-86.html" typeof="spdx:License">
  <code property="spdx:licenseId">Spencer-86</code></td>
  <td align="center"></td>
  <td><a href="./Spencer-86.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Spencer-94.html" rel="rdf:_284">Spencer License 94</a></td>
  <td about="./Spencer-94.html" typeof="spdx:License">
  <code property="spdx:licenseId">Spencer-94</code></td>
  <td align="center"></td>
  <td><a href="./Spencer-94.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Spencer-99.html" rel="rdf:_285">Spencer License 99</a></td>
  <td about="./Spencer-99.html" typeof="spdx:License">
  <code property="spdx:licenseId">Spencer-99</code></td>
  <td align="center"></td>
  <td><a href="./Spencer-99.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./SMLNJ.html" rel="rdf:_286">Standard ML of New Jersey License</a></td>
  <td about="./SMLNJ.html" typeof="spdx:License">
  <code property="spdx:licenseId">SMLNJ</code></td>
  <td align="center"></td>
  <td><a href="./SMLNJ.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./SugarCRM-1.1.3.html" rel="rdf:_287">SugarCRM Public License v1.1.3</a></td>
  <td about="./SugarCRM-1.1.3.html" typeof="spdx:License">
  <code property="spdx:licenseId">SugarCRM-1.1.3</code></td>
  <td align="center"></td>
  <td><a href="./SugarCRM-1.1.3.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./SISSL.html" rel="rdf:_288">Sun Industry Standards Source License v1.1</a></td>
  <td about="./SISSL.html" typeof="spdx:License">
  <code property="spdx:licenseId">SISSL</code></td>
  <td align="center">Y</td>
  <td><a href="./SISSL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./SISSL-1.2.html" rel="rdf:_289">Sun Industry Standards Source License v1.2</a></td>
  <td about="./SISSL-1.2.html" typeof="spdx:License">
  <code property="spdx:licenseId">SISSL-1.2</code></td>
  <td align="center"></td>
  <td><a href="./SISSL-1.2.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./SPL-1.0.html" rel="rdf:_290">Sun Public License v1.0</a></td>
  <td about="./SPL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">SPL-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./SPL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Watcom-1.0.html" rel="rdf:_291">Sybase Open Watcom Public License 1.0</a></td>
  <td about="./Watcom-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">Watcom-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./Watcom-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./TCL.html" rel="rdf:_292">TCL/TK License</a></td>
  <td about="./TCL.html" typeof="spdx:License">
  <code property="spdx:licenseId">TCL</code></td>
  <td align="center"></td>
  <td><a href="./TCL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./TCP-wrappers.html" rel="rdf:_293">TCP Wrappers License</a></td>
  <td about="./TCP-wrappers.html" typeof="spdx:License">
  <code property="spdx:licenseId">TCP-wrappers</code></td>
  <td align="center"></td>
  <td><a href="./TCP-wrappers.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Unlicense.html" rel="rdf:_294">The Unlicense</a></td>
  <td about="./Unlicense.html" typeof="spdx:License">
  <code property="spdx:licenseId">Unlicense</code></td>
  <td align="center"></td>
  <td><a href="./Unlicense.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./TMate.html" rel="rdf:_295">TMate Open Source License</a></td>
  <td about="./TMate.html" typeof="spdx:License">
  <code property="spdx:licenseId">TMate</code></td>
  <td align="center"></td>
  <td><a href="./TMate.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./TORQUE-1.1.html" rel="rdf:_296">TORQUE v2.5+ Software License v1.1</a></td>
  <td about="./TORQUE-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">TORQUE-1.1</code></td>
  <td align="center"></td>
  <td><a href="./TORQUE-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./TOSL.html" rel="rdf:_297">Trusster Open Source License</a></td>
  <td about="./TOSL.html" typeof="spdx:License">
  <code property="spdx:licenseId">TOSL</code></td>
  <td align="center"></td>
  <td><a href="./TOSL.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Unicode-DFS-2015.html" rel="rdf:_298">Unicode License Agreement - Data Files and Software (2015)</a></td>
  <td about="./Unicode-DFS-2015.html" typeof="spdx:License">
  <code property="spdx:licenseId">Unicode-DFS-2015</code></td>
  <td align="center"></td>
  <td><a href="./Unicode-DFS-2015.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Unicode-DFS-2016.html" rel="rdf:_299">Unicode License Agreement - Data Files and Software (2016)</a></td>
  <td about="./Unicode-DFS-2016.html" typeof="spdx:License">
  <code property="spdx:licenseId">Unicode-DFS-2016</code></td>
  <td align="center"></td>
  <td><a href="./Unicode-DFS-2016.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Unicode-TOU.html" rel="rdf:_300">Unicode Terms of Use</a></td>
  <td about="./Unicode-TOU.html" typeof="spdx:License">
  <code property="spdx:licenseId">Unicode-TOU</code></td>
  <td align="center"></td>
  <td><a href="./Unicode-TOU.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./UPL-1.0.html" rel="rdf:_301">Universal Permissive License v1.0</a></td>
  <td about="./UPL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">UPL-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./UPL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./NCSA.html" rel="rdf:_302">University of Illinois/NCSA Open Source License</a></td>
  <td about="./NCSA.html" typeof="spdx:License">
  <code property="spdx:licenseId">NCSA</code></td>
  <td align="center">Y</td>
  <td><a href="./NCSA.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Vim.html" rel="rdf:_303">Vim License</a></td>
  <td about="./Vim.html" typeof="spdx:License">
  <code property="spdx:licenseId">Vim</code></td>
  <td align="center"></td>
  <td><a href="./Vim.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./VOSTROM.html" rel="rdf:_304">VOSTROM Public License for Open Source</a></td>
  <td about="./VOSTROM.html" typeof="spdx:License">
  <code property="spdx:licenseId">VOSTROM</code></td>
  <td align="center"></td>
  <td><a href="./VOSTROM.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./VSL-1.0.html" rel="rdf:_305">Vovida Software License v1.0</a></td>
  <td about="./VSL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">VSL-1.0</code></td>
  <td align="center">Y</td>
  <td><a href="./VSL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./W3C-20150513.html" rel="rdf:_306">W3C Software Notice and Document License (2015-05-13)</a></td>
  <td about="./W3C-20150513.html" typeof="spdx:License">
  <code property="spdx:licenseId">W3C-20150513</code></td>
  <td align="center"></td>
  <td><a href="./W3C-20150513.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./W3C-19980720.html" rel="rdf:_307">W3C Software Notice and License (1998-07-20)</a></td>
  <td about="./W3C-19980720.html" typeof="spdx:License">
  <code property="spdx:licenseId">W3C-19980720</code></td>
  <td align="center"></td>
  <td><a href="./W3C-19980720.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./W3C.html" rel="rdf:_308">W3C Software Notice and License (2002-12-31)</a></td>
  <td about="./W3C.html" typeof="spdx:License">
  <code property="spdx:licenseId">W3C</code></td>
  <td align="center">Y</td>
  <td><a href="./W3C.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Wsuipa.html" rel="rdf:_309">Wsuipa License</a></td>
  <td about="./Wsuipa.html" typeof="spdx:License">
  <code property="spdx:licenseId">Wsuipa</code></td>
  <td align="center"></td>
  <td><a href="./Wsuipa.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Xnet.html" rel="rdf:_310">X.Net License</a></td>
  <td about="./Xnet.html" typeof="spdx:License">
  <code property="spdx:licenseId">Xnet</code></td>
  <td align="center">Y</td>
  <td><a href="./Xnet.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./X11.html" rel="rdf:_311">X11 License</a></td>
  <td about="./X11.html" typeof="spdx:License">
  <code property="spdx:licenseId">X11</code></td>
  <td align="center"></td>
  <td><a href="./X11.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Xerox.html" rel="rdf:_312">Xerox License</a></td>
  <td about="./Xerox.html" typeof="spdx:License">
  <code property="spdx:licenseId">Xerox</code></td>
  <td align="center"></td>
  <td><a href="./Xerox.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./XFree86-1.1.html" rel="rdf:_313">XFree86 License 1.1</a></td>
  <td about="./XFree86-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">XFree86-1.1</code></td>
  <td align="center"></td>
  <td><a href="./XFree86-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./xinetd.html" rel="rdf:_314">xinetd License</a></td>
  <td about="./xinetd.html" typeof="spdx:License">
  <code property="spdx:licenseId">xinetd</code></td>
  <td align="center"></td>
  <td><a href="./xinetd.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./xpp.html" rel="rdf:_315">XPP License</a></td>
  <td about="./xpp.html" typeof="spdx:License">
  <code property="spdx:licenseId">xpp</code></td>
  <td align="center"></td>
  <td><a href="./xpp.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./XSkat.html" rel="rdf:_316">XSkat License</a></td>
  <td about="./XSkat.html" typeof="spdx:License">
  <code property="spdx:licenseId">XSkat</code></td>
  <td align="center"></td>
  <td><a href="./XSkat.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./YPL-1.0.html" rel="rdf:_317">Yahoo! Public License v1.0</a></td>
  <td about="./YPL-1.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">YPL-1.0</code></td>
  <td align="center"></td>
  <td><a href="./YPL-1.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./YPL-1.1.html" rel="rdf:_318">Yahoo! Public License v1.1</a></td>
  <td about="./YPL-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">YPL-1.1</code></td>
  <td align="center"></td>
  <td><a href="./YPL-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Zed.html" rel="rdf:_319">Zed License</a></td>
  <td about="./Zed.html" typeof="spdx:License">
  <code property="spdx:licenseId">Zed</code></td>
  <td align="center"></td>
  <td><a href="./Zed.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Zend-2.0.html" rel="rdf:_320">Zend License v2.0</a></td>
  <td about="./Zend-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">Zend-2.0</code></td>
  <td align="center"></td>
  <td><a href="./Zend-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Zimbra-1.3.html" rel="rdf:_321">Zimbra Public License v1.3</a></td>
  <td about="./Zimbra-1.3.html" typeof="spdx:License">
  <code property="spdx:licenseId">Zimbra-1.3</code></td>
  <td align="center"></td>
  <td><a href="./Zimbra-1.3.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Zimbra-1.4.html" rel="rdf:_322">Zimbra Public License v1.4</a></td>
  <td about="./Zimbra-1.4.html" typeof="spdx:License">
  <code property="spdx:licenseId">Zimbra-1.4</code></td>
  <td align="center"></td>
  <td><a href="./Zimbra-1.4.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./Zlib.html" rel="rdf:_323">zlib License</a></td>
  <td about="./Zlib.html" typeof="spdx:License">
  <code property="spdx:licenseId">Zlib</code></td>
  <td align="center">Y</td>
  <td><a href="./Zlib.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./zlib-acknowledgement.html" rel="rdf:_324">zlib/libpng License with Acknowledgement</a></td>
  <td about="./zlib-acknowledgement.html" typeof="spdx:License">
  <code property="spdx:licenseId">zlib-acknowledgement</code></td>
  <td align="center"></td>
  <td><a href="./zlib-acknowledgement.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./ZPL-1.1.html" rel="rdf:_325">Zope Public License 1.1</a></td>
  <td about="./ZPL-1.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">ZPL-1.1</code></td>
  <td align="center"></td>
  <td><a href="./ZPL-1.1.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./ZPL-2.0.html" rel="rdf:_326">Zope Public License 2.0</a></td>
  <td about="./ZPL-2.0.html" typeof="spdx:License">
  <code property="spdx:licenseId">ZPL-2.0</code></td>
  <td align="center">Y</td>
  <td><a href="./ZPL-2.0.html#licenseText">License Text</a></td>
</tr>
<tr>
  <td><a href="./ZPL-2.1.html" rel="rdf:_327">Zope Public License 2.1</a></td>
  <td about="./ZPL-2.1.html" typeof="spdx:License">
  <code property="spdx:licenseId">ZPL-2.1</code></td>
  <td align="center"></td>
  <td><a href="./ZPL-2.1.html#licenseText">License Text</a></td>
</tr>
'''


licenses = re.findall('href="\./(.*.html)"', data)
wanted = ["MIT", "GPL-1.0", "GPL-2.0", "GPL-3.0", "Apache-1.0", "Apache-1.1", "Apache-2.0", "BSD-2-Clause-FreeBSD", "BSD-2-Clause-NetBSD", "BSD-2-Clause", "BSD-3-Clause-Attribution", "BSD-3-Clause-Clear", "ISC", "Artistic-1.0-cl8", "Artistic-1.0-Perl", "Artistic-1.0", "Artistic-2.0", "LGPL-2.0", "LGPL-2.1", "LGPL-3.0", "EPL-1.0", "MS-PL", "MS-RL", "CPOL-1.02", "MPL-1.0", "MPL-1.1", "MPL-2.0-no-copyleft-exception", "MPL-2.0", "AGPL-3.0", "CDDL-1.0", "CDDL-1.1", "WTFPL", "zlib-acknowledgement", "Zlib", "Fair-Source-0.9"]

# for license in [x for x in licenses if x in [y + '.html' for y in wanted]]:
for license in licenses:

    print 'Getting', license
    r = requests.get('https://spdx.org/licenses/' + license)

    with codecs.open(license, 'w', 'utf-8-sig') as myfile:
        myfile.write(r.text)
