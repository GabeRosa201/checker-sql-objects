# checker-sql-objects

Este projeto serve para fazer varreduras em bases de dados e apresentar relatórios sobre as diferenças encontradas em duas bases de dados.

# Fluxo da operação

Existe uma base modelo que vai ser utilizada para usar de comparativo.
Na base modelo será feita a extração dos dados de objetos -> Procedures / Funções / Views
Depois será informado a(s) base(s) para ser comparada.

Durante o processo de verificação, existe um serviço de mensageria que informa como está o andamento do processo.

Quando houver algo que estiver diferente vai ser salvo um insert que mostra que 
Qual o objeto (proc / função / view), nome do objeto, base que está diferente
Armazenar também qual o valor do objeto e informar a linha que estava diferente

Possiblidade de visualizar as informações precisa ser implementada. Não sei qual forma ainda