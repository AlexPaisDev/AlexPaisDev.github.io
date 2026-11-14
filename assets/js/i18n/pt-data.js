/* Portuguese (pt-PT) strings used only on the DATA side (data/index.html).
   Shared strings are in pt-common.js. */
window.I18N_PT = Object.assign(window.I18N_PT || {}, {
  'meta.title': 'Alexandre Pais · Consultor de Dados & IA',
  'meta.desc': 'Alexandre Pais, consultor de dados e IA e data engineer em Lisboa: recolha de dados em Python, pipelines na cloud e relatórios em Power BI sobre Azure, Microsoft Fabric e Databricks. Disponível para funções na Ásia.',
  'switch': 'Lado de software',
  'foot.other': 'Lado de software',

  /* hero & ID card */
  'hero.role': 'Consultor de Dados &amp; IA · Data Engineer',
  'hero.dialog': 'Olá! Sou o Alexandre, consultor de dados e IA em Lisboa. Construo a infraestrutura de dados de que as empresas dependem: recolha de dados em Python, pipelines na cloud e relatórios em Power BI, sobre Azure, Microsoft Fabric e Databricks.',
  'id.classV': 'Data Engineer',
  'id.nowV': 'Consultor de Dados &amp; IA na Noesis',
  'id.status': 'Disponível para funções em dados e IA na Ásia: remoto, híbrido ou com relocalização',
  'id.a1': 'Pipeline 90% mais rápido',
  'id.a2': 'Demos para a Marinha',
  'id.a3': 'GameJam, 2.º lugar',
  'id.a4': 'Licenciatura, 2026',

  /* about */
  'about.p1': 'Sou consultor de dados e IA na Noesis, em Lisboa. O meu trabalho é transformar fontes dispersas em relatórios em que as pessoas confiam: recolhas em Python que correm sozinhas, pipelines em Azure e Microsoft Fabric, e Power BI centralizado num só sítio em vez de no portátil de alguém.',
  'about.p2': 'Cheguei aqui por um caminho pouco comum. Comecei no desenvolvimento web, passei quase dois anos como data engineer na Fraudio a construir dashboards de análise de fraude em Databricks, e depois mudei para Unity, com simulação naval e sistemas de jogo. Essa mistura nota-se na forma como trabalho: arquitetura limpa, atenção à performance e à-vontade para apresentar o resultado a quem o vai usar.',
  'about.p3': 'Terminei a licenciatura em Engenharia Informática em 2026, com um semestre no Instituto Politécnico de Macau. O próximo passo que procuro é uma função em dados ou IA na Ásia: remota, híbrida ou com relocalização.',

  /* quest log: data-side wording */
  'exp2.b1': 'Desenvolvi em C# um sistema de recompensas modular e desacoplado, escalável e fácil de personalizar.',
  'exp2.b2': 'Construí lógica de jogo orientada a estados em Unity, com máquinas de estados de animação e uma separação clara de responsabilidades.',
  'exp3.b1': 'Desenvolvi uma simulação de navegação naval integrada com Node-RED, para validar a comunicação em tempo real entre o ambiente simulado e controladores externos.',
  'exp3.b2': 'Responsável técnico pelas demonstrações ao vivo a parceiros e clientes, incluindo a Marinha Portuguesa, a Vodafone e a Oracle.',
  'exp5.b1': 'Desenhei esquemas relacionais em MySQL que mantinham os dados consistentes e as consultas rápidas.',
  'exp5.b2': 'Transformei requisitos de negócio em funcionalidades web para clientes empresariais.',

  /* projects */
  'client.tag': 'Noesis · projeto de cliente · 2026',
  'd1.title': 'Monitor de disponibilidade de medicamentos',
  'd1.desc': 'O cliente precisava de todos os códigos de medicamentos e respetivas datas de rutura do Infarmed, a autoridade do medicamento em Portugal, sem ninguém os copiar à mão. Construí um scraper em Python que os carrega diretamente numa base de dados, e depois reescrevi-o com workers paralelos, fallbacks e retries.',
  'd1.gear': 'workers paralelos · retry &amp; fallback',
  'd1.figAria': 'Pipeline: site do Infarmed, scraper em Python, retry e fallback, base de dados. O tempo de execução passou de 20 minutos para 2.',
  'd1.fig': 'O pipeline',
  'd1.n1': 'Infarmed',
  'd1.n1s': 'origem',
  'd1.n2': 'Scraper',
  'd1.n2s': 'paralelo',
  'd1.n4': 'Base de dados',
  'd1.before': 'Antes',
  'd1.after': 'Depois',
  'd2.title': 'Power BI, migrado para o SharePoint',
  'd2.desc': 'Os dashboards de Power BI do cliente e os respetivos ficheiros de origem viviam num sistema local, baseado em ficheiros. Migrei-os para o SharePoint: relatórios e fontes estão agora online, num único sítio acessível a toda a equipa.',
  'd3.title': 'Análise de fraude em escala',
  'd3.desc': 'Dashboards de grande escala em Databricks com Scala para detetar padrões de fraude em tempo real, pipelines de relatórios que publicam diretamente no Slack para uma resposta mais rápida a incidentes, e benchmarks YCSB a MongoDB, Redis e outros para reduzir a latência das consultas.',
  'd4.title': 'Comunicação em tempo real para um simulador naval',
  'd4.desc': 'Uma simulação de navegação naval tinha de trocar dados ao vivo com controladores externos. Integrei-a com o Node-RED para o message brokering, validei o fluxo de dados e liderei as demonstrações para a Marinha Portuguesa, a Vodafone e a Oracle.',

  /* skills */
  'sk2': 'Programação &amp; dados',
  'sk2a': 'Web scraping',
  'sk3': 'Bases de dados',
  'sk4': 'Automação',
  'sk4a': 'Processamento paralelo',
  'sk4b': 'Design de retry &amp; fallback',
  'sk6': 'Ferramentas',
  'sk7': 'Também',

  /* contact */
  'contact.lede': 'Vamos trabalhar juntos? Procuro funções em dados e IA na Ásia, remotas, híbridas ou com relocalização. Escolhe uma opção abaixo.',
});
