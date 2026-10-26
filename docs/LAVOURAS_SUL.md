# Lavouras do Sul — versão 1.8.1

Dados, integração e funcionamento. A versão 1.8.1 inclui sprites próprios para as 12 lavouras e os 28 itens. O histórico da arte provisória está em `originais/LAVOURAS_SUL_1_8_0.md`.
Testado no jogo: **não** (Stardew Valley e SMAPI não rodam neste ambiente). Verificado nos arquivos: **sim** (ver VERIFICACAO.txt).

## Tabela das lavouras

| Cultura | Semente | Estações | Fases (dias) | Total | Rebrota | Rendimento | Compra / venda | Loja | Processamento |
|---|---|---|---|---|---|---|---|---|---|
| Feijão-preto | Sementes de feijão-preto | Primavera + Verão | 1-2-2-2-2 | 9 d | não | 2 | 40g / 50g | Pierre | Barril/Conserva: regras nativas de vegetal |
| Mandioca | Manivas de mandioca | Primavera + Verão + Outono | 2-3-4-5 | 14 d | não | 2 | 60g / 100g | Pierre | Barril/Conserva: regras nativas de vegetal |
| Batata-doce | Ramas de batata-doce | Primavera + Verão | 1-2-3-3 | 9 d | não | 1 +20% extra | 50g / 110g | Pierre | Barril/Conserva: regras nativas de vegetal |
| Cebola | Sementes de cebola | Inverno + Primavera | 2-2-3-3 | 10 d | não | 1 | 30g / 75g | Pierre | Barril/Conserva: regras nativas de vegetal |
| Maracujá | Sementes de maracujá | Verão + Outono | 1-2-2-3-3 | 11 d | a cada 4 d (treliça) | 1 | 70g / 60g | Pierre | Barril (vinho) e Conserva (geleia): regras nativas de fruta |
| Pimentão | Sementes de pimentão | Verão + Outono | 1-2-2-2-2 | 9 d | a cada 4 d | 1 +3% extra | 50g / 55g | Pierre | Barril/Conserva: regras nativas de vegetal |
| Aveia-branca | Sementes de aveia-branca | Outono + Inverno | 1-2-2-2 | 7 d | não | 1 (foice) | 10g / 30g | Pierre | Moinho: 1 aveia -> 1 Aveia em flocos |
| Cevada | Sementes de cevada | Outono + Inverno | 1-2-2-2 | 7 d | não | 1 (foice) | 10g / 30g | Pierre | Barril: 1 cevada -> Cerveja (1750 min, igual ao trigo) |
| Centeio | Sementes de centeio | Outono + Inverno | 1-2-2-3 | 8 d | não | 1 (foice) | 10g / 30g | Pierre | Barril: 1 centeio -> Cerveja (1750 min, igual ao trigo) |
| Soja | Sementes de soja | Verão + Outono | 1-2-2-2-3 | 10 d | não | 1-2 | 30g / 35g | Pierre | Extrator de óleo: 1 soja -> Óleo (1000 min, igual ao milho) |
| Azevém | Sementes de azevém | Outono + Inverno | 1-2-2-2 | 7 d | não | 1 (foice) | 20g / 10g | Marnie | Moinho: 1 azevém -> 2 Feno |
| Arroz irrigado em casca | Sementes de arroz irrigado | Primavera + Verão | 1-2-3-3 | 9 d | não | 1-2 (+1 no nível 10) +10% extra (foice) | 40g / 30g | Pierre | Moinho: 1 arroz em casca -> 1 Arroz (o arroz original do jogo) |

Arquivos: `data/lavouras/itens.json` (sementes, colheitas, fubá, flocos, pratos), `crops.json` (plantações), `lojas.json`, `processamento.json` (moinho, barril, extrator de óleo), `receitas.json`; textos em `i18n/default.json` (chaves `semente.*`, `lavoura.*`, `proc.*`, `prato.*`).

