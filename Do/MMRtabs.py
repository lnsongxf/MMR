# MMRtabs.py v0.00               damiancclarke             yyyy-mm-dd:2014-12-30
#---|----1----|----2----|----3----|----4----|----5----|----6----|----7----|----8
#
# This script takes summary statistics and regressions results sent out from the 
# scripts analysisMMR.do and XXXXXXXXX.do, and formats them as tables for inclu-
# sion in the paper Maternal Education and Maternal Mortality: Evidence from a
# Large Panel and Various Natural Experiments.
# 
# The script is written for Python version 2.x, and its usage is:
#
#    python MMRtabs.py tex
#    python MMRtabs.py csv
#
# depending upon whether tables should be output in LaTeX format, or as csv form-
# for inclusion in excel/word documents.
#
# contact mailto:damian.clarke@economics.ox.ac.uk

from sys import argv
import re, os
import locale
locale.setlocale(locale.LC_ALL, 'en_US')

script, ftype = argv
print '\n The script %s is making %s files \n' %(script, ftype)

#-------------------------------------------------------------------------------
# --- (1) File names
#-------------------------------------------------------------------------------
result = '~/investigacion/Activa/MMR/Results/tables'
tables = '~/investigacion/Activa/MMR/Paper/tables'

sums = 'SumStats.xls'
mmra = 'CrossCountry_female.xls'
regn = 'CrossCountry_region.xls'
incm = 'CrossCountry_income.xls'
corr = 'Zscores_female.xls'
gend = 'CrossCountry_gender.xls'
mmry = 'CrossCountry_female_yrs.xls'
mmrs = 'CrossCountry_female_yrssq.xls'
gens =  'CrossCountry_gender_yrssq.xls'

#-------------------------------------------------------------------------------
# --- (2) csv or tex options
#-------------------------------------------------------------------------------
if ftype=='tex':
    dd = '&'
    dd1  = "&\\begin{footnotesize}"
    dd2  = "\\end{footnotesize}&\\begin{footnotesize}"
    dd3  = "\\end{footnotesize}"
    end  = "tex"
    foot = "$^{*}$p$<$0.1; $^{**}$p$<$0.05; $^{***}$p$<$0.01"
    ls   = "\\\\"
    mr   = '\\midrule'
    hr   = '\\hline'
    tr   = '\\toprule'
    br   = '\\bottomrule'
    mc1  = '\\multicolumn{'
    mcsc = '}{l}{\\textsc{'
    mcbf = '}{l}{\\textbf{'
    mc2  = '}}'

elif ftyoe=='csv':
    dd = ';'
    dd1  = ";"
    dd2  = ";"
    dd3  = ";"
    end  = "csv"
    foot = "* p<0.1, ** p<0.05, *** p<0.01"
    ls   = ""
    mr   = ""
    hr   = ""
    br   = ""
    tr   = ""
    mc1  = ''
    mcsc = ''
    mcbf = ''
    mc2  = ''
