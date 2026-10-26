VARAS_LEND1_LEND2_COVOS_MERCADO
Vale das Araucárias - versão 1.1.0 - content pack para Content Patcher

Junta em um só mod:
  - peixevaras_peixeslendarios 1.0.0 (47 peixes de vara + 5 lendários)
  - ValeDasAraucarias_CovoLendariosMercado 1.1.0 (covo, Lendários II e
    Mercado Noturno)
Nomes e sprites são os mesmos dos dois mods. As descrições foram revisadas
na versão 1.1.0 (veja HISTÓRICO).

O QUE O MOD FAZ
---------------
Troca o nome exibido, a descrição e o sprite de item de 70 itens de pesca
por espécies e referências do Sul do Brasil:

  Grupo              Itens   Nome   Descrição   Sprite
  Peixes de vara       47    novo     nova       novo
  Lendários             5    novo     nova       novo
  Lendários II          5    novo     nova       novo
  Covo                 10    novo     nova       novo
  Mercado Noturno       3    novo     nova       novo
  Total                70

A lista completa (ID, nome original, nome novo e descrição) está em
LISTA.txt.
PREVIA.png mostra os 70 sprites ampliados.

Preço, dificuldade, movimento no minijogo, estação, horário, clima, local,
iscas, covos, receitas, pacotes do Centro Comunitário, missões, viveiros e
ovas continuam exatamente iguais aos do jogo original.

REQUISITOS
----------
- Stardew Valley 1.6 ou superior
- SMAPI 4.0 ou superior ............ https://smapi.io
- Content Patcher 2.0 ou superior .. https://www.nexusmods.com/stardewvalley/mods/1915

INSTALAÇÃO
----------
1. Feche o jogo.
2. APAGUE da pasta Mods as versões antigas, se estiverem lá:
     PeixesDoSul
     PeixesLendariosRenomeados
     peixevaras_peixeslendarios
     ValeDasAraucarias_CovoLendariosMercado
   Este mod já contém todos eles. Deixar os antigos instalados aplicaria as
   mesmas mudanças duas vezes.
3. Extraia o ZIP e mova a pasta "varas_lend1_lend2_covos_mercado" para dentro
   da pasta Mods. O caminho final deve ficar assim:
     Stardew Valley/Mods/varas_lend1_lend2_covos_mercado/manifest.json
4. Abra o jogo pelo SMAPI.

Onde fica a pasta do jogo (instalação padrão):
- Steam no Windows: C:\Program Files (x86)\Steam\steamapps\common\Stardew Valley
- GOG no Windows:   C:\Program Files (x86)\GOG Galaxy\Games\Stardew Valley
- Linux (Steam):    ~/.local/share/Steam/steamapps/common/Stardew Valley
- macOS (Steam):    ~/Library/Application Support/Steam/steamapps/common/
                    Stardew Valley/Contents/MacOS

COMO CONFERIR NO JOGO
---------------------
Na janela do SMAPI, digite:  patch summary
Procure "varas_lend1_lend2_covos_mercado" na lista: os 71 patches devem
aparecer como aplicados e sem erro. Para ver os itens sem precisar pescar,
um mod de spawn de itens (por exemplo, CJB Item Spawner) ajuda.

SAVES
-----
Funciona em save novo ou existente. O ID e o nome interno de cada item não
mudam: os peixes que já estão no inventário ou em baús continuam sendo os
mesmos itens e passam a mostrar o nome e o sprite novos. Para desfazer, basta
remover a pasta do mod.

COMO O MOD FUNCIONA
-------------------
content.json tem 71 patches:
- 1 EditData em Data/Objects que muda só DisplayName e Description dos
  70 itens. O nome interno (Name) não é tocado.
- 70 EditImage em Maps/springobjects. Cada um copia um PNG de 16x16 de
  assets/sprites para o quadro do ID original, com PatchMode Replace.
Todos os textos ficam em i18n/default.json. Para mudar um nome, edite só
esse arquivo (ex.: "fish.715.name": "Cavaco").
Os textos aparecem em português em qualquer idioma do jogo.

O QUE NÃO É ALTERADO
--------------------
- Data/Fish e Data/Locations não recebem nenhuma edição.
- As animações dos peixes dentro de aquários usam outra imagem e continuam
  originais.
- Cartas, falas e textos de missão que citam esses itens pelo nome original
  continuam com o nome original.
- O Ifsc é encontrado e pescado exatamente como o Legend original. As 40
  provas existem só na descrição.
- O Goby (peixe de vara da versão 1.6) não faz parte deste mod.

COMPATIBILIDADE
---------------
Outro mod que altere o nome ou o sprite dos mesmos itens pode sobrescrever
este, conforme a ordem em que forem aplicados.

VERIFICAÇÃO
-----------
Conferido sem abrir o jogo: JSON válido, 70 IDs sem repetição, cada sprite
na posição certa da folha, PNGs de 16x16 com transparência, nomes e sprites
iguais aos dos mods originais, 70 descrições presentes e só caracteres que a
fonte do jogo exibe.
O jogo e o SMAPI não foram executados ao montar este pacote.

HISTÓRICO
---------
1.1.0
- Descrição nova para os 18 itens do covo, dos Lendários II e do Mercado
  Noturno, que ainda usavam o texto original do jogo.
- 7 descrições de peixes de vara corrigidas para combinar com a espécie:
    128 Baiacu-pintado ...... o veneno do baiacu é forte, não "leve"
    140 Joaninha ............ é um ciclídeo, não um bagre
    146 Tainha .............. a tainha sobe a costa, não desce
    267 Linguado-branco ..... frase corrigida
    698 Surubim-pintado ..... falava das ovas do esturjão
    706 Sairu ............... falava da migração do peixe original (shad)
    836 Raia-viola .......... descrevia uma raia comum, não a raia-viola
- Nomes, sprites, IDs e o resto do mod continuam iguais.
1.0.0
- Primeira versão: junção dos dois mods.

AVISO
-----
As histórias das descrições dos lendários são fictícias e humorísticas.
