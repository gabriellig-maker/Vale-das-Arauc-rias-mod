VALE DAS ARAUCÁRIAS — COMPLETO COM ÁRVORES REGIONAIS
Versão 1.8.0 • Autor: belfortkafag
Stardew Valley 1.6+, SMAPI 4+ e Content Patcher 2+.

ENTREGA EM UM ÚNICO MOD
Este pacote reúne o pack anterior de peixes com o arquivo de Árvores
Regionais, com a arte final das seis árvores. Na versão 1.6.0 os cultivos
novos e a culinária nova foram retirados (veja VERSÃO 1.6.0 no fim).

Comece por INSTALAR_LEIA_PRIMEIRO.txt.
Extraia a pasta varas_lend1_lend2_covos_mercado para Mods.
Não instale o ZIP fechado nem mantenha as cópias antigas dos dois packs em Mods.
O Content Patcher e o SMAPI continuam sendo requisitos externos.

SPRITES NOVOS DE ÁRVORES
- Araucária, erva-mate, bracatinga, jabuticabeira, canela-preta e butiazeiro.
- 24 folhas sazonais de 144×160, prontas nas grades do mod.
- 13 ícones de 16×16: sementes, produtos, pinhão e folhas de erva-mate.
- Inclui crescimento, tocos, musgo, folhas soltas, rachaduras e cachos.
- Todos os arquivos novos são PNG RGBA com alpha binário.
- A arte dos peixes do pack anterior foi preservada.

As seis árvores do arquivo recebido são ADICIONAIS: não substituem os tipos
originais de Data/WildTrees nem mexem em mapas/hitboxes. Na versão 1.7.0, os itens
das árvores originais do jogo voltaram aos nomes e ícones originais.

ARQUIVOS PRINCIPAIS
PREVIA_ARVORES_REGIONAIS.png — contato visual das quatro estações e itens.
assets/arvores/ — todos os PNG novos efetivamente usados pelo jogo.
sprites_criados_organizados/arvores_novas/ — cópia organizada dos PNG finais.
sprites_criados_organizados/fontes_arte/ — fontes maiores da arte gerada.
docs/SPRITES_ARVORES_REGIONAIS.md — tabela, grade, referências e escopo.
docs/PROMPTS_ARTE_ARVORES.json — prompts usados na geração integrada de imagens.
VALIDACAO_SPRITES.json — resultados da checagem estática.
TESTE_NO_JOGO.txt — roteiro de conferência no jogo.

O QUE FOI PRESERVADO
Os seis arquivos de dados do complemento foram incorporados sem mudar seus
valores: IDs, estações, crescimento, sementes, preços, drops, produção, lojas
e receita. Do pack anterior, saíram na 1.6.0 os arquivos de cultivos e de culinária
e as vendas ligadas a eles; o resto ficou idêntico.
Apenas carregamento, traduções e manifesto foram unificados para uma só pasta.
Manteve-se o UniqueID do pack principal e todos os IDs de conteúdo.
As árvores frutíferas foram retiradas na versão 1.7.0.

VALIDAÇÃO E LIMITES
1.893 verificações estáticas passaram: JSON, caminhos, referências customizadas,
grade de sprites, transparência, quadros preenchidos e integridade dos dados.
Não houve teste executando o jogo, o SMAPI, crescimento ou receitas.
Isso não é uma certificação de compatibilidade com todos os mods/saves.
Faça backup e teste primeiro em uma cópia do save.

Os demais relatórios de versões anteriores foram mantidos como histórico.
O README anterior está em docs/originais/README_pack_1_4_historico.txt.
A documentação desta versão listada acima é a referência da entrega atual.

VERSÃO 1.6.0 — SEM CULTIVOS E SEM CULINÁRIA NOVA
Retirado:
- 6 cultivos novos (sementes, plantações e colheitas): mandioca, batata-doce,
  feijão-preto, cebola, maracujá e pimentão.
- 15 receitas novas: polenta, polenta com queijo, churrasco gaúcho, arroz
  carreteiro, barreado, pierogi, entrevero de pinhão, chimarrão, pinhão
  cozido, cuca de maçã, feijão tropeiro, doce de batata-doce, quirera com
  carne suína, pirão de peixe e aipim frito.
- 4 ingredientes: carne bovina, carne suína, charque e farinha de mandioca.
- A venda desses itens no Pierre e no JojaMart e as receitas vendidas pelo Gus.
Mantido: os 70 peixes, a Cambeva e as geleias, os 11 pratos do jogo com nomes
regionais, as árvores frutíferas (bergamoteira e pitangueira), as seis
árvores regionais e os 9 itens do jogo regionalizados.

SAVES
Se o save já tem algum desses cultivos plantados, ou sementes, colheitas,
ingredientes ou pratos novos guardados, venda, use ou tire esses itens antes
de atualizar. Sem as definições, eles aparecem como "Error Item" e as
plantações desses cultivos deixam de funcionar.

VERSÃO 1.7.0 — SÓ AS SEIS ÁRVORES REGIONAIS
Retirado:
- As árvores frutíferas: bergamoteira e pitangueira (mudas e frutos) e as
  antigas araucária e erva-mate frutíferas, que já não eram vendidas.
- Os 9 itens das árvores originais do jogo que tinham nome e ícone regional
  (sementes, madeiras, seiva e resinas): eles voltam ao nome e ao ícone
  originais. As árvores originais do jogo continuam iguais.
- As pastas assets/arvores_regionais e assets/cultivos_culinaria.
Mantido: os 70 peixes, a Cambeva e as geleias, os 11 pratos do jogo com nomes
regionais e as seis árvores regionais, com Pinhão e Folhas de erva-mate.
SAVES: mudas, bergamotas, pitangas e frutíferas plantadas que já estejam no
save viram "Error Item" ou deixam de funcionar. Venda ou tire antes de
atualizar.

VERSÃO 1.8.0 — LAVOURAS DO SUL
12 lavouras com sementes, colheitas, lojas e processamento, sem arte nova:
feijão-preto, mandioca, batata-doce, cebola, maracujá, pimentão, aveia-branca,
cevada, centeio, soja, azevém e arroz irrigado. Moinho: milho vira Farinha de
milho (fubá); arroz irrigado vira o arroz original; aveia vira Aveia em flocos;
azevém vira feno. Barril: cevada e centeio viram cerveja. Extrator de óleo: soja
vira óleo. Receitas novas no Gus: Broa de milho e Bolo de fubá.
Os 6 cultivos antigos voltaram com os mesmos IDs da versão 1.5.0.
Detalhes, tabelas, fontes e matriz: docs/LAVOURAS_SUL.md.
Roteiro de teste no jogo: ROTEIRO_TESTE_LAVOURAS.txt (ainda não executado).
