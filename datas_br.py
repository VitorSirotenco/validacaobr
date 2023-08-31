from datetime import datetime

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()


    def __str__(self):
        return self.format_data()


    def mes_cadastro(self):
        meses_do_ano = ['', 'Janeiro', 'Fevereiro', 'Março', 'abril',
                        'maio', 'junho', 'julho', 'agosto', 'setembro',
                        'outubro', 'novembro', 'dezembro']

        mes_cadastrado = self.momento_cadastro.month
        return meses_do_ano[mes_cadastrado]


    def dia_semana(self):
        dias_da_semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
        dia_da_semana = self.momento_cadastro.weekday()
        return dias_da_semana[dia_da_semana]


    def format_data(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y  %H:%M') #para formatar a data
        return data_formatada

