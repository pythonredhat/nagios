#!/usr/bin/python 

import os, sys

used_space = os.open("df -h / |grep Filesystem | awk '{print $5}'.readline().strip())

if used_space < "85%":
  print "Ok - %s of disk space used" % used_space
  sys.exit(0)

elif used_space == "85%":
  print "Warning - %s of disk space used" % used_space
  sys.exit(1)

elif used_space > "85%":
  print "Critical - %s of disk space used" % used_space
  sys.exit(2)

else:
  sys.exit(3)

