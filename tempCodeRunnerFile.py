
           print("\n\nDeregister " + DAN.profile['d_name'] + " !!!\n",  flush=True)
           DAN.deregister()
           sys.stdout = sys.__stdout__
           print(" Thread say Bye bye ---------------", flush=True)
           sys.exit( )   ## break  # raise   #  ?
        gotInput=True
        if theInput !='quit' and theInput != "exit":