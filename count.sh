#!/bin/bash
 
# download the textfile
wget ftp://sunsite.informatik.rwth-aachen.de/pub/mirror/ibiblio/gnome/README

cat README| tr '[A-Z]' '[a-z]'|      # make all text lowercase
            tr ' ' "\n"|             # split in words per line
            sort|                    # alphabetically list of words
            uniq -c |                # without duplicates and count 
            sort -nr|                # sort most common
            head -11|                # first ten words
            sed -E 's/^ *[0-9]+ //g' # without counts and command
									 # Found in thread https://superuser.com/questions/383726/get-the-most-common-appearing-lines-from-file-in-linux