from google.cloud.storage.client import Client
import papermill as pm
import sys

gcspath_input_notebook="gs://databricks-enablement/GEP/notebooktest/scala_test.ipynb"
gcspath_output_notebook="gs://databricks-enablement/GEP/notebooktest/scala_output.ipynb"

# pm.execute_notebook(
#       gcspath_input_notebook, gcspath_output_notebook, kernel_name='python3',log_output=True, progress_bar=False, stdout_file=sys.stdout, parameters=params, **kwargs)

pm.execute_notebook(
      gcspath_input_notebook, gcspath_output_notebook, progress_bar=True, log_output=True, progress_bar=False, stdout_file=sys.stdout)