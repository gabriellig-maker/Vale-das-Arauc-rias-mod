# PROGRESSO — Vale das Araucárias: Cultivos e Culinária

## Concluído
- [x] Etapa A — levantamento: documentação do Stardew Valley 1.6 (Crops, FruitTrees, Objects, Shops,
      CookingRecipes, condições de loja, comandos) e fontes regionais (Embrapa, Epagri/CNA, AEN-PR, Emater-RS,
      Revista Cultivar, Lei 11.929/2003 do RS). Arquivo: `levantamento.md`.
- [x] Etapa B — planejamento: `plano.json` é a fonte única dos dados; `PLANO.md` traz as tabelas com IDs,
      preços, estações, desbloqueios e custo dos ingredientes.
- [x] Etapa C — implementação: `scripts/gerar.py` gera o pacote inteiro a partir de `plano.json`.
- [x] Etapa D — validação estática: `scripts/validar.py` gera `VALIDACAO.txt`.
- [x] Etapa E — ZIP `ValeDasAraucarias_CultivosCulinaria.zip`.

## Conteúdo da versão 1.0.1
- 6 cultivos: mandioca, batata-doce, feijão-preto, cebola (no lugar do amendoim), maracujá, pimentão.
- 4 árvores (sistema de árvores frutíferas): bergamoteira, pitangueira, araucária (pinhão), erva-mate.
- 4 ingredientes comprados: carne bovina, carne suína, charque, farinha de mandioca.
- 15 receitas: polenta, polenta com queijo, churrasco gaúcho, arroz carreteiro, barreado, pierogi,
  entrevero de pinhão, chimarrão, pinhão cozido, cuca de maçã, feijão tropeiro, doce de batata-doce,
  quirera com carne suína, pirão de peixe, aipim frito.

## Histórico
- Pack único 1.4.0 (`varas_lend1_lend2_covos_mercado`): os cultivos e a culinária 1.0.1 foram juntados
  ao pack de peixes. Os arquivos de `data/` foram copiados sem mudança, o `content.json` ganhou 1 Include
  no final e o `i18n/default.json` recebeu as chaves novas no final. Os IDs dos itens não mudaram.
  Para atualizar: editar `plano.json` → `scripts/gerar.py` → `scripts/juntar.py`.
- 1.0.1: removida a receita Ostras gratinadas (pedido do usuário). O ID
  `ValeDasAraucarias.Culinaria_OstrasGratinadas` deixou de existir; não reutilizar.
- 1.0.0: primeira versão (16 receitas).

## Arquivos do pacote
`manifest.json`, `content.json`, `data/cultivos.json`, `data/arvores.json`, `data/receitas.json`,
`data/lojas.json`, `i18n/default.json`, `README.txt`, `COMANDOS_TESTE.txt`, `VALIDACAO.txt`, `PROGRESSO.md`.

## Fontes de desenvolvimento (fora da pasta do mod)
`ValeDasAraucarias_CultivosCulinaria_fontes.zip`: `plano.json`, `scripts/gerar.py`, `scripts/validar.py`,
`scripts/juntar.py`, `levantamento.md`, `PLANO.md`. Para regenerar o pack separado:
`python3 scripts/gerar.py plano.json build PLANO.md`; para o pack único, rodar depois
`python3 scripts/juntar.py <pack de peixes> build/ValeDasAraucarias_CultivosCulinaria build/ids.json <saída> <versão>`.
O validador também usa a lista de itens do jogo (repositório MateusAquino/stardewids, `dist/objects.json`),
os schemas do SMAPI (`src/SMAPI.Web/wwwroot/schemas`) e a pasta do pack de peixes.

## Decisões e problemas encontrados
- Sem sprites próprios (pedido do usuário): itens, plantações e árvores usam imagens do jogo como provisórias.
- Couve-manteiga não foi criada: a Couve original (250) já é a mesma variedade.
- Abóbora cabotiá não foi criada: nenhuma receita da lista precisa dela.
- Amendoim trocado por cebola: SC é o maior produtor nacional de cebola e ela entra em 2 receitas.
- Conversão de mandioca em farinha no moinho não foi feita: os IDs dos baús do moinho não estão
  documentados. A farinha de mandioca é vendida no Pierre.
- Desbloqueio por nível de habilidade evitado: só funciona ao subir de nível e não alcançaria saves avançados.
- Itens novos ficam fora da coleção de envios, das conquistas Monocultura/Policultura e do Carrinho de Viagem.
  As 15 receitas entram na coleção de culinária e na Perfeição (inevitável ao adicionar receitas).
- O jogo não pôde ser executado no ambiente de criação; os testes no jogo estão pendentes.

## Falta
- Testar no jogo (roteiro no README.txt e comandos em COMANDOS_TESTE.txt).
- Criar a arte: ícones de 16x16 para os 39 itens, linhas de plantação (16x32 por fase) e árvores.

## Próximo passo
1. Rodar o roteiro de testes num save de cópia e anotar o resultado aqui.
2. Quando houver arte, carregar os PNGs com `Load` e trocar `Texture`/`SpriteIndex` (itens e plantações)
   e `Texture`/`TextureSpriteRow` (árvores).
3. Para mudar números ou textos, editar `plano.json` e rodar `scripts/gerar.py` de novo.
