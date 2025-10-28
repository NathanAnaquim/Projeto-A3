# Projeto A3 - Sistema de Vendas

## Integrantes
- João Rodrigo Albertini – RA: 823215381
- Leone Vicenzo Esposito - RA: 82326530
- Ítalo Ribeiro Prates – RA: 824112590  
- Matheus Bueno Neri de Araujo – RA: 822160370  
- Victor França – RA: 824122809  
- Mateus Brigagão Tavares da Cunha – RA: 825117649  
- Nathan Anaquim Procaccia – RA: 823117175  
- Luiz Felipe Dutra Xavier – RA: 823126087  

## Objetivo
O projeto consiste em refatorar um **sistema de vendas legado** mal estruturado, aplicando princípios de **Clean Code, SOLID e Design Patterns**, além de incluir **testes unitários**.

## Código Original (Legado)
O código inicial foi desenvolvido com diversas más práticas, para servir de base para refatoração.

Problemas encontrados:
- Nomes de variáveis e funções pouco descritivos (`n`, `p`, `q` etc.).
- Uso de listas globais para produtos, clientes e vendas.
- Ausência de classes e modularização.
- Funções acumulam múltiplas responsabilidades.
- Lógica duplicada em busca de clientes/produtos.
- Tratamento de erros apenas com `print()`.
- Sem testes unitários.
- Dificuldade de manutenção e escalabilidade.

## Estrutura esperada no final do projeto

├── src/
│   ├── app.py                  # servidor backend Python (Flask)
│   ├── sistema_vendas.py       # lógica de negócio (backend)
│   ├── models/
│   │   ├── produto.py
│   │   ├── cliente.py
│   │   └── venda.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── clientes.html
│   │   ├── produtos.html
│   │   ├── vendas.html
│   │   └── relatorio.html
│   └── static/
│       └── style.css
│
└── README.md


## Cronograma
- Setembro/2025 → Commit do código legado.  
- Outubro/2025 → Refatoração inicial (introdução de POO e modularização).  
- Novembro/2025 → Versão final refatorada + testes unitários.  
