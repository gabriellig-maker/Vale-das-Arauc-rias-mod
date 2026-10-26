VALE DAS ARAUCÁRIAS - CULTIVOS E CULINÁRIA
ValeDasAraucarias_CultivosCulinaria - versão 1.0.1
Content pack para Content Patcher

O QUE ESTE PACOTE ADICIONA
- 6 cultivos com sementes no Pierre e no JojaMart, na estação certa.
- 4 árvores com mudas no Pierre, o ano todo.
- 4 ingredientes vendidos no Pierre e no JojaMart, o ano todo.
- 15 receitas preparadas na cozinha original.
Nada do jogo é removido ou substituído. Todos os IDs novos começam com
"ValeDasAraucarias.". Itens que o jogo já tem (milho, arroz, queijo, batata, maçã,
farinha de trigo, açúcar, ovo, óleo) são usados como estão. A couve-manteiga
não foi criada porque a Couve original já representa a mesma planta.

CULTIVOS (semente -> produto | estações | crescimento | semente Pierre/Joja | venda)
  Manivas de mandioca -> Mandioca | primavera/verão | 12 dias, colheita única | 60g/75g | 130g
  Ramas de batata-doce -> Batata-doce | primavera/verão | 8 dias, colheita única | 40g/50g | 80g
  Sementes de feijão-preto -> Feijão-preto | primavera/verão | 10 dias, colheita única | 40g/50g | 40g
  Sementes de cebola -> Cebola | primavera/outono | 7 dias, colheita única | 30g/37g | 70g
  Sementes de maracujá -> Maracujá | verão/outono | 12 dias + a cada 4 (12 colheitas em 56 dias) | 80g/100g | 60g
  Sementes de pimentão -> Pimentão | verão | 7 dias + a cada 3 (8 colheitas em 28 dias) | 50g/62g | 45g

ÁRVORES (muda -> produto | estação | muda | venda)
  Muda de bergamoteira -> Bergamota | outono | 3600g | 90g
  Muda de pitangueira -> Pitanga | primavera | 3000g | 70g
  Muda de araucária -> Pinhão | inverno | 5000g | 80g
  Muda de erva-mate -> Folhas de erva-mate | verão | 2500g | 50g
  As mudas seguem as regras das árvores frutíferas originais: 28 dias para
  crescer e os 8 espaços ao redor livres.

INGREDIENTES (Pierre | JojaMart)
  Carne bovina | 150g | 187g
  Carne suína | 120g | 150g
  Charque | 200g | 250g
  Farinha de mandioca | 100g | 125g

RECEITAS (ingredientes | como aprender)
  Polenta: Milho x2 | aprendida automaticamente
  Polenta com queijo: Polenta x1, Queijo x1 | Saloon do Gus, 250g
  Churrasco gaúcho: Carne bovina x2 | Saloon do Gus, 500g
  Arroz carreteiro: Arroz x1, Charque x1, Cebola x1 | Saloon do Gus, 400g
  Barreado: Carne bovina x2, Farinha de mandioca x1, Cebola x1 | Saloon do Gus, 600g
  Pierogi: Batata x1, Farinha de trigo x1, Queijo x1 | carta de Evelyn (5 corações)
  Entrevero de pinhão: Pinhão x2, Carne bovina x1, Carne suína x1, Pimentão x1 | Saloon do Gus, 750g
  Chimarrão: Folhas de erva-mate x2 | carta de Lewis (5 corações)
  Pinhão cozido: Pinhão x3 | carta de Linus (4 corações)
  Cuca de maçã: Maçã x1, Farinha de trigo x1, Açúcar x1, Ovo x1 | carta de Jodi (5 corações)
  Feijão tropeiro: Feijão-preto x2, Farinha de mandioca x1, Ovo x1, Carne suína x1 | carta de Marnie (5 corações)
  Doce de batata-doce: Batata-doce x1, Açúcar x1 | carta de Caroline (5 corações)
  Quirera com carne suína: Milho x1, Carne suína x1 | Saloon do Gus, 300g
  Pirão de peixe: Tainha x1, Farinha de mandioca x1 | carta de Willy (4 corações)
  Aipim frito: Mandioca x1, Óleo x1 | Saloon do Gus, 150g
  Cartas de amizade: o próprio jogo envia a carta do morador no dia seguinte
  ao nível de amizade, como nas receitas originais. Em saves que já passaram
  desse nível, a carta deve chegar nos dias seguintes (confirmar no jogo).
  Polenta é aprendida no início do dia, inclusive em saves existentes.

