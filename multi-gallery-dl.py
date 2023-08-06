#!/usr/bin/python3
import os
import random
import time
import argparse

parser = argparse.ArgumentParser(
 prog = 'multi-dir gallery-dl syncer thingy',
 description = '''
  Allows you to manage multiple gallery-dl download dirs in a specified directory, i.e.
  given a specified directory AND url prefix
  gallery-dl will be ran on each directory as such: "gallery-dl --sleep 2 --sleep-request 2 URL_PREFIX+DIRECTORY+URL_POSTFIX
  
  EXAMPLES:
   ./program_name twitter/ -u https://www.twitter.com/
   ./program_name twitter/ -u https://www.twitter.com/ -r
   ./multi-gallery-dl.py "pornhub/" --program "yt-dlp" -u "https://www.pornhub.com/model/" -r --options "-f best --restrict-filenames" --moveintodir

''',
 formatter_class=argparse.RawTextHelpFormatter
)

parser.add_argument( "dirname", help = 'main directory to search for other directories within' )
parser.add_argument( '-u', '--urlprefix', help = 'the base url (example: "https://twitter.com/")', required = True)
parser.add_argument( '--notrailingslash', help = 'by default the program will force a trailing slash onto the urlpostfix argument, specifying this arument disables that.', required = False, action = 'store_true', default = False )
parser.add_argument( '--options', help = 'extra options to pass to gallery-dl', required = False, default = "" )

parser.add_argument( '--program', help = 'the actual program to run (defaults to "gallery-dl")', required = False, default = "gallery-dl" )

parser.add_argument( '--urlpostfix', '--postfix', help = 'extra stuff to add to the end of the url', required = False, default = "")
parser.add_argument( '-r', '--random', help = 'randomize order of directories (default=True)', required = False, action = 'store_true', default = False )
parser.add_argument( '-g', '--gallerydldir', help = 'directory to gallery-dl (defaults to current dir)', required = False, default = os.getcwd() )

parser.add_argument( '--moveintodir', help = 'move into target directory before downloading (by default it will stay in the directory just above this one (which should usually be gallery-dl if you are running this with that program in mind and needed to function correctly)', required = False, action = 'store_true', default = False )

args = parser.parse_args()
args.dirname = os.path.abspath( args.dirname )


do_random_order = args.random

PORN_DIR = args.dirname
START_DIR = args.gallerydldir

URL_PREFIX = args.urlprefix
URL_POSTFIX = args.urlpostfix

#ensure that URL_PREFIX ends with '/'
if URL_PREFIX[ len(URL_PREFIX)-1 ] != '/' and not args.notrailingslash:
 URL_PREFIX = URL_PREFIX + '/'
 args.urlprefix = URL_PREFIX

#and do the same for dirname, PORN_DIR
if PORN_DIR[ len(PORN_DIR)-1 ] != '/':
 PORN_DIR = PORN_DIR + '/'
 args.dirname = PORN_DIR

def get_dir_list( i ):
 items = os.listdir( i )
 for item in items:
  if not os.path.isdir( os.path.join( i, item ) ):
   items.remove( item )
 return( items )

if os.path.exists( PORN_DIR ): print( PORN_DIR + " exists and is directory, all good!" )
else:
 print( PORN_DIR + " direcrory not found" )
 exit()

dir_list = get_dir_list( PORN_DIR )
if do_random_order: random.shuffle( dir_list )

os.chdir( os.path.join( START_DIR, ".." ) )


for i in dir_list:
 
 if args.moveintodir:
  os.chdir( os.path.join( START_DIR, PORN_DIR, i ) )
 
 cmd = args.program + " " + args.options + " \"" + URL_PREFIX + i + URL_POSTFIX + "\""
 print( cmd )
 os.system( cmd )
 time.sleep(1) #makes it easier to ctrl-c out of script

'''
original bash script without randomization (base64)

IyEvdXNyL2Jpbi9iYXNoCgpQT1JOX0RJUj0idHdpdHRlciIKCmlmIFsgLWQgIiRQT1JOX0RJUiIg
XTsKdGhlbgogZWNobyAkUE9STl9ESVIgZXhpc3RzIGFuZCBpcyBkaXJlY3RvcnksIGFsbCBnb29k
IQplbHNlCiBlY2hvICRQT1JOX0RJUiBkaXJlY3Jvcnkgbm90IGZvdW5kCiBta2RpciAiJFBPUk5f
RElSIgpmaQoKY2QgJFBPUk5fRElSCgpmb3IgaSBpbiAqOwpkbwogaWYgWyAtZCAiJGkiIF07CiB0
aGVuCiAgY2QgLi4vLi4KICBnYWxsZXJ5LWRsIC0tc2xlZXAgMiAtLXNsZWVwLXJlcXVlc3QgMiAi
aHR0cHM6Ly90d2l0dGVyLmNvbS8kaSIKICBjZCBnYWxsZXJ5LWRsLyRQT1JOX0RJUgogZmk7CmRv
bmUKCmNkIC4uCg==

'''
