import json

def lambda_handler(event, context):
    famosos = {
        25: 'Brad Pitt',
        30: 'Angelina Jolie',
        40: 'Leonardo DiCaprio',
        50: 'Jennifer Aniston',
        60: 'Tom Hanks'
    }

    encontre_famoso_por_idade = lambda idade: famosos.get(idade, 'Não há famosos com essa idade.')

    # Exemplo de uso da função lambda:
    idade_digitada = int(event['idade'])
    resultado = encontre_famoso_por_idade(idade_digitada)

    return {
        'resultado': resultado
    }