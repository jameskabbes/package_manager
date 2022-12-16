import dir_ops as do
import os
from user_profile import profile

_Dir = do.Dir( os.path.abspath( __file__ ) ).ascend()   #Dir that contains the package 
_src_Dir = _Dir.ascend()                                  #src Dir that is one above
_repo_Dir = _src_Dir.ascend()                    
_cwd_Dir = do.Dir( do.get_cwd() )

manager_search_dir = None
if profile.has_attr( 'packages_Dir' ):
    manager_search_dir = profile.get_attr( 'packages_Dir' ).path


from .Packages import Packages
from .Package import Package