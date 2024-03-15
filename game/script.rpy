# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define es = Character("[povname]")
define furry = Character("Polo")
define egirl = Character("Elīza")
define slacker = Character("kristers")

python:
    povname = renpy.input("Kas ir tavs vārds, pirmīt?", length = 32)
    povname = povname.strip()

    if not povname:
        povname = "Darude Sandstorm"


# The game starts here.

label start:

    play music "binari.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg rb19

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

    play music "binari_stink.mp3"

    "Tu lēnām pieej pie Elīzas, kas tevi sākumā nepamana savu augsto Demonia dēļ. Viņa ir kā sapnis. Vismaz tavi sapņi. Tu uztaisi mazliet patētisku skaņu un viņa paskatās uz tevi"

    show egirl_temp
    with fade

    menu:
        es "Tu esi kā princese"

        es "Vai tev patīk videospēles?"

        es "Kā iet?"

    es "*mazs pinkstiens*"

    es"{i}Tas nebija, ko es gribēju teikt! Es esmu nožēlojams!{/i}"

    egirl "Tu kaut ko teici? Tu ar mani gribēji runāt? Nē nu, es nebrīnos."

    egirl "Man īstenībā šo izglītību nevajag. Man jau ir savs ļoti ienesīgais bizness, liekot bildes internetā."

    es "{i}Diez kā tas izpaužas{/i}"

    egirl "Mani fani mani mīl un OnlyF… fui, mans galvenais sociālais medijs, manuprāt, varēs mani uzturēt līdz mūža galam."

    es "{i}Uzminēju{/i}"

    egirl "Es te tikai esmu, jo man mamma teica, ka man jādabū “īsts darbs” un jāpelna “godīga nauda”."

    menu:
        es "Es neredzu problēmu ar tavu ienākumu avotu."

        es "Nu man ir prieks, ka tomēr esi šeit un dabūjām iepazīties :)"

        es "Kāds ir tavs OnlyFans?"

    es "uhh.. mmmmmm… shhh… uuuuuuuuuuhhhhhhh."

    es "{i}Bļin, viņas skaistums ir man atņēmis vārdus!{/i}"

    egirl "Tu mēms esi vai kas? Ko tu no manis gribi?"

    menu:
        es "Gribi ar mani kopā sēdēt lekcijā?"

        es "Vai vēlies ar mani aiziet randiņā?"

        es "Kāds ir tavs OnlyFans?"

    es "…g-gribu uhhh ar.. t-tev-"

    egirl "TU tagad mēģini MANI koļīt??? Tu mazais nožēlīgais kropli! Tu vispār zini ar ko tu runā?? Ja to vispār var saukt par runāšanu"

    egirl "Tagad iedod man piecīti par to, ka es vispār ar tevi runāju"

    menu:
        "Iedod 5 eiro"
        "Nedod viņai neko"

    "Tu viņai iedod 20 eiro"

    es "{i}Tā bija mana šīs nedēļas ēdiena nauda.{/i}"

    egirl "Lūdzu! Noskenē šito, samaksā un redzēsi, ko gribēji."

    "Viņa iedod QR kodu savam OnlyFans un skaļi aizsoļo prom"



label slacker_izv:

    play music "binari_slacker.mp3"

    show slacker_temp
    with fade

    "Kristers izskatās tik skaisti. Tu pieej pie viņa kāmēr viņš kaut ko tin Raiņa Bulbāra gaitenī"

    slacker "Ko tu skaties? Gribi ar mani uzpīpēt. Zini, īpaši priekš tevis, būs 10 eiro, lai to izdarītu."

    "Tu iedod viņam 10 eiro un jūs izejat ārā pagalmā."

    slacker "Vot šeit ir labākā vietiņa. Es jau zinu, es esmu pirmajā kursā jau trešo reizi. Bet reāli tā nebija mana vaina, Datorpogu spaidīšanas kurss vienkārši bija pārāk grūts!"

    es "{i}Es to no pamatskolas informātikas stundām varēju pielīdzināt{/i}"

    slacker "Bet reāli, tu liecies baigi labais džeks. Gribi man palīdzēt ar mājasdarbiem? Tu man tos atsūti, es tev ļauju katru mēnesi samaksāt 10 eiro lai darītu tieši šo pašu."

    menu:
        "Pieņemt piedāvājumu"

        "Atteikt"

    es "uhh.. es.. uuuuhhh"

    es "{i}Tas galīgi nav pareizi! Viņa skaistums ir mani pataisījis mēmu!{/i}"

    slacker "Perfekti, tad ir sarunāts!"

    "Viņš tev padod smēķējamo, tu esi ekstāzē. Tu pieskaries ar lūpām kaut kam, kur viņš tieši tāpat pieskārās… Un tad tu sāc klepot un atdod."

    slacker "Tu vispār domā iet uz lekcijām? Es gribēju aiziet šodien nu vismaz uz pirmo dienu bet man jāiet uz koncertu Bepo vakarā un man pirms tam ir jāizguļas. Es te tikai esmu, jo man vajag, ka mamma domā, ka esmu unītī."

    es "{i}Viņš noteikti nepabeigs arī šogad. Man ir jāmēģina dabūt randiņš pirms viņu eksmatrikulē!{/i}"

    menu:
        es "Vai vēlies kopā ar mani pamācīties?"
        
        es "Kāds koncerts? Varbūt es arī varu aiziet!"

        es "Gribi iet pie manis, uzsmēķēt zāli un redzēt, kas notiek tālāk?"

    es "uhhhhhhh….mmmmmmm… e-es t-t-tevi ko-kopā"

    es "{i}Atkal! Es esmu vienkārši izgāšanās!{/i}"

    slacker "OOOOOOOOh tu man reāli sit kanti, vecīt. Zini, tu liecies diezgan chill and shi, bet like.. sorry nē. Tu vēl joprojām vari darīt manus mājasdarbus doe."