## Calendário (estação de 28 dias)

Plantando no dia X, a lavoura fica pronta na manhã do dia X + total. Lavouras de várias estações continuam crescendo na estação seguinte permitida; na primeira manhã de uma estação não permitida, morrem (regra nativa). Valores sem Speed-Gro, Agricultor ou irrigação.

| Cultura | 1ª colheita (plantando no dia 1) | Colheitas no ciclo | Último plantio por estação |
|---|---|---|---|
| Feijão-preto | Primavera 10 | 1 | Primavera 28, Verão 19 |
| Mandioca | Primavera 15 | 1 | Primavera 28, Verão 28, Outono 14 |
| Batata-doce | Primavera 10 | 1 | Primavera 28, Verão 19 |
| Cebola | Inverno 11 | 1 | Inverno 28, Primavera 18 |
| Maracujá | Verão 12 | 12 | Verão 28, Outono 17 |
| Pimentão | Verão 10 | 12 | Verão 28, Outono 19 |
| Aveia-branca | Outono 8 | 1 | Outono 28, Inverno 21 |
| Cevada | Outono 8 | 1 | Outono 28, Inverno 21 |
| Centeio | Outono 9 | 1 | Outono 28, Inverno 20 |
| Soja | Verão 11 | 1 | Verão 28, Outono 18 |
| Azevém | Outono 8 | 1 | Outono 28, Inverno 21 |
| Arroz irrigado em casca | Primavera 10 | 1 | Primavera 28, Verão 19 |

Arroz irrigado perto da água: o motor aplica +25% de velocidade (como no arroz original, 8 → 6 dias); a estimativa é 9 → 6 ou 7 dias, a confirmar no jogo.

## Por que esses valores

Cada lavoura copia a lógica de uma cultura parecida do jogo e foi ajustada para ficar na mesma faixa de lucro dela. Lucro aproximado por dia de canteiro, sem qualidade nem profissões:

| Cultura | Análogo do jogo | Lucro/dia (venda direta) | Destino processado |
|---|---|---|---|
| Feijão-preto | Batata (6 d) e Couve-flor (12 d), colheita única | 6,7g | Barril/Conserva: regras nativas de vegetal |
| Mandioca | Inhame (10 d) e Abóbora (13 d), colheita única | 10,0g | Barril/Conserva: regras nativas de vegetal |
| Batata-doce | Batata (6 d, 20% extra) e Inhame (10 d) | 9,7g | Barril/Conserva: regras nativas de vegetal |
| Cebola | Alho (4 d), com ciclo mais longo | 4,5g | Barril/Conserva: regras nativas de vegetal |
| Maracujá | Uva (10 d, rebrota 3, treliça) | 11,6g | Barril (vinho) e Conserva (geleia): regras nativas de fruta |
| Pimentão | Pimenta (5 d, rebrota 3) e Tomate (11 d, rebrota 4) | 11,3g | Barril/Conserva: regras nativas de vegetal |
| Aveia-branca | Trigo (4 d, foice) | 2,9g | Moinho: 1 aveia -> 1 Aveia em flocos |
| Cevada | Trigo (4 d, foice) | 2,9g | Barril: 1 cevada -> Cerveja (1750 min, igual ao trigo) |
| Centeio | Trigo (4 d, foice) | 2,5g | Barril: 1 centeio -> Cerveja (1750 min, igual ao trigo) |
| Soja | Batata (6 d) e Milho (óleo) | 2,2g | Extrator de óleo: 1 soja -> Óleo (1000 min, igual ao milho) |
| Azevém | Couve (6 d, foice); feno da Marnie custa 50g | -1,4g | Moinho: 1 azevém -> 2 Feno |
| Arroz irrigado em casca | Arroz do jogo (8 d, perto da água) | 0,9g | Moinho: 1 arroz em casca -> 1 Arroz (o arroz original do jogo) |

