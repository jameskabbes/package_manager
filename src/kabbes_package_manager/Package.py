from kabbes_menu import Menu
import git

class Package( git.Repo, Menu ):

    _OVERRIDE_OPTIONS = {
        1:['','do_nothing']
    }

    _IMP_ATTS = ['repo_name','Dir']
    _ONE_LINE_ATTS = ['repo_name','Dir']

    _SEARCHABLE_ATTS = [ 'repo_name' ]

    def __init__( self, Dir ):

        git.Repo.__init__( self, Dir.p )
        Menu.__init__( self )

        self.Dir = Dir
        self.url_clone = self.remotes.origin.url
        self.url_nav = self.url_clone[ : -1*len('.git') ]
        self.repo_name = self.url_nav.split( '/' )[-1]

        self.remote_refs 


        remote_refs = self.remote().refs

        for refs in remote_refs:
            print(refs.name)



