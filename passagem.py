import PySimpleGUI as sg
def Salmo(capituloX,versiculox):
    # dicionarios dos capitulos
    if capituloX == '35':
        
        cap = {
        '[35]' : 'SALMOS',
        
        '1' : '''Contende, Senhor, com aqueles que contendem
        comigo; combate contra os que me combatem.''',
        '2' : '''Pega do escudo e do pavês, e levanta-te em meu
        socorro.''',
        '3' : '''Tira da lança e do dardo contra os que me
        perseguem. Dize a minha alma: Eu sou a tua
        salvação.''',
        '4' : '''Sejam envergonhados e confundidos os que
        buscam a minha vida; voltem atrás e se
        confundam os que contra mim intentam o mal.''',
        '5' : '''Sejam como a moinha diante do vento, e o anjo
        do Senhor os faça fugir.''',

        '6' : '''Seja o seu caminho tenebroso e escorregadio, e
        o anjo do Senhor os persiga.''',

        '7' : '''Pois sem causa me armaram ocultamente um
        laço; sem razão cavaram uma cova para a minha
        vida.''',

        '8' : '''Sobrevenha-lhes inesperadamente a destruição,
        e prenda-os o laço que ocultaram; caiam eles
        nessa mesma destruição.''',

        '9' : '''Então minha alma se regozijara no Senhor;
        exultara na sua salvação.''',

        '10' : '''Todos os meus ossos dirão: Ó Senhor, quem é
        como tu, que livras o fraco daquele que é mais
        forte do que ele? sim, o pobre e o necessitado,
        daquele que o rouba.''',

        '11' : '''Levantam-se  testemunhas maliciosas;
        interrogam-me sobre coisas que eu ignoro.''',

        '12' : '''Tornam-me o mal pelo bem, causando-me luto
        na alma.''',

        '13' : '''Mas, quanto a mim, estando eles enfermos,
        vestia-me de cilicio, humilhava-me com o jejum,
        orava de cabeça sobre o peito.''',

        '14' : '''Portava-me como o faria por meu amigo ou
        meu irmão; eu andava encurvado e lamentando-
        me, como quem chora por sua mãe.''',

        '15' : '''Mas, quando eu tropeçava, eles se alegravam e
        se congregavam; congregavam-se contra mim,
        homens miseráveis que eu não conhecia;
        difamavam-me sem cessar.''',

        '16' : '''Como hipócritas zombadores nas festas,
        rangiam os dentes contra mim.''',

        '17' : '''Ó Senhor, até quando contemplarás isto?
        Livra-me das suas violências; salva a minha vida
        dos leões!''',

        '18' : '''Então te darei gracas na grande assembleia;
        entre muitíssimo povo te louvarei.''',

        '19' : '''Não se alegrem sobre mim os que são meus
        inimigos sem razio, nem pisquem os olhos
        aqueles que me odeiam sem causa.''',

        '20' : '''Pois não falaram de paz, antes inventam
        contra os quietos da terra palavras enganosas.''',


        '21' : '''Escancararam contra mim a sua boca, e
        dizem: Ah! Ah! os nossos olhos o viram.''',

        '22' : '''Tu, Senhor, o viste, não te cales; Senhor, não
        te alongues de mim.''',

        '23' : '''Acorda e desperta para o meu julgamento,
        para a minha causa, Deus meu, e Senhor meu.''',

        '24' : '''Justifica-me segundo a tua justiça, Senhor
        Deus meu, e não se regozijem eles sobre mim.''',

        '25' : '''Não digam em seu coração: Eia! cumpriu-se o
        nosso desejo! Não digam: Nós o havemos
        devorado.''',

        '26' : '''Envergonhem-se e confundam-se à uma os
        que se alegram com o meu mal; vistam-se de
        vergonha e de confusão os que se engrandecem
        contra mim.''',

        '27' : '''Bradem de júbilo e se alegrem os que desejam
        a minha justificação, e digam a minha
        justificação, e digam continuamente: Seja
        engrandecido o Senhor, que se deleita na
        prosperidade do seu servo.''',

        '28' : '''Então a minha linguá falara da tua justiça e
        do teu louvor o dia todo.'''
            }
        sg.popup_scrolled(cap[versiculox],title='versículo') # vai imprimir uma chave especifica do dicionario 
        print(cap[versiculox])  # vai imprimir uma chave especifica do dicionario que é o versículo especifico
        print('O salmo 35 tem 23 versículos')  
        print('*'*7)

    if capituloX == '117':
            
        cap = {
        '1' : '''Louvai ao SENHOR todas as nações, louvai-o 
                todos os povos.''',
        '2' : '''Porque a sua benignidade é grande para conosco,
                e a verdade do Senhor dura para sempre. Louvai ao Senhor.'''
                }
        sg.popup_scrolled(cap[versiculox],title='versículo')
        print(cap[versiculox])
        print(' Salmo 117 tem 2 versículos')
        print('*'*7)

