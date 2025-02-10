# Controle de Gestos para Elden Ring

## Descrição do Projeto
Este projeto implementa um sistema de controle baseado em gestos das mãos para jogar **Elden Ring**. Utilizando a câmera do computador e a biblioteca **MediaPipe**, o programa detecta a posição das mãos e converte os gestos em comandos de teclado e mouse, permitindo uma jogabilidade inovadora e imersiva.

## Tecnologias Utilizadas
### 1. **OpenCV**
- Biblioteca utilizada para capturar e processar imagens da câmera.
- Responsável por exibir a interface visual e manipular os frames de vídeo em tempo real.

### 2. **MediaPipe**
- Framework da Google usado para detecção e rastreamento das mãos.
- Identifica pontos de referência nas mãos e fornece coordenadas precisas para controle gestual.

### 3. **pynput**
- Biblioteca usada para simular comandos do teclado e mouse.
- Permite a interação com o jogo, enviando teclas específicas com base nos gestos.

## Como Funciona
O sistema analisa os gestos das mãos e traduz os movimentos para comandos do jogo. As principais ações configuradas são:

| Gesto | Comando |
|--------|---------|
| Somente o indicador abaixado | Mover para a esquerda (`A`) |
| Somente medio abaixado | Andar para frente (`W`) |
| Somente o anelar abaixado | Mover para a direita (`D`) |
| Somente mindinho abaixado | Clicar Mouse (Ataque) |

### **Importante:**
Para que o ataque funcione corretamente, é necessário alterar a configuração do jogo e definir a tecla **'T'** como botão de ataque.

## Como Executar o Projeto
### 1. **Instalar dependências**
Certifique-se de ter o Python instalado e instale as bibliotecas necessárias com o seguinte comando:
```bash
pip install opencv-python mediapipe pynput
```

### 2. **Executar o código**
Para iniciar o controle por gestos, basta rodar o script Python:
```bash
python controle_gestos.py
```

### 3. **Configurar o jogo**
- Acesse as configurações de controles do Elden Ring.
- Altere a tecla de ataque principal para **'T'**.

## Possíveis Melhorias
- **Adicionar suporte para mais gestos**, como esquiva e bloqueio.
- **Melhorar a precisão do rastreamento**, ajustando os filtros do MediaPipe.
- **Implementar suporte para ambas as mãos**, permitindo mais comandos.

## Contribuição
Caso tenha sugestões ou melhorias, fique à vontade para contribuir com este projeto!

## Autor
Desenvolvido por Luan.