Referências do jogo usadas na comparação: Pastinaca 3,8g/d, Batata 8,3g/d, Couve 6,7g/d, Inhame 10g/d, Abóbora 16,9g/d, Trigo 3,8g/d; Pimenta, Tomate e Uva para rebrota; Arroz 1,6 unidade por colheita (a mesma média usada aqui). Feno não tem preço de venda (0g), então o azevém não cria lucro infinito.

Escolhas de estação (clima real → estação do jogo):
- **Verão/primavera (lavouras de calor):** feijão-preto (duas safras: das águas e da seca), batata-doce, arroz irrigado (semeadura de setembro a dezembro no RS), soja (semeadura de meados de outubro ao começo de dezembro), pimentão e maracujá (oferta catarinense de janeiro a maio). Mandioca vai da primavera ao outono, com ciclo longo.
- **Inverno (escolha explícita, só para espécies adequadas):** aveia-branca, cevada, centeio e azevém (cereais e pastagens de inverno do Sul) e cebola (mudas transplantadas em junho e julho). Nenhuma regra de outra planta foi alterada.
- Os ciclos reais (meses) foram comprimidos para dias do jogo pela comparação com as culturas originais, não convertidos mês a mês.

## Processamento

- **Moinho** (`Data/Buildings` → `Mill` → `ItemConversions`, não `Data/Machines`): Milho → Farinha de milho (fubá) 1:1; Arroz irrigado em casca → Arroz original 1:1; Aveia-branca → Aveia em flocos 1:1; Azevém → 2 Feno. As conversões originais (trigo, beterraba, arroz) não foram tocadas; sem limite diário, como as originais; pronto na manhã seguinte.
- **Barril** (`(BC)12`): Cevada e Centeio → Cerveja, 1750 min (igual ao trigo). As regras foram colocadas no topo para não virar suco.
- **Extrator de óleo** (`(BC)19`): Soja → Óleo, 1000 min (igual ao milho).
- **Regras nativas por categoria:** vegetais viram suco no barril e picles na conserva; o maracujá (fruta) vira vinho e geleia. Isso já vale para qualquer vegetal do jogo e não foi forçado nem bloqueado. O azevém usa a categoria de recurso (-16) para não virar suco nem picles.
- **Feno:** sai do moinho como item. Para guardar no silo, segure o feno e clique no comedouro (regra nativa). Não há alimentação automática, pastejo nem efeito no leite.
- **Culinária:** Broa de milho (fubá + qualquer leite) e Bolo de fubá (fubá + açúcar + qualquer ovo), receitas vendidas pelo Gus (150g e 250g). Nenhuma receita antiga foi alterada; o fubá não é obrigatório em nada que já existia.
- **Gerador de Sementes:** o jogo descobre a semente pela colheita em `Data/Crops`; cada colheita nova pertence a uma única lavoura. Aceitação depende da regra nativa da máquina (testar, principalmente o azevém).

## Sprites próprios (1.8.1)

Todas as 12 lavouras agora usam folhas próprias de 128×32, com oito células de 16×32.
Sementes, colheitas, fubá, flocos, broa e bolo usam 28 ícones próprios de 16×16.
Os PNGs são RGBA, com alpha 0/255. O carregamento fica em `data/lavouras/sprites.json`.
Cada textura é isolada em `Mods/{{ModId}}/lavouras/...`, com `SpriteIndex: 0`.

Os dois primeiros quadros são as variações de plantio. Depois vêm os estágios,
a planta madura e, em maracujá e pimentão, a rebrota no oitavo quadro.
Nos cultivos de quatro fases, a planta madura fica no sexto quadro; nos de
cinco fases, no sétimo. Quadros não usados repetem a arte madura.

Veja `SPRITES_LAVOURAS_1_8_1.md`, `MAPA_SPRITES_LAVOURAS.json` e
`../PREVIA_LAVOURAS_E_FUBA.png`. As durações e as demais regras são as recebidas
na versão 1.8.0; esta atualização alterou somente as referências visuais.

