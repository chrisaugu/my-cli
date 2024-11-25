df | grep '^/dev/[hs]d' | awk '{s+=$2} END {print s/1048576 " GB"}'
cat /sys/block/sda/size | awk '{print $1/1024}'