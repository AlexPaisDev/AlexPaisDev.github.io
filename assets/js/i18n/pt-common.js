/* =====================================================================
   Portuguese (pt-PT) strings shared by BOTH sides (data and software).
   How it works: every element with data-i18n="key" in the HTML shows its English
   text by default; when PT is selected, site.js swaps in the value for that key.
   Side-specific strings live in pt-data.js / pt-software.js (loaded after this file,
   so a key there overrides the same key here).
   ===================================================================== */
window.I18N_PT = Object.assign(window.I18N_PT || {}, {
  /* navigation & buttons */
  'skip': 'Saltar para o conteúdo',
  'nav.about': 'Sobre',
  'nav.exp': 'Experiência',
  'nav.proj': 'Projetos',
  'nav.skills': 'Competências',
  'nav.records': 'Registos',
  'nav.contact': 'Contacto',
  'save': 'Guardar CV',
  'menu': 'Menu',
  'hero.cta': 'Falar comigo',
  'code': 'Ver código',

  /* ID card */
  'id.title': 'Cartão de identificação',
  'id.name': 'Nome',
  'id.class': 'Classe',
  'id.base': 'Base',
  'id.baseV': 'Lisboa, Portugal',
  'id.now': 'Agora',
  'id.speaks': 'Fala',
  'id.ach': 'Conquistas',

  /* section titles */
  'about.tab': 'Sobre',
  'exp.tab': 'Diário de missões',
  'rec.tab': 'Registos',
  'rec.sub': 'Formação &amp; línguas',
  'rec.edu': 'Formação',
  'tools.title': 'Ferramentas pessoais',
  'found.title': 'Bases',

  /* quest log: labels and the roles described the same way on both sides */
  'q.active': 'Ativa',
  'q.done': 'Concluída',
  'gear': 'Equipado',
  'exp1.when': 'Jul 2026 – Agora',
  'exp1.role': 'Consultor de Data Analytics &amp; IA',
  'exp1.where': 'Lisboa · projetos de clientes',
  'exp1.intro': 'Reporting, análise e automação em projetos de clientes, a trabalhar com um Senior Consultant.',
  'exp1.b1': 'Construí um scraper em Python que recolhe todos os códigos de medicamentos e a respetiva data de rutura do site do Infarmed e os carrega automaticamente numa base de dados.',
  'exp1.b2': 'Reduzi a execução completa de <b>20 minutos para 2</b> (90% mais rápido) com workers paralelos, fallbacks e lógica de retry.',
  'exp1.b3': 'Migrei os dashboards de Power BI de um cliente de ficheiros locais para o SharePoint: relatórios e fontes estão agora online, num só sítio.',
  'exp2.when': 'Out 2025 – Fev 2026',
  'exp3.when': 'Mar 2023 – Ago 2023',
  'exp3.role': 'Developer AR/VR',
  'exp4.when': 'Set 2020 – Abr 2022',
  'exp4.where': 'Lisboa',
  'exp4.b1': 'Construí e geri dashboards analíticos de grande escala em Databricks com Scala, para análise de padrões de fraude em tempo real.',
  'exp4.b2': 'Avaliei tecnologias de armazenamento (MongoDB, Redis e outras, com YCSB) para melhorar a latência e a escalabilidade das consultas.',
  'exp4.b3': 'Automatizei relatórios ligando o Databricks à API do Slack, o que acelerou a resposta a incidentes.',
  'exp4.b4': 'Trabalhei numa equipa ágil com práticas DevOps, a garantir a fiabilidade do processamento distribuído de dados.',
  'exp5.when': 'Mar 2020 – Jun 2020',

  /* personal tools & foundations */
  'tools.intro': 'Fora do trabalho construo ferramentas para mim e uso-as todos os dias. Estas três são open source.',
  't1.desc': 'A página inicial do meu browser, a funcionar como um pequeno sistema operativo. A pesquisa consulta várias fontes ao mesmo tempo, junta os resultados que apontam para a mesma página e dá prioridade aos que foram encontrados por mais fontes. Tem ainda um feed de tecnologia, monitorização dos serviços da rede de casa e a minha atividade no GitHub. Sem build nem frameworks.',
  't2.desc': 'Um widget para Windows (Electron), sempre visível, que mostra os meus limites de utilização do Claude (5 horas e semanal). Lê os dados de rate limit que o Claude Code passa à sua status line, e um guardião em pixel art reage à medida que os limites se aproximam.',
  't3.title': 'Agente de IA para Discord',
  't3.desc': 'Um bot de Discord em Python com a API da DeepSeek. Responde em streaming, guarda memória por canal e usa ferramentas (pesquisa web, leitura de páginas, GIFs) através de function calling. Totalmente assíncrono e empacotado com Docker para funcionar 24/7.',
  'arc0': '2.º lugar na Games For Good GameJam (IADE, 2022). Feito em 72 horas.',
  'arc1': 'Tower defense 3D em Unity com IA de inimigos, vagas e progressão por níveis.',
  'arc2': 'A biblioteca standard de C e o printf, reescritos de raiz na Piscine da 42.',
  'arc3.t': 'Reservas de hotel',
  'arc3': 'Site de reservas full-stack em PHP com back end em MySQL e painel de administração. Projeto final, 2020.',

  /* records */
  'edu1.t': 'Licenciatura em Engenharia Informática',
  'edu1.s': 'Instituto Politécnico de Setúbal (IPS)',
  'edu2.t': 'Programa de mobilidade académica',
  'edu2.s': 'Instituto Politécnico de Macau: um semestre em Macau',
  'edu3.t': 'CTeSP em Desenvolvimento de Videojogos e Multimédia',
  'edu4.t': 'Curso Profissional de Gestão e Programação de Sistemas Informáticos',
  'aw1.t': 'Piscine da 42, programação em C · 2023',
  'aw1.s': '26 dias na 42 Lisboa: libc reescrita de raiz, gestão manual de memória, código sem fugas.',
  'aw2.t': 'Games For Good GameJam, 2.º · 2022',
  'aw2.s': 'IADE. Little Help, feito em 72 horas.',
  'aw3.t': 'Lisbon Games Week · 2022',
  'aw3.s': 'Representante oficial do IPS: playtesting ao vivo e um workshop conduzido pelo CTO da Kwalee.',
  'lang.title': 'Línguas',
  'lang.pt': 'Português',
  'lang.native': 'Nativo',
  'lang.en': 'Inglês',
  'lang.es': 'Espanhol',

  /* contact & form (form.sending/ok/err are used by site.js) */
  'contact.copyAria': 'Copiar endereço de email',
  'contact.copy': 'Copiar',
  'contact.copied': 'Copiado',
  'contact.call': 'Ligar',
  'form.title': 'Deixar mensagem',
  'form.name': 'Nome',
  'form.msg': 'Mensagem',
  'form.send': 'Enviar',
  'form.sending': 'A enviar…',
  'form.ok': 'Obrigado! A tua mensagem foi enviada. Respondo em breve.',
  'form.err': 'Algo correu mal. Envia-me um email diretamente para alexpaisdev@gmail.com.',
  'foot.both': 'Os dois lados',
});