def Proverbio(capituloX,versiculox):
    if capituloX == '1':
    
        cap = {
        '[1]' : 'PROVÉRBIOS',

        '1' : '''Provérbios de Salomão, filho de Davi, rei de
        Israel:''',

        '2' : '''Para se conhecer a sabedoria e a instrução;
        para se entenderem as palavras de inteligência;''',

        '3' : '''para se instruir em sábio procedimento, em
        retidão, justiça e equidade;''',

        '4' : '''para se dar aos simples prudência, e aos jovens
        conhecimento e bom siso.''',

        '5' : '''Ouça também, o sábio e cresça em ciência, e o
        entendido adquira habilidade,''',

        '6' : '''para entender provérbios e parábolas, as
        palavras dos sábios, e seus enigmas.''',

        '7' : '''O temor do Senhor é o princípio do
        conhecimento(sabedoria); mas os insensatos desprezam a
        sabedoria e a instrução.''',

        '8' : '''Filho meu, ouve a instrução de teu pai, e não
        deixes o ensino de tua mãe.''',

        '9' : '''Porque eles serão uma grinalda de graça para a
        tua cabeça, e colares para o teu pescoço.''',

        '10' : '''Filho meu, se os pecadores te quiserem
        seduzir, não consintas.''',

        '11' : '''Se disserem: Vem conosco; embosquemo-nos
        para derramar sangue; espreitemos sem razão o
        inocente;''',

        '12' : '''traguemo-los vivos, como o Seol, e inteiros
        como os que descem à cova;''',

        '13' : '''acharemos toda sorte de bens preciosos;
        encheremos as nossas casas de despojos;''',

        '14' : '''lançarás a tua sorte entre nós; teremos todos
        uma só bolsa;''',

        '15' : '''filho meu, não andes no caminho com eles;
        guarda da sua vereda o teu pé,''',

        '16' : '''porque os seus pés correm para o mal, e eles
        se apressam a derramar sangue.''',

        '17' : '''Pois debalde se estende a rede à vista de
        qualquer ave.''',

        '18' : '''Mas estes se põem em emboscadas contra o
        seu próprio sangue, e as suas próprias vidas
        espreitam.''',

        '19' : '''Tais são as veredas de todo aquele que se
        entrega à cobiça; ela tira a vida dos que a
        possuem.''',

        '20' : '''A suprema sabedoria altissonantemente clama
        nas ruas; nas praças levanta a sua voz.''',

        '21' : '''Do alto dos muros clama; às entradas das
        portas e na cidade profere as suas palavras:''',

        '22' : '''Até quando, ó estúpidos, amareis a estupidez?
        e até quando se deleitarão no escarnio os
        escarnecedores, e odiarão os insensatos o
        conhecimento?''',

        '23' : '''Convertei-vos pela minha repreensão; eis que
        derramarei sobre vós o meu; espirito e vos farei
        saber as minhas palavras.''',

        '24' : '''Mas, porque clamei, e vós recusastes; porque
        estendi a minha mão, e não houve quem desse
        atenção;''',

        '25' : '''antes desprezastes todo o meu conselho, e não
        fizestes caso da minha repreensão;''',

        '26' : '''também eu me rirei no dia da vossa
        calamidade; zombarei, quando sobrevier o vosso
        terror,''',

        '27' : '''quando o terror vos sobrevier como
        tempestade, e a vossa calamidade passar como
        redemoinho, e quando vos sobrevierem aperto e
        angústia.''',

        '28' : '''Então a mim clamarão, mas eu não
        responderei; diligentemente me buscarão, mas
        não me acharão.''',

        '29' : '''Porquanto aborreceram o conhecimento, e não
        preferiram o temor do Senhor;''',

        '30' : '''não quiseram o meu conselho e desprezaram
        toda a minha repreensão;''',

        '31' : '''portanto comerão do fruto do seu caminho e
        se fartarão dos seus próprios conselhos.''',

        '32' : '''Porque o desvio dos néscios os matará, e a
        prosperidade dos loucos os destruirá.''',

        '33' : '''Mas o que me der ouvidos habitará em
        segurança, e estará tranquilo, sem receio do mal.'''
        }
        sg.popup_scrolled(cap[versiculox],title='versículo')
        print(cap[versiculox])
        print(' Provérbios 1 tem 33 versículos')
        print('*'*7)

