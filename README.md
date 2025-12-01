# Melhores Compras – Modelagem e Implementação de Banco de Dados

Projeto acadêmico da Fase 1 – **Database Essentials (FIAP)**

---

## Sobre o Projeto

Este repositório reúne a modelagem e a implementação de um banco de dados relacional desenvolvido a partir do estudo de caso **Melhores Compras LTDA**, uma empresa fictícia de e-commerce em expansão.

O objetivo da atividade foi transformar um conjunto de **regras de negócio complexas** em um banco de dados consistente e escalável, capaz de armazenar:

* informações de clientes (Pessoa Física e Jurídica)
* produtos e categorias
* vídeos associados aos produtos
* históricos de visualização
* chamados do SAC (incluindo índice de satisfação)
* hierarquia de funcionários e endereços

O resultado final inclui **modelo lógico, modelo físico, script DDL e solução em Python**, todos desenvolvidos em grupo.

**Ferramenta utilizada:**
Toda a modelagem (MER e Modelo Físico) e geração do DDL foram feitas usando o **Oracle SQL Developer Data Modeler**.

## Conteúdos do Repositório

```
/docs
   modelo-logico.pdf        → Modelo Entidade-Relacionamento (MER)
   modelo-fisico.pdf        → Modelo Relacional / Modelo Físico

/sql
   Script_DDL_Melhores_Compras.sql   → Criação completa das tabelas, chaves e constraints

/python
   Codigo_Nivel_Atendimento_SAC_Melhores_Compras.py → Classificação de nível de satisfação do SAC
```

---

# 1. Modelagem do Banco de Dados

A modelagem foi construída com base nas regras de negócio fornecidas na atividade da FIAP.

## **Modelo Lógico (MER)**

Inclui entidades como:

* **Clientes:** `MC_CLIENTE`, `MC_CLI_FISICA`, `MC_CLI_JURIDICA`
* **Produtos:** `MC_PRODUTO`, `MC_CATEGORIA_PROD`
* **Vídeos:** `MC_VIDEO_PROD`, `VISUALIZACAO_VIDEO`, `MC_CATEGORIA_VIDEO`
* **SAC:** `MC_SGV_SAC` (tabela rica em atributos e constraints específicas)
* **Funcionários:** `MC_FUNCIONARIO`, `MC_DEPTO`, `MC_END_FUNC`
* **Localização:** `MC_ESTADO`, `MC_CIDADE`, `MC_BAIRRO`, `MC_LOGRADOURO`, `MC_END_CLI`

As entidades seguem boas práticas de:

* nomeação
* tipos de dados adequados
* normalização
* uso correto de **PRIMARY KEY**, **FOREIGN KEY**, **UNIQUE**, **CHECK**

📌 **Arquivo:**
`/docs/modelo-logico.pdf`

## **Modelo Físico**

O modelo físico apresenta:

* chaves primárias e estrangeiras
* relacionamentos completos
* cardinalidades
* constraints obrigatórias
* campos obrigatórios e opcionais conforme regras de negócio

📌 **Arquivo:**
`/docs/modelo-fisico.pdf`

# 2. Implementação – Script SQL (DDL)

O script SQL em `/sql` contém:

* criação de todas as tabelas
* constraints de PK, FK, UNIQUE e CHECK
* sequences/identity onde aplicável
* comandos `DROP` para recriação do ambiente

Trechos contemplam várias regras de negócio, como:

* **RN01** — Status limitado (CHECK)
* **RN03** — DS_PRODUTO deve ser único
* **RN05** — Código de categoria sequencial
* **RN07** — Data/hora obrigatórias para visualização
* **RN11–RN20** — Estrutura completa do SAC

📌 Script:
`Script_DDL_Melhores_Compras.sql`

# 3. Código Python – Classificação de Satisfação (SAC)

Arquivo:
`/python/Codigo_Nivel_Atendimento_SAC_Melhores_Compras.py`

Este script lê uma nota de satisfação (0–100) e classifica o atendimento em:

* **Alta qualidade** (≥ 90)
* **Neutro** (70–89)
* **Insatisfatório** (< 70)

Representa a segunda parte da atividade prática solicitada na fase.

---

# Como Executar

## Rodando o SQL

Você pode utilizar:

* **Oracle Live SQL (recomendado pela atividade)**
* Ou um SGBD local compatível

Passos:

1. Abra `Script_DDL_Melhores_Compras.sql`
2. Execute o bloco de criação
3. Para reiniciar, use os comandos `DROP` disponíveis ao final do script

## Rodando o Python

```bash
python Codigo_Nivel_Atendimento_SAC_Melhores_Compras.py
```

---

# Integrantes do Grupo

* Carlos Vinicius Rodrigues Silva
* Diego Santos de Oliveira
* Felipe Freitas Santana
* Gabriela Sena da Silva
* Thatiane Kauffmann

---

# Aprendizados da Fase

✔ Modelagem lógica e física

✔ Interpretação de regras de negócio reais

✔ Normalização e boas práticas

✔ Criação de constraints profissionais

✔ Construção de um script DDL completo

✔ Introdução ao Python aplicado ao negócio

---

# 📩 Contato

**Gabriela Sena da Silva**

🔗 LinkedIn: [https://www.linkedin.com/in/gabrielasena/](https://www.linkedin.com/in/gabrielasena/)

📧 [gabisena@outlook.com](mailto:gabisena@outlook.com)

Sinta-se à vontade para trocar ideias sobre modelagem de dados, SQL ou Data Science!
