
# coding: utf-8

# # Code:Nation's Pandas-1 Challenge

# Você precisará de python 3.6 (ou superior) e o módulo pandas. Você pode instalar o que precisa com o arquivo `requirements.txt`.
# 
# Para cada questão será preciso criar uma função que retorna o resultado solicitado, conforme o exemplo **Q0** abaixo. No arquivo `sanity_checks.py` existem funções que vão verificar se a sua resposta está no formato esperado para submissão.
# 
# Todas as perguntas são referentes ao arquivo `data.csv`

# In[3]:


import sanity_checks as sc
import pandas as pd


# **Q0.** Cria um dataframe vazio.

# In[4]:


def part_0():
    return pd.DataFrame()

assert sc.part_0(part_0())


# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
# 

# In[5]:


df = pd.read_csv('data.csv')


# In[6]:


def part_1():
    return df.nationality.nunique()

assert sc.part_1(part_1())


# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?

# In[6]:


def part_2():
    return len(df.club.value_counts())

assert sc.part_2(part_2())


# **Q3.** Liste o primeiro nome dos 20 primeiros jogadores de acordo com a coluna `full_name`.

# In[7]:


def part_3():
    return df.full_name.str.split(expand=True).get(0).head(20)

assert sc.part_3(part_3())


# In[7]:


df.full_name.str.split(expand=True).get(0).head(20)


# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?

# In[8]:


def part_4():
    return df.sort_values('eur_wage',ascending=False).full_name.head(10)

assert sc.part_4(part_4())


# **Q5.** Quem são os 10 jogadores mais velhos?

# In[9]:


def part_5():
    return df.sort_values('birth_date').full_name.head(10)

assert sc.part_5(part_5())


# **Q6.** Conte quantos jogadores existem por idade. Para isto, utilize a o método `.groupby`.

# In[10]:


def part_6():
    return df.groupby('age').size()

assert sc.part_6(part_6())


# **Q7.** Quais jogadores tem potencial para fazerem gols mais bonitos? (chip_shot_trait == True, avoids_using_weaker_foot_trait == True).

# In[18]:


def part_7():
    return df.query('chip_shot_trait == True and avoids_using_weaker_foot_trait == True').full_name

assert sc.part_7(part_7())

