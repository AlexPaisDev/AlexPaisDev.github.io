"""
Content of the four CVs: Data & AI and Software engineering, each in English and Portuguese.
Edit the text here, then run:  python tools/cv/build_cvs.py

Every CV has the same layout (taken from template.docx): name, headline, contact line,
availability line, then the sections listed in "sections", in that order.
Section kinds:
  summary    one paragraph
  jobs       list of jobs: title line, dates, bullet points, an italic technologies line
  labelled   bullet list where each item starts with a bold label ("Cloud & BI: …")
  education  bold title + rest of the line, with an optional note underneath
  languages  the CEFR table (header row + one row per language)
Shared entries (the same job described the same way on both CVs) are defined once below.
Never mention clients by name (NDA): say "a client".
"""

NAME = 'Alexandre Pais'
EMAIL = 'alexpaisdev@gmail.com'
PHONE = '+351910863020'
LINKEDIN = 'https://www.linkedin.com/in/alexandre-pais-6740a91b2/'

# --------------------------------------------------------------------------- English
NOESIS_EN = {
    'title': 'Data Analytics & AI Consultant · Noesis',
    'dates': 'Jul 2026 – Present',
    'bullets': [
        'Deliver reporting, analytics and automation solutions on client projects, currently embedded with a client team and working alongside a Senior Consultant.',
        'Built a Python web scraper that collects every medicine code and its run-out date from the Infarmed website and loads the results automatically into a database.',
        'Optimized the scraper with parallel workers plus fallback and retry logic, cutting the full run from 20 minutes to 2 minutes (90% faster).',
        'Migrated a client’s Power BI dashboards from a local file-based setup to SharePoint, so reports and source files now live online in one central place.',
    ],
    'tech': 'Technologies: Python, Microsoft Azure, Power BI, Microsoft Fabric, SharePoint',
}
FRAUDIO_EN = {
    'title': 'Data Engineer · Fraudio B.V.',
    'dates': 'Sep 2020 – Apr 2022',
    'bullets': [
        'Built and managed large-scale analytics dashboards on Databricks using Scala, for real-time visualization and fraud pattern analysis.',
        'Benchmarked data storage technologies (MongoDB, Redis and others) to improve query latency and scalability.',
        'Automated reporting pipelines by integrating Databricks with the Slack API, speeding up incident response and team communication.',
        'Worked in an agile DevOps environment, supporting the reliability of distributed data processing.',
    ],
    'tech': 'Technologies: Databricks, Scala, Python (Pandas), SQL, MongoDB, Redis, YCSB',
}
EDUCATION_EN = [
    ('BSc in Computer Science & Engineering', ' · Polytechnic Institute of Setúbal (IPS) · 2023 – 2026', None),
    ('Academic Mobility Program', ' · Macao Polytechnic Institute · 2025', 'One-semester exchange in Macao to complete remaining courses.'),
    ('Higher Professional Technical Course (CTeSP), Game Development & Multimedia', ' · Polytechnic Institute of Setúbal (IPS) · 2021 – 2023', None),
    ('Vocational Technical Course, IT Systems Management & Programming', ' · Escola Secundária de Cacilhas-Tejo · 2017 – 2020', None),
]
LANGUAGES_EN = [
    ('Language', 'Level', 'Understanding', 'Speaking', 'Writing'),
    ('Portuguese', 'Native', 'C2', 'C2', 'C2'),
    ('English', 'Fluent', 'C2', 'C1', 'C1'),
    ('Spanish', 'Basic', 'A2', 'A2', 'A2'),
]
OPEN_EN = 'Open to remote or hybrid roles in Asia with possibility of relocation'

