import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff


st.set_page_config(page_title="Dashboard Profissional", layout="wide")


page = st.sidebar.radio("Navegação", ["Home", "Currículo", "Projetos", "Análise de Dados"])
if page == "Home":
    st.title("Vinicius Souza")
    st.image("foto.jpg", width=250)
    st.write("Fullstack Developer | Software Engineer | UI | React.JS | Vite | Node.js | JavaScript | HTML | CSS ( Flexbox e Grid) | Wordpress | Sass | Git | Github | Python | Java |")
    
    st.write("## Resumo Profissional")
    st.write("Engenheiro de Software em formação com sólida experiência em liderança e gestão de equipes, adquirida durante mais de 10 anos na área de gastronomia. Em transição para a área de tecnologia, possui competências práticas no desenvolvimento de aplicações web utilizando React, JavaScript e Python.")
    st.write("Demonstrou habilidade em liderar projetos acadêmicos inovadores, desenvolvendo soluções tecnológicas com foco em sustentabilidade e impacto social. Focado em entregar projetos de alta qualidade, priorizando a colaboração em equipe e a aplicação de boas práticas de desenvolvimento de software.")
    
elif page == "Currículo":
    st.title("Currículo Profissional")
    st.image("foto.jpg", width=250)
    st.write("## Vinicius Souza")
    st.write("### Engenheiro de Software | Fullstack Developer")
    st.write("Experiência com tecnologias modernas para desenvolvimento web e análise de dados.")
    
    st.write("**Habilidades:**")
    st.write("- React.JS, JavaScript, Vite, Node.js")
    st.write("- Python, Java, Git, GitHub")
    st.write("- HTML, CSS (Flexbox, Grid), Sass, Wordpress")
    
    st.write("**Experiência Profissional:**")
    st.write("- Desenvolvimento de projetos acadêmicos inovadores utilizando tecnologias web.")
    st.write("- Transição da Gastronomia para a Tecnologia com forte base em liderança e gestão de projetos.")
    
elif page == "Projetos":
    st.title("Projetos")
    projetos = [
        {"nome": "Projeto Wildbeast", "imagem": "wildbeastpage.png", "descricao": "Site interativo para estudo de desenvolvimento web.", "link": "https://github.com/Vinissil/wildbeast"},
        {"nome": "Hospital Consultancy", "imagem": "home.png", "descricao": "Aplicação web para hospitais.", "link": "https://github.com/Vinissil/HOSPITAL_CONSULTANCY"},
        {"nome": "SportPlace", "imagem": "tela_incial_sportplace.png", "descricao": "Marketplace de artigos esportivos.", "link": "https://github.com/Vinissil/SPORTPLACE"},
        {"nome": "Marketplace", "imagem": "home_marktplace.png", "descricao": "E-commerce com funcionalidades modernas.", "link": "https://github.com/Vinissil/MARKTPLACE"}
    ]
    
    for projeto in projetos:
        st.subheader(projeto["nome"])
        st.image(projeto["imagem"], width=400)
        st.write(projeto["descricao"])
        st.markdown(f"[Link do projeto]({projeto['link']})")
        st.divider()





