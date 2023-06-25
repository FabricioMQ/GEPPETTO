from .baseconvert.baseconvert import base



def conv(request) :
    try :
        contenido=request.data
        base_from=int(contenido.get("base_from"))
        base_to=int(contenido.get("base_to"))
        _num=contenido.get("_num")
        _newnum=base(_num,base_from,base_to,string=True)
        return {"Status":"True","Mensaje":f"Cambiar de base {base_from} a {base_to}","Numero":_newnum}
    except Exception as e:
        return  {"Status":"false","Mensaje":"Error al cambiar de base , verificar bases"}

    