def Icorintios(capituloX,versiculox):
    if capituloX == '13':
        

        cap = {
        '[13]' :       'I CORINTIOS', 

        '1' : '''Ainda que eu falasse as linguás dos homens e
        dos anjos, e não tivesse amor, seria como o metal
        que soa ou como o címbalo que retine.''',
        '2' : '''E ainda que tivesse o dom de profecia, e
        conhecesse todos os mistérios e toda a ciência, e
        ainda que tivesse toda fé, de maneira tal que
        transportasse os montes, e não tivesse amor,
        nada seria.''',
        '3' : '''E ainda que distribuísse todos os meus bens
        para sustento dos pobres, e ainda que entregasse
        o meu corpo para ser queimado, e não tivesse
        amor, nada disso me aproveitaria.''',
        '4' : '''O amor  sofredor, é benigno; o amor não é
        invejoso; o amor não se vangloria, não se
        ensoberbece,''',
        '5' : '''não se porta inconvenientemente, não busca os
        seus próprios interesses, não se irrita, não
        suspeita mal;''',

        '6' : '''não se regozija com a injustiça, mas se regozija
        com a verdade;''',

        '7' : '''tudo sofre, tudo cré, tudo espera, tudo suporta.''',

        '8' : '''O amor jamais acaba; mas havendo profecias,
        serão aniquiladas; havendo linguás, cessarão;
        havendo ciência, desaparecera;''',

        '9' : '''porque, em parte conhecemos, e em parte
        profetizamos;''',

        '10' : '''mas, quando vier o que é perfeito, então o que
        é em parte será aniquilado.''',

        '11' : '''Quando eu era menino, pensava como
        menino; mas, logo que cheguei a ser homem,
        acabei com as coisas de menino.''',

        '12' : '''Porque agora vemos como por espelho, em
        enigma, mas então veremos face a face; agora
        conheço em parte, mas então conhecerei
        plenamente, como também sou plenamente
        conhecido.''',

        '13' : '''Agora, pois, permanecem a fé, a esperança, o
        amor, estes três; mas o maior destes é o amor.'''
         }
        sg.popup_scrolled(cap[versiculox],title='versículo')
        print(cap[versiculox])
        print('I Corintios 13 tem 13 versículos')
        print('*'*7)
def Apocalipse():
    print('Apocalipse Teste rico é morto!')