elif page == "Análise de Dados":
    st.title("Análise de Dados")
    df = pd.read_excel("setores_desenvolvimento_100_numeros.xlsx", index_col="Setor")
    setores = ['Todos'] + df.index.unique().tolist()
    setor_escolhido = st.sidebar.selectbox("Filtrar por Setor", setores)
    
    df_filtered = df if setor_escolhido == 'Todos' else df.loc[[setor_escolhido]]
    st.dataframe(df_filtered)
    
    if "Likes" in df_filtered.columns:
        st.bar_chart(df_filtered["Likes"], use_container_width=True)
        
    st.write("### 1. Apresentação dos dados e tipos de variáveis")
        
    st.divider()
        
    st.write("- Explicação sobre o conjunto de dados utilizado")
    st.write("O conjunto de dados apresenta informações sobre diferentes setores de desenvolvimento, incluindo linguagens de programação utilizadas, frequência de uso, qualidade de software, popularidade e salário médio dos profissionais. Ele permite analisar quais tecnologias são mais relevantes em cada setor e como fatores como frequência de uso e qualidade do software impactam métricas como popularidade e salário médio.")
    
    st.write("- Identificação do tipo das variáveis")
    tipos = pd.DataFrame(df.dtypes, columns=["Tipo de Dado"])
    tipos["Categoria"] = tipos["Tipo de Dado"].apply(lambda x: "Numérica" if np.issubdtype(x, np.number) else "Categórica")
    st.dataframe(tipos)
    
    
    st.write("- Definição das principais perguntas de análise")
    st.write(" Quais setores apresentam maior popularidade")
    st.write(" Existe uma relação entre popularidade e salário médio")
    st.write(" Quais linguagens predominam nos setores com maior qualidade de software")
    st.write(" A frequência de uso das linguagens impacta o salário médio")
    st.write(" Setores com maior qualidade de software são também os mais populares")
    
    st.divider()

    st.write("### 2. Medidas centrais, análise inicial dos dados, dispersão, correlação")
    st.divider()
    

    st.write("#### Cálculo de média, mediana e moda")
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if numeric_cols:
        stats_df = df[numeric_cols].agg(['mean', 'median', lambda x: x.mode().values[0] if not x.mode().empty else np.nan])
        stats_df.rename(index={'mean': 'Média', 'median': 'Mediana', '<lambda_0>': 'Moda'}, inplace=True)
        st.dataframe(stats_df)
    

    st.write("#### Discussão sobre a distribuição dos dados")
    st.write("A distribuição pode ser analisada por meio de histogramas e medidas de dispersão.")
    for col in numeric_cols:
        st.write(f"##### Distribuição de {col}")
        fig = px.histogram(df, x=col, nbins=20, title=f"Histograma de {col}")
        st.plotly_chart(fig)
    

    st.write("#### Apresentação do desvio padrão e variância")
    dispersion_df = df[numeric_cols].agg(['std', 'var'])
    dispersion_df.rename(index={'std': 'Desvio Padrão', 'var': 'Variância'}, inplace=True)
    st.dataframe(dispersion_df)
    

    st.write("#### Identificação de possíveis correlações")
    correlation_matrix = df[numeric_cols].corr()
    st.dataframe(correlation_matrix)
    st.divider()
    

    st.write("### 3. Aplicação de pelo menos duas distribuições probabilísticas")

    st.write("- Apresentar visualizações e interpretações dos resultados")


    st.write("#### Distribuição Binomial")
    st.write("A distribuição binomial é utilizada para modelar o número de sucessos em uma sequência de tentativas independentes, como por exemplo, a probabilidade de um setor ter alto desempenho com base em certas condições.")
    n = 10
    p = 0.6
    x = np.arange(0, n+1)
    y = stats.binom.pmf(x, n, p)
    fig = px.bar(x=x, y=y, labels={'x': 'Número de Sucessos', 'y': 'Probabilidade'}, title="Distribuição Binomial")
    st.plotly_chart(fig)
    
    st.write("#### Distribuição Normal")
    st.write("A distribuição normal é útil para modelar variáveis contínuas, como salário médio dos setores. É aplicada quando os dados seguem um comportamento simétrico em torno da média.")
    mu, sigma = df["Salário Médio (USD)"].mean(), df["Salário Médio (USD)"].std()
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    y = stats.norm.pdf(x, mu, sigma)
    fig = px.line(x=x, y=y, labels={'x': 'Salário Médio (USD)', 'y': 'Densidade'}, title="Distribuição Normal")
    st.plotly_chart(fig)

    st.write("📊 Distribuição Binomial")
    st.write("A Distribuição Binomial foi escolhida porque ela modela eventos discretos em que há duas possibilidades: sucesso ou fracasso. No contexto dos setores de desenvolvimento, essa distribuição pode ser aplicada para modelar a chance de um setor ter alto desempenho com base em certos fatores (exemplo: qualidade de software ou popularidade).")
    
    st.write("Se considerarmos que um setor tem 60% de chance de ser bem avaliado, podemos usar a distribuição binomial para prever quantos setores, em um grupo de 10, terão alto desempenho.")
    
    st.write("Se a maioria das probabilidades estiver concentrada em valores altos, isso indica que a maioria dos setores tende a ter bom desempenho. Se os valores forem mais distribuídos, o desempenho pode variar bastante.")
    
    st.write("📈 Distribuição Normal")
    st.write("A Distribuição Normal foi escolhida porque muitas variáveis contínuas no mundo real seguem esse padrão. No conjunto de dados, o salário médio dos setores é uma variável contínua que pode ser modelada com a distribuição normal")
    st.write("Podemos analisar se os salários seguem uma distribuição normal (ou seja, se a maioria dos salários está próxima da média, com poucas variações extremas para cima ou para baixo).")
    st.write("Se os salários seguem um formato de curva de sino, isso indica que a maioria dos profissionais recebe salários próximos da média, e poucos ganham muito acima ou muito abaixo. Caso a distribuição seja assimétrica, isso pode indicar desigualdade salarial entre setores.")

st.sidebar.markdown("Desenvolvido por Vinicius Souza")