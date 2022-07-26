
# Import the Azure ML classes
from azureml.core import Workspace, Experiment, ScriptRunConfig

# Access the workspace using config.json
ws = Workspace.from_config("./config")

# Create/access the experiment from workspace 
new_experiment = Experiment(workspace=ws,
                            name="Est-SDK-Exp01")
                            # Create a script configuration
script_config = ScriptRunConfig(source_directory=".",
                                script="new_script.py")

                                # Submit a new run using the ScriptRunConfig
new_run = new_experiment.submit(config=script_config)


# Create a wait for completion of the script
new_run.wait_for_completion()