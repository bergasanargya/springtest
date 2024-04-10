import dill

# Import the module you want to dump
import greetings

# Specify the path for the dill file
dill_file_path = 'my_module_dump.dill'

# Dump the module to the dill file
with open(dill_file_path, 'wb') as f:
    dill.dump(greetings, f)
