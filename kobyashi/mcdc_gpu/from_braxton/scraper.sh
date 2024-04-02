#!/bin/bash


base=$(pwd)

for x in 2.5 5 10 20 40 80
do

for n in 1e4 1e5 1e6 1e7 1e8
do

dir=".run_${x}_${n}"
mkdir -p $dir

subscript="mod.py"
script_path="$dir/$subscript"

sed -e "s/0.05/${x}e-2/g" input.py > $script_path
sed -i -e "s/5e-5/${x}e-5/g" $script_path
sed -i -e "s/1e4/$n/g"       $script_path

diff $script_path input.py

#cpu
for targ in gpu
do


cd $dir

cmd="python3 $subscript --mode=numba --target=$targ >out 2>err"
echo "$cmd" | bsub

cd $base

done

done

done

