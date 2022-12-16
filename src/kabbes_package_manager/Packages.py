from kabbes_menu import Menu
import kabbes_package_manager
from parent_class import ParentPluralDict
import dir_ops as do

class Packages( ParentPluralDict, Menu ):

    _OVERRIDE_OPTIONS = {
        1:['Open Package', 'run_Child_user']
    }

    rel_dir = ''
    dir = kabbes_package_manager.manager_search_dir

    def __init__( self, *args, **kwargs ):

        ParentPluralDict.__init__( self, att = 'Packages' )
        Menu.__init__( self )
        self.set_atts( kwargs )

        self.get_search_Dir()
        self.load_Packages()

    def get_search_Dir( self ):

        if self.dir == None:
            self.dir = kabbes_package_manager._cwd_Dir.join_Dir( path = self.rel_dir ).path

        self.search_Dir = do.Dir( self.dir )

    def load_Packages( self ):

        package_Dirs = self.search_Dir.list_contents_Paths( block_paths=True, block_dirs=False )
        for package_Dir in package_Dirs:
            new_Package = kabbes_package_manager.Package( package_Dir )
            self._add( new_Package.repo_name, new_Package )

