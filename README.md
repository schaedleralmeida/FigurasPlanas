# FigurasPlanas


`figurasplanas` é um pacote Python para calcular as principais propriedades de área de figuras planas. O pacote permite posicionar, transladar e rotacionar figuras, além de combinar várias figuras como partes em uma figura composta.

## Funcionalidades

Calcula as seguintes grandezas:

| Símbolo | Grandeza |
| --- | --- |
| `A` | área |
| `xc`, `yc` | coordenadas do centroide |
| `Ix`, `Iy` | momentos de inércia em relação aos eixos x e y |
| `Ixy` | produto de inércia |
| `Io` | momento polar em relação à origem |
| `Sx`, `Sy` | momentos estáticos em relação aos eixos x e y |
| `rx`, `ry` | raios de giração em relação aos eixos x e y |
| `ro` | raio de giração polar |
| `I1`, `I2` | momentos principais de inércia, com `I1 >= I2` |
| `Ic` | momento de inércia polar em relação ao centroide |
| `r1`, `r2` | raios de giração principais |
| `theta_p` | ângulo do eixo principal 1, em radianos |

Obs.: *x-y* são eixos globais definidos pelo usuário e *1-2* são os eixos principais centrais da figura plana, sendo que o eixo *1* é o eixo segundo o qual . 

## Classes

### Figura Plana Genérica

A classe `FiguraPlana` representa uma figura genérica a partir de suas propriedades geométricas e serve como base para o cálculo e a manipulação das propriedades das demais figuras do pacote. As classes de figuras simples e compostas utilizam essa mesma estrutura de propriedades e operações.

```python
FiguraPlana(A, Ix, Iy, xc, yc, Ixy)
```

Além dos valores informados, calcula propriedades como `Io`, `Sx`, `Sy`, `rx`,
`ry`, `ro`, `I1`, `I2`, `Ic`, `r1`, `r2` e `theta_p`. 

Seus principais métodos são:

- `transladar(dx, dy)`: desloca a figura no plano.
- `rotacionar(ang)`: rotaciona a figura em torno da origem; `ang` deve estar em
	radianos.
- `ajustar_posição(xc, yc, theta_p)`: define a posição e a orientação dos
	eixos principais.

### Figuras Simples

As seguintes classes especializadas criam figuras a partir de suas dimensões:

- `Retangulo(b, h)`: retângulo de base `b` e altura `h`, centrado na origem.
- `Circulo(r)`: círculo de raio `r`, com centro na origem.
- `TrianguloRetangulo(b, h)`: triângulo retângulo de base `b` e altura `h`,
	com o vértice do ângulo reto na origem.
- `SemiCirculo(r)`: semicírculo de raio `r`.
- `QuartoCirculo(r)`: quarto de círculo de raio `r`.

### Figuras Compostas

#### `FiguraComposta`

Representa uma seção formada por várias figuras. 

Use `adiciona(figura, coef)` para incluir uma parte. O coeficiente padrão é `1.0`, mas valores negativos (-1) podem ser usados para representar furos ou vazios. 

Use `remove(i)` para retirar a parte no índice informado.

As operações `transladar(dx, dy)` e `rotacionar(ang)` são aplicadas a todas as partes da seção.

## Instalação

O projeto requer Python 3.11 ou superior. Para instalar diretamente do
repositório no GitHub usando `pip`:

```bash
python -m pip install git+https://github.com/schaedleralmeida/FigurasPlanas.git
```


Para contribuir com o projeto ou executar os testes localmente, clone o
repositório e instale as dependências de desenvolvimento com Poetry:

```bash
git clone https://github.com/schaedleralmeida/FigurasPlanas.git
cd FigurasPlanas
poetry install
```

## Uso

O módulo pode ser importado como `figurasplanas`. O exemplo abaixo cria um
retângulo, desloca-o e exibe suas propriedades calculadas:

```python
import figurasplanas as fp

retangulo = fp.Retangulo(b=6, h=10)
retangulo.transladar(dx=3, dy=5)

print(retangulo.A)       # área
print(retangulo.xc)      # coordenada x do centroide
print(retangulo.I1)      # maior momento principal de inércia
print(retangulo.theta_p) # orientação do eixo principal, em radianos
```

Uma seção composta pode ser montada combinando partes positivas e negativas:

```python
import figurasplanas as fp

secao = fp.FiguraComposta()

base = fp.Retangulo(b=6, h=10)
base.transladar(dx=3, dy=5)
secao.adiciona(base)

furo = fp.Circulo(r=2)
furo.transladar(dx=3, dy=4)
secao.adiciona(furo, coef=-1.0)

print(secao)
```

## Estrutura do projeto

```text
.
├── exemplos/
│   ├── exemplo_figcomposta.py  # Exemplo de seção composta
│   └── exemplo_figplana.py     # Exemplos de figuras genéricas
├── src/
│   └── figurasplanas/
│       ├── __init__.py          # API pública do pacote
│       ├── figura_composta.py   # Seções compostas
│       ├── figura_simples.py    # Figuras geométricas predefinidas
│       └── figuraplana.py       # Classe base e propriedades gerais
├── tests/
│   └── test_figuraplana.py      # Testes automatizados
├── pyproject.toml               # Configuração e dependências
└── README.md
```