# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define es = Character("Tu")
define furry = Character("Polo")
define egirl = Character("Elīza")
define slacker = Character("Kristers")


# The game starts here.

label start:

    play music "binari.wav"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene rb19_better

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "Ir tava pirmā diena Batvijas Universitātē. Tu esi pavadījis pēdējos 3 mēnešus sekmējis savu profesionālo izaugsmi…"

    "Spēlējot LOL un dažreiz paskatoties kādu labu anime."

    "Tu esi gatavs Datorikas pirmajam kursam."

    "Un gatavs atrast mīlestību"

menu:
    "Ar ko vēlies parunāties?"

    "Elīzi":
        "Nē nu vari jau mēģināt"
        jump egirl_izv

    "Kristeru":
        "Viņš izskatās foršs"
        jump slacker_izv

    "Niks":
        "Tavs vecais klasesbiedrs"
        jump furry_izv

label egirl_izv:

    play music "binari_stink.wav"

    "Tu lēnām pieej pie Elīzas, kas tevi sākumā nepamana savu augsto Demonia dēļ. Viņa ir kā sapnis. Vismaz tavi sapņi. Tu uztaisi mazliet patētisku skaņu un viņa paskatās uz tevi"

    show egirl_temp
    with fade

    menu:
        "Tu esi kā princese":
            jump turp1

        "Vai tev patīk videospēles?":
            jump turp1

        "Kā iet?":
            jump turp1

label turp1: 

    es "*mazs pinkstiens*"

    es"{i}Tas nebija, ko es gribēju teikt! Es esmu nožēlojams!{/i}"

    play sound "Generic_egirl_noise.mp3"

    egirl "Tu kaut ko teici? Tu ar mani gribēji runāt? Nē nu, es nebrīnos."

    egirl "Man īstenībā šo izglītību nevajag. Man jau ir savs ļoti ienesīgais bizness, liekot bildes internetā."

    es "{i}Diez kā tas izpaužas{/i}"

    egirl "Mani fani mani mīl un OnlyF… fui, mans galvenais sociālais medijs, manuprāt, varēs mani uzturēt līdz mūža galam."

    es "{i}Uzminēju{/i}"

    play sound "Generic_egirl_noise.mp3"

    egirl "Es te tikai esmu, jo man mamma teica, ka man jādabū “īsts darbs” un jāpelna “godīga nauda”."

    menu:
        "Es neredzu problēmu ar tavu ienākumu avotu.":
            jump turp2

        "Nu man ir prieks, ka tomēr esi šeit un dabūjām iepazīties :)":
            jump turp2

        "Kāds ir tavs OnlyFans?":
            jump turp2

label turp2:

    es "uhh.. mmmmmm… shhh… uuuuuuuuuuhhhhhhh."

    es "{i}Bļin, viņas skaistums ir man atņēmis vārdus!{/i}"

    egirl "Tu mēms esi vai kas? Ko tu no manis gribi?"

    menu:
        "Gribi ar mani kopā sēdēt lekcijā?":
            jump turp3

        "Vai vēlies ar mani aiziet randiņā?":
            jump turp3

        "Kāds ir tavs OnlyFans?":
            jump turp3

label turp3:

    es "…g-gribu uhhh ar.. t-tev-"

    play sound "Egirl_scoff.mp3"

    egirl "TU tagad mēģini MANI koļīt??? Tu mazais nožēlīgais kropli! Tu vispār zini ar ko tu runā?? Ja to vispār var saukt par runāšanu"

    egirl "Tagad iedod man piecīti par to, ka es vispār ar tevi runāju"

    menu:
        "Iedod 5 eiro":
            jump turp4

        "Nedod viņai neko":
            jump turp4

label turp4:

    "Tu viņai iedod 20 eiro"

    es "{i}Tā bija mana šīs nedēļas ēdiena nauda.{/i}"

    egirl "Lūdzu! Noskenē šito, samaksā un redzēsi, ko gribēji."

    play sound "Solosana.mp3"

    "Viņa iedod QR kodu savam OnlyFans un skaļi aizsoļo prom"

    jump beigas


label slacker_izv:

    play music "binari_slacker.wav"

    show slacker_temp
    with fade

    "Kristers izskatās tik skaisti. Tu pieej pie viņa kāmēr viņš kaut ko tin Raiņa Bulbāra gaitenī"

    slacker "Ko tu skaties? Gribi ar mani uzpīpēt. Zini, īpaši priekš tevis, būs 10 eiro, lai to izdarītu."

    "Tu iedod viņam 10 eiro un jūs izejat ārā pagalmā."

    play sound "Generic_slacker_noise.mp3"

    slacker "Vot šeit ir labākā vietiņa. Es jau zinu, es esmu pirmajā kursā jau trešo reizi. Bet reāli tā nebija mana vaina, Datorpogu spaidīšanas kurss vienkārši bija pārāk grūts!"

    es "{i}Es to no pamatskolas informātikas stundām varēju pielīdzināt{/i}"

    slacker "Bet reāli, tu liecies baigi labais džeks. Gribi man palīdzēt ar mājasdarbiem? Tu man tos atsūti, es tev ļauju katru mēnesi samaksāt 10 eiro lai darītu tieši šo pašu."

    menu:
        "Pieņemt piedāvājumu":
            jump turp5

        "Atteikt":
            jump turp5

