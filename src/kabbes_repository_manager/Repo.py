from kabbes_menu import Menu
import kabbes_repository_manager
import git

class Repo( git.Repo, Menu ):

    _OVERRIDE_OPTIONS = {
        1:['Open Remotes','run_Child_user']
    }

    _IMP_ATTS = ['repo_name','Dir','Remotes']
    _ONE_LINE_ATTS = ['repo_name','Dir']

    _SEARCHABLE_ATTS = [ 'repo_name' ]

    def __init__( self, Repos, Dir ):

        git.Repo.__init__( self, Dir.p )
        Menu.__init__( self )

        self.Repos = Repos
        self.Dir = Dir
        self.url_clone = self.remotes.origin.url
        self.url_nav = self.url_clone[ : -1*len('.git') ]
        self.repo_name = self.url_nav.split( '/' )[-1]

        self.Remotes = kabbes_repository_manager.Remotes( self )
        self._Children = [ self.Remotes ]



