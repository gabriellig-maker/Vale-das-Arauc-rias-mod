VALE DAS ARAUCÁRIAS
Versão 1.9.3 • Autor do mod: belfortkafag
Stardew Valley 1.6+ • SMAPI 4+ • Content Patcher 2+

O QUE TEM NO MOD
71 itens de pesca (peixes, covo, Mercado Noturno e a cambeva) com nomes, descrições e
sprites do Sul; 3 geleias e 11 pratos de peixe do jogo com nomes regionais; 6 árvores regionais (araucária, erva-mate, bracatinga,
jabuticabeira, canela-preta e butiazeiro); 12 lavouras do Sul com moinho, barril e
extratora de óleo; broa de milho, bolo de fubá e as 27 receitas da culinária regional.

NOVIDADES DA 1.9.0
A Culinária Regional agora vem dentro deste mod (uma pasta só). Veja o fim deste arquivo
e docs/culinaria/LEIA-ME_CULINARIA.txt.

SPRITES DAS LAVOURAS (1.8.1)
12 folhas de plantação de 128×32 (quadros de 16×32) e 28 ícones de 16×16.
Feijão-preto, mandioca, batata-doce, cebola, maracujá, pimentão,
aveia-branca, cevada, centeio, soja, azevém e arroz irrigado.
Ícones próprios para cada semente e colheita, mais farinha de milho (fubá),
aveia em flocos, broa de milho e bolo de fubá. Total: 40 PNGs novos.
Transparência binária, quadros de plantio, crescimento e colheita;
maracujá com treliça e quadro de rebrota para maracujá e pimentão.

INSTALAÇÃO
Leia INSTALAR_LEIA_PRIMEIRO.txt. Extraia a pasta
varas_lend1_lend2_covos_mercado para Mods, substituindo a pasta desta
mesma versão do mod. Mantenha apenas uma cópia desse pack em Mods.
Se você instalou a pasta separada "[CP] Vale das Araucárias - Culinária Regional", apague-a:
ela já está dentro deste mod.
SMAPI e Content Patcher continuam sendo dependências externas.

PRESERVADO
IDs e traduções; dias, estações, rendimentos, preços, lojas, receitas,
regras de moinho e máquinas; peixes, geleias, pratos adaptados e árvores.
As seis árvores regionais recebidas são adicionais, conforme a versão base.
Nos dados das lavouras e dos 28 itens, só Texture e SpriteIndex mudaram.

ONDE ENCONTRAR
PREVIA_LAVOURAS_E_FUBA.png — prévia ampliada dos PNGs finais.
assets/lavouras/ — 40 PNGs realmente utilizados pelo mod.
data/lavouras/sprites.json — carregamento das texturas.
docs/SPRITES_LAVOURAS_1_8_1.md — tabela, grade e referências.
docs/MAPA_SPRITES_LAVOURAS.json — mapa técnico de quadros.
docs/PROMPTS_ARTE_LAVOURAS.json — prompts usados na geração integrada.
sprites_criados_organizados/fontes_arte_lavouras/ — imagens-fonte maiores.
VALIDACAO_SPRITES.json — checagem estática desta entrega.
ROTEIRO_TESTE_LAVOURAS.txt — conferência no jogo ainda pendente.
PREVIA_ARVORES_REGIONAIS.png — prévia das árvores já recebidas.
docs/culinaria/ — receitas, sprites pendentes, compatibilidade e testes da culinária.

VALIDAÇÃO
Foram conferidos JSON, arquivos referenciados, tamanhos, transparência,
quadros acessados, carregamento das texturas e preservação dos dados.
Não foi executado o Stardew Valley nem o SMAPI neste ambiente.
Não há confirmação de funcionamento em runtime; use o roteiro incluído.

HISTÓRICO
Documentos antigos podem descrever versões sem lavouras ou com arte
provisória. A documentação atual é esta e docs/SPRITES_LAVOURAS_1_8_1.md.
As versões anteriores foram preservadas em docs/originais/.

VERSÃO 1.8.2 — CORREÇÃO DAS ÁRVORES REGIONAIS
- Folhas soltas: ao sacudir ou cortar, só caem folhas da estação atual. Antes,
  cada folha sazonal tinha as folhas das quatro estações misturadas.
- Queda da árvore: a copa que cai não leva mais o toco e as raízes. O toco fica
  parado no chão e só o tronco e a copa caem, como nas árvores do jogo.