## Matriz das mecânicas

| Mecânica | Comportamento esperado | Configuração / arquivo | Verificado nos arquivos | Testado no jogo |
|---|---|---|---|---|
| Arar e plantar | Semente planta só na terra arada e nas estações listadas | itens.json (Seeds, -74) + crops.json (chave = semente) | sim | pendente |
| Rega e chuva | Sem rega não cresce; chuva rega | crops.json NeedsWatering=true (nativo) | sim | pendente |
| Aspersores | Regam como qualquer lavoura | nativo, sem configuração | não se aplica | pendente |
| Arroz perto da água | Rega automática e crescimento mais rápido | crops.json IsPaddyCrop=true (só arroz irrigado) | sim | pendente |
| Fertilizantes, Speed-Gro, Agricultor | Motor nativo reduz dias e muda qualidade | DaysInPhase com fases ≥ 1 | sim | pendente |
| Qualidade e XP | Regras nativas pelo preço; colheita com foice segue a regra nativa de XP | Price em itens.json | sim | pendente |
| Treliça | Maracujá bloqueia passagem e aparece com treliça | IsRaised=true + sprite próprio com treliça | sim | pendente |
| Rebrota | Maracujá e pimentão rebrotam a cada 4 dias | RegrowDays=4 em linhas com quadro de rebrota | sim | pendente |
| Várias estações | Continuam crescendo na estação seguinte permitida | Seasons (calendário simulado) | sim | pendente |
| Cultivo no inverno | Só cebola, aveia, cevada, centeio e azevém | Seasons com Winter | sim | pendente |
| Foice e Junimos | Cereais, azevém e arroz só com foice; Junimos colhem tudo | HarvestMethod=Scythe | sim | pendente |
| Corvos e espantalhos | Regra nativa | nativo | não se aplica | pendente |
| Estufa, Ilha Gengibre, vasos | Regras nativas de cada lugar (estação ignorada onde o jogo ignora) | PlantableLocationRules não definido (padrão) | sim | pendente |
| Lavouras gigantes | Nenhuma adicionada | Data/GiantCrops intocado | sim | não se aplica |
| Lojas | 11 sementes no Pierre por estação; azevém na Marnie; 2 receitas no Gus | lojas.json | sim | pendente |
| Gerador de Sementes | Semente descoberta pela colheita | crops.json HarvestItemId único | sim | pendente |
| Moinho | Fubá, arroz, flocos e feno na manhã seguinte | processamento.json (Mill, baús Input/Output) | sim | pendente |
| Barril e extrator de óleo | Cevada/centeio → cerveja; soja → óleo | processamento.json + MoveEntries no topo | sim | pendente |
| Culinária | Broa e bolo; receitas antigas intactas | receitas.json + lojas.json | sim | pendente |
| Venda e armazenamento | Preços fixos; itens fora da coleção de envios e de vendas aleatórias | itens.json | sim | pendente |
| Saves antigos | IDs da 1.5.0 reaproveitados para os 6 cultivos antigos | itens.json / crops.json | sim | pendente |

## Adições e correções

- Adicionado: 12 lavouras (24 itens), Farinha de milho (fubá), Aveia em flocos, Broa de milho, Bolo de fubá, 4 conversões no moinho, 3 regras de máquina, 12 vendas e 2 receitas.
- Reaproveitado: os IDs antigos de feijão-preto, mandioca, batata-doce, cebola, maracujá e pimentão (sementes e colheitas), que tinham sido retirados na 1.6.0.
- Não foi preciso corrigir nada nos peixes, nas árvores ou nos pratos: arquivos idênticos à 1.7.0 (conferido byte a byte).
- Arroz, milho e trigo originais não foram duplicados nem alterados; o milho original é a matéria-prima do fubá.

## Limites conhecidos

