GOBY_GELEIAS
Vale das Araucárias - versão 1.1.1 - content pack para Content Patcher

O QUE O MOD FAZ
Renomeia os quatro itens abaixo e revisa suas descrições:

  ID          Original       Nome exibido
  Goby        Goby           Cambeva
  SeaJelly    Sea Jelly      Geleia de Florianópolis
  RiverJelly  River Jelly    Geleia do Açude
  CaveJelly   Cave Jelly     Geleia da Grota

Inclui um sprite novo SOMENTE para Cambeva (Goby), em PNG 16 x 16
com fundo transparente. Os três sprites das geleias continuam sendo
os mesmos do jogo, ou os que outros mods já aplicarem a essas geleias.

Os IDs e nomes internos são preservados. Preço, dificuldade, locais,
horários, estações, chances, efeitos, receitas e viveiros não são editados.
Data/Fish e Data/Locations não são alterados.

REQUISITOS
Stardew Valley 1.6+, SMAPI 4.0+ e Content Patcher 2.0+.

INSTALAÇÃO
1. Feche o jogo.
2. Extraia a pasta "goby_geleias" deste ZIP para a pasta Mods do jogo.
3. Se já tiver este mod, substitua a pasta antiga pela nova. Mantenha
   apenas uma cópia de goby_geleias dentro de Mods.
4. Inicie o jogo pelo SMAPI.

O caminho deve ficar assim:
  Stardew Valley/Mods/goby_geleias/manifest.json
  Stardew Valley/Mods/goby_geleias/content.json
  Stardew Valley/Mods/goby_geleias/assets/cambeva.png

Não precisa criar um save novo. Para desfazer as mudanças deste pack,
remova a pasta goby_geleias. Os itens continuam com seus IDs originais.
Outro mod que edite os mesmos textos ou a textura do Goby poderá
sobrescrever essas alterações, conforme a ordem dos patches.

CONFERIR NO JOGO
No console do SMAPI, use: patch summary
Procure estes três patches, sem erro:
  Goby e geleias - nomes e descricoes
  Cambeva - carregar sprite 16x16
  Cambeva - aplicar sprite somente ao Goby

Para inspecionar o objeto pelo ID original, use: list_items Goby
A prévia ampliada incluída é feita a partir do PNG usado no mod,
com ampliação por vizinho mais próximo, sem desfoque.

VALIDAÇÃO
JSONs, referências do sprite, tamanho, transparência, escopo dos patches
e integridade do ZIP foram conferidos. O jogo não foi executado neste
ambiente; a confirmação de funcionamento em partida depende do SMAPI.

ATUALIZAÇÃO 1.1.1
A Geleia da Grota recebeu uma referência à música Do Fundo da Grota,
do Baitaca. A referência é apenas texto de ambientação.
