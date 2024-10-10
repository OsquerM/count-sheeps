#Variables globales
sleep = ""
#Funciones
def run(num_sheeps: int) -> str:
    # TODO
    global sleep
    #Variables locales
    dormir = "sheep..."
    sleep = dormir * num_sheeps
    return sleep

#Codigo Principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(sleep)