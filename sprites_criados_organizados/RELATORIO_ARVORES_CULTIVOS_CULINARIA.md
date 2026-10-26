# Relatório de regionalização - Vale das Araucárias

## O que foi substituído

- Sementes e derivados vanilla foram regionalizados mantendo os mesmos IDs: bolota, semente de ácer, pinha, semente de mogno, madeira, madeira de lei, xarope de ácer, resina de carvalho e alcatrão de pinho.
- Receitas de construção não tiveram quantidade, desbloqueio ou lógica alterados. Como os IDs de madeira e madeira de lei foram preservados, elas passam a usar visualmente `Madeira regional` e `Madeira nobre do Sul` sem quebrar saves.
- As árvores frutíferas do mod receberam sprites próprios de linha inteira em `fruitTrees.png`, mantendo o `TextureSpriteRow` e a mecânica já configurada.

## O que foi adicionado

- `assets/cultivos_culinaria/objetos.png`: 39 sprites 16x16 para sementes, colheitas, frutas, ingredientes e pratos.
- `assets/cultivos_culinaria/crops.png`: 6 linhas de cultivo 16x32 com fases de crescimento.
- `assets/cultivos_culinaria/fruitTrees.png`: 4 linhas de árvores frutíferas regionais 48x80.
- `assets/arvores_regionais/objetos/`: 9 sprites 16x16 para itens vanilla regionalizados.
- `data/arvores_regionais_vanilla.json`: patch separado para nomes, descrições e imagens dos itens vanilla regionalizados.
- `assets/cultivos_culinaria/PREVIA_CULTIVOS_CULINARIA.png`: prévia visual rápida dos sprites criados.

## Erros encontrados e corrigidos

- O README informava que cultivos e culinária estavam com imagens provisórias. Agora os itens apontam para sprites próprios.
- Cultivos novos tinham `Texture`/`SpriteIndex` sem uma folha customizada carregada; foi criado e carregado `Mods/{{ModId}}/CultivosCulinariaCrops`.
- Objetos de cultivos, árvores frutíferas, ingredientes e receitas tinham sprites ausentes/provisórios; foram redirecionados para `Mods/{{ModId}}/CultivosCulinariaObjetos`.
- Árvores frutíferas novas tinham dados sem sprites regionais completos; foi criado `Mods/{{ModId}}/CultivosCulinariaFruitTrees`.
- Itens vanilla ligados a árvores e madeira ainda apareciam com nomes/ícones originais; foram regionalizados preservando IDs.
- O `Include` principal estava agrupando quatro arquivos em um único `FromFile`; foi separado em quatro includes compatíveis e fáceis de validar.

## Observação técnica sobre árvores comuns

A regionalização dos itens vanilla ligados às árvores foi feita por ID e sprite 16x16, o que preserva crescimento, plantio, spawn, receitas e compatibilidade com saves. O corpo visual completo das árvores comuns em `Data/WildTrees` não foi trocado neste pacote porque esse tilesheet depende do layout exato de animações/estágios do jogo e precisa ser testado no SMAPI com os assets originais carregados para garantir que não haja quebra de tiles, musgo, folhas ou hitbox. Como a regra principal era não alterar a mecânica nem quebrar mapas, a alteração segura foi limitada a nomes, descrições, sementes, madeiras e derivados.

## Tabela de mapeamento

