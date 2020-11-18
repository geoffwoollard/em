# for copying files through rsync automatically
# see links
# https://serverfault.com/questions/98745/how-to-repeatedly-call-rsync-until-files-are-sucessfully-transferred
# http://blog.iangreenleaf.com/2009/03/rsync-and-retrying-until-we-get-it.html

LOCAL_PATH_TO_DIRECTORY=$1
REMOTE_HOST=$2
REMOTE_PATH_TO_DIRECTORY=$3

echo LOCAL_PATH_TO_DIRECTORY $LOCAL_PATH_TO_DIRECTORY
echo REMOTE_HOST $REMOTE_HOST
echo REMOTE_PATH_TO_DIRECTORY $REMOTE_PATH_TO_DIRECTORY

trap "echo Exited!; exit;" SIGINT SIGTERM

MAX_RETRIES=7
i=0

# Set the initial return value to failure
false

while [ $? -ne 0 -a $i -lt $MAX_RETRIES ]
do
 i=$(($i+1))
 rsync -avz --progress --partial $LOCAL_PATH_TO_DIRECTORY $REMOTE_HOST:$REMOTE_PATH_TO_DIRECTORY
done

if [ $i -eq $MAX_RETRIES ]
then
  echo "Hit maximum number of retries, giving up."
fi