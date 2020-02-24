from random import randrange

data = {
    '0': "Faça carinho nos animais e beba água",
    '1': "Se vc recebeu essa mensange, faça o que ela manda, e ela manda voce tomar água",
    '2': "É o seguinte, vai tomar água, vlw",
    '3': "Tome agua",
    '4': "Beba água, obrigado",
    '5': "Drink water",
    '6': "AGUA, BEBA ÁGUA",
    '7': "Is water time",
    '8': "Hora de tomar uma cachaç... água",
    '9': "Deve agua tomar voce",
    '10': "Não sei o que vc está fazendo, mas neste momento essa coisa não é mais importante que tomar água",
    '11': "Imagina que gostosinho ia ser tomar um copo d'agua...",
    '12': "Bora, levanta e anda em direção a um bebedouro",
    '13': "Matenha-se hidratado, tome água",
    '14': "Melhor uma pedra no caminho do que uma no rim, então: beba água",
    '15': "Beba água, vc vai me agradecer depois",
    '16': "Coé, meno, já bebeu sua água hoje?",
    '17': "Rosas são vermelhas, violetas são azuis, vai tomar água",
    '18': "Aviso pra tomar água",
    '19': "Olha a hora mano, é hora de tomar água",
    '20': "Mein, pela sua saude, vai beber água",
    '21': "Pelo amor de Deus, camarada, não aguento mais manda tu tomar agua!!!",
    '22': "Ainn, tenho ranço de quem não está tomando água agr, então vai lá tomar pq não quero ter ranço de voce...",
    '23': "Seu rim vai agradecer se tomar água agora",
    '24': "Keep calm and vai tomar água, patrão",
    '25': "Convenhamos, talvez já seja hora de tomar água, né...",
    '26': "Não é querendo pressionar nem nada, mas voce está se hidratando corretamente? Se não, tome água, se sim, tome água também",
    '27': "Voce tem certeza de que o que voce está fazendo agora é mais importante que se hidratar?",
    '28': "Voce sabia? Quem bebe água frequentemente tem 90% de chance de entrar na faculdade, e quem já entrou consegue sair ainda mais rápido desse inferno?",
    '29': "Beba água pra chorar com tranquilidade quando tiver uma crise <3",
    '30': "Beba água AGORA! Se não eu vou contar pra sua mãe",
    '31': "Sai do celular seu preguiçoso e vai tomar uns golão de água",
    '32': "Beba água, seja asseado, lave a louça, e durma cedo",
    '33': "Quer dar orgulho a sua familia? Então drink água",
    '34': "Cerveja? To fora, pego meu galão de água e dou fora",
    '35': "'Beba água seu porra' EINSTEIN, Albert",
    '36': "Só é corno quem não toma água, pronto falei",
    '37': "Tive um pesadelo horroroso, sonhei que meus seguidores não tomam água direito, credo",
    '38': "'Drink water' que significa vai tomar água em inglês"
}

# Choose what message will send
def message():
    random_index = str(randrange(0, len(data)))
    return data[random_index]
