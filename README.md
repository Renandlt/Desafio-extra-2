# Desafio-extra-2
Projeto extra do segundo módulo do curso formação de análise de dados
Claro, aqui está um README para o script:

# Rastreamento de Candidatos por Palavras-Chave

Este é um script Python simples para rastrear candidatos com base em palavras-chave para diferentes vagas. O script permite aos candidatos escolher uma vaga e inserir um resumo do currículo. Em seguida, ele verifica se o resumo contém palavras-chave relevantes para a vaga escolhida e mantém um registro do número total de inscritos e quantos deles têm resumos válidos.

## Como Funciona

1. O script define duas vagas (Vaga 1 e Vaga 2) com suas respectivas palavras-chave associadas.

2. Dois dicionários, `inscritos` e `validos`, são criados para rastrear o número total de inscritos e candidatos com resumos válidos para cada vaga.

3. O script entra em um loop que permite aos candidatos escolher uma vaga (digitando 1 ou 2) ou sair (digitando 0).

4. Para a vaga escolhida, o candidato insere um resumo de seu currículo.

5. O resumo é dividido em palavras-chave.

6. O script verifica se o resumo contém pelo menos uma palavra-chave da vaga escolhida. Se sim, o candidato é considerado válido.

7. Os dicionários `inscritos` e `validos` são atualizados com os números apropriados.

8. O loop continua até que o candidato escolha sair digitando "0".

9. No final, o script exibe um resumo das inscrições para cada vaga, incluindo o número total de inscritos e o número de candidatos válidos.

## Como Usar

1. Execute o script em um ambiente Python.

2. Siga as instruções para escolher uma vaga e inserir um resumo.

3. Repita o processo para quantos candidatos desejar.

4. Para encerrar o programa, basta digitar "0" quando solicitado a escolher uma vaga.

5. O script fornecerá um resumo das inscrições, mostrando o número total de inscritos e o número de candidatos válidos para cada vaga.

Espero que este script seja útil para rastrear candidatos com base em palavras-chave para diferentes vagas. Você pode personalizar as vagas e as palavras-chave conforme necessário.