DATA_EN = {
    'pdf': 'Alexandre_Pais_CV_Data_EN',
    'lang': 'en',
    'doc_title': 'Alexandre Pais – CV (Data & AI)',
    'headline': 'Data & AI Consultant · Data Engineer',
    'location': 'Lisbon, Portugal',
    'open_to': OPEN_EN,
    'sections': [
        ('summary', 'Professional Summary',
         'Data and AI consultant who builds analytics, automation and big-data solutions on Azure, Power BI, Microsoft Fabric and Databricks. '
         'I optimized a Python data-collection scraper from 20 minutes to 2 minutes with parallel workers and retry logic, migrated enterprise Power BI dashboards to SharePoint, '
         'and previously engineered fraud-analytics dashboards and Slack-integrated reporting pipelines on Databricks and Scala. '
         'BSc in Computer Science & Engineering (2026), one semester at Macao Polytechnic Institute, fluent in English.'),
        ('jobs', 'Professional Experience', [
            NOESIS_EN,
            {'title': 'Game Developer · Overflow Interactive', 'dates': 'Oct 2025 – Feb 2026', 'bullets': [
                'Engineered a modular C# system with decoupled architecture, so reward logic scales and is easy to customize.',
                'Built state-driven gameplay logic in Unity, using animation state machines and clear separation of concerns.',
            ], 'tech': 'Technologies: Unity, C#, GitHub, Confluence'},
            {'title': 'AR/VR Developer · Arsenal do Alfeite S.A.', 'dates': 'Mar 2023 – Aug 2023', 'bullets': [
                'Developed a navigation simulation integrated with Node-RED to validate real-time data communication and message brokering between simulated environments and external controllers.',
                'Served as technical lead for live demos to key partners and clients, including the Portuguese Navy, Vodafone and Oracle.',
            ], 'tech': 'Technologies: Unity, C#, Node-RED, GitHub, Xcode'},
            FRAUDIO_EN,
            {'title': 'Web Developer', 'dates': 'Mar 2020 – Jun 2020', 'bullets': [
                'Designed relational schemas in MySQL, keeping data consistent and queries fast.',
                'Turned business requirements into working web features for corporate clients.',
            ], 'tech': 'Technologies: HTML, CSS, JavaScript, PHP, MySQL'},
        ]),
        ('labelled', 'Core Skills', [
            ('Cloud & BI:', ' Microsoft Azure, Microsoft Fabric, Power BI, SharePoint, Databricks'),
            ('Programming & Data:', ' Python (Pandas, web scraping), SQL, Scala'),
            ('Databases:', ' MongoDB, Redis, MySQL'),
            ('Automation & Integration:', ' parallel processing, retry and fallback design, Slack API, Node-RED'),
            ('Tools & Practices:', ' GitHub, Confluence, agile and DevOps workflows'),
        ]),
        ('education', 'Education', EDUCATION_EN),
        ('languages', 'Languages', LANGUAGES_EN),
    ],
}

SOFTWARE_EN = {
    'pdf': 'Alexandre_Pais_CV_EN',          # old filename kept so existing links keep working
    'lang': 'en',
    'doc_title': 'Alexandre Pais – CV (Software Engineering)',
    'headline': 'Software Engineer · Game Developer · AR/VR Developer',
    'location': 'Lisbon, Portugal',
    'open_to': OPEN_EN,
    'sections': [
        ('summary', 'Professional Summary',
         'Software engineer with experience across game development, AR/VR, the web and data. '
         'I built Unity applications for PC and iOS, including a navigation simulation integrated with Node-RED and an AR app for naval assets, '
         'and led live demos for the Portuguese Navy, Vodafone and Oracle. At Overflow Interactive I engineered a modular magic and loot system in C#, '
         'and I currently build Python automation as a Data & AI consultant at Noesis. '
         'BSc in Computer Science & Engineering (2026), one semester at Macao Polytechnic Institute, fluent in English.'),
        ('jobs', 'Professional Experience', [
            NOESIS_EN,
            {'title': 'Game Developer · Overflow Interactive', 'dates': 'Oct 2025 – Feb 2026', 'bullets': [
                'Engineered a modular magic and loot system in C# with a decoupled architecture, so reward logic scales and is easy to customize.',
                'Developed combat systems and animation state machines in Unity, focusing on fluid player feedback and state-driven logic.',
                'Designed and implemented responsive user interfaces and integrated spatial audio to enhance environmental immersion.',
                'Built immersive 3D environments from provided assets, balancing visual appeal with functional gameplay flow.',
            ], 'tech': 'Technologies: Unity, C#, GitHub, Confluence'},
            {'title': 'AR/VR Developer · Arsenal do Alfeite S.A.', 'dates': 'Mar 2023 – Aug 2023', 'bullets': [
                'Engineered and maintained high-fidelity 3D applications for PC and iOS in Unity, optimizing performance for mobile hardware.',
                'Developed a navigation simulation integrated with Node-RED to validate real-time data communication and message brokering between simulated environments and external controllers.',
                'Designed and deployed an iOS augmented reality app for interactive 3D visualization of naval assets.',
                'Served as technical lead for live demos to key partners and clients, including the Portuguese Navy, Vodafone and Oracle.',
            ], 'tech': 'Technologies: Unity, C#, Node-RED, GitHub, Xcode'},
            FRAUDIO_EN,
            {'title': 'Web Developer', 'dates': 'Mar 2020 – Jun 2020', 'bullets': [
                'Developed and maintained administrative web portals and landing pages for a portfolio of corporate clients.',
                'Designed relational schemas in MySQL, keeping data consistent and queries fast.',
                'Turned business requirements into working web features, with attention to user experience and cross-browser compatibility.',
            ], 'tech': 'Technologies: HTML, CSS, JavaScript, PHP, MySQL'},
        ]),
        ('labelled', 'Projects & Awards', [
            ('Home Server Infrastructure (2026 – present):', ' Ubuntu Server administered over SSH; containerizing personal projects and services with Docker and Docker Compose.'),
            ('2nd Place, Games For Good GameJam (IADE, 2022):', ' “Little Help”, an arcade game about the challenges of homelessness, built in 72 hours; I engineered its resource and time management system and reward loop.'),
            ('42 Piscine, C Programming (42 Lisboa, 2023):', ' 26-day immersion reimplementing standard C library functions from scratch, with manual memory management and leak-free code.'),
            ('Lisbon Games Week (2022):', ' official IPS representative; live playtesting of original projects and a production workshop led by Kwalee’s CTO.'),
        ]),
        ('labelled', 'Core Skills', [
            ('Programming Languages:', ' C#, C, Java, Python, SQL, PHP, JavaScript'),
            ('Game Development & XR:', ' Unity, animation state machines, combat systems, UI, spatial audio, AR for iOS, level design'),
            ('Systems & Infrastructure:', ' Linux (Ubuntu Server), SSH, Docker, Docker Compose, Node-RED'),
            ('Data & Cloud:', ' Databricks, Microsoft Azure, Power BI, MySQL, MongoDB, Redis'),
            ('Tools & Practices:', ' Git, GitHub, Visual Studio Code, Xcode, Confluence, agile and DevOps workflows'),
        ]),
        ('education', 'Education', EDUCATION_EN),
        ('languages', 'Languages', LANGUAGES_EN),
    ],
}

