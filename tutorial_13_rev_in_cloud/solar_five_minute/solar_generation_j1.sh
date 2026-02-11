#!/bin/bash
#SBATCH --account=na
#SBATCH --time=10:00:00
#SBATCH --job-name=solar_generation_j1  # job name
#SBATCH --nodes=1  # number of nodes
#SBATCH --output=/scratch/reV-tutorial/tutorial_13_rev_in_cloud/solar/logs/stdout/solar_generation_j1_%j.o
#SBATCH --error=/scratch/reV-tutorial/tutorial_13_rev_in_cloud/solar/logs/stdout/solar_generation_j1_%j.e
#SBATCH --qos=normal
#SBATCH --exclusive  # extra feature
echo Running on: $HOSTNAME, Machine Type: $MACHTYPE
echo Running python in directory `which python`
/scratch/reV-tutorial/tutorial_13_rev_in_cloud/start_hsds.sh --log
python -c 'from gaps.cli.config import run_with_status_updates; from reV.generation.generation import Gen; su_args = "/scratch/reV-tutorial/tutorial_13_rev_in_cloud/solar", "generation", "solar_generation_j1"; run_with_status_updates(   Gen, {"technology": "pvwattsv8", "project_points": "/scratch/reV-tutorial/tutorial_13_rev_in_cloud/solar/project_points_10pct.csv", "sam_files": {"default": "/scratch/reV-tutorial/tutorial_13_rev_in_cloud/solar/pvwattsv8.json5"}, "resource_file": "/nrel/nsrdb/GOES/conus/v4.0.0/nsrdb_conus_2019.h5", "low_res_resource_file": None, "output_request": ["cf_profile", "cf_profile_ac", "cf_mean", "cf_mean_ac", "ghi_mean", "lcoe_fcr", "ac", "dc", "clipped_power", "capital_cost", "fixed_operating_cost", "system_capacity", "system_capacity_ac", "fixed_charge_rate", "variable_operating_cost", "dc_ac_ratio"], "site_data": None, "curtailment": None, "gid_map": None, "drop_leap": False, "scale_outputs": True, "write_mapped_gids": False, "bias_correct": None, "analysis_years": [2018, 2019], "project_points_split_range": [0, 209519], "tag": "_j1", "command_name": "generation", "pipeline_step": "generation", "config_file": "/scratch/reV-tutorial/tutorial_13_rev_in_cloud/solar/config_generation.json5", "project_dir": "/scratch/reV-tutorial/tutorial_13_rev_in_cloud/solar", "job_name": "solar_generation_j1", "out_dir": "/scratch/reV-tutorial/tutorial_13_rev_in_cloud/solar", "out_fpath": "/scratch/reV-tutorial/tutorial_13_rev_in_cloud/solar/solar_generation", "run_method": "run", "max_workers": 47, "sites_per_worker": 750, "memory_utilization_limit": 0.7, "timeout": 1800, "pool_size": None}, {"name": "solar_generation", "log_directory": "/scratch/reV-tutorial/tutorial_13_rev_in_cloud/solar/logs", "verbose": True, "node": True}, su_args,    ["project_points"])'