SPRITES PROVISÓRIOS
Este pacote ainda não tem arte própria. Cada item, plantação e árvore usa
uma imagem do jogo original como substituta (ex.: a bergamoteira usa a
imagem da laranjeira). Para usar arte própria depois:
  - itens: troque Texture e SpriteIndex nas entradas de Data/Objects;
  - plantações: Texture e SpriteIndex nas entradas de Data/Crops;
  - árvores: Texture e TextureSpriteRow nas entradas de Data/FruitTrees;
  - carregue o PNG com uma ação Load (ex.: Mods/{{ModId}}/Itens).

EFEITOS NO PROGRESSO DO JOGO
- As 15 receitas novas entram na coleção de culinária e na contagem da
  Perfeição, como acontece com qualquer mod que adiciona receitas.
- Os itens novos ficam fora da coleção de envios, das conquistas de
  Policultura/Monocultura e do Carrinho de Viagem, para não mudar essas metas.
- Mandioca, feijão-preto, pinhão, folhas de erva-mate e carnes cruas não
  são comestíveis: precisam ser cozidos nas receitas.

COMPATIBILIDADE COM OS PEIXES DO VALE DAS ARAUCÁRIAS
- Pirão de peixe usa a Tainha pelo ID original (146). Nenhum dado de peixe
  é editado. Sem o pack de peixes, aparece o nome original (Salmonete).

SIMPLIFICAÇÕES DE GAMEPLAY
- Araucária, erva-mate, bergamoteira e pitangueira usam o sistema de árvores
  frutíferas: crescem em 28 dias e produzem em uma estação.
- A farinha de mandioca é comprada; o moinho não foi alterado.

REQUISITOS
Stardew Valley 1.6+, SMAPI 4.0+ e Content Patcher 2.0+.

INSTALAÇÃO
1. Extraia a pasta ValeDasAraucarias_CultivosCulinaria em Stardew Valley/Mods.
2. Inicie o jogo pelo SMAPI. Não precisa de save novo.
Em multijogador, todos os jogadores precisam ter este pacote instalado.

CONFERIR NO JOGO
No console do SMAPI: patch summary "belfortkafag.vale_das_araucarias_cultivos_culinaria"
Devem aparecer 1 Include e 9 EditData aplicados, sem erros.
COMANDOS_TESTE.txt traz os comandos para pegar cada item.

ARQUIVOS
  content.json ........ carrega os arquivos de data/
  data/cultivos.json .. sementes, produtos e Data/Crops
  data/arvores.json ... mudas, frutos e Data/FruitTrees
  data/receitas.json .. ingredientes, pratos e Data/CookingRecipes
  data/lojas.json ..... itens no Pierre, no JojaMart e receitas no Saloon
  i18n/default.json ... nomes e descrições (português)
  COMANDOS_TESTE.txt, VALIDACAO.txt, PROGRESSO.md

ROTEIRO DE TESTES NO JOGO (use uma cópia do save)
1. Abra pelo SMAPI. O console não deve mostrar erros deste pacote, e o
   patch summary deve listar 1 Include e 9 EditData aplicados.
2. Pierre: na primavera, manivas de mandioca, ramas de batata-doce, feijão-
   preto e cebola; no verão, mandioca, batata-doce, feijão-preto, maracujá
   e pimentão; no outono, cebola e maracujá. Mudas e ingredientes o ano todo.
   JojaMart: as mesmas sementes e os ingredientes, mais caros. Compre e
   confira o preço cobrado.
3. Plante cada semente (também em vaso e na estufa), regue, use adubo e
   aspersor. Confira as fases, a colheita do item certo e a qualidade.
4. Durma para salvar e confira se as plantações mantiveram a fase.
5. Plante uma muda com os 8 espaços ao redor livres; após 28 dias, ela
   produz na sua estação.
6. Polenta aparece no livro de receitas no dia seguinte. Compre uma receita
   no Saloon e confira na coleção de culinária. As demais podem ser
   ensinadas com os comandos de COMANDOS_TESTE.txt.
7. Cozinhe cada prato. Confira nome, descrição, energia e bônus; guarde em
   um baú, venda na caixa de envio e coma.
8. Com o pack de peixes, o Pirão de peixe pede Tainha. As receitas
   originais continuam no livro.
9. Nenhum item, plantação ou árvore deve aparecer com o ícone de erro.

LIMITES
O pacote foi conferido nos arquivos; o jogo e o SMAPI não foram executados
na montagem. Veja VALIDACAO.txt.
