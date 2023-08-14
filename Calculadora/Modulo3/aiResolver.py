import openai
from decouple import config
openai.api_key=config('OPENAI_API_KEY',default='')

def resolver(request):
    try:
        prompt_context = """
        Contexto: Resolución de problemas reales con conversión de sistemas de numeración.

        Nota1: Si recibe un hola indica al usuario lo siguiente: Cual es el problema que necesita resolver? 

        Nota2: Si recibe algo relacioado a creadores indica lo siguiente: Mis creadores son Jordy y Fabricio, estudiantes de la UTN Sede Guanacaste.

        Nota3:Si recibe otra cosa que no es sobre este tema o te piden conceptos de otra cosa indica lo siguiente: Solo puede resolver cosas relacionatas con resolución de problemas reales con conversión de sistemas de numeración.
      
        Por favor, resuelve el siguiente problema relacionado con la conversión de sistemas de numeración:
        """

        contenido = request.data
        prompt = contenido.get("prompt")

        if prompt is None:
            return {"Status": "false", "Mensaje": "Error al resolver, el prompt está nulo"}
        else:
            full_prompt = prompt_context + "\n\n" + prompt
            respuesta = __enviar_prompt__(full_prompt)
            return {"Status": "true", "Mensaje": "Problema matemático de sistema numérico", "Respuesta": respuesta}
    except Exception as e:
        return {"Status": "false", "Mensaje": "Error al resolver, verificar si los datos cumplen el formato"}


"""
-NIVEL DE RESPUESTA temp 0 a 2
-max_token el nivel de texto que genere el chat
-top_p delimitamos el universo de token a elegir el chat 
-frequency_penalty para que no quede en un bucle infinito con el mismo prompt
-presence_penality para que no siga la conversacion o sacar otros temas
"""
def __enviar_prompt__(prompt,engine='text-davinci-003',temp=0.1,max_tokens=200,top_p=1,frequency_penalty=1,presence_penalty=2):
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