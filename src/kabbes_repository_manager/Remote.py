from kabbes_menu import Menu

class Remote( Menu ):

    _OVERRIDE_OPTIONS = {
        1:[ '','do_nothing' ],
        2:[ 'Checkout Branch', 'checkout'],
        3:[ 'Pull Branch', 'pull']

    }

    _IMP_ATTS = ['name','branch']
    _ONE_LINE_ATTS = ['type','name']
    _SEARCHABLE_ATTS = ['name']

    def __init__( self, Remotes, ref ):

        Menu.__init__( self )
        self.Remotes = Remotes
        self.ref = ref #git object
        self.name = self.ref.name

        self.branch = self.ref.name.split( '/' )[-1]

    def checkout( self ):
        
        print ('Checking out {} on {}'.format( self.branch, self.Remotes.Repo.repo_name ))
        self.Remotes.Repo.git.checkout( self.branch )

