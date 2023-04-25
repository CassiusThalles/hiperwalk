#Declares data types according to neblina-core
#TODO: make it so it is not hardcoded
NEBLINA_FLOAT = 2
NEBLINA_COMPLEX = 13 

from sys import modules as sys_modules

__USING_PDB__ = 'pdb' in sys_modules
__DEBUG__ = __debug__ and __USING_PDB__

PYNEBLINA_IMPORT_ERROR_MSG =  (
    "Could not import pyneblina interface. "
    + "Do you have neblina-core and pyneblina installed?"
    + "\n#######################\n"
    + "Continuing without hpc."
    + "\n#######################\n" )
