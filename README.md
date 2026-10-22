# 📊 CVM Financial Analytics · Fabric · AI

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20constru%C3%A7%C3%A3o-orange)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Pipeline em Python que coleta dados abertos da CVM, padroniza demonstrações financeiras e alimenta painéis do Power BI para análise econômico-financeira de companhias abertas.

## 🚦 Status

🚧 **Em construção.** Etapa atual: **A — pipeline Python de extração dos dados da CVM** (estrutura do repositório concluída).

## 🚀 Como instalar e testar

Pré-requisitos: Python 3.11 ou superior e Git.

```bash
git clone https://github.com/aarrys/cvm-financial-analytics-fabric-ai.git
cd cvm-financial-analytics-fabric-ai

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -e ".[dev]"
cp .env.example .env             # Windows (PowerShell): Copy-Item .env.example .env

pytest
```

## 📄 Dados

Os dados vêm do [Portal de Dados Abertos da CVM](https://dados.cvm.gov.br/), publicados sob a licença [ODbL](https://opendatacommons.org/licenses/odbl/). O código deste repositório está sob a licença [MIT](LICENSE).
