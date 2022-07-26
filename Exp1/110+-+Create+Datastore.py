# -----------------------------------------------------
# Import the Workspace and Datastore class
# -----------------------------------------------------
from azureml.core import Workspace, Datastore


# -----------------------------------------------------
# Access the workspace from the config.json 
# -----------------------------------------------------
# azureml-core of version 1.0.72 or higher is required
# azureml-dataprep[pandas] of version 1.1.34 or higher is required
from azureml.core import Workspace, Dataset,Experiment, Datastore


subscription_id= 'eb5a257a-76e2-472d-9fdc-7f9b3172fcf6'
resource_group = 'rg-smth-3788'
workspace_name = 'smth-3788'
#az_store       = Datastore.get(workspace_name, 'azureml_ds_b01')

workspace = Workspace(subscription_id, resource_group, workspace_name)


# -----------------------------------------------------
# Create a datastore 
# -----------------------------------------------------
az_store = Datastore.register_azure_blob_container(
            workspace=workspace,
            datastore_name="smth37881976232114", 
            account_name="rg-smth-3788",
            container_name="mlexperiments",
            account_key="oDGA8zdyZLE+sQdWx1bLczGA6kRVfw7Iq0NuNYg+wX1TEgTFidLGOaQ2gcC3PQeh2ourxYZklizigunxBB0WWA==")














