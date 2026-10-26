# Arte das árvores regionais — 1.5.0

> A jabuticabeira (Semente de Jabuticaba) usa a pasta `assets/arvores/jabuticabeira`.

Todos os placeholders das seis árvores do ZIP recebido foram substituídos por
arte nova. A geração de imagens foi usada para desenhar cada espécie, com os
sprites da Wiki como referência visual. Depois foi feito apenas o recorte,
redução sem suavização, alinhamento e empacotamento nas grades do mod.
Os prompts de geração estão em `PROMPTS_ARTE_ARVORES.json`.

## Inventário da arte nova

| Espécie | Semente / plantio | Produto | Folhas sazonais | Pasta |
|---|---|---|---|---|
| Araucária | Pinhão de Araucária | Breu de Araucária | Primavera, verão, outono, inverno | `assets/arvores/araucaria` |
| Erva-mate | Semente de Erva-mate | Extrato de Erva-mate; folhas | As quatro estações | `assets/arvores/erva_mate` |
| Bracatinga | Semente de Bracatinga | Resina de Bracatinga | As quatro estações | `assets/arvores/bracatinga` |
| Jabuticabeira | Semente de Jabuticaba | Seiva Aromática | As quatro estações | `assets/arvores/jabuticabeira` |
| Canela-preta | Semente de Canela-preta | Resina de Canela-preta | As quatro estações | `assets/arvores/canela_preta` |
| Butiazeiro | Caroço de Butiá | Butiá | As quatro estações; cachos no verão/outono | `assets/arvores/butiazeiro` |

São **24 PNG sazonais de 144×160 + 13 PNG de itens de 16×16**.
As árvores são perenes: mantêm folhas no inverno, com neve, como já previsto
nos dados recebidos. A variação sazonal é visual, não altera a produção.

Cada folha sazonal contém a árvore adulta, broto, muda, juvenil, folhas soltas,
toco e três overlays de rachaduras. As duas fases juvenis maiores usam o
mesmo quadro, como no formato de árvores silvestres do jogo.

## Grade mantida

Colunas de 48 px: normal em x=0; alternativa em x=48; musgo em x=96.
O butiazeiro usa a alternativa para os cachos; não ganhou produção nova.

| Elemento | x relativo à coluna | y | Largura | Altura |
|---|---:|---:|---:|---:|
| Árvore adulta | 0 | 0 | 48 | 96 |
| Juvenil | 0 | 96 | 16 | 32 |
| Toco (região reservada) | 32 | 96 | 16 | 32 |
| Quatro folhas | 16 | 112 | 16 | 16 |
| Broto | 0 | 128 | 16 | 16 |
| Muda | 16 | 128 | 16 | 16 |
| Semente no chão | 32 | 128 | 16 | 16 |
| Rachaduras (3 quadros) | 0 | 144 | 48 | 16 |

O desenho do toco fica na metade inferior da região reservada. As raízes e
troncos permanecem centralizados. Nenhum mapa, tile ou hitbox foi alterado.
Todos os pixels finais são nítidos, sem interpolação e com alpha 0 ou 255.

## Arquivos e integração

- As referências de textura do complemento foram aproveitadas sem mudar IDs.
- Os seis JSON de dados do complemento ficam em `data/arvores_regionais/`.
- O `content.json` passou a carregar esse conteúdo dentro do pack principal.
- As traduções foram unificadas sem sobrescrever traduções conflitantes.
- `pinhao.png` e `folhas.png`, antes opcionais e ausentes, agora existem e são carregados.
- `assets/arvores/` contém apenas os sprites finais usados pelo jogo.
- A pasta `sprites_criados_organizados/arvores_novas/` repete esses PNG para edição.
- As fontes maiores da geração estão em `sprites_criados_organizados/fontes_arte/`.

Não foram criadas novas madeiras, receitas ou regras de crescimento nesta
etapa de arte. Também não foram redesenhados os peixes, cultivos e pratos já
incluídos no pack anterior. O tema visual de itens vanilla do pack anterior
foi preservado; estas seis árvores são entradas adicionais do pacote recebido.

## Referências consultadas

- [Árvores — Wiki PT-BR](https://pt.stardewvalleywiki.com/%C3%81rvores)
- [Dados de árvores silvestres](https://stardewvalleywiki.com/Modding:Wild_trees)
- Sprites de estágios adultos de carvalho, pinheiro e mogno exibidos na página
  Árvores, para densidade de pixels, contraste e apresentação das estações.

O material final é arte regional gerada, não uma cópia dos sprites da Wiki.
Não houve teste dentro do jogo: a validação realizada é estática e documentada.


## Correção 1.8.2

**Folhas soltas.** O jogo desenha as folhas que caem a partir dos quatro quadros de 8x8
em x=16..31, y=112..127 da folha sazonal carregada no momento, sorteando um dos quatro.
Cada folha sazonal tinha uma folha de cada estação nesses quadros, então as cores se
misturavam. Agora os quatro quadros de cada estação usam só a folha daquela estação
(a própria arte, espelhada para variar). No outono da erva-mate, da bracatinga e da
canela-preta entram as duas cores de outono da arte original.

| Espécie | Primavera | Verão | Outono | Inverno |
|---|---|---|---|---|
| Araucária | verde-escura | verde-escura | oliva | neve |
| Erva-mate | verde | verde-escura | oliva + frutinho vermelho | verde-escura |
| Bracatinga | verde-clara | verde-acinzentada | oliva + laranja | verde-acinzentada |
| Jabuticabeira | verde-clara | verde-azulada | oliva-dourada | neve |
| Canela-preta | verde | verde-escura | oliva + avermelhada | verde-escura |
| Butiazeiro | verde | verde-azulada | dourada | neve |

**Queda da árvore.** A copa (48x96 em y=0) é desenhada girando sobre a base quando a árvore
cai, e o toco (16x32 em x=32, y=96) continua parado no mesmo tile. A copa tinha o tronco
inteiro até o chão, com raízes, e por isso parecia que a árvore caía com o toco. Agora,
nas três colunas (normal, alternativa e musgo), a copa termina logo abaixo do topo do
toco: as linhas de baixo foram apagadas e uma faixa de casca de poucas linhas cobre o
corte do toco enquanto a árvore está de pé. De pé, a árvore fica igual; caindo, só o
tronco e a copa giram. Os quadros do toco, das mudas e das rachaduras não mudaram.

Conferido nos arquivos: mudanças só nas áreas das folhas e da base da copa; nenhuma cor
de outra estação nos quadros de folhas; nenhum pixel da copa abaixo do corte; alpha
binário mantido. Não testado no jogo.
