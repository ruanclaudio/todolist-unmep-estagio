# Desafio UnMep - Estágio de Desenvolvimento

"Esta atividade tem como objetivo avaliar a forma que vocês abordam umproblema ou desafio, não se preocupem em entregar um código perfeito, mas funcional. Se você tem foco no backend, foque em desenvolver um código limpo e de fácilmanutenção, se o seu foco é no frontend, tenha foco na experiência geral do usuário."

## Tecnologias Utilizadas

- Python: A linguagem de programação escolhida para este projeto é o Python. Sua simplicidade e versatilidade tornam-no uma ótima opção para o desenvolvimento web.
- Django: O Django é um framework de alto nível escrito em Python que facilita o desenvolvimento rápido e seguro de aplicações web. Com ele, você poderá criar facilmente rotas, modelos de dados, views e templates para a sua lista de tarefas.
- Ajax: Ajax é uma tecnologia que permite atualizar partes específicas de uma página web sem recarregar a página inteira. Neste projeto, utilizaremos Ajax para criar uma experiência de usuário mais dinâmica, permitindo a adição, edição e exclusão de tarefas sem interromper a interação do usuário.

## Configuração do Ambiente

Antes de executar o projeto, é necessário configurar o ambiente de desenvolvimento. Siga os passos abaixo:

1. Certifique-se de ter o Python instalado em sua máquina. Você pode encontrá-lo em [python.org](https://www.python.org) e seguir as instruções de instalação adequadas para o seu sistema operacional.

2. Clone este repositório em sua máquina local utilizando o comando abaixo:

```bash
git clone https://github.com/ruanclaudio/todolist-unmep-estagio.git
```

3. Navegue até o diretório do projeto:

```bash
cd todolist-unmep-estagio
```

4. Crie um ambiente virtual para isolar as dependências do projeto. Execute o seguinte comando:

```bash
python -m venv venv
```

5. Ative o ambiente virtual:

- No Windows:

```bash
venv\Scripts\Activate
```

- No macOS e Linux:

```bash
source venv/bin/activate
```

6. Instale as dependências do projeto utilizando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Executando o Projeto

Após configurar o ambiente, você está pronto para executar o projeto. Siga os passos abaixo:

1. Certifique-se de que está no diretório raiz do projeto e que o ambiente virtual está ativado.

2. Execute as migrações do Django para criar as tabelas necessárias no banco de dados:

```bash
python manage.py migrate
```

3. Inicie o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

4. Acesse o aplicativo em seu navegador através do seguinte endereço: [http://localhost:8000](http://localhost:8000).

5. Divirta-se interagindo com a lista de tarefas e mostre todo o seu talento como desenvolvedor(a)!

## Alterando os Tipos de Status na Área de Administrador do Django

No projeto do desafio UnMep, você terá a possibilidade de alterar os tipos de status das tarefas na área de administrador do Django. Isso permitirá que você crie novos tipos de status ou modifique os existentes de acordo com suas necessidades.

A área de administrador do Django fornece uma interface intuitiva e poderosa para gerenciar os modelos de dados do seu aplicativo. Para entrar na área de administrador, siga as etapas abaixo:

1. Certifique-se de que o servidor de desenvolvimento do Django está em execução. Se não estiver, inicie-o com o seguinte comando:

```bash
python manage.py runserver
```

2. Abra o seu navegador e acesse o seguinte endereço: [http://localhost:8000/admin](http://localhost:8000/admin).

3. Você será redirecionado para a página de login do Django. Utilize o nome de usuário "admin" e a senha "admin" para entrar na área de administrador.

4. Após fazer login com sucesso, você terá acesso a uma interface amigável onde poderá gerenciar os modelos de dados do seu aplicativo.

5. Navegue até a seção "Tarefas" (ou o nome correspondente ao modelo de tarefas definido em seu código) e você verá uma lista das tarefas existentes.

6. Para alterar os tipos de status das tarefas, clique no modelo de tarefa correspondente. Isso abrirá uma tela de edição onde você poderá modificar os campos, incluindo o campo de status.

7. Adicione, remova ou modifique os tipos de status existentes de acordo com suas preferências. Lembre-se de salvar as alterações antes de sair da página.

8. Agora, ao adicionar ou editar uma tarefa através da interface do usuário do seu aplicativo, você poderá selecionar os tipos de status atualizados.

A área de administrador do Django é uma ferramenta poderosa que facilita a administração dos modelos de dados do seu aplicativo. Utilize-a para personalizar e adaptar o seu projeto de acordo com as suas necessidades.

Lembre-se de que é importante proteger o acesso à área de administrador definindo senhas seguras e restringindo o acesso apenas a usuários autorizados. Em um ambiente de produção, certifique-se de seguir as melhores práticas de segurança recomendadas pelo Django para proteger seus dados.

## Conclusão

O desafio UnMep é uma oportunidade incrível para demonstrar um pouco das minhas habilidades de desenvolvimento web utilizando as tecnologias Python, Django e Ajax. Espero que este README tenha fornecido as informações necessárias para você executar o projeto com sucesso.
