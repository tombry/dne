#!/bin/bash

# Make sure we at least get something for the
# host and port without doing any validation

if [ $# != 2 ]; then
  printf "\nUsage: $0 <fqdn|ip> <port>\n"
  exit
fi

# Define our named-pipe FIFO

FIFO=/tmp/cleu2018.fifo

# If the named-pipe does not exist check
# to see if there is a file of the same name
# and if so delete it before creating the
# new named-pipe

if ! [ -p $FIFO ]; then
  if [ -f $FIFO ]; then rm $FIFO; fi
  mkfifo $FIFO;
fi

# Validate that we have a number at least
# for the port argument, then open nc and 
# pipe the output into our FIFO

if [[ "$2" =~ ^[0-9]+$ ]]; then
  /usr/bin/nc >$FIFO $1 $2
else
    echo "$2 is not a valid port number"
fi

# Run till killed

exit 0
