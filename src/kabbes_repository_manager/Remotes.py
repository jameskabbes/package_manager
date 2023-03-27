from parent_class import ParentPluralDict
from kabbes_menu import Menu
import kabbes_repository_manager

class Remotes( ParentPluralDict, Menu ):

    _OVERRIDE_OPTIONS = {
        1:['Open Remote', 'run_Child_user']
    }

    def __init__( self, Repo):

        ParentPluralDict.__init__( self, att = 'Remotes')
        Menu.__init__( self )

        self.Repo = Repo
        self.load_Remotes()


    def load_Remotes( self ):

        for ref in self.Repo.remote().refs:
            new_Remote = kabbes_repository_manager.Remote( self, ref )
            self._add( new_Remote.ref.name, new_Remote )

