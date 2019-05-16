#!/bin/bash

exp_dir=Simulation`date "+%Y-%m-%d_%H:%M:%S"`

mkdir $exp_dir
cp parametersweep.sh $exp_dir
cp test.py $exp_dir
cp people.py $exp_dir
cp neighbours.py $exp_dir
cd $exp_dir

LOW_INIT_POP=$1
HI_INIT_POP=$2
STEP_INIT_POP=$3
LOW_INIT_INFECTED=$4
HI_INIT_INFECTED=$5
STEP_INIT_INFECTED=$6
NUM_ROWS=$7
NUM_COLS=$8
NUM_STEPS=$9

echo "Parameters are: "
echo "Initial Population: " $LOW_INIT_POP $HI_INIT_POP $STEP_INIT_POP
echo "Initial Infected: " $LOW_INIT_INFECTED $HI_INIT_INFECTED $STEP_INIT_INFECTED
echo "NUM_ROWS: " $NUM_ROWS
echo "NUM_COLS: " $NUM_COLS
echo "NUM_STEP: " $NUM_STEPS

for i in `seq $LOW_INIT_POP $STEP_INIT_POP $HI_INIT_POP`;
do
	for j in `seq $LOW_INIT_INFECTED $STEP_INIT_INFECTED $HI_INIT_INFECTED`;
	do
		for k in `seq 1 1 2`;
		do 
			echo "Experiment: " $i $j $NUM_STEPS "Neighbour: " $k
			EachExperiment="Simulation_POP_"$i"INFECTED_"$j"STEPS_"$NUM_STEPS_"Neighbour_"$k
			EachExperimentOutput="Output"
			mkdir $EachExperiment
			cp parametersweep.sh $EachExperiment
			cp test.py $EachExperiment
			cp people.py $EachExperiment
			cp neighbours.py $EachExperiment
			cd $EachExperiment
			mkdir $EachExperimentOutput
			python3 test.py $i $j $NUM_ROWS $NUM_COLS $NUM_STEPS $k
			cd ..
		done
	done
done