- Os nomes dos baús do moinho (`Input` e `Output`) seguem o padrão usado pelo jogo e por mods de construção; se o moinho não aceitar milho, aveia, azevém ou o arroz irrigado, é esse o ponto a conferir com `patch export Data/Buildings`.
- As páginas da wiki em português "Lavouras" e "Calendários de Crescimento das Lavouras" não abriram pela ferramenta (erro do servidor). Os dados das culturas originais foram conferidos nas páginas em inglês e na documentação técnica.
- Sem fonte regional específica para o calendário do pimentão: a escolha seguiu a cultura análoga do jogo (pimenta) e o caráter de clima quente da espécie.

## Fontes

Jogo e técnica:
- https://pt.stardewvalleywiki.com/Cultivo
- https://wiki.stardewvalley.net/Crops
- https://stardewvalleywiki.com/Unmilled_Rice
- https://stardewvalleywiki.com/Mill
- https://stardewvalleywiki.com/Hay
- https://wiki.stardewvalley.net/Keg
- https://wiki.stardewvalley.net/Oil_Maker
- https://stardewvalleywiki.com/Modding:Crop_data
- https://stardewvalleywiki.com/Modding:Buildings
- https://stardewvalleywiki.com/Modding:Machines
- https://stardewvalleywiki.com/Modding:Shops
- https://stardewvalleywiki.com/Modding:Context_tags
- https://www.nexusmods.com/stardewvalley/articles/2958

Regionais:
- Feijão (PR maior produtor; safra das águas): https://www.parana.pr.gov.br/Audio/Maior-produtor-do-Brasil-Parana-ja-colheu-72-da-safra-das-aguas-do-feijao
- Mandioca (IDR-Paraná, época de plantio): https://www.idrparana.pr.gov.br/system/files/publico/Publica%C3%A7%C3%B5es/Notas%20T%C3%A9cnicas/NotaTecnica13_2025_EpocaPlantioMandiocanoPR.pdf
- Batata-doce (Embrapa Clima Temperado; RS maior produtor): https://www.infoteca.cnptia.embrapa.br/infoteca/bitstream/doc/952923/1/documento330.pdf
- Cebola (Epagri; transplante em junho e julho): https://ciram.epagri.sc.gov.br/ciram_arquivos/cebola/acervo/Cebola_sistema_organico.pdf
- Maracujá (Epagri/Cepa; Sul Catarinense, oferta jan-mai): https://docweb.epagri.sc.gov.br/website_cepa/Fruticultura/Maracuja/Situacao_perspectivas_maracuja.pdf
- Pimentão (Embrapa Hortaliças, cultivo protegido): https://www.infoteca.cnptia.embrapa.br/infoteca/bitstream/doc/779835/1/cot35.pdf
- Aveia-branca, cevada e centeio (Embrapa, 2023): https://www.infoteca.cnptia.embrapa.br/handle/doc/1153849
- Azevém, aveia e centeio como forrageiras de inverno (Embrapa): https://www.infoteca.cnptia.embrapa.br/infoteca/bitstream/doc/1019788/1/ID42934FL8527forrageirasparaintegracaolavourapecuarianaregiaosulbrasileira.pdf
- Soja (Embrapa, semeadura no Sul): https://www.alice.cnptia.embrapa.br/alice/bitstream/doc/1018515/1/R.164MACRORREGIAOSOJICOLAPOCADESEMEADURAEPOPULACAODE.PDF
- Arroz irrigado (zoneamento MAPA/RS): https://www.gov.br/agricultura/pt-br/assuntos/riscos-seguro/programa-nacional-de-zoneamento-agricola-de-risco-climatico/portarias/safra-2019-2020/rio-grande-do-sul-rs/port-no-41-arroz-irrigado-rs.pdf
- Arroz no RS e IRGA (Governo do RS): https://www.estado.rs.gov.br/colheita-do-arroz-e-oficialmente-aberta-em-capa-o-do-lea-o
