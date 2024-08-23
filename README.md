<<<<<<< HEAD
# ufmg-abntex2
=======
# ufmg-abntex2

Esta é uma customização do abntex2 para monografias (dissertações e teses) da UFMG.

Ela segue as diretrizes para normalização de trabalhos acadêmicos da UFMG (segunda edição, de 2023):

- https://repositorio.ufmg.br

## LaTeX

Se você escreve seu texto diretamente em LaTeX, basta baixar o arquivo ufmg-abntex2.sty na pasta do seu projeto.

Depois disso, você pode adicionar o seguinte ao seu arquivo latex:


    \usepackage{ufmg-abntex2}


A partir daí, basta seguir o uso do [abnTex2](https://github.com/abntex/abntex2) normalmente.

Há apenas dois comandos novos que você pode usar para facilitar sua vida: `UFMGresumolinguavernacula` e `UFMGresumolinguaestrangeira`.

O comando `UFMGresumolinguavernacula` serve para gerar a página com o resumo e as palavras-chave do seu trabalho em português.
Eis um exemplo de uso:

    \UFMGresumolinguavernacula{Este é o resumo do trabalho em língua
    portuguesa. Você precisa também definir as palavras-chave em português.
    Elas serão impressas logo abaixo. De acordo com as normas de UFMG, as
    palavras-chave devem ser separadas por ponto-e-vírgula e finalizadas com
    ponto final.}{primeira; segunda; terceira; palavra composta.}

O comando `UFMGresumolinguaestrangeira` serve para gerar a página com o resumo e as palavras-chave do seu trabalho em algum idioma estrangeiro.

    \UFMGresumolinguaestrangeira{This work aims to contribute to the community.}
    {keyword1; keyword2; keyword3.}
    {english}
    {Abstract}
    {Keywords}

O primeiro parâmetro é o conteúdo do resumo na lingua escolhida (no exemplo acima, inglês).

O segundo parâmetro são as palavras chave no idioma estrangeiro, separadas por ponto-e-vírgula.

O terceiro parâmetro é o idioma para hifenização (english, french, spanish, etc.).

O quarto parâmetro é o título do resumo (Abstract, Résumé, Resumen, etc.).

Por fim, o quinto parâmetro é o título da subseção de palavras-chave (Keywords, Mots-clés, etc.).

Você pode encontrar um exemplo completo em `out/exemplo.tex`.

Apenas note que esse arquivo não foi gerado diretamente por mim.
Ele é fruto de texto escrito em Markdown e convertido em LaTeX via [pandoc](https://www.pandoc.org) a partir do template `template_ufmg.tex`, também disponível nesse repositório.

## Pandoc Markdown 

Se você, como eu, prefere escrever em Markdown e gerar o PDF usando pandoc (que converte para LaTeX e depois para PDF), esse repositório tem algo mais a oferecer.

Se você usa linux e baixar uma cópia integral desse repositório, bastará entrar na pasta e rodar `make` para que ele converta o conteúdo do arquivo `exemplo.md` em um PDF completo, **já no padrão PDFA exigido pelo repositório UFMG**, com capa, contra-capa, índice, lista de tabelas, imagens e siglas, bibliografia e tudo o mais.

Isso, claro, assumindo que você já tem pandoc e pandoc-citeproc instalados.

Não testei nada disso no Windows, mas não deve ser difícil para fazer funcionar (feedback, testes e contribuições de usuários de Windows são bem vindas).

Abaixo faço uma breve descrição do papel de cada um dos arquivos:

- O arquivo `template_ufmg.tex` é um template que pode ser usado para converter seu texto Markdown em um arquivo LaTeX.

- O `Makefile` contém exemplos de como o pandoc pode ser invocado para fazer essa conversão.

- O arquivo `exemplo.md` contém um exemplo de como sua dissertação ou tese inteira pode ser escrita em Markdown. Há inclusive exemplos de como gerar tabelas e incluir imagens. O arquivo gerado é o `out/exemplo.pdf`.

- O arquivo `filtro_citacao.py` contém um script em Python que eu uso porque o pandoc utiliza `\begin{quote}` para fazer citações longas, mas por usar o abnTeX2, eu preciso que ele use `\begin{citacao}`. Esse script é chamado como um filtro do pandoc para que isso aconteça. Talvez haja uma forma melhor de fazer isso, mas fiz esse pequeno script há tantos anos e jamais tive quaisquer problemas, por isso nunca tive motivação para buscar alternativas (contribuições são bem vindas, contudo).

- Os demais arquivos (`abnt.csl, folhaaprovacao.pdf, fichacatalografia.jpg`, etc.) são apenas para demonstrar como você pode usar a ficha catalográfica fornecida pela biblioteca da sua faculdade (gealmente fornecida como uma imagem JPG), bem como a folha de aprovação (geralmente fornecida como um PDF).

- O arquivo `exemplo.yaml` contém as variáveis que o template LaTeX (o `template_ufmg.tex`) usa para formatar o arquivo PDF. É nele que você digita, por exemplo, qual o arquivo bibtex em que sua bibliografia se encontra (veja o arquivo `exemplo.bib` para um exemplo), qual o padrão a ser usado para formatar as referências no fim do trabalho (o arquivo `abnt.csl` é apenas um exemplo). É também aqui que você digita resumo em português, abstract em lingua estrangeira, palavras-chave, autor, orientador, epígrafe, agradecimentos, dedicatória, data, cidade, departamento, etc. O arquivo está bem documento e você pode lê-lo diretamente para descobrir como usar as opções existentes.

## Contato

+ [E-mail](mailto:carlos@cbarth.me)
+ [Site pessoal](https://cbarth.me)

>>>>>>> 3750948 (Initial commit.)
