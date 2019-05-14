#!/bin/bash

exp_dir=Simulation`date "+%Y-%m-%d_%H:%M:%S"`

mkdir $exp_dir
cp parametersweep.sh $exp_dir
cp test.py $exp_dir
cp people.py $exp_dir
cd $exp_dir

LOW_INIT_POP=$1
HI_INIT_POP=$2
STEP_INIT_POP=$3
LOW_INIT_INFECTED=$4
HI_INIT_INFECTED=$5
STEP_INIT_INFECTED=$6
NUM_ROWS=$7
NUM_COLS=$8
LOW_NUMSTEPS=$9
HI_NUMSTEPS=$10
STEP_NUMSTEPS=$11

echo "Parameters are: "
echo "Initial Population: " $LOW_INIT_POP $HI_INIT_POP $STEP_INIT_POP
echo "Initial Infected: " $LOW_INIT_INFECTED $HI_INIT_INFECTED $STEP_INIT_INFECTED
echo "NUM_ROWS: " $NUM_ROWS
echo "NUM_COLS: " $NUM_COLS
echo "NUM_STEPS: " $LOW_NUMSTEPS $HI_NUMSTEPS $STEP_NUMSTEPS

for i in `seq $LOW_INIT_POP $STEP_INIT_POP $HI_INIT_POP;
do
	for j in `seq $LOW_INIT_INFECTED $STEP_INIT_INFECTED $STEP_INIT_INFECTED;
	do
		for k in `seq $LOW_NUMSTEPS $STEP_NUMSTEPS $HI_NUMSTEPS;
		do
			echo "Experiment: " $i $j $k
			EachExperiment = "Simulation"$i"_"$j"_"$k
			mkdir EachExperiment
			cp parametersweep.sh $exp_dir
			cp test.py $exp_dir
			cp people.py $exp_dir
			cd $EachExperiment
			python3 test.py $i $j $NUM_ROWS $NUM_COLS $k
		done
	done
done


