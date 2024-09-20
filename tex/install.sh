#!/bin/bash
#############################################################################
# sasiraf/doc INSTALL the files from this directory.
#############################################################################
function usage {
   echo "sasiraf/doc install files from repo to the working file area."
}

while getopts ":h" opt ; do     # request to use master bib
   case $opt in
   h)
      usage
      exit 1
      ;; # process a two part parm
   esac
done

DEST=$HOME/iraf/bin/
mkdir -p $DEST

FILES=( AutoFlats.tex                   \
        BonMots/BonMots.pdfls           \
        Git.tex                         \
        ParallacticAngle.bib            \
        ParallacticAngle.pdf            \
        ParallacticAngle.tex            \
        SASIRAF.bib                     \
        SASIRAF.tex                     \
        Saltrectification.tex           \
        Testtable.txt                   \
        UWyoSkewTLogP9Feb2019_table.dat \
        ccdtime.pdf                     \
        geo.tex                         \
        identify_overview.tex           \
        images                          \
        imexamine.pdf                   \
        install.sh                      \
        mympost                         \
        p_angle.pdf                     \
        p_angle.tex                     \
        runpyraf )



for f in $FILES; do
	 if test ! -e $DEST$f; then
		  cp $f $DEST;
	 else
	    diff $f $DEST
	    retval=$?
	    if [ $retval -ne 0]; then
			  mv $f $DEST$f.bak;
			  cp $f $DEST;
		 else
			  echo "sasiraf/doc: $f not copied"
		 fi
	 fi
done