label furry_izv:

    play music "binari_furry.mp3"

    show furry_temp
    with fade

    "Viņš ir mainījies kopš vasaras sākuma. Tev viņš vienmēr likās savā veidā pievilcīgs."

    furry "Hei, mazais! *woof*"

    menu:
        es "Čau!"

        es "Čiki briki!"

        es "Slay!"

    furry "Kā tev patīk sava pirmā diena? *elsojot* Man ļoti patīk. Es esmu pavadījis visu vasaru strādājot kiberdrošībā un tik ļoti gaidu uzlabot savas prasmes!"

    furry "Arī, kā vari redzēt, esmu arī mazliet mainījis savu imidžu, kā saka. Esmu sapratis savu īsto būtību. *iekaucas*"

    es "{i}Viņš izskatās amazing, manas jūtas ir tikai pastiprinājušās kopš vidusskolas!{/i}"

    furry "Esmu tagad pūkainis (vai kā angliski sauktu, furry)."

    es "{i}Interesanti, un mazliet… seksīgi{/i}"

    menu:
        es "Kas notika?"

        es "Gribi atnākt pie manis?"

        es "Slay!"

        es "Es gribu tev pievienoties."

    es "… uhhhh k-kas?"

    es "{i}Bļin, tas nebija tas, ko gribēju teikt!{/i}"

    furry "A vot kā tas notika? Es vienreiz gāju ar kolēģiem pārgājienā pa mežu pie Baizkraukles un mēs dzirdējām kā netālu no mums dzirdējām kaukšanu."

    furry "Mēs gribējām skriet, jo baidījāmies, ka tas būs vilku bars, bet tad no tās pašas vietas dzirdējām smiešanos. Aizgājām paskatīties..."

    furry "Tur bija bars ar pūkaiņiem! Viņi skraidīja apkārt un cīkstējās uz zemes. Tas prieks, ko viņi izstaroja, bija vienreizējs! *sāk elsot*"

    furry "Mēs pievienojāmies! Mēs kaucām un skrāpējām un skrējām līdz nākamā rīta gaismai un tad es zināju - šis ir mans pulks!"

    furry "Kopš tā laika esmu izvestējis 3000 eiro uz mana jaunā izskata. Vai tev patīk?"

    menu:
        es "Tu izskaties vienreizēji!"

        es "Slay!"

        es "Vai varu pievienoties?"

    es "…haha omg wow lol xd sheesh haha"
    
    es "Es gribu sevi nogalināt."

    furry "Es zinu! Izskatos vienreizēji"

    furry "Kā tev iet? *ierejas*"

    menu:
        es "Man vispār iet ļoti labi. Tagad, kad esam jaunā vietā, gribēju tev kaut ko atzīt. Tu man esi ļoti ilgi paticis un es ļoti gribētu ar tevi aiziet randiņā, ja tas nav pārāk tieši teikts. Es arī gribētu zināt vairāk par tavām vasaras atklāsmēm."

    es "Gribi… uuuuuhhhhhh… kopā sēdēt?"

    es "{i}Viss, manai dzīvei nav jēga, es iešu mājās skatīties Euphoria.{/i}"

    furry "Uhhh.. *pieliek ķepu priekšā sejai* es zinu, ka esmu ļoti interesanta un inteliģenta persona, bet man tiešām nešķiet, ka tu esi manā līmeni. Vai tev pat ir aste? Piedod, bet lūdzu ej prom"

    # These display lines of dialogue.

    

    # This ends the game.

    return