# --------------------------------------------------------------------------- Português (pt-PT)
NOESIS_PT = {
    'title': 'Consultor de Data Analytics & IA · Noesis',
    'dates': 'Jul 2026 – Presente',
    'bullets': [
        'Desenvolvo soluções de reporting, análise e automação em projetos de clientes, atualmente integrado numa equipa de cliente e a trabalhar com um Senior Consultant.',
        'Construí um web scraper em Python que recolhe todos os códigos de medicamentos e a respetiva data de rutura do site do Infarmed e carrega automaticamente os resultados numa base de dados.',
        'Otimizei o scraper com workers paralelos e lógica de fallback e retry, reduzindo a execução completa de 20 para 2 minutos (90% mais rápido).',
        'Migrei os dashboards de Power BI de um cliente de um sistema local baseado em ficheiros para o SharePoint, ficando relatórios e ficheiros de origem online num único local.',
    ],
    'tech': 'Tecnologias: Python, Microsoft Azure, Power BI, Microsoft Fabric, SharePoint',
}
FRAUDIO_PT = {
    'title': 'Data Engineer · Fraudio B.V.',
    'dates': 'Set 2020 – Abr 2022',
    'bullets': [
        'Construí e geri dashboards analíticos de grande escala em Databricks com Scala, para visualização em tempo real e análise de padrões de fraude.',
        'Avaliei tecnologias de armazenamento de dados (MongoDB, Redis e outras) para melhorar a latência e a escalabilidade das consultas.',
        'Automatizei pipelines de relatórios integrando o Databricks com a API do Slack, acelerando a resposta a incidentes e a comunicação da equipa.',
        'Trabalhei num ambiente ágil de DevOps, contribuindo para a fiabilidade do processamento distribuído de dados.',
    ],
    'tech': 'Tecnologias: Databricks, Scala, Python (Pandas), SQL, MongoDB, Redis, YCSB',
}
EDUCATION_PT = [
    ('Licenciatura em Engenharia Informática', ' · Instituto Politécnico de Setúbal (IPS) · 2023 – 2026', None),
    ('Programa de Mobilidade Académica', ' · Instituto Politécnico de Macau · 2025', 'Semestre de intercâmbio em Macau para concluir as últimas unidades curriculares.'),
    ('Curso Técnico Superior Profissional (CTeSP) em Desenvolvimento de Videojogos e Aplicações Multimédia', ' · Instituto Politécnico de Setúbal (IPS) · 2021 – 2023', None),
    ('Curso Profissional de Técnico de Gestão e Programação de Sistemas Informáticos', ' · Escola Secundária de Cacilhas-Tejo · 2017 – 2020', None),
]
LANGUAGES_PT = [
    ('Língua', 'Nível', 'Compreensão', 'Oral', 'Escrita'),
    ('Português', 'Nativo', 'C2', 'C2', 'C2'),
    ('Inglês', 'Fluente', 'C2', 'C1', 'C1'),
    ('Espanhol', 'Básico', 'A2', 'A2', 'A2'),
]
OPEN_PT = 'Disponível para funções remotas ou híbridas na Ásia, com possibilidade de relocalização'

