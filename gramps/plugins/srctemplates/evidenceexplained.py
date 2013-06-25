# -*- coding: utf-8 -*-
#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2013       Benny Malengier
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

# $Id$

"""
Registering srctemplates for GRAMPS.
"""

from gramps.gen.const import GRAMPS_LOCALE as glocale
_ = glocale.translation.gettext

import os
from functools import partial

from gramps.gen.const import DATA_DIR
#
# SrcTemplates distributed with Gramps
#

# Add EE styles to the src templates defined
#the csv file with the template definitions
path_csv = partial(os.path.join, DATA_DIR, "evidencestyle")
csvfile = path_csv('evidence_style.csv')

#name of this style
style = 'EE'

#strings to translate
#following translations are generated with extract_trans_csv.py
if False:
    #these translations will only occur when needed first time!
    _("1790-1840")
    _("1850-1860: slaves")
    _("1850-1870")
    _("1880-1930")
    _("Abstracts")
    _("Administrative material")
    _("Appeals court record books")
    _("Application file")
    _("Archival preservation copy")
    _("Archived Material")
    _("Archived in-house")
    _("Archived off-site")
    _("Archives & Artifacts")
    _("Artifact")
    _("Audio book")
    _("Audio recordings")
    _("Basic Format")
    _("Blogs")
    _("Book")
    _("Book:")
    _("Bound volume")
    _("Broadcasts & Web Miscellanea")
    _("Business & institutional Records")
    _("CD-ROM publication")
    _("CD/DVD")
    _("CD/DVD book (text)")
    _("CD/DVD publication")
    _("Case Reporters")
    _("Case files")
    _("Cemetery Office Records")
    _("Cemetery Records")
    _("Cemetery abstracts")
    _("Census Records")
    _("Church Books")
    _("Church Records")
    _("Church record book, recopied")
    _("Church-issued certificate")
    _("Church-records database")
    _("Citing volume from title page")
    _("Codes & statutes, online")
    _("Collection, emphasis on")
    _("Congressional Records")
    _("Corporate Records")
    _("Database")
    _("Database online")
    _("Databases")
    _("Derivatives")
    _("Descriptive pamphlet, online")
    _("Diary or journal, etc.")
    _("Digital Archives")
    _("Digital Images")
    _("Digitized online")
    _("Discussion forums & lists")
    _("Document (loose record)")
    _("Document, emphasis on")
    _("Electronic Publications")
    _("Extract supplied by staff")
    _("FHL-GSU film")
    _("FHL-GSU preservation")
    _("FHL-GSU preservation copy")
    _("FHL-GSU preservation film")
    _("Family Bible Records")
    _("Family Chart or Group Sheet")
    _("File items")
    _("Files moved to state archives")
    _("France")
    _("Genetic testing")
    _("Grave markers")
    _("Historic letter")
    _("Historical research: corporate")
    _("Historical research: online")
    _("Image Copies")
    _("Images online")
    _("In-house film")
    _("Interview tape & transcript")
    _("Journal articles")
    _("LDS records at FHL")
    _("Land warrants: loose")
    _("Land-grant register")
    _("Leaflet")
    _("Legal Reference Works")
    _("Legal document, unrecorded")
    _("Legislative petitions & files")
    _("Library of Congress")
    _("Lineage-society Records")
    _("Local")
    _("Local & State Records: Courts & Governance")
    _("Local & State Records: Licenses, Registrations, Rolls & Vital Records")
    _("Local & State Records: Property & Probates")
    _("Local Records")
    _("Local copy")
    _("Magazine articles")
    _("Manuscript Records")
    _("Manuscripts")
    _("Map")
    _("Maps")
    _("Markers & Memorials (Originals)")
    _("Memorial plaques")
    _("Microfilm")
    _("Microfilm (U.S.)")
    _("Microfilm publication")
    _("Miscellaneous file")
    _("NARA Style citation")
    _("NARA film")
    _("Named volume")
    _("National Archives")
    _("National Archives (Australia)")
    _("National Archives (Canada)")
    _("National Archives (U.K.)")
    _("National Archives (U.S.)")
    _("National Archives (U.S.) guides")
    _("National Archives copy")
    _("National Archives microfilm")
    _("National Archives-Regional")
    _("National Government Records")
    _("Native-American tribal census")
    _("Newsletter articles")
    _("Newspaper articles")
    _("Nonpopulation schedules")
    _("Numbered volume")
    _("Office records")
    _("Online")
    _("Online archives")
    _("Online archives of print journals")
    _("Online commercial site")
    _("Online database")
    _("Online image")
    _("Online images")
    _("Online journals")
    _("Online publication")
    _("Online reprints, random items")
    _("Online:")
    _("Organizational Records")
    _("Original Materials (U.S.)")
    _("Original Records")
    _("Original manuscripts (U.S.)")
    _("Patent & Trademark Office (U.S.)")
    _("Periodicals")
    _("Personal Bible")
    _("Personal correspondence")
    _("Personal e-mail")
    _("Photographs")
    _("Podcasts")
    _("Population schedules")
    _("Portrait")
    _("Preliminary inventory, microfilmed")
    _("Preservation Film")
    _("Preservation film, FHL-GSU")
    _("Print Publications")
    _("Print editions")
    _("Printed Government Documents")
    _("Private Holdings")
    _("Professional Reports")
    _("Publications Style citation")
    _("Publications: Books, CDs, Maps, Leaflets & Videos")
    _("Publications: Legal Works & Government Documents")
    _("Publications: Periodicals, Broadcasts & Web Miscellanea")
    _("Radio & television clips")
    _("Railroad Retirement Board")
    _("Record Books")
    _("Record Books, archived off-site")
    _("Registers")
    _("Research Report")
    _("School Records")
    _("Series named for editor")
    _("Series, emphasis on")
    _("Slip laws:")
    _("Social Security Administration")
    _("Soundex & Miracode, microfilm")
    _("Standardized series")
    _("State database")
    _("State level")
    _("State-level")
    _("State-level Records")
    _("State-level copies")
    _("State-sponsored censuses")
    _("Statistical database")
    _("Statutes:")
    _("Student transcript")
    _("Tract book")
    _("Tradition, recorded")
    _("Traditional academic style")
    _("U.K. Wales")
    _("U.S. Code")
    _("UNC microfilm publication")
    _("Unpublished narrative")
    _("Vertical file")
    _("Video")
    _("Vital records, amended")
    _("Vital records, delayed")
    _("Vital-records certificate")
    _("Vital-records register")
    _("Website as book")
    _("archived off-site")
    _("basic format")
    _("card file")
    _("chapter")
    _("edited")
    _("federal")
    _("federal census")
    _("held by church")
    _("multivolume set")
    _("online")
    _("personally used")
    _("reprint")
    _("revised edition")
    _("rural")
    _("state")
    _("supplied by staff")
    _("urban")
    _("vertical file")

