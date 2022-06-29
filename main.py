importar  SO
importar  Shutil
importar  pêndulo
de  datetime  importação  datetime
do  PyQt5  import  uic , QtWidgets
de  PyQt5 . QtWidgets  importa  QMessageBox

def  funcao_principal ():

    caminho_procura  =  removedor . caminho . texto ()
    dados  =  removedor . data_inicial . texto ()
    data1  =  removedor . data_final . texto ()
    data2  =  datahora . strptime ( data , '%d/%m/%y' ). data ()
    data3  =  datahora . strptime ( data1 , '%d/%m/%y' ). data ()
    periodo  =  pêndulo . período ( dados2 , dados3 )

    for  raiz , diretórios , arquivos  em  os . andar ( caminho_procura ):
                para  diretório  em  diretórios :
                    por  dia  em  periodo . intervalo ( 'dias' ):
                        dia  =  str ( dia )
                        se  dia  no  diretório :
                            tente :

                                caminho_completo  =  os . caminho . join ( raiz , diretório )
                                Shutil . rmtree ( caminho_completo  +  ' \\ ' )
                                print ( caminho_completo )

                            exceto  ValueError  como  e :
                                QMessageBox . sobre ( removedor , 'Alerta' , 'Sem permissions.' )
                            exceto  PermissionError  as  e : #Mostra qualquer erro que der
                                QMessageBox . sobre ( removedor , 'Alerta' , 'Sem permissions.' )
                            exceto  FileNotFoundError  como  e :
                                QMessageBox . sobre ( removedor , 'Alerta' , 'Arquivo (s) não encontrado (s).' )
                            exceto  Exceção  como  e :
                                QMessageBox . sobre ( removedor , 'Alerta' , 'Erro desconhecido.' )

    QMessageBox . sobre ( removedor , 'Alerta' , 'Ação realizada com sucesso.' )

app = QtWidgets . QAplicativo ([])
removedor = uic . loadUi ( 'Remover_data.ui' )
removedor . botão de pressão . clicou . conectar ( funcao_principal )
removedor . mostrar ()
aplicativo . executivo ()
