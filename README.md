# multi-gallery-dl<br>
for each sub dir in a specified dir, call gallery-dl (or a different program) on that specified dir<br>
<br>
<br>
for example, lets say you have the dir structure:<br>
gallery-dl<br>
|e621<br>
||artist1<br>
||artist2<br>
||artist3<br>
|gelbooru<br>
||artist4<br>
||artist5<br>
||artist6<br>
<br>
with the main program sitting inside gallery-dl, you can run<br>
  $ ./multi-gallery-dl.py e621/ -u 'https://e621.net/posts?tags=' -r --options '--sleep 2 --sleep-request 2'<br>
it will then loop through each subdir inside of e621, and call gallery-dl on that directory (while staying inside the directory just above gallery-dl)<br>
<br>
you dont have to use gallery-dl, however, it can work with other programs like yt-dlp!<br>
take for example this set of folders<br>
|pornhub<br>
||model1<br>
||model2<br>
||model3<br>

we can use the command<br>
  $ ./multi-gallery-dl.py "pornhub/" --program "yt-dlp" -u "https://www.pornhub.com/model/" -r --options "-f best --restrict-filenames" --moveintodir<br>
<br>
when the option moveintodir is specified, the program will step inside of (lets say ./gallery-dl/pornhub/model1/) before executing the command: yt-dlp -f best --restrict-filenames https://www.pornhub.com/model/model1<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
help text:<br>
usage: multi-dir gallery-dl syncer thingy [-h] -u URLPREFIX<br>
                                          [--notrailingslash]<br>
                                          [--options OPTIONS]<br>
                                          [--program PROGRAM]<br>
                                          [--urlpostfix URLPOSTFIX] [-r]<br>
                                          [-g GALLERYDLDIR] [--moveintodir]<br>
                                          dirname<br>

  Allows you to manage multiple gallery-dl download dirs in a specified directory, i.e.<br>
  given a specified directory AND url prefix<br>
  gallery-dl will be ran on each directory as such: "gallery-dl --sleep 2 --sleep-request 2 URL_PREFIX+DIRECTORY+URL_POSTFIX
  <br>
  EXAMPLES:<br>
   ./program_name twitter/ -u https://www.twitter.com/<br>
   ./program_name twitter/ -u https://www.twitter.com/ -r<br>
   ./multi-gallery-dl.py "pornhub/" --program "yt-dlp" -u "https://www.pornhub.com/model/" -r --options "-f best --restrict-filenames" --moveintodir<br>
<br>
positional arguments:<br>
  dirname               main directory to search for other directories within<br>
<br>
options:<br>
  -h, --help            show this help message and exit<br>
  -u URLPREFIX, --urlprefix URLPREFIX<br>
                        the base url (example: "https://twitter.com/")<br>
  --notrailingslash     by default the program will force a trailing slash onto the urlpostfix argument, specifying this arument disables that.<br>
  --options OPTIONS     extra options to pass to gallery-dl<br>
  --program PROGRAM     the actual program to run (defaults to "gallery-dl")<br>
  --urlpostfix URLPOSTFIX, --postfix URLPOSTFIX<br>
                        extra stuff to add to the end of the url<br>
  -r, --random          randomize order of directories (default=True)<br>
  -g GALLERYDLDIR, --gallerydldir GALLERYDLDIR<br>
                        directory to gallery-dl (defaults to current dir)<br>
  --moveintodir         move into target directory before downloading (by default it will stay in the directory just above this one (which should usually be gallery-dl if you are running this with that program in mind and needed to function correctly)<br>
