# Sprites das lavouras — 1.8.1

## Conteúdo entregue

40 PNGs novos: 12 folhas de cultivo, 12 ícones de sementes, 12 ícones de
colheitas e 4 ícones de processados/pratos. Todos vinculados ao Content Patcher.
Na versão recebida esses 40 usos visuais recorriam às texturas do jogo.
Nenhum arquivo de imagem referenciado estava ausente: faltava arte própria.

| Cultura | Pasta em `assets/lavouras/` | Fases configuradas | Dias totais | Rebrota |
|---|---|---:|---:|---|
| Feijão-preto | feijao_preto | 5 | 9 | Não |
| Mandioca | mandioca | 4 | 14 | Não |
| Batata-doce | batata_doce | 4 | 9 | Não |
| Cebola | cebola | 4 | 10 | Não |
| Maracujá | maracuja | 5 | 11 | Sim, quadro 8 |
| Pimentão | pimentao | 5 | 9 | Sim, quadro 8 |
| Aveia-branca | aveia_branca | 4 | 7 | Não |
| Cevada | cevada | 4 | 7 | Não |
| Centeio | centeio | 4 | 8 | Não |
| Soja | soja | 5 | 10 | Não |
| Azevém | azevem | 4 | 7 | Não |
| Arroz irrigado | arroz_irrigado | 4 | 9 | Não |

Cada pasta contém `cultivo.png` (128×32), `sementes.png` (16×16) e
`colheita.png` (16×16). `processados/` contém `farinha_de_milho.png`,
`aveia_em_flocos.png`, `broa_de_milho.png` e `bolo_de_fuba.png`, todos 16×16.

## Grade funcional

As plantas têm oito células de 16×32. A numeração desta tabela começa em 1.

| Quadro | Cultivo de 4 fases | Cultivo de 5 fases |
|---:|---|---|
| 1 | Plantio A | Plantio A |
| 2 | Plantio B | Plantio B |
| 3 | Broto | Broto |
| 4 | Crescimento | Crescimento |
| 5 | Pré-colheita | Crescimento |
| 6 | Maduro | Pré-colheita |
| 7 | Reserva (maduro) | Maduro |
| 8 | Reserva (maduro) | Rebrota sem frutos, ou reserva |

Os dois quadros de plantio reutilizam a mesma arte. Maracujá e pimentão
usam o oitavo quadro sem frutos; maracujá mantém a treliça em todas as fases.
Não são oito fases de crescimento: a duração vem de `DaysInPhase`.
Quadros de reserva não prolongam o crescimento. As plantas mortas continuam
usando o comportamento e o desenho nativos do jogo.

## Integração e preservação

`data/lavouras/sprites.json` carrega 40 texturas em `Mods/{{ModId}}/lavouras/`.
Cada cultura tem sua própria folha com `SpriteIndex: 0`; cada item tem
seu PNG individual com o mesmo índice. Nenhuma folha de cultivo original
é substituída. PNGs novos em RGBA, com transparência somente 0/255.

Nos 12 cultivos e 28 itens só `Texture` e `SpriteIndex` foram alterados.
O arquivo principal recebeu um Include e o manifesto passou a 1.8.1.
Permanecem os IDs, nomes, traduções, estações, dias, preços, quantidades,
lojas, máquinas, moinho, receitas, árvores, peixes e demais conteúdos.

## Arte e referências

As fontes foram criadas com a ferramenta integrada de geração de imagens,
seguindo o estilo de sprites de Stardew Valley. Depois foram recortadas,
reduzidas, quantizadas e organizadas tecnicamente na grade real do jogo.
Os ícones não são cópias extraídas dos arquivos originais.
Os prompts completos estão em `PROMPTS_ARTE_LAVOURAS.json`; as quatro
fontes maiores ficam em `sprites_criados_organizados/fontes_arte_lavouras/`.

Referências consultadas em 19/10/2026:
- [Cultivo — wiki PT](https://pt.stardewvalleywiki.com/Cultivo)
- [Lavouras — wiki PT](https://pt.stardewvalleywiki.com/Lavouras)
- [Formato de Data/Crops](https://stardewvalleywiki.com/Modding:Crop_data)
- [Formato de Data/Objects](https://stardewvalleywiki.com/Modding:Objects)
- [Grade e alinhamento de sprites](https://stardewmodding.wiki.gg/wiki/How_to_Use_a_Template)
- [Dimensões e dois quadros de semente — documentação Json Assets](https://github.com/spacechase0/StardewValleyMods/blob/develop/framework/JsonAssets/docs/author-guide.md#crops)
- [Carregamento Load — documentação Content Patcher](https://github.com/Pathoschild/StardewMods/blob/develop/ContentPatcher/docs/author-guide/action-load.md)

A documentação Json Assets foi usada somente como referência da grade;
esse framework não foi adicionado como dependência.

## Validação e limites

Conferidos: arquivos JSON, referências de Include e Load, tamanhos,
quadros realmente acessados, ícones não vazios, transparência binária,
IDs/itens de colheita e preservação de todos os valores não visuais.
A prévia mostra os PNGs finais ampliados com vizinho mais próximo.

O Stardew Valley e o SMAPI não foram executados neste ambiente.
Colheita, rebrota, integração com solo/água e convivência com outros mods
precisam de teste no jogo. Não se afirma funcionamento 100% validado.
Use `ROTEIRO_TESTE_LAVOURAS.txt` e guarde o log se algo falhar.
