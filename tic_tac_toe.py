import random

def tahtaCiz(tahta):
    print('   |   |')
    print(' ' + tahta[7] + ' | ' + tahta[8] + ' | ' + tahta[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tahta[4] + ' | ' + tahta[5] + ' | ' + tahta[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tahta[1] + ' | ' + tahta[2] + ' | ' + tahta[3])
    print('   |   |')

def oyuncuGirisi():
    harf=''
    while not(harf=='X' or harf=='O'):
        print("X ya da O harflerinden birini seciniz:")
        harf=input().upper()
        #kullanıcının secmediği harf bilgisayarın seçimi kabul edilecek
        if harf=='X':
            return['X','O']
        else:
            return ['O','X']

def onceBaslayacakOlan():#random olarak secilecek
    if random.randint(0,1)==0:
        return 'bilgisayar'
    else:
        return 'oyuncu'

#eğer oyuncu tekrar oynamak isterse True döner
def tekrarDene():
    print("Tekrar oynamak ister misin (evet/hayir)")
    return input().lower().startswith('e')

def makeMove(tahta, harf, hareket):
    tahta[hareket]=harf

def isWinner(bo,le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # en tepede

            (bo[4] == le and bo[5] == le and bo[6] == le) or  # ortada

            (bo[1] == le and bo[2] == le and bo[3] == le) or  # altta

            (bo[7] == le and bo[4] == le and bo[1] == le) or  # sol tarafta

            (bo[8] == le and bo[5] == le and bo[2] == le) or  # ortada

            (bo[9] == le and bo[6] == le and bo[3] == le) or  # sağ tarafta

            (bo[7] == le and bo[5] == le and bo[3] == le) or  # çapraz

            (bo[9] == le and bo[5] == le and bo[1] == le))  # çapraz
def getBoardCopy(tahta):
    #tahta listesini bir kopyasını alıp çoğaltma
    dupeBoard=[]
    for i in tahta:
        dupeBoard.append(i)
    return dupeBoard

#seçilen hareket tahtada mevcutsa mevcut duruma dön
def bosVarMi(tahta,hareket):
    return tahta[hareket]==''

def getPlayerMove(tahta):
    hareket=''
    while hareket not in '1 2 3 4 5 6 7 8 9'.split() or not bosVarMi(tahta,int(hareket)):
        print("Bir sonraki hareketiniz nedir?(1-9)")
        hareket=input()
        print ("1."+hareket)
        return  int(hareket)

def listedeRastgeleHareketEt(tahta,hareketListesi):
    olasiHareket=[]
    for i in hareketListesi:
        if bosVarMi(tahta,i):
            olasiHareket.append(i)
        if len(olasiHareket)!=0:
            return random.choice(olasiHareket)
        else:
            return None

def bilgisayarHareketi(tahta,bilgisayarHarfi):
    if bilgisayarHarfi=='X':
        oyuncuHarfi='O'
    else:
        oyuncuHarfi='X'

    #bir sonraki harekette kazanıp kazanmadığımızı kontrol etme
    for i in range(0,9):
        kopya=getBoardCopy(tahta)
        if bosVarMi(kopya,i):
            makeMove(kopya,bilgisayarHarfi,i)
            if isWinner(kopya,bilgisayarHarfi):
                return i

    #oyuncunun bir sonraki hamlede kazanıp kazanmadığını kontrol etme
    for i in range(0,9):
        kopya=getBoardCopy(tahta)
        if bosVarMi(kopya,i):
            makeMove(kopya,bilgisayarHarfi,i)
            if isWinner(kopya,bilgisayarHarfi):
                return i

    #uygunsa, köşelerden birini seçme
    hareket=listedeRastgeleHareketEt(tahta,[1,3,7,9])
    if hareket!=None:
        return hareket

    #uygunsa,ortayı seçme
    if bosVarMi(tahta,5):
        return 5

    #kenarlardan birini seçme
    return listedeRastgeleHareketEt(tahta,[2,4,6,8])

def tahtaDoluMu(tahta):
    for i in range(1,10):
        if bosVarMi(tahta,i):
            return False
    return True

print("Tic Tac Toe'ya hosgeldiniz!")

while True:
    #tahtayı sıfırlama
    theBoard=['']*10
    oyuncuHarfi,bilgisayarHarfi=oyuncuGirisi()
    turn=onceBaslayacakOlan()
    print("once "+turn+" baslayacak")
    gameIsPlaying=True

    while gameIsPlaying:
        if turn=='oyuncu':
            tahtaCiz(theBoard)
            hareket=getPlayerMove(theBoard)
            makeMove(theBoard,oyuncuHarfi,hareket)

            if isWinner(theBoard,oyuncuHarfi):
                tahtaCiz(theBoard)
                print("Tebrikler, kazandiniz!")
                gameIsPlaying=False
            else:
                if tahtaDoluMu(theBoard):
                    tahtaCiz(theBoard)
                    print("Oyun berabere")
                    break
                else:
                    turn='bilgisayar'

        else:
            hareket=bilgisayarHareketi(theBoard,bilgisayarHarfi)
            makeMove(theBoard,bilgisayarHarfi,hareket)

            if isWinner(theBoard,bilgisayarHarfi):
                drawBoard(theBoard)
                print("Bilgisayar sizi yendi, kaybettiniz!")
                gameIsPlaying=False
            else:
                if tahtaDoluMu(theBoard):
                    tahtaCiz(theBoard)
                    print("Oyun berabere")
                    break
                else:
                    turn='oyuncu'

    if not tekrarDene():
        break






