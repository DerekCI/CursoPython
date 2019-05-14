with EXPR as VAR:
    BLOCK       
    mgr = (EXPR)
    exit = type(mgr).__exit__  # Not calling it yet
    value = type(mgr).__enter__(mgr)
    exc = True
    try:
        try:
          VAR = value  # Only if "as VAR" is present
          BLOCK
          except:
              # The exceptional case is handled here
              exc = False
              if not exit(mgr, *sys.exc_info()):
                raise
              # The exception is swallowed if exit() returns true
        finally:
          # The normal and non-local-goto cases are handled here
          if exc:
                exit(mgr, None, None, None)

