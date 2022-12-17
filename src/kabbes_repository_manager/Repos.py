from kabbes_menu import Menu
import kabbes_repository_manager
from parent_class import ParentPluralDict
import dir_ops as do
import py_starter as ps

class Repos( ParentPluralDict, Menu ):

    SRC_DIR = 'src'

    _OVERRIDE_OPTIONS = {
        1:['Open Repo', 'run_Child_user'],
        4:['Copy PYTHONPATH', 'copy_pythonpath']
    }

    rel_dir = ''
    dir = kabbes_repository_manager.manager_search_dir

    def __init__( self, *args, **kwargs ):

        ParentPluralDict.__init__( self, att = 'Repos' )
        Menu.__init__( self )
        self.set_atts( kwargs )

        self.get_search_Dir()
        self.load_Repos()

    def get_search_Dir( self ):

        if self.dir == None:
            self.dir = kabbes_repository_manager._cwd_Dir.join_Dir( path = self.rel_dir ).path

        self.search_Dir = do.Dir( self.dir )

    def load_Repos( self ):

        Repo_Dirs = self.search_Dir.list_contents_Paths( block_paths=True, block_dirs=False )
        for Repo_Dir in Repo_Dirs:
            new_Repo = kabbes_repository_manager.Repo( self, Repo_Dir )
            self._add( new_Repo.repo_name, new_Repo )

    def copy_pythonpath( self, src_dir = None ):

        if src_dir == None:
            src_dir = Repos.SRC_DIR

        pythonpath = do.join_env_var_paths( [Repo.Dir.join_Path( path=src_dir ).path for Repo in self] )
        print ()
        print (pythonpath)
        print ()

        ps.copy( pythonpath )