DATA_PT = {
    'pdf': 'Alexandre_Pais_CV_Data_PT',
    'lang': 'pt',
    'doc_title': 'Alexandre Pais – CV (Dados & IA)',
    'headline': 'Consultor de Dados & IA · Data Engineer',
    'location': 'Lisboa, Portugal',
    'open_to': OPEN_PT,
    'sections': [
        ('summary', 'Resumo Profissional',
         'Consultor de dados e IA que constrói soluções de análise, automação e big data em Azure, Power BI, Microsoft Fabric e Databricks. '
         'Otimizei um scraper de recolha de dados em Python de 20 para 2 minutos com workers paralelos e lógica de retry, migrei dashboards empresariais de Power BI para o SharePoint '
         'e, anteriormente, desenvolvi dashboards de análise de fraude e pipelines de relatórios integrados com o Slack em Databricks e Scala. '
         'Licenciatura em Engenharia Informática (2026), um semestre no Instituto Politécnico de Macau, inglês fluente.'),
        ('jobs', 'Experiência Profissional', [
            NOESIS_PT,
            {'title': 'Game Developer · Overflow Interactive', 'dates': 'Out 2025 – Fev 2026', 'bullets': [
                'Desenvolvi um sistema modular em C# com arquitetura desacoplada, para que a lógica de recompensas escale e seja fácil de personalizar.',
                'Construí lógica de jogo orientada a estados em Unity, com máquinas de estados de animação e uma separação clara de responsabilidades.',
            ], 'tech': 'Tecnologias: Unity, C#, GitHub, Confluence'},
            {'title': 'Developer AR/VR · Arsenal do Alfeite S.A.', 'dates': 'Mar 2023 – Ago 2023', 'bullets': [
                'Desenvolvi uma simulação de navegação integrada com Node-RED para validar a comunicação de dados em tempo real e o message brokering entre ambientes simulados e controladores externos.',
                'Responsável técnico pelas demonstrações ao vivo a parceiros e clientes, incluindo a Marinha Portuguesa, a Vodafone e a Oracle.',
            ], 'tech': 'Tecnologias: Unity, C#, Node-RED, GitHub, Xcode'},
            FRAUDIO_PT,
            {'title': 'Web Developer', 'dates': 'Mar 2020 – Jun 2020', 'bullets': [
                'Desenhei esquemas relacionais em MySQL, mantendo os dados consistentes e as consultas rápidas.',
                'Transformei requisitos de negócio em funcionalidades web para clientes empresariais.',
            ], 'tech': 'Tecnologias: HTML, CSS, JavaScript, PHP, MySQL'},
        ]),
        ('labelled', 'Competências', [
            ('Cloud & BI:', ' Microsoft Azure, Microsoft Fabric, Power BI, SharePoint, Databricks'),
            ('Programação & Dados:', ' Python (Pandas, web scraping), SQL, Scala'),
            ('Bases de Dados:', ' MongoDB, Redis, MySQL'),
            ('Automação & Integração:', ' processamento paralelo, design de retry e fallback, Slack API, Node-RED'),
            ('Ferramentas & Práticas:', ' GitHub, Confluence, metodologias ágeis e DevOps'),
        ]),
        ('education', 'Formação', EDUCATION_PT),
        ('languages', 'Línguas', LANGUAGES_PT),
    ],
}

