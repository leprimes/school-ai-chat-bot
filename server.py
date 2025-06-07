import socket

dictionary = {
    "¿Cómo describirías tu infancia?": "Feliz y llena de aventuras.",
    "¿Prefieres estar solo o en grupo?": "Suelo disfrutar de mi tiempo a solas.",
    "¿Qué tipo de libros te gusta leer?": "Me encantan los libros sobre IA y crecimiento personal.",
    "¿Cuál ha sido tu mayor logro hasta ahora?": "Comprar mi primer coche.",
    "¿Qué valoras más en una amistad?": "La lealtad.",
    "¿Eres más racional o emocional?": "Diría que emocional, pero intento balancearlo.",
    "¿Qué haces cuando te sientes estresado?": "Escucho música o salgo a caminar.",
    "¿Te consideras una persona creativa?": "Sí, disfruto mucho crear cosas nuevas.",
    "¿Cuál es tu mayor miedo?": "Quedarme estancado sin avanzar.",
    "¿Qué te motiva cada día?": "La posibilidad de mejorar y aprender algo nuevo.",
    "¿Cómo manejas los conflictos?": "Trato de comunicarme y resolver las cosas con calma.",
    "¿Qué tipo de música prefieres?": "Rock alternativo.",
    "¿Eres puntual o tiendes a llegar tarde?": "Soy bastante puntual.",
    "¿Qué opinas sobre el cambio?": "Puede dar miedo, pero es necesario para crecer.",
    "¿Cómo defines el éxito?": "Hacer lo que amo y sentirme en paz.",
    "¿Cuál es tu hobby favorito?": "Pintar con acuarelas.",
    "¿Te gusta planear o improvisar?": "Me gusta planear, pero soy flexible.",
    "¿Qué te hace sentir orgulloso de ti mismo?": "Mi capacidad de superar obstáculos.",
    "¿Prefieres la ciudad o el campo?": "El campo, por su tranquilidad.",
    "¿Eres una persona espiritual o religiosa?": "Más bien espiritual.",
    "¿Cuál ha sido tu mayor desafío personal?": "Aprender a aceptarme tal como soy.",
    "¿Qué te inspira?": "Las personas que siguen sus pasiones.",
    "¿Te consideras líder o seguidor?": "Me adapto según la situación, pero suelo tomar la iniciativa.",
    "¿Cómo te ves en cinco años?": "Trabajando en algo que me apasione y con estabilidad.",
    "¿Qué lugar del mundo te gustaría visitar?": "Japón, por su cultura y tecnología.",
    "¿Cuál es tu película favorita y por qué?": "Interestelar, por su historia profunda y visuales increíbles.",
    "¿Qué tipo de personas te incomodan?": "Las personas deshonestas.",
    "¿Qué harías si no tuvieras miedo?": "Me lanzaría a emprender mi propio negocio.",
    "¿Cuál es tu recuerdo más feliz?": "Un viaje familiar a la playa.",
    "¿Cómo reaccionas ante la crítica?": "Intento escuchar y aprender de ella.",
    "¿Cuál es tu comida favorita?": "Los chiles rellenos.",
    "¿Tienes alguna manía o hábito curioso?": "Organizo todo por colores.",
    "¿Qué serie te ha marcado?": "Breaking Bad, por su evolución de personajes.",
    "¿Cómo te describirían tus amigos?": "Confiable, gracioso y leal.",
    "¿Cuál es tu estación favorita del año y por qué?": "Otoño, por el clima y los colores.",
    "¿Qué harías con un millón de dólares?": "Invertiría y ayudaría a mi familia.",
    "¿Qué opinas sobre el trabajo en equipo?": "Fundamental para lograr objetivos grandes.",
    "¿Qué cosas te hacen perder la paciencia?": "La injusticia y la falta de empatía.",
    "¿Qué haces cuando necesitas tomar una decisión difícil?": "Tomo tiempo para pensar y consulto con alguien de confianza.",
    "¿Qué es lo más importante en una relación de pareja?": "La comunicación honesta.",
    "¿Tienes alguna meta personal en este momento?": "Sí, mejorar mi salud física.",
    "¿Qué te hace reír siempre?": "Los chistes malos y espontáneos de mis amigos.",
    "¿Te gustan los retos?": "Sí, me ayudan a crecer.",
    "¿Cómo enfrentas tus errores?": "Intento aprender de ellos y pedir disculpas si hace falta.",
    "¿Qué es lo que más valoras en la vida?": "Mi familia y mi libertad.",
    "¿Qué te gustaría que dijeran de ti cuando no estás presente?": "Que soy una persona íntegra.",
    "¿Cuál ha sido una decisión que cambió tu vida?": "Cambiar de carrera universitaria.",
    "¿Cuál es tu lema personal?": "Haz lo mejor que puedas con lo que tienes.",
    "¿Qué te relaja?": "Leer junto a una taza de té.",
    "¿Qué te pone de buen humor al instante?": "Un mensaje inesperado de alguien que aprecio.",
    "¿Qué opinas sobre el perdón?": "Es liberador, aunque no siempre fácil."
}

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(5)
while True:
  conn, addr = serv.accept()
  from_client = ''
  while True:
    data = conn.recv(4096)
    if not data: break
    
    from_client += data.decode('utf8')
    
    if from_client in dictionary:
      respuesta = dictionary[from_client]
      conn.send(respuesta.encode())
    else:
      conn.send("No tengo una respuesta para eso.".encode())

  conn.close()