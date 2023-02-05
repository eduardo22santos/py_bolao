from aposta import Aposta
import datetime
import click
from banco import Banco

# Comando principal
@click.group()
def pyBolao():
    pass

# Comando para inserir dados de Jogos
@click.command()
@click.option('--num',default=6,help='Quantidade de números no jogo (Jogo Mínimo de 6 números de 1 a 60)')
@click.option('--jogos',default=1,help='Quantidade de jogos a ser realizado com o mesmo jogador.')
@click.argument('nome')
@click.argument('diretorio')

def inserirJogo(num,jogos,nome,diretorio):
    for a in range(jogos):
        parar_probrama = False
        jogo = []
        data = str(datetime.datetime.now())
        click.echo('Ensira 0 para fechar o programa!')

        for i in range(num):
            valor = click.prompt('Ensira um número inteiro 1 <= x <= 60',type=int)
            if valor == 0:
                parar_probrama = True
                break
            if valor < 1 or valor > 60:
                click.echo('Valor iválido, por favor tenha mais atenção!\nAbortando a execução do programa')
                parar_probrama = True
                break
            for b in jogo:
                if valor == b:
                    click.echo('Por favor tenha mais atençao!!!\nAbortando a execução do programa')
                    parar_probrama = True
                    break            
            if not parar_probrama:
                jogo.append(valor)
            else:
                break
        if not parar_probrama:
            novoJogo = Aposta(jogo,nome,diretorio,data)
        else:
            break
        click.echo(f'Jogo nº {a+1} registrado com sucesso!')
    click.echo('Programa encerrado!')

pyBolao.add_command(inserirJogo)   

# Comando para mostrar no terminal os dados dos jogos
@click.command()
def mostrar():
    banco = Banco
    click.echo(banco.read_data())

pyBolao.add_command(mostrar)


pyBolao()
