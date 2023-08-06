# multi-gallery-dl
for each sub dir in a specified dir, call gallery-dl (or a different program) on that specified dir


for example, lets say you have the dir structure:
gallery-dl
|e621
||artist1
||artist2
||artist3
|gelbooru
||artist4
||artist5
||artist6

with the main program sitting inside gallery-dl, you can run
  $ ./multi-gallery-dl.py e621/ -u 'https://e621.net/posts?tags=' -r --options '--sleep 2 --sleep-request 2'
it will then loop through each subdir inside of e621, and call gallery-dl on that directory (while staying inside the directory just above gallery-dl)

you dont have to use gallery-dl, however, it can work with other programs like yt-dlp!
take for example this set of folders
|pornhub
||model1
||model2
||model3

we can use the command
  $ ./multi-gallery-dl.py "pornhub/" --program "yt-dlp" -u "https://www.pornhub.com/model/" -r --options "-f best --restrict-filenames" --moveintodir

when the option moveintodir is specified, the program will step inside of (lets say ./gallery-dl/pornhub/model1/) before executing the command: yt-dlp -f best --restrict-filenames https://www.pornhub.com/model/model1







help text:
usage: multi-dir gallery-dl syncer thingy [-h] -u URLPREFIX
                                          [--notrailingslash]
                                          [--options OPTIONS]
                                          [--program PROGRAM]
                                          [--urlpostfix URLPOSTFIX] [-r]
                                          [-g GALLERYDLDIR] [--moveintodir]
                                          dirname

  Allows you to manage multiple gallery-dl download dirs in a specified directory, i.e.
  given a specified directory AND url prefix
  gallery-dl will be ran on each directory as such: "gallery-dl --sleep 2 --sleep-request 2 URL_PREFIX+DIRECTORY+URL_POSTFIX
  
  EXAMPLES:
   ./program_name twitter/ -u https://www.twitter.com/
   ./program_name twitter/ -u https://www.twitter.com/ -r
   ./multi-gallery-dl.py "pornhub/" --program "yt-dlp" -u "https://www.pornhub.com/model/" -r --options "-f best --restrict-filenames" --moveintodir

positional arguments:
  dirname               main directory to search for other directories within

options:
  -h, --help            show this help message and exit
  -u URLPREFIX, --urlprefix URLPREFIX
                        the base url (example: "https://twitter.com/")
  --notrailingslash     by default the program will force a trailing slash onto the urlpostfix argument, specifying this arument disables that.
  --options OPTIONS     extra options to pass to gallery-dl
  --program PROGRAM     the actual program to run (defaults to "gallery-dl")
  --urlpostfix URLPOSTFIX, --postfix URLPOSTFIX
                        extra stuff to add to the end of the url
  -r, --random          randomize order of directories (default=True)
  -g GALLERYDLDIR, --gallerydldir GALLERYDLDIR
                        directory to gallery-dl (defaults to current dir)
  --moveintodir         move into target directory before downloading (by default it will stay in the directory just above this one (which should usually be gallery-dl if you are running this with that program in mind and needed to function correctly)
