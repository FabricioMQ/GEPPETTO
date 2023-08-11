import openai
from decouple import config
openai.api_key=config('OPENAI_API_KEY',default='')

def resolver(request) :
    try :
       contenido=request.data
       prompt=contenido.get("prompt")
       if prompt is None: 
            return  {"Status":"false","Mensaje":"Error al resolver ,el prompt esta nulo"}
       else:    
            return {"Status":"true","Mensaje":"Problema matematicos sistema numerico","Respuesta":__enviar_prompt__(prompt)}
    except Exception as e:
        return  {"Status":"false","Mensaje":"Error al resolver , verificar si los datos cumplen el formato"}



"""
-NIVEL DE RESPUESTA temp 0 a 2
-max_token el nivel de texto que genere el chat
-top_p delimitamos el universo de token a elegir el chat 
-frequency_penalty para que no quede en un bucle infinito con el mismo prompt
-presence_penality para que no siga la conversacion o sacar otros temas
"""
def __enviar_prompt__(prompt,engine='text-davinci-003',temp=1,max_tokens=100,top_p=1,frequency_penalty=1,presence_penalty=2):
    respuesta = openai.Completion.create(
                                            engine=engine,
                                            prompt=prompt,
                                            temperature=temp,
                                            max_tokens=max_tokens,
                                            top_p=top_p,
                                            frequency_penalty=frequency_penalty,
                                            presence_penalty=presence_penalty
                                            )
    return respuesta['choices'][0]['text']