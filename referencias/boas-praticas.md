# 🚀 Boas Práticas

Organização do Código: mantenha os scripts limpos, modulares e bem comentados para facilitar manutenção e colaboração.  
Versionamento Semântico: use commits claros e padronizados para rastrear mudanças com precisão.  
Automação Gradual: comece com pequenas tarefas, valide resultados e escale progressivamente para evitar falhas críticas.  
Segurança e Sigilo: evite expor dados sensíveis em código, logs ou documentação pública.  
Documentação Atualizada: registre decisões, fluxos e configurações para garantir continuidade e facilitar onboarding.  
Comunicação Ativa: troque feedbacks frequentes com o time para antecipar problemas e alinhar expectativas.  

## Padronização de Commits

| Tipo         | Descrição                                   | Exemplo                                      |
|--------------|---------------------------------------------|----------------------------------------------|
| **feat**     | Nova funcionalidade ou recurso               | feat: adicionar integração com BotCity       |
| **fix**      | Correção de bug ou problema                   | fix: corrigir erro no deploy do bot           |
| **docs**     | Atualização na documentação                   | docs: atualizar README com instruções de uso |
| **style**    | Mudanças estéticas ou de formatação (sem código) | style: corrigir indentação e espaços           |
| **refactor** | Refatoração de código (sem alterar funcionalidades) | refactor: melhorar organização dos módulos     |
| **test**     | Adição ou ajuste de testes                     | test: incluir testes para workflow de orquestração |
| **chore**    | Tarefas gerais, atualizações de ferramentas, config | chore: atualizar dependências do projeto      |
| **perf**     | Melhorias de performance                       | perf: otimizar consulta de dados               |
| **ci**       | Ajustes em configuração de integração contínua | ci: configurar pipeline de deploy automatizado |

---

### Dicas bônus:

- Comece sempre a mensagem com o tipo (feat, fix...) seguido de dois pontos e um espaço.
- Seja breve, mas claro.
- Evite abreviações obscuras (ex.: “fix bug” pode virar “fix: corrigir erro na conexão API”).
- Para commits maiores, escreva uma descrição detalhada no corpo da mensagem.