SOFTWARE_PT = {
    'pdf': 'Alexandre_Pais_CV_PT',          # old filename kept so existing links keep working
    'lang': 'pt',
    'doc_title': 'Alexandre Pais – CV (Engenharia de Software)',
    'headline': 'Engenheiro de Software · Game Developer · Developer AR/VR',
    'location': 'Lisboa, Portugal',
    'open_to': OPEN_PT,
    'sections': [
        ('summary', 'Resumo Profissional',
         'Engenheiro de software com experiência em desenvolvimento de jogos, AR/VR, web e dados. '
         'Desenvolvi aplicações Unity para PC e iOS, incluindo uma simulação de navegação integrada com Node-RED e uma aplicação de realidade aumentada de meios navais, '
         'e liderei demonstrações ao vivo para a Marinha Portuguesa, a Vodafone e a Oracle. Na Overflow Interactive desenvolvi em C# um sistema modular de magia e loot '
         'e, atualmente, desenvolvo automação em Python como consultor de Dados & IA na Noesis. '
         'Licenciatura em Engenharia Informática (2026), um semestre no Instituto Politécnico de Macau, inglês fluente.'),
        ('jobs', 'Experiência Profissional', [
            NOESIS_PT,
            {'title': 'Game Developer · Overflow Interactive', 'dates': 'Out 2025 – Fev 2026', 'bullets': [
                'Desenvolvi em C# um sistema modular de magia e loot com arquitetura desacoplada, para que a lógica de recompensas escale e seja fácil de personalizar.',
                'Desenvolvi sistemas de combate e máquinas de estados de animação em Unity, com foco em feedback fluido para o jogador e lógica orientada a estados.',
                'Desenhei e implementei interfaces de utilizador responsivas e integrei áudio espacializado para reforçar a imersão no ambiente.',
                'Construí ambientes 3D imersivos a partir de assets fornecidos, equilibrando o aspeto visual com o fluxo de jogo.',
            ], 'tech': 'Tecnologias: Unity, C#, GitHub, Confluence'},
            {'title': 'Developer AR/VR · Arsenal do Alfeite S.A.', 'dates': 'Mar 2023 – Ago 2023', 'bullets': [
                'Desenvolvi e mantive aplicações 3D de alta fidelidade para PC e iOS em Unity, otimizando a performance para hardware móvel.',
                'Desenvolvi uma simulação de navegação integrada com Node-RED para validar a comunicação de dados em tempo real e o message brokering entre ambientes simulados e controladores externos.',
                'Desenhei e implementei uma aplicação de realidade aumentada para iOS, para visualização interativa de modelos 3D de meios navais.',
                'Responsável técnico pelas demonstrações ao vivo a parceiros e clientes, incluindo a Marinha Portuguesa, a Vodafone e a Oracle.',
            ], 'tech': 'Tecnologias: Unity, C#, Node-RED, GitHub, Xcode'},
            FRAUDIO_PT,
            {'title': 'Web Developer', 'dates': 'Mar 2020 – Jun 2020', 'bullets': [
                'Desenvolvi e mantive portais de administração e landing pages para várias empresas clientes.',
                'Desenhei esquemas relacionais em MySQL, mantendo os dados consistentes e as consultas rápidas.',
                'Transformei requisitos de negócio em funcionalidades web, com atenção à experiência de utilização e à compatibilidade entre browsers.',
            ], 'tech': 'Tecnologias: HTML, CSS, JavaScript, PHP, MySQL'},
        ]),
        ('labelled', 'Projetos e Distinções', [
            ('Infraestrutura de Servidor Doméstico (2026 – presente):', ' Ubuntu Server administrado por SSH; a containerizar projetos e serviços pessoais com Docker e Docker Compose.'),
            ('2.º Lugar, Games For Good GameJam (IADE, 2022):', ' “Little Help”, um jogo arcade sobre os desafios das pessoas em situação de sem-abrigo, feito em 72 horas; desenvolvi o sistema de gestão de recursos e tempo e o ciclo de recompensa.'),
            ('Piscine da 42, Programação em C (42 Lisboa, 2023):', ' imersão de 26 dias a reimplementar funções da biblioteca standard de C de raiz, com gestão manual de memória e código sem fugas.'),
            ('Lisbon Games Week (2022):', ' representante oficial do IPS; playtesting ao vivo de projetos próprios e workshop de produção conduzido pelo CTO da Kwalee.'),
        ]),
        ('labelled', 'Competências', [
            ('Linguagens de Programação:', ' C#, C, Java, Python, SQL, PHP, JavaScript'),
            ('Desenvolvimento de Jogos & XR:', ' Unity, máquinas de estados de animação, sistemas de combate, UI, áudio espacial, AR para iOS, level design'),
            ('Sistemas & Infraestrutura:', ' Linux (Ubuntu Server), SSH, Docker, Docker Compose, Node-RED'),
            ('Dados & Cloud:', ' Databricks, Microsoft Azure, Power BI, MySQL, MongoDB, Redis'),
            ('Ferramentas & Práticas:', ' Git, GitHub, Visual Studio Code, Xcode, Confluence, metodologias ágeis e DevOps'),
        ]),
        ('education', 'Formação', EDUCATION_PT),
        ('languages', 'Línguas', LANGUAGES_PT),
    ],
}

CVS = [DATA_EN, DATA_PT, SOFTWARE_EN, SOFTWARE_PT]