- Só as 24 folhas de sprite das árvores mudaram (e as cópias organizadas).
  Dados, IDs, peixes, lavouras e o resto do mod continuam iguais.
- Antes e depois: docs/PREVIA_CORRECAO_ARVORES_1_8_2.png.

VERSÃO 1.8.3 — JABUTICABEIRA
- A árvore de madeira de lei de casca escura passou a ser a jabuticabeira: Semente de
  Jabuticaba e novas descrições da semente e da Seiva Aromática (produto da torneira).
- Sprites, crescimento, madeira de lei ao cortar, Seiva Aromática, preços, lojas (Robin e
  Carrinho de Viagem) e coleta no Bosque Secreto continuaram iguais.
- Prévia com o nome novo: PREVIA_ARVORES_REGIONAIS.png.

VERSÃO 1.9.0 — CULINÁRIA REGIONAL INCLUÍDA
- O mod "[CP] Vale das Araucárias - Culinária Regional" foi juntado a este: 27 receitas do Sul
  (aprendidas por cartas dos moradores ou compradas no Pierre, no Gus e na Marnie) e 3 receitas
  de jabuticaba, prontas, ligadas pela opção FrutosDaJabuticabeira (vem desligada).
- Os IDs da culinária são os mesmos da versão separada: receitas aprendidas e pratos
  guardados continuam valendo. Apague a pasta separada se ela estiver em Mods.
- Nenhum sprite novo nesta versão: os pratos usavam ícones provisórios do jogo (resolvido na
  1.9.2, veja abaixo).
- Correção para saves antigos: a receita do caroço de butiá (Coleta nível 1) agora também
  é ensinada no começo do dia a quem já tem Coleta 1 ou mais e ainda não a conhece.
- Revisão das mecânicas (estática): peixes, árvores, lavouras, lojas, coleta, moinho, barril,
  extratora, receitas e textos conferidos, com a opção da jabuticaba desligada e ligada.

VERSÃO 1.9.1 — JABUTICABEIRA EM TUDO
- Nomes internos, pastas, arquivos, textos e documentos agora usam jabuticaba/jabuticabeira:
  semente ValeAraucarias_JabuticabaSeed, árvore ValeAraucarias_JabuticabeiraTree e sprites em
  assets/arvores/jabuticabeira.
- Saves antigos: as sementes guardadas são convertidas sozinhas para o ID novo no primeiro dia
  (ação MigrateIds do Content Patcher 2.1 ou mais novo). As jabuticabeiras já plantadas continuam
  crescendo e produzindo normalmente por uma entrada de compatibilidade invisível no jogo.
- Requer Content Patcher 2.1 ou mais novo.

VERSÃO 1.9.2 — SPRITES DAS COMIDAS
- Os 30 pratos da culinária regional ganharam sprites próprios (assets/comidas). Eles entram
  sozinhos no lugar dos ícones provisórios, sem mudar nenhum dado.
- Broa de milho e bolo de fubá com sprites novos (assets/lavouras/processados).
- Só a fruta jabuticaba (opção desligada por padrão) continua com ícone provisório; para
  trocar, coloque assets/comidas/jabuticaba.png (16x16, fundo transparente).
- Mecânicas revisadas de novo, com a opção da jabuticaba desligada e ligada: nenhum erro.

VERSÃO 1.9.3 — TRAJE GAÚCHO
- O mod "[CP] Vale das Araucarias - Traje Gaucho" 1.0.0 foi juntado a este: Chapéu Campeiro,
  Camisa Gaúcha com Lenço Vermelho, Bombacha Tradicional e Botas Campeiras (+1 defesa e
  +1 imunidade), à venda no Armazém do Pierre (opção TrajeGauchoNoPierre, vem ligada).
- Os IDs das peças são os mesmos do mod separado: peças já compradas continuam valendo.
  Apague a pasta separada se ela estiver em Mods.
- Correção: o mod separado procurava assets/Chapeu.png, Camisa.png e Botas.png, arquivos que
  não existiam, e chapéu, camisa e botas ficariam sem imagem. Agora cada textura aponta para o
  arquivo certo em assets/traje (sprites do traje sem nenhuma alteração).
- Bombacha: sem assets/traje/Bombacha_Cinto.png, usa uma calça bufante do próprio jogo
  tingida de cinza-azulado. Para a versão com cinto, veja docs/traje/LEIAME_TRAJE.txt.
