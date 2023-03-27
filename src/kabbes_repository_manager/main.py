def run_main():
    import kabbes_repository_manager
    import py_starter as ps
    args, kwargs = ps.get_system_input_arguments()

    repos = kabbes_repository_manager.Repos( *args, **kwargs )
    repos.run()

if __name__ == '__main__':
    run_main()