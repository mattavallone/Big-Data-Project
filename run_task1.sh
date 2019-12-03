# TO USE:
# Change scratch location USER to individual using it
# File was run on NYU DUMBO HPC

# /usr/bin/hadoop fs -get "/user/hm74/NYCOpenData" "/scratch/mva271"

for filename in /scratch/mva271/NYCOpenData/*.gz; do
	# /usr/bin/hadoop fs -put "$filename"
	echo "${filename##*/}"
	read -p 'skip this file? (y/n):' skipvar
	if [ "$skipvar" = "n" ]
	then
    	spark-submit --conf spark.pyspark.python=$PYSPARK_PYTHON profiling.py "${filename##*/}"
    fi
done