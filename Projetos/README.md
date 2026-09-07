# ⚡ Calculadora de Consumo Elétrico Inteligente

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge\&logo=github\&logoColor=white)
![Energia](https://img.shields.io/badge/Energia-Elétrica-yellow?style=for-the-badge\&logo=lightning\&logoColor=white)

## 📖 Sobre o projeto

Este projeto tem como objetivo calcular o consumo mensal de energia elétrica de um aparelho, com base em sua potência em Watts e no tempo médio de uso diário.

O programa foi desenvolvido utilizando a linguagem de programação Python e também calcula um custo mensal estimado com base no consumo de energia.

## 🐍 Tecnologias utilizadas

* Python
* Git
* GitHub

## 🧮 Fórmula utilizada

O consumo mensal de energia é calculado utilizando a seguinte fórmula:

consumoMensal = (potencia * horasDia * 30) / 1000

Onde:

* potencia = potência do aparelho em Watts.
* horasDia = tempo médio de uso diário.
* 30 = quantidade estimada de dias no mês.
* 1000 = conversão de Watts para quilowatts.

## 💰 Cálculo do custo estimado

Foi utilizado o valor fixo de **R$ 0,80 por kWh** para calcular uma estimativa de custo mensal.

custoMensal = consumoMensal * valorKwh

## 🚀 Como executar o projeto

1. Clone este repositório ou faça o download dos arquivos.
2. Certifique-se de ter o Python instalado em seu computador.
3. Execute o arquivo app.py.

## 📊 Exemplo de resultado

```
Aparelho: Forno Elétrico
Consumo estimado: 45,00 kWh/mês
Custo estimado: R$ 36,00
```


