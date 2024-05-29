import schedule
import datetime
import time

print("Teste aqui")

# Função que será executada no primeiro dia de cada mês
def tarefa_mensal():
    # Obtém a data e hora atual
    data_hora_atual = datetime.datetime.now()
    print("Teste aqui 2")
    # Verifica se é o primeiro dia do mês
    if data_hora_atual.day == 1:
        print("Teste aqui 3")
        # Coloque aqui o código que deseja executar no primeiro dia de cada mês
        print("Executando tarefa mensal...")
        time.sleep(3)
        # Adicione aqui qualquer código adicional que deseja executar
        # após a conclusão da tarefa mensal
        return True  # Indica que a tarefa foi realizada com sucesso
    else:
        print("Não é o primeiro dia do mês. Tarefa não realizada.")
        time.sleep(3)
        return False  # Indica que a tarefa não foi realizada

# Agendando a execução da função para ser executada a cada dia às 00:01
schedule.every().day.at("14:13").do(tarefa_mensal)

# Loop infinito para verificar e executar as tarefas agendadas
while True:
    schedule.run_pending()
    time.sleep(1)