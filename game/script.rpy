# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:
define n = Character("", kind=nvl) ##pensamientos en modo NVL
define k = Character("kazuki")
define kn = Character("kazuki", kind=nvl) ##Kazuki en modo NVL
define z = Character("Zero")
define v = Character("Voz")
define vn = Character("Voz", kind=nvl) ##Voz en modo NVL
define i = Character ("Imperial")
define t = Character ("Todos")
define mama = Character ("Mama")
define h = Character ("Hermana de Kazuki")




# El juego comienza aquí.

label start:
    scene pc
    "¿Cuánto tiempo ha pasado ya?"
    "..."

    k "supongo que ya es hora..."

    n "Habiendo terminado el trabajo del día, decido salir de mi oficina para volver a casa"
    scene cornisa
    n "A pesar de que sé que no hay nadie esperándome, me apresuro para llegar, cuando de repente..."
    nvl clear ##limpia el NVL para que no se acumulen varios textos

    z "Hola, Kazuki..."
    k "...!"

    ##scene calle_2
    k "Sin pensarlo, comencé a correr. Él era una persona la cual ni siquiera podía mirar a la cara"

    z "Por favor, espera! Sólo quiero hablar!"

    k "Déjame en paz! No fue mi culpa! Yo no maté a nadie!"
    ##scene calle_3
    n "Una calle"
    ##hide calle_3
    ##SE USA HIDE Y SHOW EN VEZ DE SCENE PARA MANTENER EL TEXTO Y SOLO CAMBIAR EL BG
    ##show calle_4
    n "Dos calles"
    ##hide calle_4
    ##show calle_5
    n "Tres calles"
    n "A pesar de vivir en esta ciudad hace más de 20 años, luego de tantas vueltas terminé perdido"

    ##scene edificio_fuera
    n "Eventualmente encontré un edificio abandonado hace varios años"
    n "Pensando que este sería el mejor escondite, me adentré en el mismo para evitar a Zero"
    nvl clear
    ##scene techo
    n "Finalmente, habiendo llegado a la asotea, decidí descansar unos minutos y esperar que Zero se vaya"
    nvl clear

    k "Ha..."

    scene black
    n "...creak"
    n "La única conexión entre esta asotea y el resto del edifico produjo un ruido un tanto aterrador, casi sacado de una película"
    nvl clear

    k "...!"
    z "Por favor, sólo quiero hablar. No debes sentirte culpa-"
    k "LEJOS, POR FAVOR MANTENTE LEJOS!"
    z "Kazuki, por favor, necesito saber qué pasó con mi hermano"

    scene cielo
    n "Acorralado por Zero y los recuerdos del pasado, sentí que no tenía escapatoria"
    n "Toda mi vida pensé que, como era un adulto, sólo tenía que seguir"
    n "Pero hoy, sin más remedio, creo que lo mejor es abandonar"

    kn "Nos vemos en un rato, amigo..."
    nvl clear

    scene cornisa
    z "Kazuki, no!"

    ##scene caida
    n "Por primera vez en muchos años, sentí paz."
    n "Una paz que parecía durar una eternidad, mientras esperaba que mi vida termine"
    n "Pensándolo bien, ni siquiera podría encontrarme con él en el otro mundo, ya que probablemente iría al infierno"
    n "Aún así, sentí paz. Pronto se terminaría esta tristeza. Una tristeza que no existiría si él estuviera aquí"

    vn "Así es como termina?"
    n "...!"
    nvl clear

    n "Claro que no quiero morir, no hay nada que desee más que poder seguir viviendo y disfrutando con mis amigos"
    n "Pero ellos ya no están aquí"
    vn "Entonces, recupéralos!"
    n "Quién pingo es esta voz? Finalmente me estoy volviendo loco antes de morir?"
    vn "Changuito, más respeto o me tomo el palo"
    nvl clear

    vn "Soy un Generator, si así lo deseas, puedo darte el poder de recuperar lo que perdiste"
    vn "Lo único que tienes que hacer es firmar el contrato, y tus deseos se harán realidad"
    kn "<No thank you>"
    vn "... Es broma, verdad?"
    kn "Prefiero morir antes que hacer un contrato con mi propia delusion"
    vn "Changuito, deja de decirme delusion o te voy a tener que-"
    nvl clear

    scene black
    n "*tuck*"
    n "Ah, parece que ya es hora..."
    n "Esta vez sí, voy a descansar en paz..."

    n "4 de Mayo de 2030 - Se reporta la muerte del último miembro de los Churuguys, Kazuki."
    nvl clear

    scene pasillo
    n "..."
    n "El cielo? En serio estoy yendo al cielo? No creo que el infierno sea de este color"
    nvl clear
    vn "klk mamahuevo, por qué tan rápido?"
    n "...!"
    n "Esa voz..."
    n "Impe!"
    vn "Todavía no, kazuki..."
    kn "HAAAAAAAAAAAAAAAAAAAAAAA!"
    nvl clear

    scene pc
    k "Otro sueño?"
    "Al parecer tuve una pesadilla, no puedo recordar los últimos momentos pero creo que moría"
    k "Bueno, a prepararme para el trabajo"
    "Cuando me levanto de la cama, noto algo raro"
    k "Dónde pingo estoy?"
    "Sé donde estoy, pero es un lugar al que ya no pertenezco"
    "Al salir de la habitación lo confirmo: estoy en la casa de mis padres, de la cual fui expulsado hace muchos años"
    h "Buenos días, Kazuki"
    k "Buenos... dias?"
    "Por qué estoy en la casa de mis padres?"
    k "Eh... Qué día es hoy?"
    h "Es broma?"
    k "Ah, claro, jaja..."

    ##scene comedor
    "Al bajar al comedor no encuentro a nadie, como de costumbre"
    "Cuando de repente..."

    scene black
    n "PAM!"
    n "Papeles vuelan por todos lados, fuertes sonidos acechan mis oídos, y siento un fuerte dolor en el pecho"
    n "Otra vez? Otra vez me van a quitar a las persoas que amo?"
    nvl clear

    ##scene comedor
    t "Feliz cumpleaños!!!"
    k "Eh...?"
    t "Feliz cumple número 19, Kazuki!"
    "Número 19? yo?"
    k "QUÉ DÍA ES? RÁPIDO!"
    mama "4 de Mayo de 2022, por qué?"
    "2022...?"

    scene black
    n "En ese momento, un fuerte dolor de cabeza me asalta"
    vn "A pesar de no haber firmado el contrato, te voy a dar un pequeño testeo, para que luego decidas si lo quieres o no"
    kn "Testeo?"
    vn "Así es, te devolví al pasado, 5 meses antes de la tragedia que cambiaría tu vida"
    vn "Tómalo o déjalo, la decisión es tuya. Te daré 5 días de prueba para que finalmente firmes el contrato o mueras"
    kn "Qué pingo está pasando?"
    nvl clear
    vn "Podría contestarte, pero sería más divertido si él te da las respuestas, no?"
    kn "él?"
    vn "Ah, tal vez lo olvidaste, pero ya debería ser hora de que..."
    n "*ding dong*"
    n "la puerta?"
    nvl clear

    mama "Kazuki, abre la puerta por favor!"

    ##scene puerta
    "Al abrir la puerta, mi shock aumenta aún más"
    "Parado ahí, como si nada hubiera pasado, está él"
    i "KLK KAZUKIIIII"
    k "Eh...?"
    "Las lágrimas no paran"
    "Ah, parece que ya es hora..."
    "Finalmente, podré vivir en paz?"
    i "klk mamahuevo, por qué lloras?"
    "Impe intenta abrazarme, pero cuando lo hace ambos somos asaltados por un fuerte dolor de cabeza"
    i "Kazuki! Tú también...?!"

    scene black
    n "sin entender bien qué pasó, ambos perdemos la consciencia"

    vn "Te lo dije, no? Sería más divertido si él te lo explica. Nos vemos en 5 días, *Kazu*. Ja ja ja..."
    nvl clear







    return
