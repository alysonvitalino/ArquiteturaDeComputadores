# Criptografia

🔐 Cifra de César
🧩 O que é Criptografia de César?

A Cifra de César é um tipo de cifra de substituição, onde cada letra do texto original é substituída por outra que se encontra um número fixo de posições adiante no alfabeto.

É considerada o primeiro método documentado de criptografia da história, tendo sido utilizada por Júlio César em suas comunicações militares para proteger mensagens confidenciais.

🎯 Objetivo

Desenvolver um algoritmo básico capaz de codificar e decodificar mensagens de texto utilizando o princípio da Cifra de César.

⚙️ Funcionalidades e Descrição do Algoritmo

O algoritmo implementa a Cifra de César por meio de duas funções principais:

encode() — responsável pela codificação (criptografia);

decode() — responsável pela decodificação (descriptografia).

🔁 Fluxo de execução

Ao ser executado, o programa entra em um loop contínuo, solicitando que o usuário digite uma senha (pt).

Em seguida, é chamada a função:

ct = encode(pt, 3)

que recebe dois parâmetros:

A senha digitada pelo usuário;

O valor 3, que representa o número de posições de deslocamento no alfabeto.

A função encode() aplica a Cifra de César, deslocando cada letra três posições à frente no alfabeto.
O resultado é exibido na tela como:

Criptografia: (senha criptografada)

Logo após, o programa imprime:

Decodificação: (senha decodificada)

Essa mensagem é gerada pela função:

decode(ct, 3)

que realiza o processo inverso da criptografia, retrocedendo três posições no alfabeto para recuperar a senha original.

Após a exibição dos resultados, o programa reinicia o loop, permitindo que o usuário digite novas senhas indefinidamente.

💻 Exemplo de uso

Entrada:

Digite sua senha: senha123

Saída:

Criptografia: vhqkd456
Decodificação: senha123

📜 Observações

O algoritmo também foi adaptado para criptografar números (0–9), mantendo a mesma lógica de deslocamento circular.

Caracteres especiais e espaços não são alterados durante o processo.

O deslocamento pode ser modificado pelo usuário para diferentes valores de cifragem.