label turp5:

    es "uhh.. es.. uuuuhhh"

    es "{i}Tas galīgi nav pareizi! Viņa skaistums ir mani pataisījis mēmu!{/i}"

    play sound "Smoking.mp3"

    slacker "Perfekti, tad ir sarunāts!"

    "Viņš tev padod smēķējamo, tu esi ekstāzē. Tu pieskaries ar lūpām kaut kam, kur viņš tieši tāpat pieskārās… Un tad tu sāc klepot un atdod."

    slacker "Tu vispār domā iet uz lekcijām? Es gribēju aiziet šodien nu vismaz uz pirmo dienu bet man jāiet uz koncertu Bepo vakarā un man pirms tam ir jāizguļas. Es te tikai esmu, jo man vajag, ka mamma domā, ka esmu unītī."

    es "{i}Viņš noteikti nepabeigs arī šogad. Man ir jāmēģina dabūt randiņš pirms viņu eksmatrikulē!{/i}"

    menu:
        "Vai vēlies kopā ar mani pamācīties?":
            jump turp6

        "Kāds koncerts? Varbūt es arī varu aiziet!":
            jump turp6

        "Gribi iet pie manis, uzsmēķēt zāli un redzēt, kas notiek tālāk?":
            jump turp6

label turp6:

    es "uhhhhhhh….mmmmmmm… e-es t-t-tevi ko-kopā"

    es "{i}Atkal! Es esmu vienkārši izgāšanās!{/i}"

    slacker "OOOOOOOOh tu man reāli sit kanti, vecīt. Zini, tu liecies diezgan chill and shi, bet like.. sorry nē. Tu vēl joprojām vari darīt manus mājasdarbus doe."

    jump beigas



label furry_izv:

    play music "binari_furry.wav"

    show furry_temp
    with fade

    "Viņš ir mainījies kopš vasaras sākuma. Tev viņš vienmēr likās savā veidā pievilcīgs."

    play sound "Woof.mp3"

    furry "Hei, mazais! *woof*"

    menu:
        "Čau!":
            jump turp7

        "Čiki briki!":
            jump turp7

        "Slay!":
            jump turp7

label turp7:

    play sound "Elsosana.mp3"

    furry "Kā tev patīk sava pirmā diena? *elsojot* Man ļoti patīk. Es esmu pavadījis visu vasaru strādājot kiberdrošībā un tik ļoti gaidu uzlabot savas prasmes!"

    furry "Arī, kā vari redzēt, esmu arī mazliet mainījis savu imidžu, kā saka. Esmu sapratis savu īsto būtību. *iekaucas*"

    es "{i}Viņš izskatās amazing, manas jūtas ir tikai pastiprinājušās kopš vidusskolas!{/i}"

    furry "Esmu tagad pūkainis (vai kā angliski sauktu, furry)."

    es "{i}Interesanti, un mazliet… seksīgi{/i}"

    menu:
        "Kas notika?":
            jump turp8

        "Gribi atnākt pie manis?":
            jump turp8

        "Slay!":
            jump turp8

        "Es gribu tev pievienoties.":
            jump turp8

label turp8:
    es "… uhhhh k-kas?"

    es "{i}Bļin, tas nebija tas, ko gribēju teikt!{/i}"

    play sound "Kauksaba.mp3"

    furry "A vot kā tas notika? Es vienreiz gāju ar kolēģiem pārgājienā pa mežu pie Baizkraukles un mēs dzirdējām kā netālu no mums dzirdējām kaukšanu."

    furry "Mēs gribējām skriet, jo baidījāmies, ka tas būs vilku bars, bet tad no tās pašas vietas dzirdējām smiešanos. Aizgājām paskatīties..."

    play sound "Elsosana.mp3"

    furry "Tur bija bars ar pūkaiņiem! Viņi skraidīja apkārt un cīkstējās uz zemes. Tas prieks, ko viņi izstaroja, bija vienreizējs! *sāk elsot*"

    furry "Mēs pievienojāmies! Mēs kaucām un skrāpējām un skrējām līdz nākamā rīta gaismai un tad es zināju - šis ir mans pulks!"

    furry "Kopš tā laika esmu izvestējis 3000 eiro uz mana jaunā izskata. Vai tev patīk?"

    menu:
        "Tu izskaties vienreizēji!":
            jump turp9

        "Slay!":
            jump turp9

        "Vai varu pievienoties?":
            jump turp9

label turp9:

    es "…haha omg wow lol xd sheesh haha"
    
    es "Es gribu sevi nogalināt."

    furry "Es zinu! Izskatos vienreizēji"

    play sound "Woof.mp3"

    furry "Kā tev iet? *ierejas*"

    es "{i}Man vispār iet ļoti labi. Tagad, kad esam jaunā vietā, gribēju tev kaut ko atzīt. Tu man esi ļoti ilgi paticis un es ļoti gribētu ar tevi aiziet randiņā, ja tas nav pārāk tieši teikts. Es arī gribētu zināt vairāk par tavām vasaras atklāsmēm.{/i}"

    es "Gribi… uuuuuhhhhhh… kopā sēdēt?"

    es "{i}Viss, manai dzīvei nav jēga, es iešu mājās skatīties Euphoria.{/i}"

    furry "Uhhh.. *pieliek ķepu priekšā sejai* es zinu, ka esmu ļoti interesanta un inteliģenta persona, bet man tiešām nešķiet, ka tu esi manā līmeni. Vai tev pat ir aste? Piedod, bet lūdzu ej prom"

    jump beigas
    # These display lines of dialogue.
label beigas:

    play music "game_over.wav"
    
    scene rb19_better
    with fade
    
    "Tu aizej mājās un raudi gultā."

    "Uztaisījām ar Ren'Py. Izabella un Olivers <3"

    # This ends the game.

return