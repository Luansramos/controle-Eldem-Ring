import cv2
import mediapipe as mp # 'as' dá apelido a biblioteca
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MouseController
import time



mp_maos = mp.solutions.hands # detecta maos
mp_desenho = mp.solutions.drawing_utils #desenha maos

maos = mp_maos.Hands()
mouse = MouseController()
#acessae imagem da camera
camera = cv2.VideoCapture(0)

resol_x = 480
resol_y = 640

#teclado:
kb = Controller() #controlador teclado



def coordenadas_maos(img,lado_invertido=False):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #muda tipo de cor da img
    resultado = maos.process(img_rgb) 
    todas_maos = []
    
    if resultado.multi_hand_landmarks: #'mult_hand_landmarks' resulta na nas coordenadas dos pontos    
        for lado_mao, marcacao_maos in zip( resultado.multi_handedness, resultado.multi_hand_landmarks):
            
            info_mao = {}
            coordenadas = []
            for marcacao in marcacao_maos.landmark:
                coord_x = int(marcacao.x * resol_x)
                coord_y = int(marcacao.y * resol_y)
                coord_z = int(marcacao.z * resol_x)
                coordenadas.append((coord_x, coord_y, coord_z))

            info_mao['coordenadas'] = coordenadas
            if lado_invertido:
                if lado_mao.classification[0].label == 'Left':
                     info_mao['lado'] = "Right"
                else:
                     info_mao['lado'] = "Left"
            else:
                     info_mao['lado'] = lado_mao.classification[0].label
                     
            #print(lado_mao.classification[0].label)
            
            todas_maos.append(info_mao)
            mp_desenho.draw_landmarks(img,
                                      marcacao_maos,
                                      mp_maos.HAND_CONNECTIONS)
    return img, todas_maos

def dedos_levantados(mao):
    dedos = []
    for ponta_dedo in [8,12,16,20]:
        if mao['coordenadas'][ponta_dedo][1] < mao['coordenadas'][ponta_dedo-2][1]:
            dedos.append(True)
        else:
            dedos.append(False)
    return dedos    




def controlar_tecla(info_dedos, estado_atual, tecla, padrao_dedos):
    """
    Controla o pressionamento e liberação de uma tecla com base nos dedos levantados.

    :param info_dedos: Lista com o estado dos dedos levantados.
    :param estado_atual: Variável que mantém o estado da tecla atual.
    :param tecla: Tecla a ser controlada.
    :param padrao_dedos: Configuração de dedos levantados para acionar a tecla.
    :return: O estado atualizado da tecla.
    """

    
    if info_dedos == padrao_dedos:
        if estado_atual != tecla:  # Só pressiona se ainda não estiver pressionada
            kb.press(tecla)
            return tecla
    else:
        if estado_atual == tecla:  # Solta a tecla quando o gesto não corresponde
            kb.release(tecla)
            return None
    return estado_atual



estado_da_tecla = None

while True:
    
    sucesso, img = camera.read() # ler img
    img = cv2.flip(img, 1)
    img, todas_maos = coordenadas_maos(img)    #mudar nome disso 
    
    #teclada
    # cv2.rectangle(img,(50,50), (100,100),BRANCO,cv2.FILLED)
    # cv2.putText(img,'Q',(65,85), cv2.FONT_HERSHEY_COMPLEX,1,PRETO, 2)
    
    
    if len(todas_maos) == 1:
        info_dedos_mao1 = dedos_levantados(todas_maos[0])
        

            
        estado_da_tecla = controlar_tecla(info_dedos_mao1, estado_da_tecla, 'w', [True, False, True, True])
        estado_da_tecla = controlar_tecla(info_dedos_mao1, estado_da_tecla, 'a', [False, True, True, True])
        estado_da_tecla = controlar_tecla(info_dedos_mao1, estado_da_tecla, 'd', [True, True, False, True])
        
        estado_da_tecla = controlar_tecla(info_dedos_mao1, estado_da_tecla, 't', [True, True, True, False])
        

        
    
        
    cv2.imshow('Imagem', img)
    tecla = cv2.waitKey(1)
    if tecla == 27:
        break