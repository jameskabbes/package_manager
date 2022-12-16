import kabbes_package_manager
import py_starter as ps
args, kwargs = ps.get_system_input_arguments()

packages = kabbes_package_manager.Packages( *args, **kwargs )
packages.run()