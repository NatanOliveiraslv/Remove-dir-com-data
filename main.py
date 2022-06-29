import os
import shutil
import pendulum
from datetime import datetime
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox


def funcao_principal():
    caminho_procura = remover.caminho.text()
    data = remover.data_inicial.text()
    data1 = remover.data_final.text()
    data2 = datetime.strptime(data, '%d/%m/%y').date()
    data3 = datetime.strptime(data1, '%d/%m/%y').date()
    periodo = pendulum.period(data2, data3)

    for raiz, diretorios, arquivos in os.walk(caminho_procura):
        for diretorio in diretorios:
            for day in periodo.range('days'):
                dia = str(day)
                if dia in diretorio:
                    try:

                        caminho_completo = os.path.join(raiz, diretorio)
                        shutil.rmtree(caminho_completo + '\\')
                        print(caminho_completo)

                    except ValueError as e:
                        QMessageBox.about(remover, 'Alerta', 'Sem permissões.')
                    except PermissionError as e:  # Mostra qualquer erro que der
                        QMessageBox.about(remover, 'Alerta', 'Sem permissões.')
                    except FileNotFoundError as e:
                        QMessageBox.about(remover, 'Alerta', 'Arquivo (s) não encontrado (s).')
                    except Exception as e:
                        QMessageBox.about(remover, 'Alerta', 'Erro desconhecido.')

    QMessageBox.about(remover, 'Alerta', 'Ação realizada com êxito.')


app = QtWidgets.QApplication([])
remover = uic.loadUi('Remover_data.ui')
remover.pushButton.clicked.connect(funcao_principal)
remover.show()
app.exec()