| Item original | Item regional novo | Tipo | Estação | Semente | Sprite criado | Arquivo alterado |
|---|---|---|---|---|---|---|
| Carvalho / Bolota | Jabuticabeira / Semente de jabuticaba | Árvore comum e semente | Mesma da original | Semente de jabuticaba | 309-semente-jabuticaba.png | data/arvores_regionais_vanilla.json |
| Ácer / Semente de ácer | Bracatinga / Semente de bracatinga | Árvore comum e semente | Mesma da original | Semente de bracatinga | 310-semente-bracatinga.png | data/arvores_regionais_vanilla.json |
| Pinheiro / Pinha | Araucária / Pinha de araucária | Árvore comum e semente | Mesma da original | Pinha de araucária | 311-pinha-araucaria.png | data/arvores_regionais_vanilla.json |
| Mogno / Semente de mogno | Canela / Semente de canela | Árvore comum e semente | Mesma da original | Semente de canela | 292-semente-canela.png | data/arvores_regionais_vanilla.json |
| Madeira | Madeira regional | Material | N/A | N/A | 388-madeira-regional.png | data/arvores_regionais_vanilla.json |
| Madeira de lei | Madeira nobre do Sul | Material | N/A | N/A | 709-madeira-nobre-sul.png | data/arvores_regionais_vanilla.json |
| Xarope de ácer | Seiva de bracatinga | Derivado de torneirinha | N/A | N/A | 724-seiva-bracatinga.png | data/arvores_regionais_vanilla.json |
| Resina de carvalho | Resina de jabuticabeira | Derivado de torneirinha | N/A | N/A | 725-resina-jabuticabeira.png | data/arvores_regionais_vanilla.json |
| Alcatrão de pinho | Resina de araucária | Derivado de torneirinha | N/A | N/A | 726-resina-araucaria.png | data/arvores_regionais_vanilla.json |
| Muda/fruto de árvore frutífera custom | Bergamoteira / Bergamota | Árvore frutífera | Mesma configurada no mod | Muda de bergamoteira | fruitTrees.png row 0 + objetos.png | data/arvores.json |
| Muda/fruto de árvore frutífera custom | Pitangueira / Pitanga | Árvore frutífera | Mesma configurada no mod | Muda de pitangueira | fruitTrees.png row 1 + objetos.png | data/arvores.json |
| Muda/fruto de árvore frutífera custom | Araucária / Pinhão | Árvore frutífera | Mesma configurada no mod | Muda de araucária | fruitTrees.png row 2 + objetos.png | data/arvores.json |
| Muda/fruto de árvore frutífera custom | Erva-mate / Erva-mate | Árvore frutífera | Mesma configurada no mod | Muda de erva-mate | fruitTrees.png row 3 + objetos.png | data/arvores.json |
| Novo cultivo do mod | Mandioca | Lavoura | Mesma configurada no mod | Muda de mandioca | crops.png row 0 + objetos.png | data/cultivos.json |
| Novo cultivo do mod | Batata-doce | Lavoura | Mesma configurada no mod | Muda de batata-doce | crops.png row 1 + objetos.png | data/cultivos.json |
| Novo cultivo do mod | Feijão-preto | Lavoura | Mesma configurada no mod | Semente de feijão-preto | crops.png row 2 + objetos.png | data/cultivos.json |
| Novo cultivo do mod | Cebola | Lavoura | Mesma configurada no mod | Muda de cebola | crops.png row 3 + objetos.png | data/cultivos.json |
| Novo cultivo do mod | Maracujá | Lavoura | Mesma configurada no mod | Semente de maracujá | crops.png row 4 + objetos.png | data/cultivos.json |
| Novo cultivo do mod | Pimentão | Lavoura | Mesma configurada no mod | Muda de pimentão | crops.png row 5 + objetos.png | data/cultivos.json |
| Nova receita do mod | Polenta | Receita culinária | N/A | N/A | objetos.png slot 24 | data/receitas.json |
| Nova receita do mod | Polenta com queijo | Receita culinária | N/A | N/A | objetos.png slot 25 | data/receitas.json |
| Nova receita do mod | Churrasco gaúcho | Receita culinária | N/A | N/A | objetos.png slot 26 | data/receitas.json |
| Nova receita do mod | Arroz carreteiro | Receita culinária | N/A | N/A | objetos.png slot 27 | data/receitas.json |
| Nova receita do mod | Barreado | Receita culinária | N/A | N/A | objetos.png slot 28 | data/receitas.json |
| Nova receita do mod | Pierogi | Receita culinária | N/A | N/A | objetos.png slot 29 | data/receitas.json |
| Nova receita do mod | Entrevero de pinhão | Receita culinária | N/A | N/A | objetos.png slot 30 | data/receitas.json |
| Nova receita do mod | Chimarrão | Receita culinária | N/A | N/A | objetos.png slot 31 | data/receitas.json |
| Nova receita do mod | Pinhão cozido | Receita culinária | N/A | N/A | objetos.png slot 32 | data/receitas.json |
| Nova receita do mod | Cuca de maçã | Receita culinária | N/A | N/A | objetos.png slot 33 | data/receitas.json |
| Nova receita do mod | Feijão tropeiro | Receita culinária | N/A | N/A | objetos.png slot 34 | data/receitas.json |
| Nova receita do mod | Doce de batata-doce | Receita culinária | N/A | N/A | objetos.png slot 35 | data/receitas.json |
| Nova receita do mod | Quirera com carne suína | Receita culinária | N/A | N/A | objetos.png slot 36 | data/receitas.json |
| Nova receita do mod | Pirão de peixe | Receita culinária | N/A | N/A | objetos.png slot 37 | data/receitas.json |
| Nova receita do mod | Aipim frito | Receita culinária | N/A | N/A | objetos.png slot 38 | data/receitas.json |

## Validação estática

- `manifest.json` e todos os JSONs do mod foram validados com parser JSON.
- Caminhos de sprites adicionados existem no pacote.
- Tamanhos dos sprites criados:
  - `objetos.png`: 128x80.
  - `crops.png`: 128x192.
  - `fruitTrees.png`: 432x320.
  - sprites vanilla regionalizados: 16x16 cada.
- Mecânicas de crescimento, estações, quantidades, ingredientes, lojas e desbloqueios não foram alterados intencionalmente.

## Teste no jogo

Não foi possível executar Stardew Valley/SMAPI neste ambiente. A validação feita aqui é estática: JSON, caminhos, dimensões de imagem e integridade do zip.
