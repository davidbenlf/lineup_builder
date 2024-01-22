# LINE UP Builder
Esse é um simulador de montar escalas de time de futebol ⚽. Feito com o objetivo de melhorar minhas habilidades no desenvolvimento backend com Python e Django; e treinar modelagem de banco de dados relacionais, visto que só tinha experiência com não-relacionais (MongoDB).
<br><br>
Techs usadas:
- Django;
- Python;
- PostgreSQL;
- HTML;
- CSS;
- JavaScript
<br><br>
Você pode:
- adicionar/editar/excluir jogadores;
- adicionar/editar/excluir times;
- adicionar/editar/excluir nacionalidades;
- criar templates de formações (ex.: 4-4-2, 4-5-1, 4-4-1-1 etc.); (para finalizar)
- montar uma escalação usando os jogadores adicionados no Banco de Dados; (para finalizar)
- visualizar as escalações criadas. (para finalizar)

Criar times e nacionalidades serve para que, na hora que for criar um jogador, ambos poderem ser atribuidos a ele (tenho o plano de mostrar o time e a nacionalidade no icone do jogador)
<p>
O projeto foi criado usando o framework web <b>Django</b> para montar tanto o backend, quanto o front com o uso dos templates.
<p>
Para guardar todas as informações/registros fora utilizado o <b>PostgreSQL</b>. A seguir as tabelas e suas seguintes relações:

# TABELAS

## Jogadores
| ID       | nome              | time    | nacionalidade | foto
|:-------: | :---------------- | :-----: | :---:         | :--:   |
|    1     | Ibrahimovic       |   FK(times_id)    | FK(nacionalidade_id)            | public/media/image.webp   |

## Formações
| ID  | numero_jogadores  | nome     | p1x | p1y | p2x | p2y | ...  | p11x | p11y
| :-: | :---------------- | :------  | :-: | :-: | :-: | :-: | :--: | :--: | :--:
| 10  | 11                | 4-4-3    | 300 | 200 | 500 | 400 | ...  | 800  | 700

## Nacionalidades
| ID  | nome     | foto
| :-: | :------- | :--: |
| 14  | Suécia   | public/media/image.webp   |

## Times
| ID  | nome                     | foto
| :-: | :----------------        | :--: |
| 16  | Seleção Sueca de Futebol | public/media/image.webp   |

## Escalações
| ID  | UUID          | titulo                  | imagem                  |
| :-: | :---:         | :----------------       | :----------------       |
| 34  | 35DJ...39483  | PSG - Época de ouro     | public/media/image.webp |
